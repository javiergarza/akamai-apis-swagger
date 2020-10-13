---
title: "requestControl"
slug: "requestcontrol"
hidden: false
createdAt: "2020-06-15T21:53:10.707Z"
updatedAt: "2020-06-15T21:53:10.707Z"
---
__Property Manager name__: [Request Control Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0073)

The Request Control Cloudlet allows you to control access to your web content based on the incoming request's IP or geographic location.  With cloudlets available on your contract, choose __Your services__ &rArr; __Edge logic Cloudlets__ to control how the feature works within [Control Center](https://control.akamai.com), or use the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to configure it programmatically.

__Options__:

<div class="option" markdown="1" id="requestControl.enabled" >

- `enabled` (_boolean_): Enables the Request Control Cloudlet.

</div>

<div class="option" markdown="1" id="requestControl.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="requestControl.enableBranded403" >

- `enableBranded403` (_boolean_): If enabled, serves a branded 403 page for this Cloudlet instance.

</div>

<div class="option" markdown="1" id="requestControl.branded403StatusCode" >

- `branded403StatusCode` (_numeric enum_): Specifies the response status code for the branded deny action, either `200`, `302`, `403`, or `503`.

</div>

<div class="option" markdown="1" id="requestControl.netStorage" >

- `netStorage` (_object_): Specifies the NetStorage domain that contains the branded 403 page.

</div>

<div class="option" markdown="1" id="requestControl.branded403File" >

- `branded403File` (_string_): Specifies the full path of the branded 403 page, including the filename, but excluding the NetStorage CP code path component.

</div>

<div class="option" markdown="1" id="requestControl.branded403Url" >

- `branded403Url` (_string_): Specifies the redirect URL for the branded deny action.

</div>

<div class="option" markdown="1" id="requestControl.brandedDenyCacheTtl" >

- `brandedDenyCacheTtl` (_number within 5-30 range_): Specifies the branded response page's time to live in the cache, `5` minutes by default.

</div>

</div>

<div class="feature" data-feature="requestTypeMarker" markdown="1">
