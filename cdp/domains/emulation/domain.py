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
from cdp.domains.emulation.types import (
    CanEmulateReturnT,
    DisplayFeature,
    ScreenOrientation,
    SetVirtualTimePolicyReturnT,
    UserAgentMetadata,
    VirtualTimePolicy
)
from cdp.domains.dom.types import (
    RGBA
)
from cdp.domains.page.types import (
    Viewport
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Emulation(BaseDomain):
    def can_emulate(
            self
    ) -> 'IResponse[CanEmulateReturnT]':
        params = {}

        return self._send_command(
            'Emulation.canEmulate',
            params,
            True,
            lambda data: from_dict(
                CanEmulateReturnT,
                data,
                'camel'
            )
        )

    def clear_device_metrics_override(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Emulation.clearDeviceMetricsOverride',
            params,
            False
        )

    def clear_geolocation_override(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Emulation.clearGeolocationOverride',
            params,
            False
        )

    def reset_page_scale_factor(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Emulation.resetPageScaleFactor',
            params,
            False
        )

    def set_focus_emulation_enabled(
            self,
            enabled: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Emulation.setFocusEmulationEnabled',
            params,
            False
        )

    def set_auto_dark_mode_override(
            self,
            enabled: 'bool' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {}

        if is_defined(enabled):
            params['enabled'] = enabled

        return self._send_command(
            'Emulation.setAutoDarkModeOverride',
            params,
            False
        )

    def set_cpu_throttling_rate(
            self,
            rate: 'float'
    ) -> 'IResponse[None]':
        params = {
            'rate': rate,
        }

        return self._send_command(
            'Emulation.setCPUThrottlingRate',
            params,
            False
        )

    def set_default_background_color_override(
            self,
            color: 'RGBA' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {}

        if is_defined(color):
            params['color'] = to_dict(
                color,
                'camel'
            )

        return self._send_command(
            'Emulation.setDefaultBackgroundColorOverride',
            params,
            False
        )

    def set_device_metrics_override(
            self,
            width: 'int',
            height: 'int',
            device_scale_factor: 'float',
            mobile: 'bool',
            scale: 'float' = UNDEFINED,
            screen_width: 'int' = UNDEFINED,
            screen_height: 'int' = UNDEFINED,
            position_x: 'int' = UNDEFINED,
            position_y: 'int' = UNDEFINED,
            dont_set_visible_size: 'bool' = UNDEFINED,
            screen_orientation: 'ScreenOrientation' = UNDEFINED,
            viewport: 'Viewport' = UNDEFINED,
            display_feature: 'DisplayFeature' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {
            'width': width,
            'height': height,
            'deviceScaleFactor': device_scale_factor,
            'mobile': mobile,
        }

        if is_defined(scale):
            params['scale'] = scale

        if is_defined(screen_width):
            params['screenWidth'] = screen_width

        if is_defined(screen_height):
            params['screenHeight'] = screen_height

        if is_defined(position_x):
            params['positionX'] = position_x

        if is_defined(position_y):
            params['positionY'] = position_y

        if is_defined(dont_set_visible_size):
            params['dontSetVisibleSize'] = dont_set_visible_size

        if is_defined(screen_orientation):
            params['screenOrientation'] = to_dict(
                screen_orientation,
                'camel'
            )

        if is_defined(viewport):
            params['viewport'] = to_dict(
                viewport,
                'camel'
            )

        if is_defined(display_feature):
            params['displayFeature'] = to_dict(
                display_feature,
                'camel'
            )

        return self._send_command(
            'Emulation.setDeviceMetricsOverride',
            params,
            False
        )

    def set_scrollbars_hidden(
            self,
            hidden: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'hidden': hidden,
        }

        return self._send_command(
            'Emulation.setScrollbarsHidden',
            params,
            False
        )

    def set_document_cookie_disabled(
            self,
            disabled: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'disabled': disabled,
        }

        return self._send_command(
            'Emulation.setDocumentCookieDisabled',
            params,
            False
        )

    def set_emit_touch_events_for_mouse(
            self,
            enabled: 'bool',
            configuration: 'str' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {
            'enabled': enabled,
        }

        if is_defined(configuration):
            params['configuration'] = configuration

        return self._send_command(
            'Emulation.setEmitTouchEventsForMouse',
            params,
            False
        )

    def set_emulated_media(
            self,
            media: 'str' = UNDEFINED,
            features: 'list' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {}

        if is_defined(media):
            params['media'] = media

        if is_defined(features):
            params['features'] = [
                to_dict(item, 'camel')
                for item in features
            ]

        return self._send_command(
            'Emulation.setEmulatedMedia',
            params,
            False
        )

    def set_emulated_vision_deficiency(
            self,
            type_: 'str'
    ) -> 'IResponse[None]':
        params = {
            'type': type_,
        }

        return self._send_command(
            'Emulation.setEmulatedVisionDeficiency',
            params,
            False
        )

    def set_geolocation_override(
            self,
            latitude: 'float' = UNDEFINED,
            longitude: 'float' = UNDEFINED,
            accuracy: 'float' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {}

        if is_defined(latitude):
            params['latitude'] = latitude

        if is_defined(longitude):
            params['longitude'] = longitude

        if is_defined(accuracy):
            params['accuracy'] = accuracy

        return self._send_command(
            'Emulation.setGeolocationOverride',
            params,
            False
        )

    def set_idle_override(
            self,
            is_user_active: 'bool',
            is_screen_unlocked: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'isUserActive': is_user_active,
            'isScreenUnlocked': is_screen_unlocked,
        }

        return self._send_command(
            'Emulation.setIdleOverride',
            params,
            False
        )

    def clear_idle_override(
            self
    ) -> 'IResponse[None]':
        params = {}

        return self._send_command(
            'Emulation.clearIdleOverride',
            params,
            False
        )

    def set_navigator_overrides(
            self,
            platform: 'str'
    ) -> 'IResponse[None]':
        params = {
            'platform': platform,
        }

        return self._send_command(
            'Emulation.setNavigatorOverrides',
            params,
            False
        )

    def set_page_scale_factor(
            self,
            page_scale_factor: 'float'
    ) -> 'IResponse[None]':
        params = {
            'pageScaleFactor': page_scale_factor,
        }

        return self._send_command(
            'Emulation.setPageScaleFactor',
            params,
            False
        )

    def set_script_execution_disabled(
            self,
            value: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'value': value,
        }

        return self._send_command(
            'Emulation.setScriptExecutionDisabled',
            params,
            False
        )

    def set_touch_emulation_enabled(
            self,
            enabled: 'bool',
            max_touch_points: 'int' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {
            'enabled': enabled,
        }

        if is_defined(max_touch_points):
            params['maxTouchPoints'] = max_touch_points

        return self._send_command(
            'Emulation.setTouchEmulationEnabled',
            params,
            False
        )

    def set_virtual_time_policy(
            self,
            policy: 'VirtualTimePolicy',
            budget: 'float' = UNDEFINED,
            max_virtual_time_task_starvation_count: 'int' = UNDEFINED,
            initial_virtual_time: 'TimeSinceEpoch' = UNDEFINED
    ) -> 'IResponse[SetVirtualTimePolicyReturnT]':
        params = {
            'policy': policy,
        }

        if is_defined(budget):
            params['budget'] = budget

        if is_defined(max_virtual_time_task_starvation_count):
            params['maxVirtualTimeTaskStarvationCount'] = max_virtual_time_task_starvation_count

        if is_defined(initial_virtual_time):
            params['initialVirtualTime'] = initial_virtual_time

        return self._send_command(
            'Emulation.setVirtualTimePolicy',
            params,
            True,
            lambda data: from_dict(
                SetVirtualTimePolicyReturnT,
                data,
                'camel'
            )
        )

    def set_locale_override(
            self,
            locale: 'str' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {}

        if is_defined(locale):
            params['locale'] = locale

        return self._send_command(
            'Emulation.setLocaleOverride',
            params,
            False
        )

    def set_timezone_override(
            self,
            timezone_id: 'str'
    ) -> 'IResponse[None]':
        params = {
            'timezoneId': timezone_id,
        }

        return self._send_command(
            'Emulation.setTimezoneOverride',
            params,
            False
        )

    def set_visible_size(
            self,
            width: 'int',
            height: 'int'
    ) -> 'IResponse[None]':
        params = {
            'width': width,
            'height': height,
        }

        return self._send_command(
            'Emulation.setVisibleSize',
            params,
            False
        )

    def set_disabled_image_types(
            self,
            image_types: 'list'
    ) -> 'IResponse[None]':
        params = {
            'imageTypes': image_types,
        }

        return self._send_command(
            'Emulation.setDisabledImageTypes',
            params,
            False
        )

    def set_hardware_concurrency_override(
            self,
            hardware_concurrency: 'int'
    ) -> 'IResponse[None]':
        params = {
            'hardwareConcurrency': hardware_concurrency,
        }

        return self._send_command(
            'Emulation.setHardwareConcurrencyOverride',
            params,
            False
        )

    def set_user_agent_override(
            self,
            user_agent: 'str',
            accept_language: 'str' = UNDEFINED,
            platform: 'str' = UNDEFINED,
            user_agent_metadata: 'UserAgentMetadata' = UNDEFINED
    ) -> 'IResponse[None]':
        params = {
            'userAgent': user_agent,
        }

        if is_defined(accept_language):
            params['acceptLanguage'] = accept_language

        if is_defined(platform):
            params['platform'] = platform

        if is_defined(user_agent_metadata):
            params['userAgentMetadata'] = to_dict(
                user_agent_metadata,
                'camel'
            )

        return self._send_command(
            'Emulation.setUserAgentOverride',
            params,
            False
        )

    def set_automation_override(
            self,
            enabled: 'bool'
    ) -> 'IResponse[None]':
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Emulation.setAutomationOverride',
            params,
            False
        )
