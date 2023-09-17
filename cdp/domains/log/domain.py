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
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Log(BaseDomain):
    def clear(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Log.clear',
            params,
            False
        )

    def disable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Log.disable',
            params,
            False
        )

    def enable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Log.enable',
            params,
            False
        )

    def start_violations_report(
            self,
            config: 'list'
    ) -> 'IResponse[None]':
        params = {
            'config': [
                to_dict(item, 'camel')
                for item in config
            ],
        }

        return self._send_command(
            'Log.startViolationsReport',
            params,
            False
        )

    def stop_violations_report(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Log.stopViolationsReport',
            params,
            False
        )
