---
title: "edgeRedirector"
slug: "edgeredirector"
hidden: false
createdAt: "2020-06-15T21:21:10.334Z"
updatedAt: "2020-06-15T21:21:10.334Z"
---
__Property Manager name__: [Edge Redirector Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0042)

This behavior enables the [Edge Redirector Cloudlet](http://www.akamai.com/html/technology/edge-redirector.html) application, which is designed to help you manage large numbers of redirects. With cloudlets available on your contract, choose __Your services__ &rArr; __Edge logic Cloudlets__ to control the Edge Redirector within [Control Center](https://control.akamai.com). Otherwise use the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to configure it programmatically.

__Options__:

<div class="option" markdown="1" id="edgeRedirector.enabled" >

- `enabled` (_boolean_): Enables the Edge Redirector Cloudlet.

</div>

<div class="option" markdown="1" id="edgeRedirector.cloudletPolicy" >

- `cloudletPolicy` (_object_): Specifies the Cloudlet policy as an object containing two members: a descriptive `name` string and an integer `id` set by the Cloudlet application.

</div>

</div>

<div class="feature" data-feature="edgeScape" markdown="1">
