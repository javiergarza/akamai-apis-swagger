---
title: "forwardRewrite"
slug: "forwardrewrite"
hidden: false
createdAt: "2020-06-15T21:25:07.053Z"
updatedAt: "2020-06-15T21:25:07.053Z"
---
__Property Manager name__: [Forward Rewrite Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0047)

The Forward Rewrite Cloudlet allows you to conditionally modify the forward path in edge content without affecting the URL that displays in the user's address bar. If cloudlets are available on your contract, choose __Your services__ &rArr; __Edge logic Cloudlets__ to control how this feature works within [Control Center](https://control.akamai.com), or use the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to configure it programmatically.

__Options__:

<div class="option" markdown="1" id="forwardRewrite.enabled" >

- `enabled` (_boolean_): Enables the Forward Rewrite Cloudlet behavior.

</div>

<div class="option" markdown="1" id="forwardRewrite.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

</div>

<div class="feature" data-feature="frontEndOptimization" markdown="1">
