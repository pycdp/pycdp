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
from cdp.domains.dom_snapshot.types import (
    CaptureSnapshotReturnT,
    GetSnapshotReturnT
)


@dataclass
class DOMSnapshot(BaseDomain):
    def disable(
            self
    ) -> None:
        params = {}

        return self._send_command(
            'DOMSnapshot.disable',
            params
        )

    def enable(
            self
    ) -> None:
        params = {}

        return self._send_command(
            'DOMSnapshot.enable',
            params
        )

    def get_snapshot(
            self,
            computed_style_whitelist: list,
            include_event_listeners: bool = UNDEFINED,
            include_paint_order: bool = UNDEFINED,
            include_user_agent_shadow_tree: bool = UNDEFINED
    ) -> 'GetSnapshotReturnT':
        params = {
            'computedStyleWhitelist': computed_style_whitelist,
        }

        if is_defined(include_event_listeners):
            params['includeEventListeners'] = include_event_listeners

        if is_defined(include_paint_order):
            params['includePaintOrder'] = include_paint_order

        if is_defined(include_user_agent_shadow_tree):
            params['includeUserAgentShadowTree'] = include_user_agent_shadow_tree

        return self._send_command(
            'DOMSnapshot.getSnapshot',
            params
        )

    def capture_snapshot(
            self,
            computed_styles: list,
            include_paint_order: bool = UNDEFINED,
            include_dom_rects: bool = UNDEFINED,
            include_blended_background_colors: bool = UNDEFINED,
            include_text_color_opacities: bool = UNDEFINED
    ) -> 'CaptureSnapshotReturnT':
        params = {
            'computedStyles': computed_styles,
        }

        if is_defined(include_paint_order):
            params['includePaintOrder'] = include_paint_order

        if is_defined(include_dom_rects):
            params['includeDOMRects'] = include_dom_rects

        if is_defined(include_blended_background_colors):
            params['includeBlendedBackgroundColors'] = include_blended_background_colors

        if is_defined(include_text_color_opacities):
            params['includeTextColorOpacities'] = include_text_color_opacities

        return self._send_command(
            'DOMSnapshot.captureSnapshot',
            params
        )
