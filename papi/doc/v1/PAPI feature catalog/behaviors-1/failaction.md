---
title: "failAction"
slug: "failaction"
hidden: false
createdAt: "2020-06-15T21:23:30.675Z"
updatedAt: "2020-06-15T21:23:30.675Z"
---
__Property Manager name__: [Site Failover](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9017)

Specifies how to respond when the origin is not available: by serving stale content, by serving an error page, or by redirecting.  To apply this behavior, you should match on an [`originTimeout`](#origintimeout) or [`matchResponseCode`](#matchresponsecode).

__Options__:

<div class="option" markdown="1" id="failAction.enabled" >

- `enabled` (_boolean_): When enabled in case of a failure to contact the origin, the current behavior applies.

</div>

<div class="option" markdown="1" id="failAction.actionType" >

- `actionType` (_enum string_): Specifies the basic action to take when there is a failure to contact the origin:

    - `SERVE_STALE` serves content that is already in the cache.
    - `REDIRECT` specifies a redirect action. (Use with these options:     `redirectHostnameType`, `redirectHostname`, `redirectCustomPath`,     `redirectPath`, `redirectMethod`, `modifyProtocol`, and `protocol`.)
    - `RECREATED_CEX` serves alternate content from an external     network.  (Use with these options: `cexHostname`, `cexCustomPath`,     and `cexPath`.)
    - `RECREATED_CO` serves alternate content from your network.  (Use     with these options: `contentHostname`, `contentCustomPath`, and `contentPath`.)
    - `RECREATED_NS` serves     [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)     content. (Use with these options: `netStorageHostname`,     `netStoragePath`, and `cpCode`.)
    - `DYNAMIC` allows you to serve dynamic SaaS content if SaaS     acceleration is available on your contract.  (Use with these     options: `dynamicMethod`, `dynamicCustomPath`, `saasType`,     `saasSuffix`, `saasRegex`, and `saasReplace`.)

</div>

<div class="option" markdown="1" id="failAction.statusCode" >

- `statusCode` (_numeric enum_): Assigns a new HTTP status code to the failure response.  <!-- `100`, `101`, `102`, `103`, `122`, `200`, `201`, `202`, `203`, `204`, `205`, `206`, `207`, `226`, `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `422`, `423`, `424`, `425`, `426`, `428`, `429`, `431`, `444`, `449`, `450`, `499`, `500`, `501`, `502`, `503`, `504`, `505`, `506`, `507`, `509`, `510`, `511`, `598`, `599`-->

</div>

<div class="option" markdown="1" id="failAction.cpCode" >

- `cpCode` (_object_): When `actionType` is `RECREATED_NS`, this specifies a _cpcode_ for which to log errors for the NetStorage location. It appears as an object that includes an `id` key and a descriptive `name`:

        "cpCode": {
            "id"   : 12345,
            "name" : "my cpcode"
        }

</div>

<div class="option" markdown="1" id="failAction.netStorageHostname" >

- `netStorageHostname` (_object_): When the `actionType` is `RECREATED_NS`, specifies the [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) origin to serve the alternate content, as in the example below. Contact Akamai Professional Services for your NetStorage origin's `id`.

        "netStorageHostname": {
            "id"                 : "netstorage_id",
            "name"               : "Example Downloads",
            "downloadDomainName" : "download.example.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="failAction.netStoragePath" >

- `netStoragePath` (_string; allows [variables](#vf)_): When the `actionType` is `RECREATED_NS`, specifies the path for the [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) request.

</div>

<div class="option" markdown="1" id="failAction.redirectMethod" >

- `redirectMethod` (_numeric enum_): When the `actionType` is `REDIRECT`, specifies the HTTP response code, either `301` or `302`.

</div>

<div class="option" markdown="1" id="failAction.redirectHostnameType" >

- `redirectHostnameType` (_enum string_): When the `actionType` is `REDIRECT`, this specifies whether to preserve the `ORIGINAL` hostname in the redirect, or whether to use an `ALTERNATE` hostname specified with `redirectHostname`.

</div>

<div class="option" markdown="1" id="failAction.redirectHostname" >

- `redirectHostname` (_string; allows [variables](#vf)_): When the `actionType` is `REDIRECT` and the `redirectHostnameType` is `ALTERNATE`, this specifies the hostname for the redirect.

</div>

<div class="option" markdown="1" id="failAction.redirectCustomPath" >

- `redirectCustomPath` (_boolean_): When the `actionType` is `REDIRECT`, enabling this allows you use `redirectPath` to customize a new path.

</div>

<div class="option" markdown="1" id="failAction.redirectPath" >

- `redirectPath` (_string; allows [variables](#vf)_): When the `actionType` is `REDIRECT`, this specifies a new path.

</div>

<div class="option" markdown="1" id="failAction.modifyProtocol" >

- `modifyProtocol` (_boolean_): When the `actionType` is `REDIRECT`, or if the `dynamicMethod` is either `SERVE_301` or `SERVE_302`, enabling this allows you to modify the redirect's protocol using the value of the `protocol` field.

</div>

<div class="option" markdown="1" id="failAction.protocol" >

- `protocol` (_enum string_): When the `actionType` is `REDIRECT` and `modifyProtocol` is enabled, this specifies the redirect's protocol, either `HTTP` or `HTTPS`.

</div>

<div class="option" markdown="1" id="failAction.preserveQueryString" >

- `preserveQueryString` (_boolean_): When using either `contentCustomPath`, `cexCustomPath`, `dynamicCustomPath`, or `redirectCustomPath` to specify a custom path, enabling this passes in the original request's query string as part of the path.

</div>

<div class="option" markdown="1" id="failAction.cexHostname" >

- `cexHostname` (_string; allows [variables](#vf)_): When `actionType` is `RECREATED_CEX`, this specifies a hostname.

</div>

<div class="option" markdown="1" id="failAction.cexCustomPath" >

- `cexCustomPath` (_boolean_): When `actionType` is `RECREATED_CEX`, enabling this allows you to specify a custom path.

</div>

<div class="option" markdown="1" id="failAction.cexPath" >

- `cexPath` (_string; allows [variables](#vf)_): When `actionType` is `RECREATED_CEX` and `cexCustomPath` is enabled, this specifies a custom path.

</div>

<div class="option" markdown="1" id="failAction.contentHostname" >

- `contentHostname` (_string; allows [variables](#vf)_): When the `actionType` is `RECREATED_CO`, specifies the static hostname for the alternate redirect.

</div>

<div class="option" markdown="1" id="failAction.contentCustomPath" >

- `contentCustomPath` (_boolean_): When the `actionType` is `RECREATED_CO`, enabling this allows you to specify a custom redirect path.

</div>

<div class="option" markdown="1" id="failAction.contentPath" >

- `contentPath` (_string; allows [variables](#vf)_): When the `actionType` is `RECREATED_CO` and `contentCustomPath` is enabled, this specifies a custom redirect path.

</div>

<div class="option" markdown="1" id="failAction.dynamicMethod" >

- `dynamicMethod` (_enum string_): With the `actionType` set to `DYNAMIC`, specifies the redirect method, either `SERVE_301`, `SERVE_302`, or `SERVE_ALTERNATE`.

</div>

<div class="option" markdown="1" id="failAction.dynamicCustomPath" >

- `dynamicCustomPath` (_boolean_): When enabled, allows you to modify the original requested path.

</div>

<div class="option" markdown="1" id="failAction.dynamicPath" >

- `dynamicPath` (_string; allows [variables](#vf)_): With `dynamicCustomPath` enabled, specifies the new path.

</div>

<div class="option" markdown="1" id="failAction.saasType" >

- `saasType` (_enum string_): Identifies the component of the request that identifies the SaaS dynamic failaction: either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="failAction.saasSuffix" >

- `saasSuffix` (_string; allows [variables](#vf)_): With `actionType` set to `DYNAMIC`, specifies the static portion of the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasRegex" >

- `saasRegex` (_string_): With `actionType` set to `DYNAMIC`, specifies the substitution pattern (a Perl-compatible regular expression) that defines the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasReplace" >

- `saasReplace` (_string; allows [variables](#vf)_): With `actionType` set to `DYNAMIC`, specifies the replacement pattern that defines the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCnameEnabled" >

- `saasCnameEnabled` (_boolean_): With the `saasType` set to `HOSTNAME`, specifies whether to use a CNAME chain to determine the hostname for the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCnameLevel" >

- `saasCnameLevel` (_number_): With `saasCnameEnabled` on, specifies the number of elements in the CNAME chain backwards from the edge hostname that determines the hostname for the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCookie" >

- `saasCookie` (_string; allows [variables](#vf)_): With `saasType` set to `COOKIE`, specifies the name of the cookie that identifies this SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasQueryString" >

- `saasQueryString` (_string; allows [variables](#vf)_): With `saasType` set to `QUERY_STRING`, specifies the name of the query parameter that identifies this SaaS dynamic failaction.

</div>

</div>

<div class="feature" data-feature="fastInvalidate" markdown="1">
