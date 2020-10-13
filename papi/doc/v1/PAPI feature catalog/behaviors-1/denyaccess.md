---
title: "denyAccess"
slug: "denyaccess"
hidden: false
createdAt: "2020-06-15T21:11:02.747Z"
updatedAt: "2020-06-15T21:11:02.747Z"
---
__Property Manager name__: [Control Access](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0032)

Assuming a condition in the rule matches, this denies access to the requested content. For example, a [`userLocation`](#userlocation) match paired with the `denyaccess` behavior would deny requests from a specified part of the world.

By keying on the value of the `reason` option, `denyaccess` behaviors may override each other when called from nested rules. For example, a parent rule might deny access to a certain geographic area, citing `"location"` as the `reason`, but another nested rule can then allow access for a set of IPs within that area, so long as the `reason` matches.

__Options__:

<div class="option" markdown="1" id="denyAccess.enabled" >

- `enabled` (_boolean_): Denies access when enabled.

</div>

<div class="option" markdown="1" id="denyAccess.reason" >

- `reason` (_string_): Text message that keys why access is denied. Any subsequent `denyaccess` behaviors within the rule tree may refer to the same `reason` key to override the current behavior.

</div>

</div>

<div class="feature" data-feature="denyDirectFailoverAccess" markdown="1">
