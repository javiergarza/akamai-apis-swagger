---
title: "allowDelete"
slug: "allowdelete"
hidden: false
createdAt: "2020-06-15T20:34:34.643Z"
updatedAt: "2020-06-15T20:34:34.643Z"
---
__Property Manager name__: [Allow DELETE](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0011)

Allow HTTP requests using the DELETE method. By default, only GET and HEAD requests are allowed, and all other methods result in a 403 error. Such content does not cache, and any DELETE requests pass to the origin. See also the [`allowOptions`](#allowoptions), [`allowPatch`](#allowpatch), [`allowPost`](#allowpost), and [`allowPut`](#allowput) behaviors.

__Options__:

<div class="option" markdown="1" id="allowDelete.enabled" >

- `enabled` (_boolean_): When enabled, allows DELETE requests. Content does _not_ cache.

</div>

<div class="option" markdown="1" id="allowDelete.allowBody" >

- `allowBody` (_boolean_): When enabled, allows data in the body of the DELETE request.

</div>
