addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "1.1.0")

/**
 * Helps us publish the artifacts to sonatype, which in turn
 * pushes to maven central.
 *
 * https://github.com/xerial/sbt-sonatype/releases
 */
addSbtPlugin("org.xerial.sbt" % "sbt-sonatype" % "3.9.5") //https://github.com/xerial/sbt-sonatype/releases

/**
 *
 * Signs all the jars, used in conjunction with sbt-sonatype.
 *
 * https://github.com/sbt/sbt-pgp/releases
 */
addSbtPlugin("com.jsuereth" % "sbt-pgp" % "2.0.1") //https://github.com/sbt/sbt-pgp/releases

/**
 *
 * Supports more advanced dependency tree scripts
 * 
 * ex.
 * sbt dependencyTree -java-home /Library/Java/JavaVirtualMachines/jdk1.8.0_282-msft.jdk/Contents/Home
 * https://www.baeldung.com/scala/sbt-dependency-tree
 */
addDependencyTreePlugin
