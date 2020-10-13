---
title: "firstPartyMarketingPlus"
slug: "firstpartymarketingplus"
hidden: false
createdAt: "2020-06-15T21:24:42.435Z"
updatedAt: "2020-06-15T21:24:42.435Z"
---
__Property Manager name__: [Cloud Marketing Plus Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0046)

Enables the [Cloud Marketing Plus Cloudlet](https://learn.akamai.com/pdf/CloudMarketing-CS.pdf), which helps MediaMath customers collect usage data and place corresponding tags for use in online advertising.  You can configure tags using either the Cloudlets Policy Manager application or the [Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html). See also the [`firstPartyMarketing`](#firstpartymarketing) behavior, which integrates with MediaMath but not its partners. Both behaviors support the same set of options.

__Options__:

<div class="option" markdown="1" id="firstPartyMarketingPlus.enabled" >

- `enabled` (_boolean_): Enables the Cloud Marketing Plus Cloudlet.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.javaScriptInsertionRule" >

- `javaScriptInsertionRule` (_enum string_): Select how to insert the MediaMath JavaScript reference script, either `NEVER` if inserting it at the origin, `ALWAYS` to insert it for all edge requests, or `POLICY` to allow the Cloudlet policy to determine when to insert it.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.cloudletPolicy" >

- `cloudletPolicy` (_object_): Identifies the Cloudlet policy in an object featuring unique numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.mediaMathPrefix" >

- `mediaMathPrefix` (_string_): Specify the URL path prefix that distinguishes Cloud Marketing requests from your other web traffic. Include the leading slash character, but no trailing slash.  For example, if the path prefix is `/mmath`, and the request is for `www.example.com/dir`, the new URL is `www.example.com/mmath/dir`.

</div>

</div>

<div class="feature" data-feature="forwardRewrite" markdown="1">
