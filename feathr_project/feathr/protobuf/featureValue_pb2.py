# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: featureValue.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66\x65\x61tureValue.proto\x12\x08protobuf\"\xce\x06\n\x0c\x46\x65\x61tureValue\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x05 \x01(\x05H\x00\x12\x14\n\nlong_value\x18\x06 \x01(\x03H\x00\x12/\n\rboolean_array\x18\n \x01(\x0b\x32\x16.protobuf.BooleanArrayH\x00\x12-\n\x0cstring_array\x18\x0b \x01(\x0b\x32\x15.protobuf.StringArrayH\x00\x12+\n\x0b\x66loat_array\x18\x0c \x01(\x0b\x32\x14.protobuf.FloatArrayH\x00\x12-\n\x0c\x64ouble_array\x18\r \x01(\x0b\x32\x15.protobuf.DoubleArrayH\x00\x12+\n\tint_array\x18\x0e \x01(\x0b\x32\x16.protobuf.IntegerArrayH\x00\x12)\n\nlong_array\x18\x0f \x01(\x0b\x32\x13.protobuf.LongArrayH\x00\x12*\n\nbyte_array\x18\x10 \x01(\x0b\x32\x14.protobuf.BytesArrayH\x00\x12:\n\x13sparse_string_array\x18\x14 \x01(\x0b\x32\x1b.protobuf.SparseStringArrayH\x00\x12\x36\n\x11sparse_bool_array\x18\x15 \x01(\x0b\x32\x19.protobuf.SparseBoolArrayH\x00\x12<\n\x14sparse_integer_array\x18\x16 \x01(\x0b\x32\x1c.protobuf.SparseIntegerArrayH\x00\x12\x36\n\x11sparse_long_array\x18\x17 \x01(\x0b\x32\x19.protobuf.SparseLongArrayH\x00\x12:\n\x13sparse_double_array\x18\x18 \x01(\x0b\x32\x1b.protobuf.SparseDoubleArrayH\x00\x12\x38\n\x12sparse_float_array\x18\x19 \x01(\x0b\x32\x1a.protobuf.SparseFloatArrayH\x00\x42\x13\n\x11\x46\x65\x61tureValueOneOf\" \n\x0c\x42ooleanArray\x12\x10\n\x08\x62ooleans\x18\x01 \x03(\x08\"\x1e\n\x0bStringArray\x12\x0f\n\x07strings\x18\x01 \x03(\t\"\x1e\n\x0b\x44oubleArray\x12\x0f\n\x07\x64oubles\x18\x01 \x03(\x01\"\x1c\n\nFloatArray\x12\x0e\n\x06\x66loats\x18\x01 \x03(\x02\" \n\x0cIntegerArray\x12\x10\n\x08integers\x18\x01 \x03(\x05\"\x1a\n\tLongArray\x12\r\n\x05longs\x18\x01 \x03(\x03\"\x1b\n\nBytesArray\x12\r\n\x05\x62ytes\x18\x01 \x03(\x0c\"B\n\x11SparseStringArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x15\n\rvalue_strings\x18\x02 \x03(\t\"A\n\x0fSparseBoolArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x16\n\x0evalue_booleans\x18\x02 \x03(\x08\"D\n\x12SparseIntegerArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x16\n\x0evalue_integers\x18\x02 \x03(\x05\">\n\x0fSparseLongArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x13\n\x0bvalue_longs\x18\x02 \x03(\x03\"B\n\x11SparseDoubleArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x15\n\rvalue_doubles\x18\x02 \x03(\x01\"@\n\x10SparseFloatArray\x12\x16\n\x0eindex_integers\x18\x01 \x03(\x05\x12\x14\n\x0cvalue_floats\x18\x02 \x03(\x02\x42+\n)com.linkedin.feathr.common.types.protobufb\x06proto3')



_FEATUREVALUE = DESCRIPTOR.message_types_by_name['FeatureValue']
_BOOLEANARRAY = DESCRIPTOR.message_types_by_name['BooleanArray']
_STRINGARRAY = DESCRIPTOR.message_types_by_name['StringArray']
_DOUBLEARRAY = DESCRIPTOR.message_types_by_name['DoubleArray']
_FLOATARRAY = DESCRIPTOR.message_types_by_name['FloatArray']
_INTEGERARRAY = DESCRIPTOR.message_types_by_name['IntegerArray']
_LONGARRAY = DESCRIPTOR.message_types_by_name['LongArray']
_BYTESARRAY = DESCRIPTOR.message_types_by_name['BytesArray']
_SPARSESTRINGARRAY = DESCRIPTOR.message_types_by_name['SparseStringArray']
_SPARSEBOOLARRAY = DESCRIPTOR.message_types_by_name['SparseBoolArray']
_SPARSEINTEGERARRAY = DESCRIPTOR.message_types_by_name['SparseIntegerArray']
_SPARSELONGARRAY = DESCRIPTOR.message_types_by_name['SparseLongArray']
_SPARSEDOUBLEARRAY = DESCRIPTOR.message_types_by_name['SparseDoubleArray']
_SPARSEFLOATARRAY = DESCRIPTOR.message_types_by_name['SparseFloatArray']
FeatureValue = _reflection.GeneratedProtocolMessageType('FeatureValue', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREVALUE,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.FeatureValue)
})
_sym_db.RegisterMessage(FeatureValue)

BooleanArray = _reflection.GeneratedProtocolMessageType('BooleanArray', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEANARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.BooleanArray)
})
_sym_db.RegisterMessage(BooleanArray)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.StringArray)
})
_sym_db.RegisterMessage(StringArray)

DoubleArray = _reflection.GeneratedProtocolMessageType('DoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.DoubleArray)
})
_sym_db.RegisterMessage(DoubleArray)

FloatArray = _reflection.GeneratedProtocolMessageType('FloatArray', (_message.Message,), {
  'DESCRIPTOR' : _FLOATARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.FloatArray)
})
_sym_db.RegisterMessage(FloatArray)

IntegerArray = _reflection.GeneratedProtocolMessageType('IntegerArray', (_message.Message,), {
  'DESCRIPTOR' : _INTEGERARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.IntegerArray)
})
_sym_db.RegisterMessage(IntegerArray)

LongArray = _reflection.GeneratedProtocolMessageType('LongArray', (_message.Message,), {
  'DESCRIPTOR' : _LONGARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.LongArray)
})
_sym_db.RegisterMessage(LongArray)

BytesArray = _reflection.GeneratedProtocolMessageType('BytesArray', (_message.Message,), {
  'DESCRIPTOR' : _BYTESARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.BytesArray)
})
_sym_db.RegisterMessage(BytesArray)

SparseStringArray = _reflection.GeneratedProtocolMessageType('SparseStringArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSESTRINGARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseStringArray)
})
_sym_db.RegisterMessage(SparseStringArray)

SparseBoolArray = _reflection.GeneratedProtocolMessageType('SparseBoolArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEBOOLARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseBoolArray)
})
_sym_db.RegisterMessage(SparseBoolArray)

SparseIntegerArray = _reflection.GeneratedProtocolMessageType('SparseIntegerArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEINTEGERARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseIntegerArray)
})
_sym_db.RegisterMessage(SparseIntegerArray)

SparseLongArray = _reflection.GeneratedProtocolMessageType('SparseLongArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSELONGARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseLongArray)
})
_sym_db.RegisterMessage(SparseLongArray)

SparseDoubleArray = _reflection.GeneratedProtocolMessageType('SparseDoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEDOUBLEARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseDoubleArray)
})
_sym_db.RegisterMessage(SparseDoubleArray)

SparseFloatArray = _reflection.GeneratedProtocolMessageType('SparseFloatArray', (_message.Message,), {
  'DESCRIPTOR' : _SPARSEFLOATARRAY,
  '__module__' : 'featureValue_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SparseFloatArray)
})
_sym_db.RegisterMessage(SparseFloatArray)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.linkedin.feathr.common.types.protobuf'
  _FEATUREVALUE._serialized_start=33
  _FEATUREVALUE._serialized_end=879
  _BOOLEANARRAY._serialized_start=881
  _BOOLEANARRAY._serialized_end=913
  _STRINGARRAY._serialized_start=915
  _STRINGARRAY._serialized_end=945
  _DOUBLEARRAY._serialized_start=947
  _DOUBLEARRAY._serialized_end=977
  _FLOATARRAY._serialized_start=979
  _FLOATARRAY._serialized_end=1007
  _INTEGERARRAY._serialized_start=1009
  _INTEGERARRAY._serialized_end=1041
  _LONGARRAY._serialized_start=1043
  _LONGARRAY._serialized_end=1069
  _BYTESARRAY._serialized_start=1071
  _BYTESARRAY._serialized_end=1098
  _SPARSESTRINGARRAY._serialized_start=1100
  _SPARSESTRINGARRAY._serialized_end=1166
  _SPARSEBOOLARRAY._serialized_start=1168
  _SPARSEBOOLARRAY._serialized_end=1233
  _SPARSEINTEGERARRAY._serialized_start=1235
  _SPARSEINTEGERARRAY._serialized_end=1303
  _SPARSELONGARRAY._serialized_start=1305
  _SPARSELONGARRAY._serialized_end=1367
  _SPARSEDOUBLEARRAY._serialized_start=1369
  _SPARSEDOUBLEARRAY._serialized_end=1435
  _SPARSEFLOATARRAY._serialized_start=1437
  _SPARSEFLOATARRAY._serialized_end=1501
# @@protoc_insertion_point(module_scope)
