---
title: "allowPatch"
slug: "allowpatch"
hidden: false
createdAt: "2020-06-15T20:37:22.250Z"
updatedAt: "2020-06-15T20:37:22.250Z"
---
__Property Manager name__: [Allow PATCH](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9016)

Allow HTTP requests using the PATCH method. By default, only GET and HEAD requests are allowed, and all other methods result in a 403 error. Such content does not cache, and any PATCH requests pass to the origin. See also the [`allowDelete`](#allowdelete), [`allowOptions`](#allowoptions), [`allowPost`](#allowpost), and [`allowPut`](#allowput) behaviors.

__Options__:

<div class="option" markdown="1" id="allowPatch.enabled" >

- `enabled` (_boolean_): When enabled, allows PATCH requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowPost" markdown="1">
