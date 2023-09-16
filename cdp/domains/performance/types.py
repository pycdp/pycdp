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


@dataclass
class Metric:
    name: str
    value: float
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'value': self.value,
            }        
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'value': self.value,
            }        
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Value': self.value,
            }


@dataclass
class GetMetricsReturnT:
    metrics: list
