---
title: "adaptiveAcceleration"
slug: "adaptiveacceleration"
excerpt: "__Property Manager name__: [Adaptive Acceleration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0120)"
hidden: false
createdAt: "2020-06-15T20:24:46.595Z"
updatedAt: "2020-06-15T21:00:39.685Z"
---
With the [`http2`](#http2) and [`realUserMonitoring`](#realusermonitoring) features enabled, uses HTTP/2 server push to pre-position content and improve the performance of HTML page loading based on Real User Monitoring (RUM) timing data. Also use this feature to allow browsers to preconnect to content likely needed for upcoming requests.  Use the [Adaptive Acceleration API](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html) to report on the set of assets this feature optimizes.

__Options__:

<div class="option" markdown="1" id="adaptiveAcceleration.source" >

- `source` (_string_): With `enablePreconnect` or `enablePush` on, specifies the type of data that anticipates optimal connections. If you specify a value of `Real User Monitoring`, make sure to enable the corresponding [`realUserMonitoring`](#realusermonitoring) behavior. If you specify `mPulse`, enable the [`mPulse`](#mpulse) behavior.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enablePush" >

- `enablePush` (_boolean_): Enables adaptive acceleration's HTTP/2 server push feature.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enablePreconnect" >

- `enablePreconnect` (_boolean_): When enabled, allows browsers to open TCP connections to web pages before making requests.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.preloadEnable" >

- `preloadEnable` (_boolean_): With the beacon `source` set to `mPulse`, allows fonts to preload.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enableRo" >

- `enableRo` (_boolean_): Enables the Resource Optimizer, which compresses common file components such as scripts, fonts, and CSS, and caches them on the Akamai network.

</div>

</div>

<div class="feature" data-feature="adaptiveImageCompression" markdown="1">
