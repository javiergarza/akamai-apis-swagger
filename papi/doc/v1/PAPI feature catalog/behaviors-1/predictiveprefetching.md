---
title: "predictivePrefetching"
slug: "predictiveprefetching"
hidden: false
createdAt: "2020-06-15T21:45:59.971Z"
updatedAt: "2020-06-15T21:45:59.971Z"
---
__Property Manager name__: [Predictive Prefetching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0063)

This behavior potentially reduces the client's page load time by pre-caching objects based on historical data for the page, not just its current set of referenced objects. It also detects second-level dependencies, such as objects retrieved by JavaScript.

__Options__:

<div class="option" markdown="1" id="predictivePrefetching.enabled" >

- `enabled` (_boolean_): Enables the predictive prefetching behavior.

</div>

<div class="option" markdown="1" id="predictivePrefetching.accuracyTarget" >

- `accuracyTarget` (_enum string_): The level of prefetching, either `LOW`, `MEDIUM`, or `HIGH`. A higher level results in better client performance, but potentially greater load on the origin.

</div>

</div>

<div class="feature" data-feature="prefetch" markdown="1">
