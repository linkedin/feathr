package com.linkedin.feathr.offline.source.accessor

import com.linkedin.feathr.offline.config.location.KafkaEndpoint
import com.linkedin.feathr.offline.source.DataSource
import com.linkedin.feathr.offline.source.dataloader.{CaseInsensitiveGenericRecordWrapper, DataLoaderFactory}
import com.linkedin.feathr.offline.testfwk.TestFwkUtils
import com.linkedin.feathr.offline.transformation.DataFrameExt._
import org.apache.avro.generic.{GenericRecord, IndexedRecord}
import org.apache.avro.specific.SpecificRecordBase
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.{DataFrame, SparkSession}
/**
 * load a dataset from a non-partitioned source.
 * @param ss the spark session
 * @param fileLoaderFactory loader for a single file
 * @param source          datasource
 * @param expectDatumType expected datum type of the loaded dataset, could be Avro GenericRecord or Avro SpecificRecord
 */
private[offline] class NonTimeBasedDataSourceAccessor(
    ss: SparkSession,
    fileLoaderFactory: DataLoaderFactory,
    source: DataSource,
    expectDatumType: Option[Class[_]])
    extends DataSourceAccessor(source) {

  /**
   * get source data as a dataframe
   *
   * @return the dataframe
   */
  override def get(): DataFrame = {
    val df = if (source.location.isInstanceOf[KafkaEndpoint]) {
     fileLoaderFactory.createFromLocation(source.location).loadDataFrame()
    } else {
      source.pathList.map(fileLoaderFactory.create(_).loadDataFrame()).reduce((x, y) => x.fuzzyUnion(y))
    }
    if (TestFwkUtils.IS_DEBUGGER_ENABLED) {
      println()
      println()
      source.pathList.foreach(sourcePath => println(f"${Console.GREEN}Source is: $sourcePath${Console.RESET}"))
      println(f"${Console.GREEN}Your source data schema is: ${Console.RESET}")
      println(f"${Console.GREEN}(meaning: |-- fieldName: type (nullable = true))${Console.RESET}")
      df.printSchema()
      println(f"${Console.GREEN}Showing source data: ${Console.RESET}")
      df.show(10)
      println()
      println()
    }
    df
  }

  /**
   * get source data as RDD.
   * This is only for features are defined using SpecificRecordSourceKeyExtractor
   *
   * @return source view in RDD formats
   */
  def getAsRdd(): RDD[IndexedRecord] = {
    require(expectDatumType.nonEmpty)
    val rdd = source.pathList
      .map(
        path =>
          fileLoaderFactory
            .create(path)
            .loadRdd(expectDatumType.get)
            .asInstanceOf[RDD[IndexedRecord]])
      .reduce(_ union _)
    if (classOf[GenericRecord].isAssignableFrom(expectDatumType.get) &&
      !classOf[SpecificRecordBase].isAssignableFrom(expectDatumType.get)) {
      rdd.asInstanceOf[RDD[GenericRecord]].map(new CaseInsensitiveGenericRecordWrapper(_))
    } else {
      rdd
    }
  }
}