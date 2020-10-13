---
title: "dynamicWebContent"
slug: "dynamicwebcontent"
hidden: false
createdAt: "2020-06-15T21:17:14.371Z"
updatedAt: "2020-06-15T21:17:14.371Z"
---
__Property Manager name__: [Content Characteristics - Dynamic Web Content](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5008)

In conjunction with the [`subCustomer`](#subcustomer) behavior, this optional behavior allows you to control how dynamic web content behaves for your subcustomers using [Akamai Cloud Embed](https://learn.akamai.com/en-us/products/media_delivery/cloud_embed.html).

__Options__:

<div class="option" markdown="1" id="dynamicWebContent.sureRoute" >

- `sureRoute` (_boolean_): Optimizes how subcustomer traffic routes from origin to edge servers.  See the [`sureRoute`](#sureroute) behavior for more information.

</div>

<div class="option" markdown="1" id="dynamicWebContent.prefetch" >

- `prefetch` (_boolean_): Allows subcustomer content to prefetch over HTTP/2.

</div>

<div class="option" markdown="1" id="dynamicWebContent.realUserMonitoring" >

- `realUserMonitoring` (_boolean_): Allows Real User Monitoring (RUM) to collect performance data for subcustomer content. See the [`realUserMonitoring`](#realusermonitoring) behavior for more information.

</div>

<div class="option" markdown="1" id="dynamicWebContent.imageCompression" >

- `imageCompression` (_boolean_): Enables image compression for subcustomer content.

</div>

</div>

<div class="feature" data-feature="edgeConnect" markdown="1">
