---
title: "baseDirectory"
slug: "basedirectory"
hidden: false
createdAt: "2020-06-15T20:44:21.730Z"
updatedAt: "2020-06-15T20:44:21.730Z"
---
__Property Manager name__: [Origin Base Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0203)

Prefix URLs sent to the origin with a base path.

For example, with an origin of `example.com`, setting the `value` to `/images` sets the origin's base path to `example.com/images`. Any request for a `my_pics/home.jpg` file resolves on the origin server to `example.com/images/my_pics/home.jpg`.

Note that changing the origin's base path also causes a change to the cache key. Until that resolves, it may cause a traffic spike to your origin server.

__Options__:

<div class="option" markdown="1" id="baseDirectory.value" >

- `value` (_string; allows [variables](#vf)_): Specifies the base path of content on your origin server. The value must begin and end with a slash (`/`) character, for example `/parent/child/`.

</div>

</div>

<div class="feature" data-feature="bossBeaconing" markdown="1">
