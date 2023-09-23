# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from typing import (
    Literal,
    NotRequired,
    TypedDict
)

SubsamplingFormat = Literal[
    'yuv420',
    'yuv422',
    'yuv444'
]

ImageType = Literal[
    'jpeg',
    'webp',
    'unknown'
]


class GPUDevice(TypedDict):
    vendor_id: float
    device_id: float
    vendor_string: str
    device_string: str
    driver_vendor: str
    driver_version: str
    sub_sys_id: NotRequired[float]
    revision: NotRequired[float]


class Size(TypedDict):
    width: int
    height: int


class VideoDecodeAcceleratorCapability(TypedDict):
    profile: str
    max_resolution: 'Size'
    min_resolution: 'Size'


class VideoEncodeAcceleratorCapability(TypedDict):
    profile: str
    max_resolution: 'Size'
    max_framerate_numerator: int
    max_framerate_denominator: int


class ImageDecodeAcceleratorCapability(TypedDict):
    image_type: 'ImageType'
    max_dimensions: 'Size'
    min_dimensions: 'Size'
    subsamplings: list


class GPUInfo(TypedDict):
    devices: list
    driver_bug_workarounds: list
    video_decoding: list
    video_encoding: list
    image_decoding: list
    aux_attributes: NotRequired[dict]
    feature_status: NotRequired[dict]


class ProcessInfo(TypedDict):
    type: str
    id: int
    cpu_time: float


class GetFeatureStateParamsT(TypedDict):
    feature_state: str


class GetInfoReturnT(TypedDict):
    gpu: 'GPUInfo'
    model_name: str
    model_version: str
    command_line: str


class GetFeatureStateReturnT(TypedDict):
    feature_enabled: bool


class GetProcessInfoReturnT(TypedDict):
    process_info: list
