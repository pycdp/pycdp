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
from cdp.domains.schema.types import (
    GetDomainsReturnT
)


@dataclass
class Schema(BaseDomain):
    def get_domains(
            self
    ) -> 'GetDomainsReturnT':
        params = {}

        return self._send_command(
            'Schema.getDomains',
            params
        )
