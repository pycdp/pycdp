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
    from cdp.domains.page.types import (
        FrameId
    )
    from cdp.domains.browser.types import (
        BrowserContextID
    )

TargetID = str

SessionID = str

TargetFilter = list['FilterEntry']


@dataclass
class TargetInfo:
    target_id: 'TargetID'
    type: str
    title: str
    url: str
    attached: bool
    opener_id: 'TargetID'
    can_access_opener: bool
    opener_frame_id: 'FrameId'
    browser_context_id: 'BrowserContextID'
    subtype: str
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
                'target_id': self.target_id.to_dict(
                    casing_strategy
                ),
                'type': self.type_,
                'title': self.title,
                'url': self.url,
                'attached': self.attached,
                'opener_id': self.opener_id.to_dict(
                    casing_strategy
                ),
                'can_access_opener': self.can_access_opener,
                'opener_frame_id': self.opener_frame_id.to_dict(
                    casing_strategy
                ),
                'browser_context_id': self.browser_context_id.to_dict(
                    casing_strategy
                ),
                'subtype': self.subtype,
            }
        if casing_strategy == 'camel':
            return {
                'targetId': self.target_id.to_dict(
                    casing_strategy
                ),
                'type': self.type_,
                'title': self.title,
                'url': self.url,
                'attached': self.attached,
                'openerId': self.opener_id.to_dict(
                    casing_strategy
                ),
                'canAccessOpener': self.can_access_opener,
                'openerFrameId': self.opener_frame_id.to_dict(
                    casing_strategy
                ),
                'browserContextId': self.browser_context_id.to_dict(
                    casing_strategy
                ),
                'subtype': self.subtype,
            }
        if casing_strategy == 'pascal':
            return {
                'TargetId': self.target_id.to_dict(
                    casing_strategy
                ),
                'Type': self.type_,
                'Title': self.title,
                'Url': self.url,
                'Attached': self.attached,
                'OpenerId': self.opener_id.to_dict(
                    casing_strategy
                ),
                'CanAccessOpener': self.can_access_opener,
                'OpenerFrameId': self.opener_frame_id.to_dict(
                    casing_strategy
                ),
                'BrowserContextId': self.browser_context_id.to_dict(
                    casing_strategy
                ),
                'Subtype': self.subtype,
            }


@dataclass
class FilterEntry:
    exclude: bool
    type: str
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
                'exclude': self.exclude,
                'type': self.type_,
            }
        if casing_strategy == 'camel':
            return {
                'exclude': self.exclude,
                'type': self.type_,
            }
        if casing_strategy == 'pascal':
            return {
                'Exclude': self.exclude,
                'Type': self.type_,
            }


@dataclass
class RemoteLocation:
    host: str
    port: int
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
                'host': self.host,
                'port': self.port,
            }
        if casing_strategy == 'camel':
            return {
                'host': self.host,
                'port': self.port,
            }
        if casing_strategy == 'pascal':
            return {
                'Host': self.host,
                'Port': self.port,
            }


@dataclass
class AttachToTargetReturnT:
    session_id: 'SessionID'


@dataclass
class AttachToBrowserTargetReturnT:
    session_id: 'SessionID'


@dataclass
class CloseTargetReturnT:
    success: bool


@dataclass
class CreateBrowserContextReturnT:
    browser_context_id: 'BrowserContextID'


@dataclass
class GetBrowserContextsReturnT:
    browser_context_ids: list


@dataclass
class CreateTargetReturnT:
    target_id: 'TargetID'


@dataclass
class GetTargetInfoReturnT:
    target_info: 'TargetInfo'


@dataclass
class GetTargetsReturnT:
    target_infos: list
