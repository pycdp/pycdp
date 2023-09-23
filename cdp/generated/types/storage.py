# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.generated.types import (
    browser,
    network,
    page
)
from typing import (
    Literal,
    NotRequired,
    TypedDict
)

SerializedStorageKey = str

UnsignedInt64AsBase10 = str

UnsignedInt128AsBase16 = str

SignedInt64AsBase10 = str

StorageType = Literal[
    'appcache',
    'cookies',
    'file_systems',
    'indexeddb',
    'local_storage',
    'shader_cache',
    'websql',
    'service_workers',
    'cache_storage',
    'interest_groups',
    'shared_storage',
    'storage_buckets',
    'all',
    'other'
]

InterestGroupAccessType = Literal[
    'join',
    'leave',
    'update',
    'loaded',
    'bid',
    'win'
]

SharedStorageAccessType = Literal[
    'documentAddModule',
    'documentSelectURL',
    'documentRun',
    'documentSet',
    'documentAppend',
    'documentDelete',
    'documentClear',
    'workletSet',
    'workletAppend',
    'workletDelete',
    'workletClear',
    'workletGet',
    'workletKeys',
    'workletEntries',
    'workletLength',
    'workletRemainingBudget'
]

StorageBucketsDurability = Literal[
    'relaxed',
    'strict'
]

AttributionReportingSourceType = Literal[
    'navigation',
    'event'
]

AttributionReportingSourceRegistrationResult = Literal[
    'success',
    'internalError',
    'insufficientSourceCapacity',
    'insufficientUniqueDestinationCapacity',
    'excessiveReportingOrigins',
    'prohibitedByBrowserPolicy',
    'successNoised',
    'destinationReportingLimitReached',
    'destinationGlobalLimitReached',
    'destinationBothLimitsReached',
    'reportingOriginsPerSiteLimitReached',
    'exceedsMaxChannelCapacity'
]


class UsageForType(TypedDict):
    storage_type: 'StorageType'
    usage: float


class TrustTokens(TypedDict):
    issuer_origin: str
    count: float


class InterestGroupAd(TypedDict):
    render_url: str
    metadata: NotRequired[str]


class InterestGroupDetails(TypedDict):
    owner_origin: str
    name: str
    expiration_time: 'network.TimeSinceEpoch'
    joining_origin: str
    trusted_bidding_signals_keys: list
    ads: list
    ad_components: list
    bidding_url: NotRequired[str]
    bidding_wasm_helper_url: NotRequired[str]
    update_url: NotRequired[str]
    trusted_bidding_signals_url: NotRequired[str]
    user_bidding_signals: NotRequired[str]


class SharedStorageEntry(TypedDict):
    key: str
    value: str


class SharedStorageMetadata(TypedDict):
    creation_time: 'network.TimeSinceEpoch'
    length: int
    remaining_budget: float


class SharedStorageReportingMetadata(TypedDict):
    event_type: str
    reporting_url: str


class SharedStorageUrlWithMetadata(TypedDict):
    url: str
    reporting_metadata: list


class SharedStorageAccessParams(TypedDict):
    script_source_url: NotRequired[str]
    operation_name: NotRequired[str]
    serialized_data: NotRequired[str]
    urls_with_metadata: NotRequired[list]
    key: NotRequired[str]
    value: NotRequired[str]
    ignore_if_present: NotRequired[bool]


class StorageBucket(TypedDict):
    storage_key: 'SerializedStorageKey'
    name: NotRequired[str]


class StorageBucketInfo(TypedDict):
    bucket: 'StorageBucket'
    id: str
    expiration: 'network.TimeSinceEpoch'
    quota: float
    persistent: bool
    durability: 'StorageBucketsDurability'


class AttributionReportingFilterDataEntry(TypedDict):
    key: str
    values: list


class AttributionReportingAggregationKeysEntry(TypedDict):
    key: str
    value: 'UnsignedInt128AsBase16'


class AttributionReportingEventReportWindows(TypedDict):
    start: int
    ends: list


class AttributionReportingSourceRegistration(TypedDict):
    time: 'network.TimeSinceEpoch'
    type: 'AttributionReportingSourceType'
    source_origin: str
    reporting_origin: str
    destination_sites: list
    event_id: 'UnsignedInt64AsBase10'
    priority: 'SignedInt64AsBase10'
    filter_data: list
    aggregation_keys: list
    expiry: NotRequired[int]
    event_report_window: NotRequired[int]
    event_report_windows: NotRequired['AttributionReportingEventReportWindows']
    aggregatable_report_window: NotRequired[int]
    debug_key: NotRequired['UnsignedInt64AsBase10']


class GetStorageKeyForFrameParamsT(TypedDict):
    frame_id: 'page.FrameId'


class ClearDataForOriginParamsT(TypedDict):
    origin: str
    storage_types: str


class ClearDataForStorageKeyParamsT(TypedDict):
    storage_key: str
    storage_types: str


class GetCookiesParamsT(TypedDict):
    browser_context_id: NotRequired['browser.BrowserContextID']


class SetCookiesParamsT(TypedDict):
    cookies: list
    browser_context_id: NotRequired['browser.BrowserContextID']


class ClearCookiesParamsT(TypedDict):
    browser_context_id: NotRequired['browser.BrowserContextID']


class GetUsageAndQuotaParamsT(TypedDict):
    origin: str


class OverrideQuotaForOriginParamsT(TypedDict):
    origin: str
    quota_size: NotRequired[float]


class TrackCacheStorageForOriginParamsT(TypedDict):
    origin: str


class TrackCacheStorageForStorageKeyParamsT(TypedDict):
    storage_key: str


class TrackIndexedDBForOriginParamsT(TypedDict):
    origin: str


class TrackIndexedDBForStorageKeyParamsT(TypedDict):
    storage_key: str


class UntrackCacheStorageForOriginParamsT(TypedDict):
    origin: str


class UntrackCacheStorageForStorageKeyParamsT(TypedDict):
    storage_key: str


class UntrackIndexedDBForOriginParamsT(TypedDict):
    origin: str


class UntrackIndexedDBForStorageKeyParamsT(TypedDict):
    storage_key: str


class ClearTrustTokensParamsT(TypedDict):
    issuer_origin: str


class GetInterestGroupDetailsParamsT(TypedDict):
    owner_origin: str
    name: str


class SetInterestGroupTrackingParamsT(TypedDict):
    enable: bool


class GetSharedStorageMetadataParamsT(TypedDict):
    owner_origin: str


class GetSharedStorageEntriesParamsT(TypedDict):
    owner_origin: str


class SetSharedStorageEntryParamsT(TypedDict):
    owner_origin: str
    key: str
    value: str
    ignore_if_present: NotRequired[bool]


class DeleteSharedStorageEntryParamsT(TypedDict):
    owner_origin: str
    key: str


class ClearSharedStorageEntriesParamsT(TypedDict):
    owner_origin: str


class ResetSharedStorageBudgetParamsT(TypedDict):
    owner_origin: str


class SetSharedStorageTrackingParamsT(TypedDict):
    enable: bool


class SetStorageBucketTrackingParamsT(TypedDict):
    storage_key: str
    enable: bool


class DeleteStorageBucketParamsT(TypedDict):
    bucket: 'StorageBucket'


class SetAttributionReportingLocalTestingModeParamsT(TypedDict):
    enabled: bool


class SetAttributionReportingTrackingParamsT(TypedDict):
    enable: bool


class GetStorageKeyForFrameReturnT(TypedDict):
    storage_key: 'SerializedStorageKey'


class GetCookiesReturnT(TypedDict):
    cookies: list


class GetUsageAndQuotaReturnT(TypedDict):
    usage: float
    quota: float
    override_active: bool
    usage_breakdown: list


class GetTrustTokensReturnT(TypedDict):
    tokens: list


class ClearTrustTokensReturnT(TypedDict):
    did_delete_tokens: bool


class GetInterestGroupDetailsReturnT(TypedDict):
    details: 'InterestGroupDetails'


class GetSharedStorageMetadataReturnT(TypedDict):
    metadata: 'SharedStorageMetadata'


class GetSharedStorageEntriesReturnT(TypedDict):
    entries: list


class RunBounceTrackingMitigationsReturnT(TypedDict):
    deleted_sites: list


class CacheStorageContentUpdatedEventT(TypedDict):
    name: Literal['cache_storage_content_updated']
    params: 'CacheStorageContentUpdatedParamsT'


class CacheStorageListUpdatedEventT(TypedDict):
    name: Literal['cache_storage_list_updated']
    params: 'CacheStorageListUpdatedParamsT'


class IndexedDBContentUpdatedEventT(TypedDict):
    name: Literal['indexed_db_content_updated']
    params: 'IndexedDBContentUpdatedParamsT'


class IndexedDBListUpdatedEventT(TypedDict):
    name: Literal['indexed_db_list_updated']
    params: 'IndexedDBListUpdatedParamsT'


class InterestGroupAccessedEventT(TypedDict):
    name: Literal['interest_group_accessed']
    params: 'InterestGroupAccessedParamsT'


class SharedStorageAccessedEventT(TypedDict):
    name: Literal['shared_storage_accessed']
    params: 'SharedStorageAccessedParamsT'


class StorageBucketCreatedOrUpdatedEventT(TypedDict):
    name: Literal['storage_bucket_created_or_updated']
    params: 'StorageBucketCreatedOrUpdatedParamsT'


class StorageBucketDeletedEventT(TypedDict):
    name: Literal['storage_bucket_deleted']
    params: 'StorageBucketDeletedParamsT'


class AttributionReportingSourceRegisteredEventT(TypedDict):
    name: Literal['attribution_reporting_source_registered']
    params: 'AttributionReportingSourceRegisteredParamsT'


class CacheStorageContentUpdatedParamsT(TypedDict):
    origin: str
    storage_key: str
    bucket_id: str
    cache_name: str


class CacheStorageListUpdatedParamsT(TypedDict):
    origin: str
    storage_key: str
    bucket_id: str


class IndexedDBContentUpdatedParamsT(TypedDict):
    origin: str
    storage_key: str
    bucket_id: str
    database_name: str
    object_store_name: str


class IndexedDBListUpdatedParamsT(TypedDict):
    origin: str
    storage_key: str
    bucket_id: str


class InterestGroupAccessedParamsT(TypedDict):
    access_time: 'network.TimeSinceEpoch'
    type: 'InterestGroupAccessType'
    owner_origin: str
    name: str


class SharedStorageAccessedParamsT(TypedDict):
    access_time: 'network.TimeSinceEpoch'
    type: 'SharedStorageAccessType'
    main_frame_id: 'page.FrameId'
    owner_origin: str
    params: 'SharedStorageAccessParams'


class StorageBucketCreatedOrUpdatedParamsT(TypedDict):
    bucket_info: 'StorageBucketInfo'


class StorageBucketDeletedParamsT(TypedDict):
    bucket_id: str


class AttributionReportingSourceRegisteredParamsT(TypedDict):
    registration: 'AttributionReportingSourceRegistration'
    result: 'AttributionReportingSourceRegistrationResult'
