---
title: "refererChecking"
slug: "refererchecking"
hidden: false
createdAt: "2020-06-15T21:50:18.965Z"
updatedAt: "2020-06-15T21:50:18.965Z"
---
__Property Manager name__: [Legacy Referrer Checking](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0070)

Limits allowed requests to a set of domains you specify.

__Options__:

<div class="option" markdown="1" id="refererChecking.enabled" >

- `enabled` (_boolean_): Enables the referer-checking behavior.

</div>

<div class="option" markdown="1" id="refererChecking.strict" >

- `strict` (_boolean_): When enabled, excludes requests whose `Referer` header include a relative path, or that are missing a `Referer`. When disabled, only excludes requests whose `Referer` hostname is not part of the `domains` set.

</div>

<div class="option" markdown="1" id="refererChecking.domains" >

- `domains` (_array of string values_): Specifies the set of allowed domains. With `allowChildren` disabled, prefixing values with `*.` specifies domains for which subdomains are allowed.

</div>

<div class="option" markdown="1" id="refererChecking.allowChildren" >

- `allowChildren` (_boolean_): When enabled, allows all subdomains for the `domains` set, just like adding a `*.` prefix to each.

</div>

</div>

<div class="feature" data-feature="removeQueryParameter" markdown="1">
