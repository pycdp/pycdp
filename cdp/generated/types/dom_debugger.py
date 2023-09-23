# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    dom,
    runtime
)
from typing import (
    Literal,
    NotRequired,
    TypedDict
)

DOMBreakpointType = Literal[
    'subtree-modified',
    'attribute-modified',
    'node-removed'
]

CSPViolationType = Literal[
    'trustedtype-sink-violation',
    'trustedtype-policy-violation'
]


class EventListener(TypedDict):
    type: str
    use_capture: bool
    passive: bool
    once: bool
    script_id: 'runtime.ScriptId'
    line_number: int
    column_number: int
    handler: NotRequired['runtime.RemoteObject']
    original_handler: NotRequired['runtime.RemoteObject']
    backend_node_id: NotRequired['dom.BackendNodeId']


class GetEventListenersParamsT(TypedDict):
    object_id: 'runtime.RemoteObjectId'
    depth: NotRequired[int]
    pierce: NotRequired[bool]


class RemoveDOMBreakpointParamsT(TypedDict):
    node_id: 'dom.NodeId'
    type: 'DOMBreakpointType'


class RemoveEventListenerBreakpointParamsT(TypedDict):
    event_name: str
    target_name: NotRequired[str]


class RemoveInstrumentationBreakpointParamsT(TypedDict):
    event_name: str


class RemoveXHRBreakpointParamsT(TypedDict):
    url: str


class SetBreakOnCSPViolationParamsT(TypedDict):
    violation_types: list


class SetDOMBreakpointParamsT(TypedDict):
    node_id: 'dom.NodeId'
    type: 'DOMBreakpointType'


class SetEventListenerBreakpointParamsT(TypedDict):
    event_name: str
    target_name: NotRequired[str]


class SetInstrumentationBreakpointParamsT(TypedDict):
    event_name: str


class SetXHRBreakpointParamsT(TypedDict):
    url: str


class GetEventListenersReturnT(TypedDict):
    listeners: list
