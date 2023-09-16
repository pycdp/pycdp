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
from cdp.domains.memory.types import (
    PressureLevel,
    SamplingProfile
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Memory(BaseDomain):
    def get_dom_counters(
        self
    ) -> 'GetDOMCountersReturnT':
        params = {}
        
        return self._send_command(
            'Memory.getDOMCounters',

            params
        )

    def prepare_for_leak_detection(
        self
    ) -> 'PrepareForLeakDetectionReturnT':
        params = {}
        
        return self._send_command(
            'Memory.prepareForLeakDetection',

            params
        )

    def forcibly_purge_java_script_memory(
        self
    ) -> 'ForciblyPurgeJavaScriptMemoryReturnT':
        params = {}
        
        return self._send_command(
            'Memory.forciblyPurgeJavaScriptMemory',

            params
        )

    def set_pressure_notifications_suppressed(
        self,
        suppressed: bool
    ) -> 'SetPressureNotificationsSuppressedReturnT':
        params = {
            'suppressed': suppressed,
        }
        
        return self._send_command(
            'Memory.setPressureNotificationsSuppressed',

            params
        )

    def simulate_pressure_notification(
        self,
        level: PressureLevel
    ) -> 'SimulatePressureNotificationReturnT':
        params = {
            'level': level,
        }
        
        return self._send_command(
            'Memory.simulatePressureNotification',

            params
        )

    def start_sampling(
        self,
        sampling_interval: int = UNDEFINED,
        suppress_randomness: bool = UNDEFINED
    ) -> 'StartSamplingReturnT':
        params = {}
        
        if is_defined(sampling_interval):
params['samplingInterval'] = sampling_interval
        
        if is_defined(suppress_randomness):
params['suppressRandomness'] = suppress_randomness
        
        return self._send_command(
            'Memory.startSampling',

            params
        )

    def stop_sampling(
        self
    ) -> 'StopSamplingReturnT':
        params = {}
        
        return self._send_command(
            'Memory.stopSampling',

            params
        )

    def get_all_time_sampling_profile(
        self
    ) -> 'GetAllTimeSamplingProfileReturnT':
        params = {}
        
        return self._send_command(
            'Memory.getAllTimeSamplingProfile',

            params
        )

    def get_browser_sampling_profile(
        self
    ) -> 'GetBrowserSamplingProfileReturnT':
        params = {}
        
        return self._send_command(
            'Memory.getBrowserSamplingProfile',

            params
        )

    def get_sampling_profile(
        self
    ) -> 'GetSamplingProfileReturnT':
        params = {}
        
        return self._send_command(
            'Memory.getSamplingProfile',

            params
        )

