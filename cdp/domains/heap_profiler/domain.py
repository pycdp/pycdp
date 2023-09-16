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
from cdp.domains.heap_profiler.types import (
    GetHeapObjectIdReturnT,
    GetObjectByHeapObjectIdReturnT,
    GetSamplingProfileReturnT,
    HeapSnapshotObjectId,
    StopSamplingReturnT
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)


@dataclass
class HeapProfiler(BaseDomain):
    def add_inspected_heap_object(
            self,
            heap_object_id: HeapSnapshotObjectId
    ) -> None:
        params = {
            'heapObjectId': heap_object_id,
        }

        return self._send_command(
            'HeapProfiler.addInspectedHeapObject',
            params
        )

    def collect_garbage(
            self
    ) -> None:
        params = {}

        return self._send_command(
            'HeapProfiler.collectGarbage',
            params
        )

    def disable(
            self
    ) -> None:
        params = {}

        return self._send_command(
            'HeapProfiler.disable',
            params
        )

    def enable(
            self
    ) -> None:
        params = {}

        return self._send_command(
            'HeapProfiler.enable',
            params
        )

    def get_heap_object_id(
            self,
            object_id: RemoteObjectId
    ) -> 'GetHeapObjectIdReturnT':
        params = {
            'objectId': object_id,
        }

        return self._send_command(
            'HeapProfiler.getHeapObjectId',
            params
        )

    def get_object_by_heap_object_id(
            self,
            object_id: HeapSnapshotObjectId,
            object_group: str = UNDEFINED
    ) -> 'GetObjectByHeapObjectIdReturnT':
        params = {
            'objectId': object_id,
        }

        if is_defined(object_group):
            params['objectGroup'] = object_group

        return self._send_command(
            'HeapProfiler.getObjectByHeapObjectId',
            params
        )

    def get_sampling_profile(
            self
    ) -> 'GetSamplingProfileReturnT':
        params = {}

        return self._send_command(
            'HeapProfiler.getSamplingProfile',
            params
        )

    def start_sampling(
            self,
            sampling_interval: float = UNDEFINED
    ) -> None:
        params = {}

        if is_defined(sampling_interval):
            params['samplingInterval'] = sampling_interval

        return self._send_command(
            'HeapProfiler.startSampling',
            params
        )

    def start_tracking_heap_objects(
            self,
            track_allocations: bool = UNDEFINED
    ) -> None:
        params = {}

        if is_defined(track_allocations):
            params['trackAllocations'] = track_allocations

        return self._send_command(
            'HeapProfiler.startTrackingHeapObjects',
            params
        )

    def stop_sampling(
            self
    ) -> 'StopSamplingReturnT':
        params = {}

        return self._send_command(
            'HeapProfiler.stopSampling',
            params
        )

    def stop_tracking_heap_objects(
            self,
            report_progress: bool = UNDEFINED
    ) -> None:
        params = {}

        if is_defined(report_progress):
            params['reportProgress'] = report_progress

        return self._send_command(
            'HeapProfiler.stopTrackingHeapObjects',
            params
        )

    def take_heap_snapshot(
            self,
            report_progress: bool = UNDEFINED
    ) -> None:
        params = {}

        if is_defined(report_progress):
            params['reportProgress'] = report_progress

        return self._send_command(
            'HeapProfiler.takeHeapSnapshot',
            params
        )
