---
title: "userAgent"
slug: "useragent"
hidden: false
createdAt: "2020-06-15T22:29:03.146Z"
updatedAt: "2020-06-15T22:29:03.146Z"
---
__Property Manager name__: [User Agent](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the user agent string that helps identify the client browser and device.

__Options__:

- `matchOperator` (_enum string_): Matches the specified set of `values` when set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_): The `User-Agent` header's value. For example, `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`.

- `matchWildcard` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `value` field. For example, `*Android*`, `*iPhone5*`, `*Firefox*`, or `*Chrome*`.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive for the `value` field.
