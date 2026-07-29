from typing import Literal, TypeAlias

from typing_extensions import NotRequired, TypedDict
from datetime import datetime

Literals: TypeAlias = str | int | float | bool
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | Literals | None


class Patch(TypedDict):
    op: Literal["add"] | Literal["replace"] | Literal["remove"]
    path: str
    value: JSON


class AcronisRequestParams(TypedDict):
    created_at_min: NotRequired[datetime]
    created_at_max: NotRequired[datetime]
    updated_at_min: NotRequired[datetime]
    updated_at_min: NotRequired[datetime]
    customFieldConditions: NotRequired[str]
    page_token: NotRequired[str]
    page: NotRequired[int]
    limit: NotRequired[int]
    organization_id: NotRequired[int]
    platform: NotRequired[str]
    status: NotRequired[str]
    indicator_type: NotRequired[str]
    severity: NotRequired[str]
    platform: NotRequired[str]
    agent_id: NotRequired[str]
    type: NotRequired[str]
    entity_id: NotRequired[int]
    types: NotRequired[str]
    statuses: NotRequired[str]
    # Account Management API (v2) query parameters
    after: NotRequired[str]
    allow_deleted: NotRequired[bool]
    access_policies: NotRequired[str]
    application_id: NotRequired[str]
    available_only: NotRequired[str]
    code: NotRequired[str]
    edition: NotRequired[str]
    editions: NotRequired[str]
    effective: NotRequired[int]
    embed_path: NotRequired[bool]
    enable: NotRequired[bool]
    expand_offering_items: NotRequired[bool]
    external_ids: NotRequired[str]
    for_ui: NotRequired[bool]
    force: NotRequired[bool]
    include_grand_children: NotRequired[bool]
    include_hidden: NotRequired[bool]
    include_relative_path: NotRequired[bool]
    include_secondary: NotRequired[bool]
    includeUserGroupPolicies: NotRequired[bool]
    infra_uuid: NotRequired[str]
    inside_organization: NotRequired[bool]
    kind: NotRequired[str]
    lod: NotRequired[str]
    login: NotRequired[str]
    offering_items: NotRequired[str]
    order: NotRequired[str]
    origin_id: NotRequired[str]
    ott: NotRequired[str]
    parent_id: NotRequired[str]
    subtree_root_id: NotRequired[str]
    subtree_root_tenant_id: NotRequired[str]
    target_edition: NotRequired[str]
    target_tenant_id: NotRequired[str]
    targetURI: NotRequired[str]
    tenant: NotRequired[str]
    tenant_id: NotRequired[str]
    tenant_kinds: NotRequired[str]
    tenant_uuid: NotRequired[str]
    tenants: NotRequired[str]
    text: NotRequired[str]
    updated_since: NotRequired[datetime]
    usage_names: NotRequired[str]
    username: NotRequired[str]
    uuids: NotRequired[str]
    version: NotRequired[int]
    with_contacts: NotRequired[bool]
    with_access_policies: NotRequired[bool]
    with_infra_offering_items: NotRequired[bool]
    with_offering_items: NotRequired[bool]


GenericRequestParams: TypeAlias = dict[str, Literals]
RequestParams: TypeAlias = AcronisRequestParams | GenericRequestParams
PatchRequestData: TypeAlias = list[Patch]
RequestData: TypeAlias = JSON | PatchRequestData
RequestMethod: TypeAlias = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
