from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.debugger.types import (
    Location,
    CallFrameId,
    BreakpointId
)
from cdp.domains.runtime.types import (
    CallArgument,
    StackTraceId,
    ScriptId,
    RemoteObjectId,
    RemoteObject,
    UniqueDebuggerId,
    StackTrace,
    ExceptionDetails,
    TimeDelta
)


@dataclass
class Debugger(BaseDomain):
    def continue_to_location(
        self,
        location: Location,
        target_call_frames: str = UNDEFINED
    ):
        params = {
            "location": location,
        }

        if is_defined(
            target_call_frames
        ):
            params["targetCallFrames"] = target_call_frames

        return self._send_command(
            "Debugger.continueToLocation",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.disable",
            params
        )

    def enable(
        self,
        max_scripts_cache_size: float = UNDEFINED
    ):
        params = {}

        if is_defined(
            max_scripts_cache_size
        ):
            params["maxScriptsCacheSize"] = max_scripts_cache_size

        return self._send_command(
            "Debugger.enable",
            params
        )

    def evaluate_on_call_frame(
        self,
        call_frame_id: CallFrameId,
        expression: str,
        object_group: str = UNDEFINED,
        include_command_line_api: bool = UNDEFINED,
        silent: bool = UNDEFINED,
        return_by_value: bool = UNDEFINED,
        generate_preview: bool = UNDEFINED,
        throw_on_side_effect: bool = UNDEFINED,
        timeout: TimeDelta = UNDEFINED
    ):
        params = {
            "callFrameId": call_frame_id,
            "expression": expression,
        }

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        if is_defined(
            include_command_line_api
        ):
            params["includeCommandLineAPI"] = include_command_line_api

        if is_defined(
            silent
        ):
            params["silent"] = silent

        if is_defined(
            return_by_value
        ):
            params["returnByValue"] = return_by_value

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        if is_defined(
            throw_on_side_effect
        ):
            params["throwOnSideEffect"] = throw_on_side_effect

        if is_defined(
            timeout
        ):
            params["timeout"] = timeout

        return self._send_command(
            "Debugger.evaluateOnCallFrame",
            params
        )

    def get_possible_breakpoints(
        self,
        start: Location,
        end: Location = UNDEFINED,
        restrict_to_function: bool = UNDEFINED
    ):
        params = {
            "start": start,
        }

        if is_defined(
            end
        ):
            params["end"] = end

        if is_defined(
            restrict_to_function
        ):
            params["restrictToFunction"] = restrict_to_function

        return self._send_command(
            "Debugger.getPossibleBreakpoints",
            params
        )

    def get_script_source(
        self,
        script_id: ScriptId
    ):
        params = {
            "scriptId": script_id,
        }

        return self._send_command(
            "Debugger.getScriptSource",
            params
        )

    def get_stack_trace(
        self,
        stack_trace_id: StackTraceId
    ):
        params = {
            "stackTraceId": stack_trace_id,
        }

        return self._send_command(
            "Debugger.getStackTrace",
            params
        )

    def pause(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.pause",
            params
        )

    def pause_on_async_call(
        self,
        parent_stack_trace_id: StackTraceId
    ):
        params = {
            "parentStackTraceId": parent_stack_trace_id,
        }

        return self._send_command(
            "Debugger.pauseOnAsyncCall",
            params
        )

    def remove_breakpoint(
        self,
        breakpoint_id: BreakpointId
    ):
        params = {
            "breakpointId": breakpoint_id,
        }

        return self._send_command(
            "Debugger.removeBreakpoint",
            params
        )

    def restart_frame(
        self,
        call_frame_id: CallFrameId
    ):
        params = {
            "callFrameId": call_frame_id,
        }

        return self._send_command(
            "Debugger.restartFrame",
            params
        )

    def resume(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.resume",
            params
        )

    def search_in_content(
        self,
        script_id: ScriptId,
        query: str,
        case_sensitive: bool = UNDEFINED,
        is_regex: bool = UNDEFINED
    ):
        params = {
            "scriptId": script_id,
            "query": query,
        }

        if is_defined(
            case_sensitive
        ):
            params["caseSensitive"] = case_sensitive

        if is_defined(
            is_regex
        ):
            params["isRegex"] = is_regex

        return self._send_command(
            "Debugger.searchInContent",
            params
        )

    def set_async_call_stack_depth(
        self,
        max_depth: int
    ):
        params = {
            "maxDepth": max_depth,
        }

        return self._send_command(
            "Debugger.setAsyncCallStackDepth",
            params
        )

    def set_blackbox_patterns(
        self,
        patterns: list
    ):
        params = {
            "patterns": patterns,
        }

        return self._send_command(
            "Debugger.setBlackboxPatterns",
            params
        )

    def set_blackboxed_ranges(
        self,
        script_id: ScriptId,
        positions: list
    ):
        params = {
            "scriptId": script_id,
            "positions": positions,
        }

        return self._send_command(
            "Debugger.setBlackboxedRanges",
            params
        )

    def set_breakpoint(
        self,
        location: Location,
        condition: str = UNDEFINED
    ):
        params = {
            "location": location,
        }

        if is_defined(
            condition
        ):
            params["condition"] = condition

        return self._send_command(
            "Debugger.setBreakpoint",
            params
        )

    def set_instrumentation_breakpoint(
        self,
        instrumentation: str
    ):
        params = {
            "instrumentation": instrumentation,
        }

        return self._send_command(
            "Debugger.setInstrumentationBreakpoint",
            params
        )

    def set_breakpoint_by_url(
        self,
        line_number: int,
        url: str = UNDEFINED,
        url_regex: str = UNDEFINED,
        script_hash: str = UNDEFINED,
        column_number: int = UNDEFINED,
        condition: str = UNDEFINED
    ):
        params = {
            "lineNumber": line_number,
        }

        if is_defined(
            url
        ):
            params["url"] = url

        if is_defined(
            url_regex
        ):
            params["urlRegex"] = url_regex

        if is_defined(
            script_hash
        ):
            params["scriptHash"] = script_hash

        if is_defined(
            column_number
        ):
            params["columnNumber"] = column_number

        if is_defined(
            condition
        ):
            params["condition"] = condition

        return self._send_command(
            "Debugger.setBreakpointByUrl",
            params
        )

    def set_breakpoint_on_function_call(
        self,
        object_id: RemoteObjectId,
        condition: str = UNDEFINED
    ):
        params = {
            "objectId": object_id,
        }

        if is_defined(
            condition
        ):
            params["condition"] = condition

        return self._send_command(
            "Debugger.setBreakpointOnFunctionCall",
            params
        )

    def set_breakpoints_active(
        self,
        active: bool
    ):
        params = {
            "active": active,
        }

        return self._send_command(
            "Debugger.setBreakpointsActive",
            params
        )

    def set_pause_on_exceptions(
        self,
        state: str
    ):
        params = {
            "state": state,
        }

        return self._send_command(
            "Debugger.setPauseOnExceptions",
            params
        )

    def set_return_value(
        self,
        new_value: CallArgument
    ):
        params = {
            "newValue": new_value,
        }

        return self._send_command(
            "Debugger.setReturnValue",
            params
        )

    def set_script_source(
        self,
        script_id: ScriptId,
        script_source: str,
        dry_run: bool = UNDEFINED
    ):
        params = {
            "scriptId": script_id,
            "scriptSource": script_source,
        }

        if is_defined(
            dry_run
        ):
            params["dryRun"] = dry_run

        return self._send_command(
            "Debugger.setScriptSource",
            params
        )

    def set_skip_all_pauses(
        self,
        skip: bool
    ):
        params = {
            "skip": skip,
        }

        return self._send_command(
            "Debugger.setSkipAllPauses",
            params
        )

    def set_variable_value(
        self,
        scope_number: int,
        variable_name: str,
        new_value: CallArgument,
        call_frame_id: CallFrameId
    ):
        params = {
            "scopeNumber": scope_number,
            "variableName": variable_name,
            "newValue": new_value,
            "callFrameId": call_frame_id,
        }

        return self._send_command(
            "Debugger.setVariableValue",
            params
        )

    def step_into(
        self,
        break_on_async_call: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            break_on_async_call
        ):
            params["breakOnAsyncCall"] = break_on_async_call

        return self._send_command(
            "Debugger.stepInto",
            params
        )

    def step_out(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.stepOut",
            params
        )

    def step_over(
        self
    ):
        params = {}

        return self._send_command(
            "Debugger.stepOver",
            params
        )

