from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.preload.types import (
    SpeculationAction,
    SpeculationTargetHint,
    PreloadingAttemptKey,
    PrerenderFinalStatus,
    PreloadingStatus,
    PrefetchStatus,
    RuleSetId,
    RuleSetErrorType,
    RuleSet
)
from cdp.domains.network.types import (
    RequestId,
    LoaderId
)
from cdp.domains.dom.types import (
    BackendNodeId
)
from cdp.domains.page.types import (
    FrameId
)


@dataclass
class Preload(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Preload.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Preload.disable",
            params
        )

