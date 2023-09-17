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
from cdp.domains.background_service.types import (
    ServiceName
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class BackgroundService(BaseDomain):
    def start_observing(
            self,
            service: 'ServiceName'
    ) -> 'IResponse[None]':
        params = {
            'service': service,
        }

        return self._send_command(
            'BackgroundService.startObserving',
            params,
            False
        )

    def stop_observing(
            self,
            service: 'ServiceName'
    ) -> 'IResponse[None]':
        params = {
            'service': service,
        }

        return self._send_command(
            'BackgroundService.stopObserving',
            params,
            False
        )

    def set_recording(
            self,
            should_record: 'bool',
            service: 'ServiceName'
    ) -> 'IResponse[None]':
        params = {
            'shouldRecord': should_record,
            'service': service,
        }

        return self._send_command(
            'BackgroundService.setRecording',
            params,
            False
        )

    def clear_events(
            self,
            service: 'ServiceName'
    ) -> 'IResponse[None]':
        params = {
            'service': service,
        }

        return self._send_command(
            'BackgroundService.clearEvents',
            params,
            False
        )
