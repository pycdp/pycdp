# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.


from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from cdp.target.target import (
        Target
    )
    from cdp.generated.types import (
        accessibility,
        animation,
        audits,
        autofill,
        background_service,
        browser,
        css,
        cache_storage,
        cast,
        dom,
        dom_debugger,
        event_breakpoints,
        dom_snapshot,
        dom_storage,
        database,
        device_orientation,
        emulation,
        headless_experimental,
        io,
        indexed_db,
        input,
        inspector,
        layer_tree,
        log,
        memory,
        network,
        overlay,
        page,
        performance,
        performance_timeline,
        security,
        service_worker,
        storage,
        system_info,
        target,
        tethering,
        tracing,
        fetch,
        web_audio,
        web_authn,
        media,
        device_access,
        preload,
        fed_cm,
        console,
        debugger,
        heap_profiler,
        profiler,
        runtime,
        schema
    )


@dataclass
class Domains:
    ws_target: 'Target'
