---
title: "prefreshCache"
slug: "prefreshcache"
hidden: false
createdAt: "2020-06-15T21:47:04.237Z"
updatedAt: "2020-06-15T21:47:04.237Z"
---
__Property Manager name__: [Cache Prefreshing](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0065)

Refresh cached content before its time-to-live (TTL) expires, to keep end users from having to wait for the origin to provide fresh content.

Prefreshing starts asynchronously based on a percentage of remaining TTL. The edge serves the prefreshed content only after the TTL expires. If the percentage is set too high, and there is not enough time to retrieve the object, the end user waits for it to refresh from the origin, as is true by default without this prefresh behavior enabled. The edge does not serve stale content.

__Options__:

<div class="option" markdown="1" id="prefreshCache.enabled" >

- `enabled` (_boolean_): Enables the cache prefreshing behavior.

</div>

<div class="option" markdown="1" id="prefreshCache.prefreshval" >

- `prefreshval` (_number within 0-99 range_): Specifies when the prefresh occurs as a percentage of the TTL. For example, for an object whose cache has 10 minutes left to live, and an origin response that is routinely less than 30 seconds, a percentage of `95` prefreshes the content without unnecessarily increasing load on the origin.

</div>

</div>

<div class="feature" data-feature="quicBeta" markdown="1">
