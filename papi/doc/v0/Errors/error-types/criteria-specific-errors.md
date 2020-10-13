---
title: "Criteria-specific errors"
slug: "criteria-specific-errors"
hidden: false
createdAt: "2020-06-05T21:26:40.722Z"
updatedAt: "2020-06-05T21:26:52.887Z"
---
These errors relate to how specific match criteria execute. They may
be listed within [Rule](#rule) objects, and may prevent you
from activating the property version.

| Type | Description |
| :--- | :--- |
| `cloudlets_origin_group` |  For [`cloudletsOrigin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#cloudletsorigin) criteria to work, there must be an [`allowCloudletsOrigins`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#allowcloudletsorigins) placed within a parent rule. |
| `general_warning` |  The criteria match may negatively affect performance. Test thoroughly on `staging` before deploying to `production`. |
| `incompatible_origin_type` |  The [`cloudletsOrigin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#cloudletsorigin) criteria only works when the [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior's `originType` is set to `CUSTOMER`, `NET_STORAGE`, or `APPLICATION_LOAD_BALANCER`. |
| `incompatible_with_any_conditions` |  Specifying [`cloudletsOrigin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#cloudletsorigin) along with any other criteria may make the origin inaccessible during a client request. |
| `need_allowpatch` |  To use [`requestMethod`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#requestmethod) to match PATCH requests, you need to enable the [`allowPatch`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#allowpatch) behavior. |
| `need_allowpost` |  To use [`requestMethod`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#requestmethod) to match POST requests, you need to enable the [`allowPost`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#allowpost) behavior. |
| `need_token_verify_behavior` |  The [`tokenAuthorization`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#tokenauthorization) match requires a [`verifyTokenAuthorization`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#verifytokenauthorization) behavior in a parent rule with its `failureResponse` option disabled.
| `need_webdav` |  To use [`requestMethod`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#requestmethod) to match the specified method, you need to enable the [`webdav`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#webdav) behavior. |
| `onlyonedge` |  Criteria such as [`clientIp`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#clientip), [`clientIpVersion`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#clientipversion), [`userLocation`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#userlocation), and [`userNetwork`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#usernetwork) only match on edge servers, not when requests are forwarded to other Akamai servers. Contact your Akamai representative for guidance. |
| `options_with_webdav` |  Requests that specify the OPTIONS method are always passed to the origin, so you can't use [`requestMethod`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#requestmethod) to match them. |
| `origin_is_required` |  The [`cloudletsOrigin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#cloudletsorigin) behavior must be paired with an [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior. |
| `purge_warning` |  The [`requestMethod`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#requestmethod) match on `AKAMAI_PURGE` or `AKAMAI_TRANSLATE` values requires familiarity with Akamai's edge content purge system. Test thoroughly on `staging` before deploying to `production`. |
| `requires_spdy` |  The [`bucket`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#bucket) criteria can only be used along with the [`spdy`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#spdy) behavior. |
| `should_vary_by_user_agent` |  When modifying content based on the [`deviceCharacteristic`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#devicecharacteristic), you should use the [`modifyOutgoingResponseHeader`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#modifyoutgoingresponseheader) behavior to specify a `Vary: User-Agent` header. |
| `suggest_audiencesegmentation` |  Rather than [randomly]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#random) segmenting your traffic, consider applying [`audienceSegmentation`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#audiencesegmentation) to divide users into different groups based on a persistent cookie. |
| `upper_lower_warning` |  The match specifies a `lowerBound` value that's greater than the `upperBound`. |
| `warn_use_headers` |  Requests that don't include an `X-Forwarded-For` header don't match. Consider disabling the `useOnlyFirstXForwardedForIp` option. |