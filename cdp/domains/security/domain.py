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
from cdp.domains.security.types import (
    CertificateErrorAction
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Security(BaseDomain):
    def disable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Security.disable',
            params,
            False
        )

    def enable(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Security.enable',
            params,
            False
        )

    def set_ignore_certificate_errors(
            self,
            ignore: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'ignore': ignore,
        }

        return self._send_command(
            'Security.setIgnoreCertificateErrors',
            params,
            False
        )

    def handle_certificate_error(
            self,
            event_id: 'int',
            action: 'CertificateErrorAction'
    ) -> 'IResponse[None]':
        params = {
            'eventId': event_id,
            'action': action,
        }

        return self._send_command(
            'Security.handleCertificateError',
            params,
            False
        )

    def set_override_certificate_errors(
            self,
            override: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'override': override,
        }

        return self._send_command(
            'Security.setOverrideCertificateErrors',
            params,
            False
        )
