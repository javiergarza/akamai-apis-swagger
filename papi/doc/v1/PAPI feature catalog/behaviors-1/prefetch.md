---
title: "prefetch"
slug: "prefetch"
hidden: false
createdAt: "2020-06-15T21:46:22.515Z"
updatedAt: "2020-06-15T21:46:22.515Z"
---
__Property Manager name__: [Prefetch Objects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0064)

Instructs edge servers to retrieve content linked from requested pages as they load, rather than waiting for separate requests for the linked content. This behavior applies depending on the rule's set of matching conditions. Use in conjunction with the [`prefetchable`](#prefetchable) behavior, which specifies the set of objects to prefetch.

__Options__:

<div class="option" markdown="1" id="prefetch.enabled" >

- `enabled` (_boolean_): Applies prefetching behavior when enabled.

</div>

</div>

<div class="feature" data-feature="prefetchable" markdown="1">
