from __future__ import annotations

from datetime import date, datetime
from typing import Any

from pydantic import Field

from pyacronis.models.base.base_model import AcronisModel


class PagingCursors(AcronisModel):
    after: str | None = Field(default=None, alias="after")


class Paging(AcronisModel):
    cursors: PagingCursors | None = Field(default=None, alias="cursors")


class ErrorDetails(AcronisModel):
    info: str | None = Field(default=None, alias="info")


class Error(AcronisModel):
    code: str | int | None = Field(default=None, alias="code")
    context: dict[str, Any] | None = Field(default=None, alias="context")
    domain: str | None = Field(default=None, alias="domain")
    message: str | None = Field(default=None, alias="message")
    details: ErrorDetails | None = Field(default=None, alias="details")
    data: list[str] | None = Field(default=None, alias="data")


class ErrorScheme(AcronisModel):
    error: Error | None = Field(default=None, alias="error")


class OpenIDConfiguration(AcronisModel):
    issuer: str | None = Field(default=None, alias="issuer")
    authorization_endpoint: str | None = Field(default=None, alias="authorization_endpoint")
    token_endpoint: str | None = Field(default=None, alias="token_endpoint")
    jwks_uri: str | None = Field(default=None, alias="jwks_uri")
    response_types_supported: list[str] | None = Field(default=None, alias="response_types_supported")
    subject_types_supported: list[str] | None = Field(default=None, alias="subject_types_supported")
    id_token_signing_alg_values_supported: list[str] | None = Field(
        default=None, alias="id_token_signing_alg_values_supported"
    )
    scopes_supported: list[str] | None = Field(default=None, alias="scopes_supported")
    token_endpoint_auth_methods_supported: list[str] | None = Field(
        default=None, alias="token_endpoint_auth_methods_supported"
    )
    revocation_endpoint: str | None = Field(default=None, alias="revocation_endpoint")
    revocation_endpoint_auth_methods_supported: list[str] | None = Field(
        default=None, alias="revocation_endpoint_auth_methods_supported"
    )
    device_authorization_endpoint: str | None = Field(default=None, alias="device_authorization_endpoint")


class ForgotLink(AcronisModel):
    link: str | None = Field(default=None, alias="link")


class Application(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    name: str | None = Field(default=None, alias="name")
    type: str | None = Field(default=None, alias="type")
    usages: list[str] | None = Field(default=None, alias="usages")
    api_base_url: str | None = Field(default=None, alias="api_base_url")


class SettingOwner(AcronisModel):
    type: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None, alias="id")


class SettingOwn(AcronisModel):
    value: Any | None = Field(default=None, alias="value")
    lock: bool | None = Field(default=None, alias="lock")
    exclusive: bool | None = Field(default=None, alias="exclusive")


class SettingEffective(AcronisModel):
    owner: SettingOwner | None = Field(default=None, alias="owner")
    value: Any | None = Field(default=None, alias="value")
    lock: bool | None = Field(default=None, alias="lock")


class Setting(AcronisModel):
    name: str | None = Field(default=None, alias="name")
    application_id: str | None = Field(default=None, alias="application_id")
    own: SettingOwn | None = Field(default=None, alias="own")
    effective: SettingEffective | None = Field(default=None, alias="effective")


class Client(AcronisModel):
    client_id: str | None = Field(default=None, alias="client_id")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    client_secret_expires_at: int | None = Field(default=None, alias="client_secret_expires_at")
    type: str | None = Field(default=None, alias="type")
    data: dict[str, Any] | None = Field(default=None, alias="data")
    token_endpoint_auth_method: str | None = Field(default=None, alias="token_endpoint_auth_method")
    created_at: datetime | None = Field(default=None, alias="created_at")
    created_by: str | None = Field(default=None, alias="created_by")
    last_access_at: datetime | None = Field(default=None, alias="last_access_at")
    last_access_from_ip: str | None = Field(default=None, alias="last_access_from_ip")
    status: str | None = Field(default=None, alias="status")
    redirect_uris: list[str] | None = Field(default=None, alias="redirect_uris")
    origin_id: str | None = Field(default=None, alias="origin_id")


class ClientPostResult(Client):
    """A newly created client. Carries the one-time secret and registration access token."""

    client_secret: str | None = Field(default=None, alias="client_secret")
    registration_access_token: str | None = Field(default=None, alias="registration_access_token")


class Token(AcronisModel):
    access_token: str | None = Field(default=None, alias="access_token")
    token_type: str | None = Field(default=None, alias="token_type")
    expires_in: int | None = Field(default=None, alias="expires_in")
    expires_on: int | None = Field(default=None, alias="expires_on")
    id_token: str | None = Field(default=None, alias="id_token")
    refresh_token: str | None = Field(default=None, alias="refresh_token")


class TokenError(AcronisModel):
    error: str | None = Field(default=None, alias="error")
    error_description: str | None = Field(default=None, alias="error_description")


class RevokeError(AcronisModel):
    error: str | None = Field(default=None, alias="error")
    error_description: str | None = Field(default=None, alias="error_description")


class TokenIntrospectionScope(AcronisModel):
    tuid: str | None = Field(default=None, alias="tuid")
    tid: str | None = Field(default=None, alias="tid")
    role: str | None = Field(default=None, alias="role")
    rn: str | None = Field(default=None, alias="rn")
    rs: str | None = Field(default=None, alias="rs")
    rp: str | None = Field(default=None, alias="rp")


class TokenIntrospectionResponse(AcronisModel):
    active: bool | None = Field(default=None, alias="active")
    token_type: str | None = Field(default=None, alias="token_type")
    exp: int | None = Field(default=None, alias="exp")
    aud: str | None = Field(default=None, alias="aud")
    jti: str | None = Field(default=None, alias="jti")
    iss: str | None = Field(default=None, alias="iss")
    sub: str | None = Field(default=None, alias="sub")
    sub_type: str | None = Field(default=None, alias="sub_type")
    client_id: str | None = Field(default=None, alias="client_id")
    owner_tuid: str | None = Field(default=None, alias="owner_tuid")
    scope: list[TokenIntrospectionScope] | None = Field(default=None, alias="scope")


class IdpOtt(AcronisModel):
    ott: str | None = Field(default=None, alias="ott")


class DeviceAuthorizationResponse(AcronisModel):
    device_code: str | None = Field(default=None, alias="device_code")
    user_code: str | None = Field(default=None, alias="user_code")
    verification_uri: str | None = Field(default=None, alias="verification_uri")
    verification_uri_complete: str | None = Field(default=None, alias="verification_uri_complete")
    expires_in: int | None = Field(default=None, alias="expires_in")
    interval: int | None = Field(default=None, alias="interval")


class DeviceAuthorizationApprovalResponse(AcronisModel):
    client_id: str | None = Field(default=None, alias="client_id")
    display_name: str | None = Field(default=None, alias="display_name")
    scope: list[str] | None = Field(default=None, alias="scope")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    tenant_name: str | None = Field(default=None, alias="tenant_name")
    is_current_tenant: bool | None = Field(default=None, alias="is_current_tenant")


class Contact(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    created_at: datetime | None = Field(default=None, alias="created_at")
    updated_at: datetime | None = Field(default=None, alias="updated_at")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    user_id: str | None = Field(default=None, alias="user_id")
    types: list[str] | None = Field(default=None, alias="types")
    email: str | None = Field(default=None, alias="email")
    address1: str | None = Field(default=None, alias="address1")
    address2: str | None = Field(default=None, alias="address2")
    country: str | None = Field(default=None, alias="country")
    state: str | None = Field(default=None, alias="state")
    city: str | None = Field(default=None, alias="city")
    zipcode: str | None = Field(default=None, alias="zipcode")
    phone: str | None = Field(default=None, alias="phone")
    firstname: str | None = Field(default=None, alias="firstname")
    lastname: str | None = Field(default=None, alias="lastname")
    title: str | None = Field(default=None, alias="title")
    website: str | None = Field(default=None, alias="website")
    industry: str | None = Field(default=None, alias="industry")
    organization_size: str | None = Field(default=None, alias="organization_size")
    email_confirmed: bool | None = Field(default=None, alias="email_confirmed")
    email_domain_type: str | None = Field(default=None, alias="email_domain_type")
    aan: str | None = Field(default=None, alias="aan")
    fax: str | None = Field(default=None, alias="fax")
    language: str | None = Field(default=None, alias="language")


class AccessPolicy(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    version: int | None = Field(default=None, alias="version")
    created_at: datetime | None = Field(default=None, alias="created_at")
    updated_at: datetime | None = Field(default=None, alias="updated_at")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")
    trustee_id: str | None = Field(default=None, alias="trustee_id")
    trustee_type: str | None = Field(default=None, alias="trustee_type")
    issuer_id: str | None = Field(default=None, alias="issuer_id")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    resource_server_id: str | None = Field(default=None, alias="resource_server_id")
    resource_namespace: str | None = Field(default=None, alias="resource_namespace")
    resource_path: str | None = Field(default=None, alias="resource_path")
    role_id: str | None = Field(default=None, alias="role_id")


class AccessPoliciesList(AcronisModel):
    paging: Paging | None = Field(default=None, alias="paging")
    timestamp: datetime | None = Field(default=None, alias="timestamp")
    items: list[AccessPolicy] | None = Field(default=None, alias="items")


class User(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    version: int | None = Field(default=None, alias="version")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    login: str | None = Field(default=None, alias="login")
    contact: Contact | None = Field(default=None, alias="contact")
    activated: bool | None = Field(default=None, alias="activated")
    enabled: bool | None = Field(default=None, alias="enabled")
    access_policies: list[AccessPolicy] | None = Field(default=None, alias="access_policies")
    created_at: datetime | None = Field(default=None, alias="created_at")
    updated_at: datetime | None = Field(default=None, alias="updated_at")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")
    language: str | None = Field(default=None, alias="language")
    idp_id: str | None = Field(default=None, alias="idp_id")
    external_id: str | None = Field(default=None, alias="external_id")
    origin_id: str | None = Field(default=None, alias="origin_id")
    origin_external_id: str | None = Field(default=None, alias="origin_external_id")
    disable_after: datetime | None = Field(default=None, alias="disable_after")
    personal_tenant_id: str | None = Field(default=None, alias="personal_tenant_id")
    business_types: list[str] | None = Field(default=None, alias="business_types")
    notifications: list[str] | None = Field(default=None, alias="notifications")
    mfa_status: str | None = Field(default=None, alias="mfa_status")
    session_mfa_status: str | None = Field(default=None, alias="session_mfa_status")
    delivery_channel: str | None = Field(default=None, alias="delivery_channel")
    external_operation_status: str | None = Field(default=None, alias="external_operation_status")
    terms_accepted: bool | None = Field(default=None, alias="terms_accepted")
    login_totp_time: datetime | None = Field(default=None, alias="login_totp_time")
    tenant_kind: str | None = Field(default=None, alias="tenant_kind")
    tenant_pricing_model: str | None = Field(default=None, alias="tenant_pricing_model")
    brand_id: str | None = Field(default=None, alias="brand_id")


class UserMe(User):
    """The currently authenticated user, as returned by /users/me."""


class UserBatch(AcronisModel):
    paging: Paging | None = Field(default=None, alias="paging")
    timestamp: datetime | None = Field(default=None, alias="timestamp")
    items: list[User] | None = Field(default=None, alias="items")


class CheckPasswordResult(AcronisModel):
    compromised: bool | None = Field(default=None, alias="compromised")


class Infra(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    owner_tenant_id: str | None = Field(default=None, alias="owner_tenant_id")
    location_id: str | None = Field(default=None, alias="location_id")
    platform_owned: bool | None = Field(default=None, alias="platform_owned")
    name: str | None = Field(default=None, alias="name")
    url: str | None = Field(default=None, alias="url")
    capabilities: list[str] | None = Field(default=None, alias="capabilities")
    content_url: str | None = Field(default=None, alias="content_url")
    content_mobile_url: str | None = Field(default=None, alias="content_mobile_url")
    backend_type: str | None = Field(default=None, alias="backend_type")
    version: int | None = Field(default=None, alias="version")
    readonly: bool | None = Field(default=None, alias="readonly")


class Location(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    owner_tenant_id: str | None = Field(default=None, alias="owner_tenant_id")
    platform_owned: bool | None = Field(default=None, alias="platform_owned")
    name: str | None = Field(default=None, alias="name")
    version: int | None = Field(default=None, alias="version")
    readonly: bool | None = Field(default=None, alias="readonly")


class RegistrationToken(AcronisModel):
    id: int | None = Field(default=None, alias="id")
    token: str | None = Field(default=None, alias="token")
    created_at: datetime | None = Field(default=None, alias="created_at")
    expires_at: datetime | None = Field(default=None, alias="expires_at")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    tenant_uuid: str | None = Field(default=None, alias="tenant_uuid")
    scopes: list[str] | None = Field(default=None, alias="scopes")


class ReportPeriod(AcronisModel):
    start: date | None = Field(default=None, alias="start")
    end: date | None = Field(default=None, alias="end")


class ReportParameters(AcronisModel):
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    level: str | None = Field(default=None, alias="level")
    kind: str | None = Field(default=None, alias="kind")
    formats: list[str] | None = Field(default=None, alias="formats")
    period: ReportPeriod | None = Field(default=None, alias="period")
    hide_zero_usage: bool | None = Field(default=None, alias="hide_zero_usage")
    show_skus: bool | None = Field(default=None, alias="show_skus")


class ReportSchedule(AcronisModel):
    enabled: bool | None = Field(default=None, alias="enabled")
    type: str | None = Field(default=None, alias="type")


class Report(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    version: int | None = Field(default=None, alias="version")
    result_action: str | None = Field(default=None, alias="result_action")
    recipients: list[str] | None = Field(default=None, alias="recipients")
    parameters: ReportParameters | None = Field(default=None, alias="parameters")
    schedule: ReportSchedule | None = Field(default=None, alias="schedule")
    generation_date: date | None = Field(default=None, alias="generation_date")


class StoredReport(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    report_format: str | None = Field(default=None, alias="report_format")
    size: int | None = Field(default=None, alias="size")
    created_at: datetime | None = Field(default=None, alias="created_at")
    status: str | None = Field(default=None, alias="status")


class GlobalSearchResult(AcronisModel):
    obj_type: str | None = Field(default=None, alias="obj_type")
    id: str | None = Field(default=None, alias="id")
    parent_id: str | None = Field(default=None, alias="parent_id")
    path: list[str] | None = Field(default=None, alias="path")
    kind: str | None = Field(default=None, alias="kind")
    login: str | None = Field(default=None, alias="login")
    name: str | None = Field(default=None, alias="name")
    first_name: str | None = Field(default=None, alias="first_name")
    last_name: str | None = Field(default=None, alias="last_name")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")


class Quota(AcronisModel):
    value: int | None = Field(default=None, alias="value")
    overage: int | None = Field(default=None, alias="overage")
    version: int | None = Field(default=None, alias="version")


class OfferingItem(AcronisModel):
    application_id: str | None = Field(default=None, alias="application_id")
    name: str | None = Field(default=None, alias="name")
    edition: str | None = Field(default=None, alias="edition")
    usage_name: str | None = Field(default=None, alias="usage_name")
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    updated_at: datetime | None = Field(default=None, alias="updated_at")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")
    status: int | None = Field(default=None, alias="status")
    locked: bool | None = Field(default=None, alias="locked")
    quota: Quota | None = Field(default=None, alias="quota")
    type: str | None = Field(default=None, alias="type")
    infra_id: str | None = Field(default=None, alias="infra_id")
    measurement_unit: str | None = Field(default=None, alias="measurement_unit")


class OfferingItemList(AcronisModel):
    paging: Paging | None = Field(default=None, alias="paging")
    timestamp: datetime | None = Field(default=None, alias="timestamp")
    items: list[OfferingItem] | None = Field(default=None, alias="items")


class OfferingItemPrice(AcronisModel):
    application_id: str | None = Field(default=None, alias="application_id")
    infra_id: str | None = Field(default=None, alias="infra_id")
    name: str | None = Field(default=None, alias="name")
    price: str | None = Field(default=None, alias="price")
    version: int | None = Field(default=None, alias="version")


class TenantUpdateLock(AcronisModel):
    enabled: bool | None = Field(default=None, alias="enabled")
    owner_id: str | None = Field(default=None, alias="owner_id")


class Tenant(AcronisModel):
    id: str | None = Field(default=None, alias="id")
    version: int | None = Field(default=None, alias="version")
    created_at: datetime | None = Field(default=None, alias="created_at")
    updated_at: datetime | None = Field(default=None, alias="updated_at")
    deleted_at: datetime | None = Field(default=None, alias="deleted_at")
    production_start_date: datetime | None = Field(default=None, alias="production_start_date")
    name: str | None = Field(default=None, alias="name")
    customer_type: str | None = Field(default=None, alias="customer_type")
    parent_id: str | None = Field(default=None, alias="parent_id")
    kind: str | None = Field(default=None, alias="kind")
    contact: Contact | None = Field(default=None, alias="contact")
    contacts: list[Contact] | None = Field(default=None, alias="contacts")
    offering_items: list[OfferingItem] | None = Field(default=None, alias="offering_items")
    enabled: bool | None = Field(default=None, alias="enabled")
    customer_id: str | None = Field(default=None, alias="customer_id")
    brand_id: int | None = Field(default=None, alias="brand_id")
    brand_uuid: str | None = Field(default=None, alias="brand_uuid")
    brand_enabled: bool | None = Field(default=None, alias="brand_enabled")
    barrier: int | None = Field(default=None, alias="barrier")
    internal_tag: str | None = Field(default=None, alias="internal_tag")
    language: str | None = Field(default=None, alias="language")
    owner_id: str | None = Field(default=None, alias="owner_id")
    has_children: bool | None = Field(default=None, alias="has_children")
    default_idp_id: str | None = Field(default=None, alias="default_idp_id")
    update_lock: TenantUpdateLock | None = Field(default=None, alias="update_lock")
    ancestral_access: bool | None = Field(default=None, alias="ancestral_access")
    mfa_status: str | None = Field(default=None, alias="mfa_status")
    pricing_mode: str | None = Field(default=None, alias="pricing_mode")
    external_operation_status: str | None = Field(default=None, alias="external_operation_status")


class TenantBatch(AcronisModel):
    paging: Paging | None = Field(default=None, alias="paging")
    timestamp: datetime | None = Field(default=None, alias="timestamp")
    items: list[Tenant] | None = Field(default=None, alias="items")


class TenantApplications(AcronisModel):
    tenant: str | None = Field(default=None, alias="tenant")
    applications: list[str] | None = Field(default=None, alias="applications")


class UsageOfferingItem(AcronisModel):
    status: int | None = Field(default=None, alias="status")
    quota: Quota | None = Field(default=None, alias="quota")


class Usage(AcronisModel):
    application_id: str | None = Field(default=None, alias="application_id")
    name: str | None = Field(default=None, alias="name")
    edition: str | None = Field(default=None, alias="edition")
    usage_name: str | None = Field(default=None, alias="usage_name")
    type: str | None = Field(default=None, alias="type")
    measurement_unit: str | None = Field(default=None, alias="measurement_unit")
    infra_id: str | None = Field(default=None, alias="infra_id")
    tenant_uuid: str | None = Field(default=None, alias="tenant_uuid")
    tenant_id: int | None = Field(default=None, alias="tenant_id")
    range_start: datetime | None = Field(default=None, alias="range_start")
    absolute_value: int | None = Field(default=None, alias="absolute_value")
    value: int | None = Field(default=None, alias="value")
    offering_item: UsageOfferingItem | None = Field(default=None, alias="offering_item")


class TenantUsages(AcronisModel):
    tenant: str | None = Field(default=None, alias="tenant")
    usages: list[Usage] | None = Field(default=None, alias="usages")


class UsagePutResultItem(AcronisModel):
    tenant_id: str | None = Field(default=None, alias="tenant_id")
    resource_id: str | None = Field(default=None, alias="resource_id")
    usage_type: str | None = Field(default=None, alias="usage_type")
    offering_item: str | None = Field(default=None, alias="offering_item")
    infra_id: str | None = Field(default=None, alias="infra_id")
    error: ErrorScheme | None = Field(default=None, alias="error")


class EditionSwitchWarnings(AcronisModel):
    warnings: list[str] | None = Field(default=None, alias="warnings")


class TenantPricingSettings(AcronisModel):
    mode: str | None = Field(default=None, alias="mode")
    currency: str | None = Field(default=None, alias="currency")
    version: int | None = Field(default=None, alias="version")
    production_start_date: datetime | None = Field(default=None, alias="production_start_date")


class TenantBrand(AcronisModel):
    """Branding options of a tenant, combining the brand and SMTP settings schemas."""

    id: str | None = Field(default=None, alias="id")
    company_name: str | None = Field(default=None, alias="company_name")
    service_name: str | None = Field(default=None, alias="service_name")
    color: str | None = Field(default=None, alias="color")
    color_scheme: str | None = Field(default=None, alias="color_scheme")
    logotype: str | None = Field(default=None, alias="logotype")
    account_server_url: str | None = Field(default=None, alias="account_server_url")
    backup_console_url: str | None = Field(default=None, alias="backup_console_url")
    router_url: str | None = Field(default=None, alias="router_url")
    reg_server_url: str | None = Field(default=None, alias="reg_server_url")
    agent_gateway_url: str | None = Field(default=None, alias="agent_gateway_url")
    home_url: str | None = Field(default=None, alias="home_url")
    help_url: str | None = Field(default=None, alias="help_url")
    support_url: str | None = Field(default=None, alias="support_url")
    support_phone: str | None = Field(default=None, alias="support_phone")
    knowledgebase_url: str | None = Field(default=None, alias="knowledgebase_url")
    user_guide_url: str | None = Field(default=None, alias="user_guide_url")
    upsell_url: str | None = Field(default=None, alias="upsell_url")
    terms_url: str | None = Field(default=None, alias="terms_url")
    platform_terms_url: str | None = Field(default=None, alias="platform_terms_url")
    privacy_policy_url: str | None = Field(default=None, alias="privacy_policy_url")
    mobile_app_android_download_url: str | None = Field(default=None, alias="mobile_app_android_download_url")
    mobile_app_ios_download_url: str | None = Field(default=None, alias="mobile_app_ios_download_url")
    owns_custom_legal_docs: bool | None = Field(default=None, alias="owns_custom_legal_docs")
    white_labeled_agent: bool | None = Field(default=None, alias="white_labeled_agent")
    smtp_override: int | None = Field(default=None, alias="smtp_override")
    smtp_reply_address: str | None = Field(default=None, alias="smtp_reply_address")
    smtp_server: str | None = Field(default=None, alias="smtp_server")
    smtp_port: int | None = Field(default=None, alias="smtp_port")
    smtp_user: str | None = Field(default=None, alias="smtp_user")
    smtp_password: str | None = Field(default=None, alias="smtp_password")
    smtp_encryption: str | None = Field(default=None, alias="smtp_encryption")


class MfaTenantStatus(AcronisModel):
    mfa_status: str | None = Field(default=None, alias="mfa_status")
    users: int | None = Field(default=None, alias="users")
    users_with_totp_enabled: int | None = Field(default=None, alias="users_with_totp_enabled")
    users_count: int | None = Field(default=None, alias="users_count")
    users_with_totp_enabled_count: int | None = Field(default=None, alias="users_with_totp_enabled_count")
    update_allowed: bool | None = Field(default=None, alias="update_allowed")
