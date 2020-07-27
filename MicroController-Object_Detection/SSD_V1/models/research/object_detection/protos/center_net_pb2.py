# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/center_net.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import image_resizer_pb2 as object__detection_dot_protos_dot_image__resizer__pb2
from object_detection.protos import losses_pb2 as object__detection_dot_protos_dot_losses__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/center_net.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_pb=_b('\n(object_detection/protos/center_net.proto\x12\x17object_detection.protos\x1a+object_detection/protos/image_resizer.proto\x1a$object_detection/protos/losses.proto\"\x9b\x10\n\tCenterNet\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x12M\n\x11\x66\x65\x61ture_extractor\x18\x02 \x01(\x0b\x32\x32.object_detection.protos.CenterNetFeatureExtractor\x12<\n\rimage_resizer\x18\x03 \x01(\x0b\x32%.object_detection.protos.ImageResizer\x12Q\n\x15object_detection_task\x18\x04 \x01(\x0b\x32\x32.object_detection.protos.CenterNet.ObjectDetection\x12S\n\x14object_center_params\x18\x05 \x01(\x0b\x32\x35.object_detection.protos.CenterNet.ObjectCenterParams\x12\x1f\n\x17keypoint_label_map_path\x18\x06 \x01(\t\x12W\n\x18keypoint_estimation_task\x18\x07 \x03(\x0b\x32\x35.object_detection.protos.CenterNet.KeypointEstimation\x12O\n\x14mask_estimation_task\x18\x08 \x01(\x0b\x32\x31.object_detection.protos.CenterNet.MaskEstimation\x1a\xcb\x01\n\x0fObjectDetection\x12\x1b\n\x10task_loss_weight\x18\x01 \x01(\x02:\x01\x31\x12\x1d\n\x12offset_loss_weight\x18\x03 \x01(\x02:\x01\x31\x12\x1e\n\x11scale_loss_weight\x18\x04 \x01(\x02:\x03\x30.1\x12\x44\n\x11localization_loss\x18\x08 \x01(\x0b\x32).object_detection.protos.LocalizationLossJ\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\x1a\x8e\x02\n\x12ObjectCenterParams\x12$\n\x19object_center_loss_weight\x18\x01 \x01(\x02:\x01\x31\x12H\n\x13\x63lassification_loss\x18\x02 \x01(\x0b\x32+.object_detection.protos.ClassificationLoss\x12 \n\x11heatmap_bias_init\x18\x03 \x01(\x02:\x05-2.19\x12 \n\x13min_box_overlap_iou\x18\x04 \x01(\x02:\x03\x30.7\x12 \n\x13max_box_predictions\x18\x05 \x01(\x05:\x03\x31\x30\x30\x12\"\n\x13use_labeled_classes\x18\x06 \x01(\x08:\x05\x66\x61lse\x1a\xac\x06\n\x12KeypointEstimation\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x1b\n\x10task_loss_weight\x18\x02 \x01(\x02:\x01\x31\x12+\n\x04loss\x18\x03 \x01(\x0b\x32\x1d.object_detection.protos.Loss\x12\x1b\n\x13keypoint_class_name\x18\x04 \x01(\t\x12l\n\x15keypoint_label_to_std\x18\x05 \x03(\x0b\x32M.object_detection.protos.CenterNet.KeypointEstimation.KeypointLabelToStdEntry\x12*\n\x1fkeypoint_regression_loss_weight\x18\x06 \x01(\x02:\x01\x31\x12\'\n\x1ckeypoint_heatmap_loss_weight\x18\x07 \x01(\x02:\x01\x31\x12&\n\x1bkeypoint_offset_loss_weight\x18\x08 \x01(\x02:\x01\x31\x12 \n\x11heatmap_bias_init\x18\t \x01(\x02:\x05-2.19\x12/\n\"keypoint_candidate_score_threshold\x18\n \x01(\x02:\x03\x30.1\x12(\n\x1bnum_candidates_per_keypoint\x18\x0b \x01(\x05:\x03\x31\x30\x30\x12$\n\x19peak_max_pool_kernel_size\x18\x0c \x01(\x05:\x01\x33\x12%\n\x18unmatched_keypoint_score\x18\r \x01(\x02:\x03\x30.1\x12\x16\n\tbox_scale\x18\x0e \x01(\x02:\x03\x31.2\x12#\n\x16\x63\x61ndidate_search_scale\x18\x0f \x01(\x02:\x03\x30.3\x12,\n\x16\x63\x61ndidate_ranking_mode\x18\x10 \x01(\t:\x0cmin_distance\x12\x1d\n\x12offset_peak_radius\x18\x11 \x01(\x05:\x01\x30\x12\"\n\x13per_keypoint_offset\x18\x12 \x01(\x08:\x05\x66\x61lse\x1a\x39\n\x17KeypointLabelToStdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\xea\x01\n\x0eMaskEstimation\x12\x1b\n\x10task_loss_weight\x18\x01 \x01(\x02:\x01\x31\x12H\n\x13\x63lassification_loss\x18\x02 \x01(\x0b\x32+.object_detection.protos.ClassificationLoss\x12\x18\n\x0bmask_height\x18\x04 \x01(\x05:\x03\x32\x35\x36\x12\x17\n\nmask_width\x18\x05 \x01(\x05:\x03\x32\x35\x36\x12\x1c\n\x0fscore_threshold\x18\x06 \x01(\x02:\x03\x30.5\x12 \n\x11heatmap_bias_init\x18\x03 \x01(\x02:\x05-2.19\"s\n\x19\x43\x65nterNetFeatureExtractor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rchannel_means\x18\x02 \x03(\x02\x12\x14\n\x0c\x63hannel_stds\x18\x03 \x03(\x02\x12\x1b\n\x0c\x62gr_ordering\x18\x04 \x01(\x08:\x05\x66\x61lse')
  ,
  dependencies=[object__detection_dot_protos_dot_image__resizer__pb2.DESCRIPTOR,object__detection_dot_protos_dot_losses__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CENTERNET_OBJECTDETECTION = _descriptor.Descriptor(
  name='ObjectDetection',
  full_name='object_detection.protos.CenterNet.ObjectDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_loss_weight', full_name='object_detection.protos.CenterNet.ObjectDetection.task_loss_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset_loss_weight', full_name='object_detection.protos.CenterNet.ObjectDetection.offset_loss_weight', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale_loss_weight', full_name='object_detection.protos.CenterNet.ObjectDetection.scale_loss_weight', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localization_loss', full_name='object_detection.protos.CenterNet.ObjectDetection.localization_loss', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=903,
)

_CENTERNET_OBJECTCENTERPARAMS = _descriptor.Descriptor(
  name='ObjectCenterParams',
  full_name='object_detection.protos.CenterNet.ObjectCenterParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_center_loss_weight', full_name='object_detection.protos.CenterNet.ObjectCenterParams.object_center_loss_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classification_loss', full_name='object_detection.protos.CenterNet.ObjectCenterParams.classification_loss', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heatmap_bias_init', full_name='object_detection.protos.CenterNet.ObjectCenterParams.heatmap_bias_init', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-2.19),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_box_overlap_iou', full_name='object_detection.protos.CenterNet.ObjectCenterParams.min_box_overlap_iou', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.7),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_box_predictions', full_name='object_detection.protos.CenterNet.ObjectCenterParams.max_box_predictions', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_labeled_classes', full_name='object_detection.protos.CenterNet.ObjectCenterParams.use_labeled_classes', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=1176,
)

_CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY = _descriptor.Descriptor(
  name='KeypointLabelToStdEntry',
  full_name='object_detection.protos.CenterNet.KeypointEstimation.KeypointLabelToStdEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='object_detection.protos.CenterNet.KeypointEstimation.KeypointLabelToStdEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='object_detection.protos.CenterNet.KeypointEstimation.KeypointLabelToStdEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1934,
  serialized_end=1991,
)

_CENTERNET_KEYPOINTESTIMATION = _descriptor.Descriptor(
  name='KeypointEstimation',
  full_name='object_detection.protos.CenterNet.KeypointEstimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='object_detection.protos.CenterNet.KeypointEstimation.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_loss_weight', full_name='object_detection.protos.CenterNet.KeypointEstimation.task_loss_weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='object_detection.protos.CenterNet.KeypointEstimation.loss', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_class_name', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_class_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_label_to_std', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_label_to_std', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_regression_loss_weight', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_regression_loss_weight', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_heatmap_loss_weight', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_heatmap_loss_weight', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_offset_loss_weight', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_offset_loss_weight', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heatmap_bias_init', full_name='object_detection.protos.CenterNet.KeypointEstimation.heatmap_bias_init', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-2.19),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_candidate_score_threshold', full_name='object_detection.protos.CenterNet.KeypointEstimation.keypoint_candidate_score_threshold', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_candidates_per_keypoint', full_name='object_detection.protos.CenterNet.KeypointEstimation.num_candidates_per_keypoint', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peak_max_pool_kernel_size', full_name='object_detection.protos.CenterNet.KeypointEstimation.peak_max_pool_kernel_size', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unmatched_keypoint_score', full_name='object_detection.protos.CenterNet.KeypointEstimation.unmatched_keypoint_score', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_scale', full_name='object_detection.protos.CenterNet.KeypointEstimation.box_scale', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candidate_search_scale', full_name='object_detection.protos.CenterNet.KeypointEstimation.candidate_search_scale', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candidate_ranking_mode', full_name='object_detection.protos.CenterNet.KeypointEstimation.candidate_ranking_mode', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("min_distance").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset_peak_radius', full_name='object_detection.protos.CenterNet.KeypointEstimation.offset_peak_radius', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='per_keypoint_offset', full_name='object_detection.protos.CenterNet.KeypointEstimation.per_keypoint_offset', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1991,
)

_CENTERNET_MASKESTIMATION = _descriptor.Descriptor(
  name='MaskEstimation',
  full_name='object_detection.protos.CenterNet.MaskEstimation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_loss_weight', full_name='object_detection.protos.CenterNet.MaskEstimation.task_loss_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classification_loss', full_name='object_detection.protos.CenterNet.MaskEstimation.classification_loss', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_height', full_name='object_detection.protos.CenterNet.MaskEstimation.mask_height', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_width', full_name='object_detection.protos.CenterNet.MaskEstimation.mask_width', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='object_detection.protos.CenterNet.MaskEstimation.score_threshold', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heatmap_bias_init', full_name='object_detection.protos.CenterNet.MaskEstimation.heatmap_bias_init', index=5,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-2.19),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1994,
  serialized_end=2228,
)

_CENTERNET = _descriptor.Descriptor(
  name='CenterNet',
  full_name='object_detection.protos.CenterNet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='object_detection.protos.CenterNet.num_classes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_extractor', full_name='object_detection.protos.CenterNet.feature_extractor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_resizer', full_name='object_detection.protos.CenterNet.image_resizer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_detection_task', full_name='object_detection.protos.CenterNet.object_detection_task', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_center_params', full_name='object_detection.protos.CenterNet.object_center_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_label_map_path', full_name='object_detection.protos.CenterNet.keypoint_label_map_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_estimation_task', full_name='object_detection.protos.CenterNet.keypoint_estimation_task', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mask_estimation_task', full_name='object_detection.protos.CenterNet.mask_estimation_task', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CENTERNET_OBJECTDETECTION, _CENTERNET_OBJECTCENTERPARAMS, _CENTERNET_KEYPOINTESTIMATION, _CENTERNET_MASKESTIMATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=2228,
)


_CENTERNETFEATUREEXTRACTOR = _descriptor.Descriptor(
  name='CenterNetFeatureExtractor',
  full_name='object_detection.protos.CenterNetFeatureExtractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='object_detection.protos.CenterNetFeatureExtractor.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_means', full_name='object_detection.protos.CenterNetFeatureExtractor.channel_means', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_stds', full_name='object_detection.protos.CenterNetFeatureExtractor.channel_stds', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bgr_ordering', full_name='object_detection.protos.CenterNetFeatureExtractor.bgr_ordering', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2230,
  serialized_end=2345,
)

_CENTERNET_OBJECTDETECTION.fields_by_name['localization_loss'].message_type = object__detection_dot_protos_dot_losses__pb2._LOCALIZATIONLOSS
_CENTERNET_OBJECTDETECTION.containing_type = _CENTERNET
_CENTERNET_OBJECTCENTERPARAMS.fields_by_name['classification_loss'].message_type = object__detection_dot_protos_dot_losses__pb2._CLASSIFICATIONLOSS
_CENTERNET_OBJECTCENTERPARAMS.containing_type = _CENTERNET
_CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY.containing_type = _CENTERNET_KEYPOINTESTIMATION
_CENTERNET_KEYPOINTESTIMATION.fields_by_name['loss'].message_type = object__detection_dot_protos_dot_losses__pb2._LOSS
_CENTERNET_KEYPOINTESTIMATION.fields_by_name['keypoint_label_to_std'].message_type = _CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY
_CENTERNET_KEYPOINTESTIMATION.containing_type = _CENTERNET
_CENTERNET_MASKESTIMATION.fields_by_name['classification_loss'].message_type = object__detection_dot_protos_dot_losses__pb2._CLASSIFICATIONLOSS
_CENTERNET_MASKESTIMATION.containing_type = _CENTERNET
_CENTERNET.fields_by_name['feature_extractor'].message_type = _CENTERNETFEATUREEXTRACTOR
_CENTERNET.fields_by_name['image_resizer'].message_type = object__detection_dot_protos_dot_image__resizer__pb2._IMAGERESIZER
_CENTERNET.fields_by_name['object_detection_task'].message_type = _CENTERNET_OBJECTDETECTION
_CENTERNET.fields_by_name['object_center_params'].message_type = _CENTERNET_OBJECTCENTERPARAMS
_CENTERNET.fields_by_name['keypoint_estimation_task'].message_type = _CENTERNET_KEYPOINTESTIMATION
_CENTERNET.fields_by_name['mask_estimation_task'].message_type = _CENTERNET_MASKESTIMATION
DESCRIPTOR.message_types_by_name['CenterNet'] = _CENTERNET
DESCRIPTOR.message_types_by_name['CenterNetFeatureExtractor'] = _CENTERNETFEATUREEXTRACTOR

CenterNet = _reflection.GeneratedProtocolMessageType('CenterNet', (_message.Message,), dict(

  ObjectDetection = _reflection.GeneratedProtocolMessageType('ObjectDetection', (_message.Message,), dict(
    DESCRIPTOR = _CENTERNET_OBJECTDETECTION,
    __module__ = 'object_detection.protos.center_net_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet.ObjectDetection)
    ))
  ,

  ObjectCenterParams = _reflection.GeneratedProtocolMessageType('ObjectCenterParams', (_message.Message,), dict(
    DESCRIPTOR = _CENTERNET_OBJECTCENTERPARAMS,
    __module__ = 'object_detection.protos.center_net_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet.ObjectCenterParams)
    ))
  ,

  KeypointEstimation = _reflection.GeneratedProtocolMessageType('KeypointEstimation', (_message.Message,), dict(

    KeypointLabelToStdEntry = _reflection.GeneratedProtocolMessageType('KeypointLabelToStdEntry', (_message.Message,), dict(
      DESCRIPTOR = _CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY,
      __module__ = 'object_detection.protos.center_net_pb2'
      # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet.KeypointEstimation.KeypointLabelToStdEntry)
      ))
    ,
    DESCRIPTOR = _CENTERNET_KEYPOINTESTIMATION,
    __module__ = 'object_detection.protos.center_net_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet.KeypointEstimation)
    ))
  ,

  MaskEstimation = _reflection.GeneratedProtocolMessageType('MaskEstimation', (_message.Message,), dict(
    DESCRIPTOR = _CENTERNET_MASKESTIMATION,
    __module__ = 'object_detection.protos.center_net_pb2'
    # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet.MaskEstimation)
    ))
  ,
  DESCRIPTOR = _CENTERNET,
  __module__ = 'object_detection.protos.center_net_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNet)
  ))
_sym_db.RegisterMessage(CenterNet)
_sym_db.RegisterMessage(CenterNet.ObjectDetection)
_sym_db.RegisterMessage(CenterNet.ObjectCenterParams)
_sym_db.RegisterMessage(CenterNet.KeypointEstimation)
_sym_db.RegisterMessage(CenterNet.KeypointEstimation.KeypointLabelToStdEntry)
_sym_db.RegisterMessage(CenterNet.MaskEstimation)

CenterNetFeatureExtractor = _reflection.GeneratedProtocolMessageType('CenterNetFeatureExtractor', (_message.Message,), dict(
  DESCRIPTOR = _CENTERNETFEATUREEXTRACTOR,
  __module__ = 'object_detection.protos.center_net_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.CenterNetFeatureExtractor)
  ))
_sym_db.RegisterMessage(CenterNetFeatureExtractor)


_CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY.has_options = True
_CENTERNET_KEYPOINTESTIMATION_KEYPOINTLABELTOSTDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
