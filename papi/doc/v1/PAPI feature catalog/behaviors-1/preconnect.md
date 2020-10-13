---
title: "preconnect"
slug: "preconnect"
hidden: false
createdAt: "2020-06-15T21:45:35.452Z"
updatedAt: "2020-06-15T21:45:35.452Z"
---
__Property Manager name__: [Manual Preconnect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9029)

With the [`http2`](#http2) behavior enabled, this requests a specified set of domains that relate to your property hostname, and keeps the connection open for faster loading of content from those domains.

__Options__:

<div class="option" markdown="1" id="preconnect.preconnectlist" >

- `preconnectlist` (_array of string values_): Specifies the set of hostnames to which to preconnect over HTTP2.

</div>

</div>

<div class="feature" data-feature="predictivePrefetching" markdown="1">
