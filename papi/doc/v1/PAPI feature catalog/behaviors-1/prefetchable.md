---
title: "prefetchable"
slug: "prefetchable"
hidden: false
createdAt: "2020-06-15T21:46:41.781Z"
updatedAt: "2020-06-15T21:46:41.781Z"
---
__Property Manager name__: [Prefetchable Objects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0064)

Allow matching objects to prefetch into the edge cache as the parent page that links to them loads, rather than waiting for a direct request. This behavior applies depending on the rule's set of matching conditions. Use [`prefetch`](#prefetch) to enable the overall behavior for parent pages that contain links to the object. To apply this behavior, you need to match on a [`filename`](#filename) or [`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="prefetchable.enabled" >

- `enabled` (_boolean_): When enabled, allows matching content to prefetch when referenced on a requested parent page.

</div>

</div>

<div class="feature" data-feature="prefreshCache" markdown="1">
