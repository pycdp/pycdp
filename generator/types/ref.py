from dataclasses import dataclass

from generator.types.base import Node
from generator.utils import UNDEFINED, MaybeUndefined, snake_case


@dataclass
class Ref(Node):
    domain: MaybeUndefined[str]
    type: str

    @property
    def domain_snake_case(self):
        return snake_case(self.domain)

    @classmethod
    def from_str(cls, s: str):
        if '.' in s:
            s = s.split('.')
            return cls(
                domain=s[0],
                type=s[1]
            )

        else:
            return cls(
                domain=UNDEFINED,
                type=s
            )
