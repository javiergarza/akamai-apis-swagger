---
title: "applicationLoadBalancer"
slug: "applicationloadbalancer"
hidden: false
createdAt: "2020-06-15T20:41:39.183Z"
updatedAt: "2020-06-15T20:41:39.184Z"
---
__Property Manager name__: [Application Load Balancer Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0017)

Enables the Application Load Balancer Cloudlet, which automates load balancing based on configurable criteria. To configure this behavior, use either the Cloudlets Policy Manager or the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to set up a policy.

__Options__:

<div class="option" markdown="1" id="applicationLoadBalancer.enabled" >

- `enabled` (_boolean_): Activates the Application Load Balancer Cloudlet.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.label" >

- `label` (_string_): A label to distinguish this Application Load Balancer policy from any others within the same property.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieType" >

- `stickinessCookieType` (_enum string_): Determines how a cookie persistently associates the client with a load-balanced origin.  Specify an overall `DURATION` or a `FIXED_DATE` for when the cookie expires.  Specify `ON_BROWSER_CLOSE` to limit the cookie duration to browser sessions, or to when the `ORIGIN_SESSION` terminates.  (After the cookie expires, the cookie type re-evaluates.) To preserve the cookie indefinitely, specify `NEVER`.  To dynamically reassign different load-balanced origins for each request, specify `NONE`.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessExpirationDate" >

- `stickinessExpirationDate` (_ISO 8601 format date/time string_): With `stickinessCookieType` set to `FIXED_DATE`, this specifies when the cookie expires.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessDuration" >

- `stickinessDuration` (_duration string_): With `stickinessCookieType` set to `DURATION`, sets how long it is before the cookie expires.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessRefresh" >

- `stickinessRefresh` (_boolean_): With `stickinessCookieType` set to `DURATION`, enabling this extends the duration of the cookie with each new request. When enabled, the `DURATION` thus specifies the latency between requests that would cause the cookie to expire.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.originCookieName" >

- `originCookieName` (_string_): Specifies the name for your session cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.specifyStickinessCookieDomain" >

- `specifyStickinessCookieDomain` (_boolean_): Specifies whether to use a cookie domain with the stickiness cookie, to tell the browser to which domain to send the cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieDomain" >

- `stickinessCookieDomain` (_string_): With `specifyStickinessCookieDomain` enabled, specifies the domain to track the stickiness cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieAutomaticSalt" >

- `stickinessCookieAutomaticSalt` (_boolean_): Sets whether to assign a _salt_ value automatically to the cookie to prevent manipulation by the user. You should not enable this if sharing the population cookie across more than one property.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSalt" >

- `stickinessCookieSalt` (_string_): With `stickinessCookieAutomaticSalt` disabled, specifies the stickiness cookie's salt value. Use this option to share the cookie across many properties.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSetHttpOnlyFlag" >

- `stickinessCookieSetHttpOnlyFlag` (_boolean_): Ensures the cookie is transmitted only over HTTP.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSetSecureFlag" >

- `stickinessCookieSetSecureFlag` (_boolean_): Deploys the stickiness cookie as secure.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownNetStorage" >

- `allDownNetStorage` (_object_): Specifies a NetStorage account for a static maintenance page as a fallback when no origins are available. This example shows the object's structure:

        "allDownNetStorage": {
            "id"                 : "uniq_id",
            "name"               : "Download Area",
            "downloadDomainName" : "download.example.akamai.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownNetStorageFile" >

- `allDownNetStorageFile` (_string_): Specifies the fallback maintenance page's filename, expressed as a full path from the root of the NetStorage server.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownStatusCode" >

- `allDownStatusCode` (_string_): Specifies the HTTP response code when all load-balancing origins are unavailable.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverStatusCodes" >

- `failoverStatusCodes` (_array of string values_): Specifies a set of HTTP status codes that signal a failure on the origin, in which case the cookie that binds the client to that origin is invalidated and the client is rerouted to another available origin.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverMode" >

- `failoverMode` (_enum string_): Determines what to do if an origin fails. If set to `AUTOMATIC`, automatically determines which origin in the policy to try next.  If set to `MANUAL`, you define a sequence of failover origins.  (If failover runs out of origins, requests are sent to NetStorage.) Setting `DISABLED` turns off failover, but maintains origin stickiness even when the origin goes down.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverOriginMap" >

- `failoverOriginMap` (_array_): With `failoverMode` set to `MANUAL`, this specifies a fixed set of failover mapping rules.  If the origin identified by `fromOriginId` fails, requests stuck to that origin retry for each alternate origin `toOriginIds` specifies, until one succeeds:

        "failoverOriginMap" : [
            {
                "fromOriginId": "origin1",
                "toOriginIds": [ "origin2", "origin3" ]
            }
        ]

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverAttemptsThreshold" >

- `failoverAttemptsThreshold` (_number_): Sets the number of failed requests that would trigger the failover process.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allowCachePrefresh" >

- `allowCachePrefresh` (_boolean_): When enabled, allows the cache to prefresh.  Only appropriate if all origins serve the same content for the same URL.

</div>

</div>

<div class="feature" data-feature="audienceSegmentation" markdown="1">
