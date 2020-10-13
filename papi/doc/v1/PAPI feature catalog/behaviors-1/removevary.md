---
title: "removeVary"
slug: "removevary"
hidden: false
createdAt: "2020-06-15T21:51:22.077Z"
updatedAt: "2020-06-15T21:51:22.077Z"
---
__Property Manager name__: [Remove Vary Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0071)

By default, responses that feature a `Vary` header value of anything other than `Accept-Encoding` and a corresponding `Content-Encoding: gzip` header aren't cached on edge servers. `Vary` headers indicate when a URL's content varies depending on some variable, such as which `User-Agent` requests it. This behavior simply removes the `Vary` header to make responses cacheable.

> __WARNING__: If your site relies on `Vary: User-Agent` to customize
content, removing the header may lead the edge to serve content
inappropriate for specific devices.

__Options__:

<div class="option" markdown="1" id="removeVary.enabled" >

- `enabled` (_boolean_): When enabled, removes the `Vary` header to ensure objects can be cached.

</div>

</div>

<div class="feature" data-feature="report" markdown="1">
