---
title: "cacheRedirect"
slug: "cacheredirect"
hidden: false
createdAt: "2020-06-15T20:52:12.822Z"
updatedAt: "2020-06-15T20:52:12.822Z"
---
__Property Manager name__: [Cache HTTP Redirects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0023)

Caches HTTP 302 redirect responses. By default, Akamai edge servers cache HTTP 302 redirects depending on their `Cache-Control` or `Expires` headers. Enabling this behavior instructs edge servers to cache 302 redirects the same as they would for HTTP 200 responses.

__Options__:

<div class="option" markdown="1" id="cacheRedirect.enabled" >

- `enabled` (_boolean_): Enables the redirect caching behavior.

</div>

</div>

<div class="feature" data-feature="cacheTagVisible" markdown="1">
