---
title: "chaseRedirects"
slug: "chaseredirects"
hidden: false
createdAt: "2020-06-15T20:55:18.584Z"
updatedAt: "2020-06-15T20:55:18.584Z"
---
__Property Manager name__: [Chase Redirects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9037)

Controls whether the edge server chases any redirects served from the origin.

__Options__:

<div class="option" markdown="1" id="chaseRedirects.enabled" >

- `enabled` (_boolean_): When enabled, allows edge servers to chase redirects.

</div>

<div class="option" markdown="1" id="chaseRedirects.limit" >

- `limit` (_string_): Specifies, as a string, the maximum number of redirects to follow.

</div>

<div class="option" markdown="1" id="chaseRedirects.serve404" >

- `serve404` (_boolean_): Once the redirect `limit` is reached, enabling this option serves an HTTP `404` (Not Found) error instead of the last redirect.

</div>

</div>

<div class="feature" data-feature="clientCharacteristics" markdown="1">
