# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.types import (
    dom
)
from typing import (
    Literal,
    TypedDict
)

LayerId = str

SnapshotId = str

PaintProfile = list


class ScrollRect(TypedDict):
    rect: 'dom.Rect'
    type: str


class StickyPositionConstraint(TypedDict):
    sticky_box_rect: 'dom.Rect'
    containing_block_rect: 'dom.Rect'
    nearest_layer_shifting_sticky_box: 'LayerId'
    nearest_layer_shifting_containing_block: 'LayerId'


class PictureTile(TypedDict):
    x: float
    y: float
    picture: str


class Layer(TypedDict):
    layer_id: 'LayerId'
    offset_x: float
    offset_y: float
    width: float
    height: float
    paint_count: int
    draws_content: bool
    parent_layer_id: 'LayerId'
    backend_node_id: 'dom.BackendNodeId'
    transform: list
    anchor_x: float
    anchor_y: float
    anchor_z: float
    invisible: bool
    scroll_rects: list
    sticky_position_constraint: 'StickyPositionConstraint'


class CompositingReasonsParamsT(TypedDict):
    layer_id: 'LayerId'


class LoadSnapshotParamsT(TypedDict):
    tiles: list


class MakeSnapshotParamsT(TypedDict):
    layer_id: 'LayerId'


class ProfileSnapshotParamsT(TypedDict):
    snapshot_id: 'SnapshotId'
    min_repeat_count: int
    min_duration: float
    clip_rect: 'dom.Rect'


class ReleaseSnapshotParamsT(TypedDict):
    snapshot_id: 'SnapshotId'


class ReplaySnapshotParamsT(TypedDict):
    snapshot_id: 'SnapshotId'
    from_step: int
    to_step: int
    scale: float


class SnapshotCommandLogParamsT(TypedDict):
    snapshot_id: 'SnapshotId'


class CompositingReasonsReturnT(TypedDict):
    compositing_reasons: list
    compositing_reason_ids: list


class LoadSnapshotReturnT(TypedDict):
    snapshot_id: 'SnapshotId'


class MakeSnapshotReturnT(TypedDict):
    snapshot_id: 'SnapshotId'


class ProfileSnapshotReturnT(TypedDict):
    timings: list


class ReplaySnapshotReturnT(TypedDict):
    data_url: str


class SnapshotCommandLogReturnT(TypedDict):
    command_log: list


class LayerPaintedEventT(TypedDict):
    name: Literal['layer_painted']
    params: 'LayerPaintedParamsT'


class LayerTreeDidChangeEventT(TypedDict):
    name: Literal['layer_tree_did_change']
    params: 'LayerTreeDidChangeParamsT'


class LayerPaintedParamsT(TypedDict):
    layer_id: 'LayerId'
    clip: 'dom.Rect'


class LayerTreeDidChangeParamsT(TypedDict):
    layers: list
