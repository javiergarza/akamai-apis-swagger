---
title: "allowPut"
slug: "allowput"
hidden: false
createdAt: "2020-06-15T20:38:45.379Z"
updatedAt: "2020-06-15T20:38:45.379Z"
---
__Property Manager name__: [Allow PUT](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0013)

Allow HTTP requests using the PUT method.  By default, only GET and HEAD are allowed, and all other methods result in a 403 error. Such content does not cache, and any PUT requests pass to the origin. See also the [`allowDelete`](#allowdelete), [`allowOptions`](#allowoptions), [`allowPatch`](#allowpatch), and [`allowPost`](#allowpost) behaviors.

__Options__:

<div class="option" markdown="1" id="allowPut.enabled" >

- `enabled` (_boolean_): When enabled, allows PUT requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowTransferEncoding" markdown="1">
