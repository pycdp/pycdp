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
if TYPE_CHECKING:
    from cdp.domains.dom.types import (
        BackendNodeId,
        Rect
    )

LayerId = str

SnapshotId = str

PaintProfile = list[float]


@dataclass
class ScrollRect:
    rect: 'Rect'
    type: str
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'rect': self.rect.to_dict(casing_strategy),
                'type': self.type,
            }        
        if casing_strategy == 'camel':
            return {
                'rect': self.rect.to_dict(casing_strategy),
                'type': self.type,
            }        
        if casing_strategy == 'pascal':
            return {
                'Rect': self.rect.to_dict(casing_strategy),
                'Type': self.type,
            }


@dataclass
class StickyPositionConstraint:
    sticky_box_rect: 'Rect'
    containing_block_rect: 'Rect'
    nearest_layer_shifting_sticky_box: 'LayerId'
    nearest_layer_shifting_containing_block: 'LayerId'
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'sticky_box_rect': self.sticky_box_rect.to_dict(casing_strategy),
                'containing_block_rect': self.containing_block_rect.to_dict(casing_strategy),
                'nearest_layer_shifting_sticky_box': self.nearest_layer_shifting_sticky_box,
                'nearest_layer_shifting_containing_block': self.nearest_layer_shifting_containing_block,
            }        
        if casing_strategy == 'camel':
            return {
                'stickyBoxRect': self.sticky_box_rect.to_dict(casing_strategy),
                'containingBlockRect': self.containing_block_rect.to_dict(casing_strategy),
                'nearestLayerShiftingStickyBox': self.nearest_layer_shifting_sticky_box,
                'nearestLayerShiftingContainingBlock': self.nearest_layer_shifting_containing_block,
            }        
        if casing_strategy == 'pascal':
            return {
                'StickyBoxRect': self.sticky_box_rect.to_dict(casing_strategy),
                'ContainingBlockRect': self.containing_block_rect.to_dict(casing_strategy),
                'NearestLayerShiftingStickyBox': self.nearest_layer_shifting_sticky_box,
                'NearestLayerShiftingContainingBlock': self.nearest_layer_shifting_containing_block,
            }


@dataclass
class PictureTile:
    x: float
    y: float
    picture: str
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'x': self.x,
                'y': self.y,
                'picture': self.picture,
            }        
        if casing_strategy == 'camel':
            return {
                'x': self.x,
                'y': self.y,
                'picture': self.picture,
            }        
        if casing_strategy == 'pascal':
            return {
                'X': self.x,
                'Y': self.y,
                'Picture': self.picture,
            }


@dataclass
class Layer:
    layer_id: 'LayerId'
    parent_layer_id: 'LayerId'
    backend_node_id: 'BackendNodeId'
    offset_x: float
    offset_y: float
    width: float
    height: float
    transform: list
    anchor_x: float
    anchor_y: float
    anchor_z: float
    paint_count: int
    draws_content: bool
    invisible: bool
    scroll_rects: list
    sticky_position_constraint: 'StickyPositionConstraint'
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'layer_id': self.layer_id,
                'parent_layer_id': self.parent_layer_id,
                'backend_node_id': self.backend_node_id,
                'offset_x': self.offset_x,
                'offset_y': self.offset_y,
                'width': self.width,
                'height': self.height,
                'transform': self.transform,
                'anchor_x': self.anchor_x,
                'anchor_y': self.anchor_y,
                'anchor_z': self.anchor_z,
                'paint_count': self.paint_count,
                'draws_content': self.draws_content,
                'invisible': self.invisible,
                'scroll_rects': [
                    _.to_dict(casing_strategy)
                    for _ in self.scroll_rects
                ],
                'sticky_position_constraint': self.sticky_position_constraint.to_dict(casing_strategy),
            }        
        if casing_strategy == 'camel':
            return {
                'layerId': self.layer_id,
                'parentLayerId': self.parent_layer_id,
                'backendNodeId': self.backend_node_id,
                'offsetX': self.offset_x,
                'offsetY': self.offset_y,
                'width': self.width,
                'height': self.height,
                'transform': self.transform,
                'anchorX': self.anchor_x,
                'anchorY': self.anchor_y,
                'anchorZ': self.anchor_z,
                'paintCount': self.paint_count,
                'drawsContent': self.draws_content,
                'invisible': self.invisible,
                'scrollRects': [
                    _.to_dict(casing_strategy)
                    for _ in self.scroll_rects
                ],
                'stickyPositionConstraint': self.sticky_position_constraint.to_dict(casing_strategy),
            }        
        if casing_strategy == 'pascal':
            return {
                'LayerId': self.layer_id,
                'ParentLayerId': self.parent_layer_id,
                'BackendNodeId': self.backend_node_id,
                'OffsetX': self.offset_x,
                'OffsetY': self.offset_y,
                'Width': self.width,
                'Height': self.height,
                'Transform': self.transform,
                'AnchorX': self.anchor_x,
                'AnchorY': self.anchor_y,
                'AnchorZ': self.anchor_z,
                'PaintCount': self.paint_count,
                'DrawsContent': self.draws_content,
                'Invisible': self.invisible,
                'ScrollRects': [
                    _.to_dict(casing_strategy)
                    for _ in self.scroll_rects
                ],
                'StickyPositionConstraint': self.sticky_position_constraint.to_dict(casing_strategy),
            }


@dataclass
class CompositingReasonsReturnT:
    compositing_reasons: list
    compositing_reason_ids: list


@dataclass
class LoadSnapshotReturnT:
    snapshot_id: 'SnapshotId'


@dataclass
class MakeSnapshotReturnT:
    snapshot_id: 'SnapshotId'


@dataclass
class ProfileSnapshotReturnT:
    timings: list


@dataclass
class ReplaySnapshotReturnT:
    data_url: str


@dataclass
class SnapshotCommandLogReturnT:
    command_log: list
