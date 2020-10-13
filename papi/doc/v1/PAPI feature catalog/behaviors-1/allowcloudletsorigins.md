---
title: "allowCloudletsOrigins"
slug: "allowcloudletsorigins"
hidden: false
createdAt: "2020-06-15T20:33:48.442Z"
updatedAt: "2020-06-15T20:33:48.442Z"
---
__Property Manager name__: [Allow Conditional Origins](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0014)

Allows Cloudlets Origins to determine the criteria, separately from the Property Manager, under which alternate [`origin`](#origin) definitions are assigned.

This behavior must appear alone within its own rule. When enabled, it allows any [`cloudletsOrigin`](#cloudletsorigin) criteria within sub-rules to override the prevailing origin.

__Options__:

<div class="option" markdown="1" id="allowCloudletsOrigins.enabled" >

- `enabled` (_boolean_): Allows you to assign custom origin definitions referenced in sub-rules by [`cloudletsOrigin`](#cloudletsorigin) labels. If disabled, all sub-rules are ignored.

</div>

<div class="option" markdown="1" id="allowCloudletsOrigins.honorBaseDirectory" >

- `honorBaseDirectory` (_boolean_): If enabled, prefixes any Cloudlet-generated origin path with a path defined by an Origin Base Path behavior. If no path is defined, it has no effect. If another Cloudlet policy already prepends the same Origin Base Path, the path is not duplicated.

</div>

<div class="option" markdown="1" id="allowCloudletsOrigins.purgeOriginQueryParameter" >

- `purgeOriginQueryParameter` (_string_): When purging content from a Cloudlets Origin, this specifies a query parameter name whose value is the specific named origin to purge.  Note that this only applies to content purge requests, for example when using the [Content Control Utility API](https://learn.akamai.com/en-us/api/web_performance/content_control_utility/v2.html).

</div>
