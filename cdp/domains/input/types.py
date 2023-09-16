# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    Literal,
    TYPE_CHECKING
)
from dataclasses import (
    dataclass
)

TimeSinceEpoch = float
GestureSourceType = Literal[
    'default',
    'touch',
    'mouse'
]
MouseButton = Literal[
    'none',
    'left',
    'middle',
    'right',
    'back',
    'forward'
]

@dataclass
class TouchPoint:
    x: float
    y: float
    radius_x: float
    radius_y: float
    rotation_angle: float
    force: float
    tangential_pressure: float
    tilt_x: int
    tilt_y: int
    twist: int
    id: float


@dataclass
class DragDataItem:
    mime_type: str
    data: str
    title: str
    base_url: str


@dataclass
class DragData:
    items: list['DragDataItem']
    files: list[str]
    drag_operations_mask: int
