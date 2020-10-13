---
title: "validateEntityTag"
slug: "validateentitytag"
hidden: false
createdAt: "2020-06-15T22:08:15.276Z"
updatedAt: "2020-06-15T22:08:15.276Z"
---
__Property Manager name__: [Validate Entity Tag](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9034)

Instructs edge servers to compare the request's ETag header with that of the cached object. If they differ, the edge server sends a new copy of the object. This validation occurs in addition to the default validation of `Last-Modified` and `If-Modified-Since` headers.

__Options__:

<div class="option" markdown="1" id="validateEntityTag.enabled" >

- `enabled` (_boolean_): Enables the ETag validation behavior.

</div>

</div>

<div class="feature" data-feature="verifyJsonWebToken" markdown="1">
