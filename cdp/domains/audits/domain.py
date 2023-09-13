from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.network.types import (
    IPAddressSpace,
    CorsErrorStatus,
    ClientSecurityState,
    LoaderId,
    RequestId
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.audits.types import (
    ContentSecurityPolicyViolationType,
    AttributionReportingIssueType,
    HeavyAdResolutionStatus,
    ClientHintIssueReason,
    NavigatorUserAgentIssueDetails,
    BounceTrackingIssueDetails,
    FederatedAuthUserInfoRequestIssueReason,
    ContentSecurityPolicyIssueDetails,
    AttributionReportingIssueDetails,
    ClientHintIssueDetails,
    InspectorIssue,
    BlockedByResponseReason,
    SharedArrayBufferIssueType,
    SourceCodeLocation,
    StylesheetLoadingIssueDetails,
    CookieOperation,
    SharedArrayBufferIssueDetails,
    FederatedAuthUserInfoRequestIssueDetails,
    FederatedAuthRequestIssueReason,
    FailedRequestInfo,
    LowTextContrastIssueDetails,
    HeavyAdReason,
    HeavyAdIssueDetails,
    InspectorIssueCode,
    BlockedByResponseIssueDetails,
    QuirksModeIssueDetails,
    StyleSheetLoadingIssueReason,
    MixedContentResourceType,
    AffectedRequest,
    GenericIssueDetails,
    CookieIssueDetails,
    GenericIssueErrorType,
    CorsIssueDetails,
    FederatedAuthRequestIssueDetails,
    MixedContentResolutionStatus,
    InspectorIssueDetails,
    MixedContentIssueDetails,
    IssueId,
    DeprecationIssueDetails,
    AffectedFrame,
    AffectedCookie
)
from cdp.domains.runtime.types import (
    ScriptId
)
from cdp.domains.dom.types import (
    BackendNodeId
)


@dataclass
class Audits(BaseDomain):
    def get_encoded_response(
        self,
        request_id: RequestId,
        encoding: str,
        quality: MaybeUndefined[float],
        size_only: MaybeUndefined[bool]
    ):
        params = {
            "requestId": request_id,
            "encoding": encoding,
        }

        if is_defined(
            quality
        ):
            params["quality"] = quality

        if is_defined(
            size_only
        ):
            params["sizeOnly"] = size_only

        return self._send_command(
            "Audits.getEncodedResponse",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.enable",
            params
        )

    def check_contrast(
        self,
        report_aaa: MaybeUndefined[bool]
    ):
        params = {}

        if is_defined(
            report_aaa
        ):
            params["reportAAA"] = report_aaa

        return self._send_command(
            "Audits.checkContrast",
            params
        )

    def check_forms_issues(
        self
    ):
        params = {}

        return self._send_command(
            "Audits.checkFormsIssues",
            params
        )

