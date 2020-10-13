---
title: "returnCacheStatus"
slug: "returncachestatus"
hidden: false
createdAt: "2020-06-15T21:55:54.053Z"
updatedAt: "2020-06-15T21:55:54.053Z"
---
__Property Manager name__: [Return Cache Status](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9028)

Generates a response header with information about cache status. Among other things, this can tell you whether the response came from the Akamai cache, or from the origin. Status values report with either of these forms of syntax, depending for example on whether you're deploying traffic using [`sureRoute`](#sureroute) or [`tieredDistribution`](#tiereddistribution):

    {status} from child
    {status} from child, {status} from parent

The `status` value can be any of the following:

- `Hit`: The object was retrieved from Akamai's cache.

- `Miss`: The object was not found in the Akamai cache.

- `RefreshHit`: The object was found in Akamai's cache, but was stale, so an `If-Modified-Since` request was made to the customer origin, with 304 as the response code, indicating unmodified content.

- `HitStale`: The object was found in Akamai's cache and was stale, but a more recent object was not available from the customer origin, so the cache served the stale object to the client.

- `Constructed`: The [`constructResponse`](#constructresponse) behavior directly specified the response to the client.

- `Redirect`: The Akamai edge configuration specified a redirect, typically by executing the [`redirect`](#redirect), [`redirectPlus`](#redirectplus), or [`edgeRedirector`](#edgeredirector) behaviors.

- `Error`: An error occurred, typically when authorization is denied or the request is rejected by WAF.

__Options__:

<div class="option" markdown="1" id="returnCacheStatus.responseHeaderName" >

- `responseHeaderName` (_string_): Specifies the name of the HTTP header in which to report the cache status value.

</div>

</div>

<div class="feature" data-feature="rewriteUrl" markdown="1">
