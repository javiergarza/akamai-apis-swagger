---
title: "allowOptions"
slug: "allowoptions"
hidden: false
createdAt: "2020-06-15T20:36:48.374Z"
updatedAt: "2020-06-15T20:36:48.374Z"
---
__Property Manager name__: [Allow OPTIONS](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0013)

Allow HTTP requests using the OPTIONS method. By default, only GET and HEAD requests are allowed, and all other methods result in a 403 error. Such content does not cache, and any OPTIONS requests pass to the origin. See also the [`allowDelete`](#allowdelete), [`allowPatch`](#allowpatch), [`allowPost`](#allowpost), and [`allowPut`](#allowput) behaviors.

__Options__:

<div class="option" markdown="1" id="allowOptions.enabled" >

- `enabled` (_boolean_): When enabled, allows OPTIONS requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowPatch" markdown="1">
