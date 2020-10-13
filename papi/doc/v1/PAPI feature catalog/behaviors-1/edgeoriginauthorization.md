---
title: "edgeOriginAuthorization"
slug: "edgeoriginauthorization"
hidden: false
createdAt: "2020-06-15T21:20:43.767Z"
updatedAt: "2020-06-15T21:20:43.767Z"
---
__Property Manager name__: [Edge Server Identification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0041)

Allows the origin server to use a cookie to ensure requests from Akamai servers are genuine.

This behavior requires that you specify the cookie's domain name, so it is best to deploy within a match of the hostname.  It does not work properly when the origin server accepts more than one hostname (for example, using virtual servers) that do not share the same top-level domain.

__Options__:

<div class="option" markdown="1" id="edgeOriginAuthorization.enabled" >

- `enabled` (_boolean_): Enables the cookie-authorization behavior.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.cookieName" >

- `cookieName` (_string_): Specifies the name of the cookie to use for authorization.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.value" >

- `value` (_string_): Specifies the value of the authorization cookie.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.domain" >

- `domain` (_string_): Specify the cookie's domain, which must match the top-level domain of the `Host` header the origin server receives.

</div>

</div>

<div class="feature" data-feature="edgeRedirector" markdown="1">
