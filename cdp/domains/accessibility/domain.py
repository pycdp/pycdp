# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.mapper import (
    from_dict,
    to_dict
)
from cdp.domains.accessibility.types import (
    AXNodeId,
    GetAXNodeAndAncestorsReturnT,
    GetChildAXNodesReturnT,
    GetFullAXTreeReturnT,
    GetPartialAXTreeReturnT,
    GetRootAXNodeReturnT,
    QueryAXTreeReturnT
)
from cdp.domains.dom.types import (
    BackendNodeId,
    NodeId
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)
from cdp.domains.page.types import (
    FrameId
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Accessibility(BaseDomain):
    def disable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Accessibility.disable',
            params,
            False
        )

    def enable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Accessibility.enable',
            params,
            False
        )

    def get_partial_ax_tree(
            self,
            node_id: 'NodeId' = UNDEFINED,
            backend_node_id: 'BackendNodeId' = UNDEFINED,
            object_id: 'RemoteObjectId' = UNDEFINED,
            fetch_relatives: 'bool' = UNDEFINED
    ) -> 'IResponse[GetPartialAXTreeReturnT]':
        params = {}

        if is_defined(node_id):
            params['nodeId'] = node_id

        if is_defined(backend_node_id):
            params['backendNodeId'] = backend_node_id

        if is_defined(object_id):
            params['objectId'] = object_id

        if is_defined(fetch_relatives):
            params['fetchRelatives'] = fetch_relatives

        return self._send_command(
            'Accessibility.getPartialAXTree',
            params,
            True,
            lambda data: from_dict(
                GetPartialAXTreeReturnT,
                data,
                'camel'
            )
        )

    def get_full_ax_tree(
            self,
            depth: 'int' = UNDEFINED,
            frame_id: 'FrameId' = UNDEFINED
    ) -> 'IResponse[GetFullAXTreeReturnT]':
        params = {}

        if is_defined(depth):
            params['depth'] = depth

        if is_defined(frame_id):
            params['frameId'] = frame_id

        return self._send_command(
            'Accessibility.getFullAXTree',
            params,
            True,
            lambda data: from_dict(
                GetFullAXTreeReturnT,
                data,
                'camel'
            )
        )

    def get_root_ax_node(
            self,
            frame_id: 'FrameId' = UNDEFINED
    ) -> 'IResponse[GetRootAXNodeReturnT]':
        params = {}

        if is_defined(frame_id):
            params['frameId'] = frame_id

        return self._send_command(
            'Accessibility.getRootAXNode',
            params,
            True,
            lambda data: from_dict(
                GetRootAXNodeReturnT,
                data,
                'camel'
            )
        )

    def get_ax_node_and_ancestors(
            self,
            node_id: 'NodeId' = UNDEFINED,
            backend_node_id: 'BackendNodeId' = UNDEFINED,
            object_id: 'RemoteObjectId' = UNDEFINED
    ) -> 'IResponse[GetAXNodeAndAncestorsReturnT]':
        params = {}

        if is_defined(node_id):
            params['nodeId'] = node_id

        if is_defined(backend_node_id):
            params['backendNodeId'] = backend_node_id

        if is_defined(object_id):
            params['objectId'] = object_id

        return self._send_command(
            'Accessibility.getAXNodeAndAncestors',
            params,
            True,
            lambda data: from_dict(
                GetAXNodeAndAncestorsReturnT,
                data,
                'camel'
            )
        )

    def get_child_ax_nodes(
            self,
            id_: 'AXNodeId',
            frame_id: 'FrameId' = UNDEFINED
    ) -> 'IResponse[GetChildAXNodesReturnT]':
        params = {
            'id': id_,
        }

        if is_defined(frame_id):
            params['frameId'] = frame_id

        return self._send_command(
            'Accessibility.getChildAXNodes',
            params,
            True,
            lambda data: from_dict(
                GetChildAXNodesReturnT,
                data,
                'camel'
            )
        )

    def query_ax_tree(
            self,
            node_id: 'NodeId' = UNDEFINED,
            backend_node_id: 'BackendNodeId' = UNDEFINED,
            object_id: 'RemoteObjectId' = UNDEFINED,
            accessible_name: 'str' = UNDEFINED,
            role: 'str' = UNDEFINED
    ) -> 'IResponse[QueryAXTreeReturnT]':
        params = {}

        if is_defined(node_id):
            params['nodeId'] = node_id

        if is_defined(backend_node_id):
            params['backendNodeId'] = backend_node_id

        if is_defined(object_id):
            params['objectId'] = object_id

        if is_defined(accessible_name):
            params['accessibleName'] = accessible_name

        if is_defined(role):
            params['role'] = role

        return self._send_command(
            'Accessibility.queryAXTree',
            params,
            True,
            lambda data: from_dict(
                QueryAXTreeReturnT,
                data,
                'camel'
            )
        )
