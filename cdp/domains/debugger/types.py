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
    from cdp.domains.runtime.types import (
        CallArgument,
        ExceptionDetails,
        RemoteObject,
        RemoteObjectId,
        ScriptId,
        StackTrace,
        StackTraceId,
        TimeDelta,
        UniqueDebuggerId
    )

BreakpointId = str

CallFrameId = str


@dataclass
class Location:
    script_id: 'ScriptId'
    line_number: int
    column_number: int
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'script_id': self.script_id.to_dict(
                    casing_strategy
                ),
                'line_number': self.line_number,
                'column_number': self.column_number,
            }
        if casing_strategy == 'camel':
            return {
                'scriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
            }
        if casing_strategy == 'pascal':
            return {
                'ScriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
            }


@dataclass
class ScriptPosition:
    line_number: int
    column_number: int
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'line_number': self.line_number,
                'column_number': self.column_number,
            }
        if casing_strategy == 'camel':
            return {
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
            }
        if casing_strategy == 'pascal':
            return {
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
            }


@dataclass
class CallFrame:
    call_frame_id: 'CallFrameId'
    function_name: str
    function_location: 'Location'
    location: 'Location'
    url: str
    scope_chain: list
    this: 'RemoteObject'
    return_value: 'RemoteObject'
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'call_frame_id': self.call_frame_id.to_dict(
                    casing_strategy
                ),
                'function_name': self.function_name,
                'function_location': self.function_location.to_dict(
                    casing_strategy
                ),
                'location': self.location.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'scope_chain': _.to_dict(
                    casing_strategy
                )_scope_chain,
                'this': self.this.to_dict(
                    casing_strategy
                ),
                'return_value': self.return_value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'callFrameId': self.call_frame_id.to_dict(
                    casing_strategy
                ),
                'functionName': self.function_name,
                'functionLocation': self.function_location.to_dict(
                    casing_strategy
                ),
                'location': self.location.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'scopeChain': _.to_dict(
                    casing_strategy
                )_scope_chain,
                'this': self.this.to_dict(
                    casing_strategy
                ),
                'returnValue': self.return_value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'CallFrameId': self.call_frame_id.to_dict(
                    casing_strategy
                ),
                'FunctionName': self.function_name,
                'FunctionLocation': self.function_location.to_dict(
                    casing_strategy
                ),
                'Location': self.location.to_dict(
                    casing_strategy
                ),
                'Url': self.url,
                'ScopeChain': _.to_dict(
                    casing_strategy
                )_scope_chain,
                'This': self.this.to_dict(
                    casing_strategy
                ),
                'ReturnValue': self.return_value.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class Scope:
    type: str
    object: 'RemoteObject'
    name: str
    start_location: 'Location'
    end_location: 'Location'
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'type': self.type_,
                'object': self.object_.to_dict(
                    casing_strategy
                ),
                'name': self.name,
                'start_location': self.start_location.to_dict(
                    casing_strategy
                ),
                'end_location': self.end_location.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'type': self.type_,
                'object': self.object_.to_dict(
                    casing_strategy
                ),
                'name': self.name,
                'startLocation': self.start_location.to_dict(
                    casing_strategy
                ),
                'endLocation': self.end_location.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Type': self.type_,
                'Object': self.object_.to_dict(
                    casing_strategy
                ),
                'Name': self.name,
                'StartLocation': self.start_location.to_dict(
                    casing_strategy
                ),
                'EndLocation': self.end_location.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class SearchMatch:
    line_number: float
    line_content: str
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'line_number': self.line_number,
                'line_content': self.line_content,
            }
        if casing_strategy == 'camel':
            return {
                'lineNumber': self.line_number,
                'lineContent': self.line_content,
            }
        if casing_strategy == 'pascal':
            return {
                'LineNumber': self.line_number,
                'LineContent': self.line_content,
            }


@dataclass
class BreakLocation:
    script_id: 'ScriptId'
    line_number: int
    column_number: int
    type: str
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'script_id': self.script_id.to_dict(
                    casing_strategy
                ),
                'line_number': self.line_number,
                'column_number': self.column_number,
                'type': self.type_,
            }
        if casing_strategy == 'camel':
            return {
                'scriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
                'type': self.type_,
            }
        if casing_strategy == 'pascal':
            return {
                'ScriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
                'Type': self.type_,
            }


@dataclass
class EnableReturnT:
    debugger_id: 'UniqueDebuggerId'


@dataclass
class EvaluateOnCallFrameReturnT:
    result: 'RemoteObject'
    exception_details: 'ExceptionDetails'


@dataclass
class GetPossibleBreakpointsReturnT:
    locations: list


@dataclass
class GetScriptSourceReturnT:
    script_source: str


@dataclass
class GetStackTraceReturnT:
    stack_trace: 'StackTrace'


@dataclass
class RestartFrameReturnT:
    call_frames: list
    async_stack_trace: 'StackTrace'
    async_stack_trace_id: 'StackTraceId'


@dataclass
class SearchInContentReturnT:
    result: list


@dataclass
class SetBreakpointReturnT:
    breakpoint_id: 'BreakpointId'
    actual_location: 'Location'


@dataclass
class SetInstrumentationBreakpointReturnT:
    breakpoint_id: 'BreakpointId'


@dataclass
class SetBreakpointByUrlReturnT:
    breakpoint_id: 'BreakpointId'
    locations: list


@dataclass
class SetBreakpointOnFunctionCallReturnT:
    breakpoint_id: 'BreakpointId'


@dataclass
class SetScriptSourceReturnT:
    call_frames: list
    stack_changed: bool
    async_stack_trace: 'StackTrace'
    async_stack_trace_id: 'StackTraceId'
    exception_details: 'ExceptionDetails'
