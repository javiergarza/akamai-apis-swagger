---
title: "segmentedMediaOptimization"
slug: "segmentedmediaoptimization"
hidden: false
createdAt: "2020-06-15T22:00:31.726Z"
updatedAt: "2020-06-15T22:00:31.726Z"
---
__Property Manager name__: [Segmented Media Delivery Mode](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0080)

Optimizes segmented media for live or streaming delivery contexts.

__Options__:

<div class="option" markdown="1" id="segmentedMediaOptimization.behavior" >

- `behavior` (_enum string_): Set to either cached `ON_DEMAND`, or streaming `LIVE`. Only `ON_DEMAND` is allowed for [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) origins.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.enableUllStreaming" >

- `enableUllStreaming` (_boolean_): 2DO

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.showAdvanced" >

- `showAdvanced` (_boolean_): When enabled, allows you to configure advanced media options.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.liveType" >

- `liveType` (_enum string_): The type of live media, either `CONTINUOUS` or an `EVENT` for a range of time.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.startTime" >

- `startTime` (_ISO 8601 format date/time string_): With `liveType` set to `EVENT`, this specifies when the live media event begins.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.endTime" >

- `endTime` (_ISO 8601 format date/time string_): With `liveType` set to `EVENT`, this specifies when the live media event ends.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.dvrType" >

- `dvrType` (_enum string_): The type of DVR, either `CONFIGURABLE` or `UNKNOWN`.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.dvrWindow" >

- `dvrWindow` (_duration string_): Set the duration for your media, or `0m` if a DVR is not required.

</div>

</div>

<div class="feature" data-feature="segmentedMediaStreamingPrefetch" markdown="1">
