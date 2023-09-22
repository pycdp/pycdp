# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from typing import (
    Literal,
    TypedDict
)

SerializedStorageKey = str

Item = list


class StorageId(TypedDict):
    is_local_storage: bool
    security_origin: str
    storage_key: 'SerializedStorageKey'


class ClearParamsT(TypedDict):
    storage_id: 'StorageId'


class GetDOMStorageItemsParamsT(TypedDict):
    storage_id: 'StorageId'


class RemoveDOMStorageItemParamsT(TypedDict):
    storage_id: 'StorageId'
    key: str


class SetDOMStorageItemParamsT(TypedDict):
    storage_id: 'StorageId'
    key: str
    value: str


class GetDOMStorageItemsReturnT(TypedDict):
    entries: list


class DomStorageItemAddedEventT(TypedDict):
    name: Literal['dom_storage_item_added']
    params: 'DomStorageItemAddedParamsT'


class DomStorageItemRemovedEventT(TypedDict):
    name: Literal['dom_storage_item_removed']
    params: 'DomStorageItemRemovedParamsT'


class DomStorageItemUpdatedEventT(TypedDict):
    name: Literal['dom_storage_item_updated']
    params: 'DomStorageItemUpdatedParamsT'


class DomStorageItemsClearedEventT(TypedDict):
    name: Literal['dom_storage_items_cleared']
    params: 'DomStorageItemsClearedParamsT'


class DomStorageItemAddedParamsT(TypedDict):
    storage_id: 'StorageId'
    key: str
    new_value: str


class DomStorageItemRemovedParamsT(TypedDict):
    storage_id: 'StorageId'
    key: str


class DomStorageItemUpdatedParamsT(TypedDict):
    storage_id: 'StorageId'
    key: str
    old_value: str
    new_value: str


class DomStorageItemsClearedParamsT(TypedDict):
    storage_id: 'StorageId'
