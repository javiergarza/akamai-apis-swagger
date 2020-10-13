---
title: "networkConditionsHeader"
slug: "networkconditionsheader"
hidden: false
createdAt: "2020-06-15T21:41:30.896Z"
updatedAt: "2020-06-15T21:41:30.896Z"
---
__Property Manager name__: [Network Conditions Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9051)

Instructs edge servers to send an `X-Akamai-Network-Condition` header to the origin assessing the quality of the network.

__Options__:

<div class="option" markdown="1" id="networkConditionsHeader.behavior" >

- `behavior` (_enum string_): If set to `TWO_TIER`, assessment is either `Excellent` or `Poor`. If set to `THREE_TIER`, the assessment can also be `Fair`.

</div>

</div>

<div class="feature" data-feature="origin" markdown="1">
