---
title: "manualServerPush"
slug: "manualserverpush"
hidden: false
createdAt: "2020-06-15T21:35:09.645Z"
updatedAt: "2020-06-15T21:35:09.645Z"
---
__Property Manager name__: [Manual Server Push](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9065)

With the [`http2`](#http2) behavior enabled, this loads a specified set of objects into the client browser's cache. To apply this behavior, you should match on a [`path`](#path) or [`filename`](#filename).

__Options__:

<div class="option" markdown="1" id="manualServerPush.serverpushlist" >

- `serverpushlist` (_array of string values_): Specifies the set of objects to load into the client browser's cache over HTTP2. Each value in the array represents a hostname and full path to the object, such as `www.example.com/js/site.js`

</div>

</div>

<div class="feature" data-feature="mediaAcceleration" markdown="1">
