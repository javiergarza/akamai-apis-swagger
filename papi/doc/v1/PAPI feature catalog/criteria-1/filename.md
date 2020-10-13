---
title: "filename"
slug: "filename"
hidden: false
createdAt: "2020-06-15T22:20:24.883Z"
updatedAt: "2020-06-15T22:20:24.883Z"
---
__Property Manager name__: [Filename](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested filename, or test whether it is present.

__Options__:

- `matchOperator` (_enum string_): If set to `IS_ONE_OF` or `IS_NOT_ONE_OF`, matches whether the `value` matches. If set to `IS_EMPTY` or `IS_NOT_EMPTY`, matches whether the specified filename is part of the path.

- `values` (_array of string values_): Matches the filename component of the request URL. Wildcards are allowed, where `?` matches a single character and `*` matches more than one. For example, specify `filename.*` to accept any extension.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive for the `value` field.
