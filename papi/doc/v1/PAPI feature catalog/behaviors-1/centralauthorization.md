---
title: "centralAuthorization"
slug: "centralauthorization"
hidden: false
createdAt: "2020-06-15T20:54:48.482Z"
updatedAt: "2020-06-15T20:54:48.482Z"
---
__Property Manager name__: [Centralized Authorization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0025)

Forward client requests to the origin server for authorization, along with optional `Set-Cookie` headers, useful when you need to maintain tight access control. The edge server forwards an `If-Modified-Since` header, to which the origin needs to respond with a `304` (Not-Modified) HTTP status when authorization succeeds. If so, the edge server responds to the client with the cached object, since it does not need to be re-acquired from the origin.

__Options__:

<div class="option" markdown="1" id="centralAuthorization.enabled" >

- `enabled` (_boolean_): Enables the centralized authorization behavior.

</div>

</div>

<div class="feature" data-feature="chaseRedirects" markdown="1">
