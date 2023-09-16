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
from cdp.domains.animation.types import (
    GetCurrentTimeReturnT,
    GetPlaybackRateReturnT,
    ResolveAnimationReturnT
)


@dataclass
class Animation(BaseDomain):
    def disable(
        self
    ) -> 'DisableReturnT':
        params = {}
        
        return self._send_command(
            'Animation.disable',

            params
        )

    def enable(
        self
    ) -> 'EnableReturnT':
        params = {}
        
        return self._send_command(
            'Animation.enable',

            params
        )

    def get_current_time(
        self,
        id_: str
    ) -> 'GetCurrentTimeReturnT':
        params = {
            'id': id_,
        }
        
        return self._send_command(
            'Animation.getCurrentTime',

            params
        )

    def get_playback_rate(
        self
    ) -> 'GetPlaybackRateReturnT':
        params = {}
        
        return self._send_command(
            'Animation.getPlaybackRate',

            params
        )

    def release_animations(
        self,
        animations: list
    ) -> 'ReleaseAnimationsReturnT':
        params = {
            'animations': animations,
        }
        
        return self._send_command(
            'Animation.releaseAnimations',

            params
        )

    def resolve_animation(
        self,
        animation_id: str
    ) -> 'ResolveAnimationReturnT':
        params = {
            'animationId': animation_id,
        }
        
        return self._send_command(
            'Animation.resolveAnimation',

            params
        )

    def seek_animations(
        self,
        animations: list,
        current_time: float
    ) -> 'SeekAnimationsReturnT':
        params = {
            'animations': animations,
            'currentTime': current_time,
        }
        
        return self._send_command(
            'Animation.seekAnimations',

            params
        )

    def set_paused(
        self,
        animations: list,
        paused: bool
    ) -> 'SetPausedReturnT':
        params = {
            'animations': animations,
            'paused': paused,
        }
        
        return self._send_command(
            'Animation.setPaused',

            params
        )

    def set_playback_rate(
        self,
        playback_rate: float
    ) -> 'SetPlaybackRateReturnT':
        params = {
            'playbackRate': playback_rate,
        }
        
        return self._send_command(
            'Animation.setPlaybackRate',

            params
        )

    def set_timing(
        self,
        animation_id: str,
        duration: float,
        delay: float
    ) -> 'SetTimingReturnT':
        params = {
            'animationId': animation_id,
            'duration': duration,
            'delay': delay,
        }
        
        return self._send_command(
            'Animation.setTiming',

            params
        )

