---
title: "tieredDistribution"
slug: "tiereddistribution"
hidden: false
createdAt: "2020-06-15T22:06:45.527Z"
updatedAt: "2020-06-15T22:06:45.527Z"
---
__Property Manager name__: [Tiered Distribution](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0083)

This behavior allows Akamai edge servers to retrieve cached content from other Akamai servers, rather than directly from the origin. These interim _parent_ servers in the _cache hierarchy_ (`CH`) are positioned close to the origin, and fall along the path from the origin to the edge server. Tiered Distribution typically reduces the origin server's load, and reduces the time it takes for edge servers to refresh content.

See also the [`tieredDistributionAdvanced`](#tiereddistributionadvanced) behavior.

__Options__:

<div class="option" markdown="1" id="tieredDistribution.enabled" >

- `enabled` (_boolean_): When enabled, activates tiered distribution.

</div>

<div class="option" markdown="1" id="tieredDistribution.tieredDistributionMap" >

- `tieredDistributionMap` (_enum string_): Optionally map the tiered parent server's location close to your origin: `CHEU2` for Europe; `CHAUS` for Australia; `CHAPAC` for China and the Asian Pacific area; `CHWUS2`, `CHCUS2`, and `CHEUS2` for different parts of the United States. Choose `CH` or `CH2` for a more global map. A narrower local map minimizes the origin server's load, and increases the likelihood the requested object is cached. A wider global map reduces end-user latency, but decreases the likelihood the requested object is in any given parent server's cache.  This option cannot apply if the property is marked as secure. See [Secure property requirements](#sf) for guidance.

</div>

</div>

<div class="feature" data-feature="tieredDistributionCustomization" markdown="1">
