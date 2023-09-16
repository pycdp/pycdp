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
    from cdp.domains.dom.types import (
        RGBA
    )
    from cdp.domains.page.types import (
        Viewport
    )
    from cdp.domains.network.types import (
        TimeSinceEpoch
    )

VirtualTimePolicy = Literal[
    'advance',
    'pause',
    'pauseIfNetworkFetchesPending'
]

DisabledImageType = Literal[
    'avif',
    'webp'
]


@dataclass
class ScreenOrientation:
    type: str
    angle: int
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'type': self.type,
                'angle': self.angle,
            }        
        if casing_strategy == 'camel':
            return {
                'type': self.type,
                'angle': self.angle,
            }        
        if casing_strategy == 'pascal':
            return {
                'Type': self.type,
                'Angle': self.angle,
            }


@dataclass
class DisplayFeature:
    orientation: str
    offset: int
    mask_length: int
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'orientation': self.orientation,
                'offset': self.offset,
                'mask_length': self.mask_length,
            }        
        if casing_strategy == 'camel':
            return {
                'orientation': self.orientation,
                'offset': self.offset,
                'maskLength': self.mask_length,
            }        
        if casing_strategy == 'pascal':
            return {
                'Orientation': self.orientation,
                'Offset': self.offset,
                'MaskLength': self.mask_length,
            }


@dataclass
class MediaFeature:
    name: str
    value: str
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
class UserAgentBrandVersion:
    brand: str
    version: str
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'brand': self.brand,
                'version': self.version,
            }        
        if casing_strategy == 'camel':
            return {
                'brand': self.brand,
                'version': self.version,
            }        
        if casing_strategy == 'pascal':
            return {
                'Brand': self.brand,
                'Version': self.version,
            }


@dataclass
class UserAgentMetadata:
    brands: list
    full_version_list: list
    full_version: str
    platform: str
    platform_version: str
    architecture: str
    model: str
    mobile: bool
    bitness: str
    wow64: bool
    def to_dict(
        self,
        casing_strategy: Literal['snake', 'camel', 'pascal'] = 'snake'
    ):
        
        if casing_strategy == 'snake':
            return {
                'brands': [
                    _.to_dict(casing_strategy)
                    for _ in self.brands
                ],
                'full_version_list': [
                    _.to_dict(casing_strategy)
                    for _ in self.full_version_list
                ],
                'full_version': self.full_version,
                'platform': self.platform,
                'platform_version': self.platform_version,
                'architecture': self.architecture,
                'model': self.model,
                'mobile': self.mobile,
                'bitness': self.bitness,
                'wow64': self.wow64,
            }        
        if casing_strategy == 'camel':
            return {
                'brands': [
                    _.to_dict(casing_strategy)
                    for _ in self.brands
                ],
                'fullVersionList': [
                    _.to_dict(casing_strategy)
                    for _ in self.full_version_list
                ],
                'fullVersion': self.full_version,
                'platform': self.platform,
                'platformVersion': self.platform_version,
                'architecture': self.architecture,
                'model': self.model,
                'mobile': self.mobile,
                'bitness': self.bitness,
                'wow64': self.wow64,
            }        
        if casing_strategy == 'pascal':
            return {
                'Brands': [
                    _.to_dict(casing_strategy)
                    for _ in self.brands
                ],
                'FullVersionList': [
                    _.to_dict(casing_strategy)
                    for _ in self.full_version_list
                ],
                'FullVersion': self.full_version,
                'Platform': self.platform,
                'PlatformVersion': self.platform_version,
                'Architecture': self.architecture,
                'Model': self.model,
                'Mobile': self.mobile,
                'Bitness': self.bitness,
                'Wow64': self.wow64,
            }


@dataclass
class CanEmulateReturnT:
    result: bool


@dataclass
class SetVirtualTimePolicyReturnT:
    virtual_time_ticks_base: float
