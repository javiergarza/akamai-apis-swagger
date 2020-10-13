---
title: "segmentedMediaStreamingPrefetch"
slug: "segmentedmediastreamingprefetch"
hidden: false
createdAt: "2020-06-15T22:00:52.819Z"
updatedAt: "2020-06-15T22:00:52.819Z"
---
__Property Manager name__: [Segmented Media Streaming - Prefetch](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5007)

Prefetches HLS and DASH media stream manifest and segment files, accelerating delivery to end users. For prefetching to work, your origin media's response needs to specify `CDN-Origin-Assist-Prefetch-Path` headers with each URL to prefetch, expressed as either a relative or absolute path.

__Options__:

<div class="option" markdown="1" id="segmentedMediaStreamingPrefetch.enabled" >

- `enabled` (_boolean_): Enables media stream prefetching.

</div>

</div>

<div class="feature" data-feature="setVariable" markdown="1">
