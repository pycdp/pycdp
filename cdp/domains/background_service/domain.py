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
from cdp.domains.background_service.types import (
    ServiceName
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class BackgroundService(BaseDomain):
    def start_observing(
        self,
        service: ServiceName
    ) -> 'StartObservingReturnT':
        params = {
            'service': service,
        }
        
        return self._send_command(
            'BackgroundService.startObserving',

            params
        )

    def stop_observing(
        self,
        service: ServiceName
    ) -> 'StopObservingReturnT':
        params = {
            'service': service,
        }
        
        return self._send_command(
            'BackgroundService.stopObserving',

            params
        )

    def set_recording(
        self,
        should_record: bool,
        service: ServiceName
    ) -> 'SetRecordingReturnT':
        params = {
            'shouldRecord': should_record,
            'service': service,
        }
        
        return self._send_command(
            'BackgroundService.setRecording',

            params
        )

    def clear_events(
        self,
        service: ServiceName
    ) -> 'ClearEventsReturnT':
        params = {
            'service': service,
        }
        
        return self._send_command(
            'BackgroundService.clearEvents',

            params
        )

