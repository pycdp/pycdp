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

RequestId = str

DeviceId = str


@dataclass
class PromptDevice:
    id: 'DeviceId'
    name: str
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
                'id': self.id_.to_dict(
                    casing_strategy
                ),
                'name': self.name,
            }
        if casing_strategy == 'camel':
            return {
                'id': self.id_.to_dict(
                    casing_strategy
                ),
                'name': self.name,
            }
        if casing_strategy == 'pascal':
            return {
                'Id': self.id_.to_dict(
                    casing_strategy
                ),
                'Name': self.name,
            }
