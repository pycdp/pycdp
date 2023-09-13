from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.dom.types import (
    RGBA
)
from cdp.domains.emulation.types import (
    UserAgentMetadata,
    VirtualTimePolicy,
    DisplayFeature,
    ScreenOrientation
)
from cdp.domains.page.types import (
    Viewport
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)


@dataclass
class Emulation(BaseDomain):
    def can_emulate(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.canEmulate",
            params
        )

    def clear_device_metrics_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearDeviceMetricsOverride",
            params
        )

    def clear_geolocation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearGeolocationOverride",
            params
        )

    def reset_page_scale_factor(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.resetPageScaleFactor",
            params
        )

    def set_focus_emulation_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Emulation.setFocusEmulationEnabled",
            params
        )

    def set_auto_dark_mode_override(
        self,
        enabled: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            enabled
        ):
            params["enabled"] = enabled

        return self._send_command(
            "Emulation.setAutoDarkModeOverride",
            params
        )

    def set_cpu_throttling_rate(
        self,
        rate: float
    ):
        params = {
            "rate": rate,
        }

        return self._send_command(
            "Emulation.setCPUThrottlingRate",
            params
        )

    def set_default_background_color_override(
        self,
        color: MaybeUndefined[RGBA]
    ):
        params = {}

        if is_defined(
            color
        ):
            params["color"] = color

        return self._send_command(
            "Emulation.setDefaultBackgroundColorOverride",
            params
        )

    def set_device_metrics_override(
        self,
        width: int,
        height: int,
        device_scale_factor: float,
        mobile: bool,
        scale: MaybeUndefined[float],
        screen_width: MaybeUndefined[int],
        screen_height: MaybeUndefined[int],
        position_x: MaybeUndefined[int],
        position_y: MaybeUndefined[int],
        dont_set_visible_size: MaybeUndefined[bool],
        screen_orientation: MaybeUndefined[ScreenOrientation],
        viewport: MaybeUndefined[Viewport],
        display_feature: MaybeUndefined[DisplayFeature]
    ):
        params = {
            "width": width,
            "height": height,
            "deviceScaleFactor": device_scale_factor,
            "mobile": mobile,
        }

        if is_defined(
            scale
        ):
            params["scale"] = scale

        if is_defined(
            screen_width
        ):
            params["screenWidth"] = screen_width

        if is_defined(
            screen_height
        ):
            params["screenHeight"] = screen_height

        if is_defined(
            position_x
        ):
            params["positionX"] = position_x

        if is_defined(
            position_y
        ):
            params["positionY"] = position_y

        if is_defined(
            dont_set_visible_size
        ):
            params["dontSetVisibleSize"] = dont_set_visible_size

        if is_defined(
            screen_orientation
        ):
            params["screenOrientation"] = screen_orientation

        if is_defined(
            viewport
        ):
            params["viewport"] = viewport

        if is_defined(
            display_feature
        ):
            params["displayFeature"] = display_feature

        return self._send_command(
            "Emulation.setDeviceMetricsOverride",
            params
        )

    def set_scrollbars_hidden(
        self,
        hidden: bool
    ):
        params = {
            "hidden": hidden,
        }

        return self._send_command(
            "Emulation.setScrollbarsHidden",
            params
        )

    def set_document_cookie_disabled(
        self,
        disabled: bool
    ):
        params = {
            "disabled": disabled,
        }

        return self._send_command(
            "Emulation.setDocumentCookieDisabled",
            params
        )

    def set_emit_touch_events_for_mouse(
        self,
        enabled: bool,
        configuration: MaybeUndefined[str]
    ):
        params = {
            "enabled": enabled,
        }

        if is_defined(
            configuration
        ):
            params["configuration"] = configuration

        return self._send_command(
            "Emulation.setEmitTouchEventsForMouse",
            params
        )

    def set_emulated_media(
        self,
        media: MaybeUndefined[str],
        features: MaybeUndefined[list]
    ):
        params = {}

        if is_defined(
            media
        ):
            params["media"] = media

        if is_defined(
            features
        ):
            params["features"] = features

        return self._send_command(
            "Emulation.setEmulatedMedia",
            params
        )

    def set_emulated_vision_deficiency(
        self,
        type_: str
    ):
        params = {
            "type": type_,
        }

        return self._send_command(
            "Emulation.setEmulatedVisionDeficiency",
            params
        )

    def set_geolocation_override(
        self,
        latitude: MaybeUndefined[float],
        longitude: MaybeUndefined[float],
        accuracy: MaybeUndefined[float]
    ):
        params = {}

        if is_defined(
            latitude
        ):
            params["latitude"] = latitude

        if is_defined(
            longitude
        ):
            params["longitude"] = longitude

        if is_defined(
            accuracy
        ):
            params["accuracy"] = accuracy

        return self._send_command(
            "Emulation.setGeolocationOverride",
            params
        )

    def set_idle_override(
        self,
        is_user_active: bool,
        is_screen_unlocked: bool
    ):
        params = {
            "isUserActive": is_user_active,
            "isScreenUnlocked": is_screen_unlocked,
        }

        return self._send_command(
            "Emulation.setIdleOverride",
            params
        )

    def clear_idle_override(
        self
    ):
        params = {}

        return self._send_command(
            "Emulation.clearIdleOverride",
            params
        )

    def set_navigator_overrides(
        self,
        platform: str
    ):
        params = {
            "platform": platform,
        }

        return self._send_command(
            "Emulation.setNavigatorOverrides",
            params
        )

    def set_page_scale_factor(
        self,
        page_scale_factor: float
    ):
        params = {
            "pageScaleFactor": page_scale_factor,
        }

        return self._send_command(
            "Emulation.setPageScaleFactor",
            params
        )

    def set_script_execution_disabled(
        self,
        value: bool
    ):
        params = {
            "value": value,
        }

        return self._send_command(
            "Emulation.setScriptExecutionDisabled",
            params
        )

    def set_touch_emulation_enabled(
        self,
        enabled: bool,
        max_touch_points: MaybeUndefined[int]
    ):
        params = {
            "enabled": enabled,
        }

        if is_defined(
            max_touch_points
        ):
            params["maxTouchPoints"] = max_touch_points

        return self._send_command(
            "Emulation.setTouchEmulationEnabled",
            params
        )

    def set_virtual_time_policy(
        self,
        policy: VirtualTimePolicy,
        budget: MaybeUndefined[float],
        max_virtual_time_task_starvation_count: MaybeUndefined[int],
        initial_virtual_time: MaybeUndefined[TimeSinceEpoch]
    ):
        params = {
            "policy": policy,
        }

        if is_defined(
            budget
        ):
            params["budget"] = budget

        if is_defined(
            max_virtual_time_task_starvation_count
        ):
            params["maxVirtualTimeTaskStarvationCount"] = max_virtual_time_task_starvation_count

        if is_defined(
            initial_virtual_time
        ):
            params["initialVirtualTime"] = initial_virtual_time

        return self._send_command(
            "Emulation.setVirtualTimePolicy",
            params
        )

    def set_locale_override(
        self,
        locale: MaybeUndefined[str]
    ):
        params = {}

        if is_defined(
            locale
        ):
            params["locale"] = locale

        return self._send_command(
            "Emulation.setLocaleOverride",
            params
        )

    def set_timezone_override(
        self,
        timezone_id: str
    ):
        params = {
            "timezoneId": timezone_id,
        }

        return self._send_command(
            "Emulation.setTimezoneOverride",
            params
        )

    def set_visible_size(
        self,
        width: int,
        height: int
    ):
        params = {
            "width": width,
            "height": height,
        }

        return self._send_command(
            "Emulation.setVisibleSize",
            params
        )

    def set_disabled_image_types(
        self,
        image_types: list
    ):
        params = {
            "imageTypes": image_types,
        }

        return self._send_command(
            "Emulation.setDisabledImageTypes",
            params
        )

    def set_hardware_concurrency_override(
        self,
        hardware_concurrency: int
    ):
        params = {
            "hardwareConcurrency": hardware_concurrency,
        }

        return self._send_command(
            "Emulation.setHardwareConcurrencyOverride",
            params
        )

    def set_user_agent_override(
        self,
        user_agent: str,
        accept_language: MaybeUndefined[str],
        platform: MaybeUndefined[str],
        user_agent_metadata: MaybeUndefined[UserAgentMetadata]
    ):
        params = {
            "userAgent": user_agent,
        }

        if is_defined(
            accept_language
        ):
            params["acceptLanguage"] = accept_language

        if is_defined(
            platform
        ):
            params["platform"] = platform

        if is_defined(
            user_agent_metadata
        ):
            params["userAgentMetadata"] = user_agent_metadata

        return self._send_command(
            "Emulation.setUserAgentOverride",
            params
        )

    def set_automation_override(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Emulation.setAutomationOverride",
            params
        )

