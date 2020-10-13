---
title: "hostname"
slug: "hostname"
hidden: false
createdAt: "2020-06-15T22:20:46.518Z"
updatedAt: "2020-06-15T22:20:46.518Z"
---
__Property Manager name__: [Hostname](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested hostname.

__Options__:

- `matchOperator` (_enum string_): Matches the contents of `values` when set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_): A list of hostnames. Wildcards match, so `*.example.com` matches both `m.example.com` and `www.example.com`.
