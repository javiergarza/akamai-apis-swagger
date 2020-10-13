---
title: "siteShield"
slug: "siteshield"
hidden: false
createdAt: "2020-06-15T22:03:10.704Z"
updatedAt: "2020-06-15T22:03:10.704Z"
---
__Property Manager name__: [SiteShield](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9063)

A [read-only behavior](#ro) implementing the [Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html) feature, which helps prevent non-Akamai machines from contacting your origin. Your service representative periodically sends you a list of Akamai servers allowed to contact your origin, with which you establish an Access Control List on your firewall to prevent any other requests.

__Options__:

<div class="option" markdown="1" id="siteShield.ssmap" >

- `ssmap` (_object_): Identifies the hostname for the Site Shield map, available from your Akamai representative. Form an object with a `value` key that references the hostname, for example: `"ssmap":{"value":"ss.akamai.net"}`.

</div>

</div>

<div class="feature" data-feature="spdy" markdown="1">
