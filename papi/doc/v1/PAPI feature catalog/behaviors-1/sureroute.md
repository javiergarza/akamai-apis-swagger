---
title: "sureRoute"
slug: "sureroute"
hidden: false
createdAt: "2020-06-15T22:05:36.085Z"
updatedAt: "2020-06-15T22:05:36.085Z"
---
__Property Manager name__: [SureRoute](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0081)

The [SureRoute](http://www.akamai.com/dl/feature_sheets/fs_edgesuite_sureroute.pdf) feature continually tests different routes between origin and edge servers to identify the optimal path. By default, it conducts _races_ to identify alternative paths to use in case of a transmission failure. These races increase origin traffic slightly.

This behavior allows you to configure SureRoute along with a test
object to improve delivery of non-cacheable `no-store` or
`bypass-cache` content. Since edge servers are already positioned as
close as possible to requesting clients, the behavior does not apply
to cacheable content.

__Options__:

<div class="option" markdown="1" id="sureRoute.enabled" >

- `enabled` (_boolean_): Enables the SureRoute behavior, to optimize delivery of non-cached content.

</div>

<div class="option" markdown="1" id="sureRoute.type" >

- `type` (_enum string_): Specifies the set of edge servers used to test routes, either the default `PERFORMANCE` or a `CUSTOM_MAP` that must be provided to you by Akamai Professional Services.

</div>

<div class="option" markdown="1" id="sureRoute.customMap" >

- `customMap` (_string_): If `type` is `CUSTOM_MAP`, this specifies the map string provided to you by Akamai Professional Services, or included as part of the [Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html) product.

</div>

<div class="option" markdown="1" id="sureRoute.testObjectUrl" >

- `testObjectUrl` (_string_): Specifies the path and filename for your origin's test object to use in races to test routes.

    Akamai provides sample test objects for the
    [Dynamic Site Accelerator](https://dl.akamai.com/DSA/DSA_SLA_test_page.zip)
    and
    [Web Application Accelerator](https://dl.akamai.com/WAA/Waa_sla_sr_v1.zip)
    products. If you want to use your own test object, it needs to be on
    the same origin server as the traffic being served through
    SureRoute. Make sure it returns a `200` HTTP response and does not
    require authentication. The file should be an average-sized static
    HTML file (`Content-Type: text/html`) that is no smaller than 8KB,
    with no back-end processing.

    If you have more than one origin server deployed behind a load
    balancer, you can configure it to serve the test object directly on
    behalf of the origin, or route requests to the same origin server to
    avoid deploying the test object on each origin server.

</div>

<div class="option" markdown="1" id="sureRoute.toHostStatus" >

- `toHostStatus` (_enum string_): If set to `INCOMING_HH`, uses the incoming `Host` header when requesting the SureRoute test object. If set to `OTHER`, use `toHost` to specify a custom `Host` header.

</div>

<div class="option" markdown="1" id="sureRoute.toHost" >

- `toHost` (_string_): If `toHostStatus` is `OTHER`, this specifies the custom `Host` header to use when requesting the SureRoute test object.

</div>

<div class="option" markdown="1" id="sureRoute.raceStatTtl" >

- `raceStatTtl` (_duration string_): Specifies the time-to-live to preserve SureRoute race results, typically `30m`. If traffic exceeds a certain threshold after TTL expires, the overflow is routed directly to the origin, not necessarily optimally. If traffic remains under the threshold, the route is determined by the winner of the most recent race.

</div>

<div class="option" markdown="1" id="sureRoute.forceSslForward" >

- `forceSslForward` (_boolean_): Forces SureRoute to use SSL when requesting the origin's test object, appropriate if your origin does not respond to HTTP requests, or responds with a redirect to HTTPS.

</div>

<div class="option" markdown="1" id="sureRoute.enableCustomKey" >

- `enableCustomKey` (_boolean_): When disabled, caches race results under the race destination's hostname. If enabled, use `customStatKey` to specify a custom hostname.

</div>

<div class="option" markdown="1" id="sureRoute.customStatKey" >

- `customStatKey` (_string_): With `enableCustomKey` enabled, this specifies a hostname under which to cache race results. This may be useful when a property corresponds to many origin hostnames. By default, SureRoute would launch races for each origin, but consolidating under a single hostname runs only one race.

</div>

</div>

<div class="feature" data-feature="tcpOptimization" markdown="1">
