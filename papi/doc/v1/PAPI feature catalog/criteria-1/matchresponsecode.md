---
title: "matchResponseCode"
slug: "matchresponsecode"
hidden: false
createdAt: "2020-06-15T22:21:49.976Z"
updatedAt: "2020-06-15T22:21:49.976Z"
---
__Property Manager name__: [Response Status Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match a set or range of HTTP response codes.

__Options__:

- `matchOperator` (_enum string_): Matches the contents of `values` if set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match. If set to `IS_BETWEEN`, matches the numeric range between `lowerBound` and `upperBound`, otherwise `IS_NOT_BETWEEN` reverses the match.

- `values` (_array of string values_): A set of response codes to match, for example `["404","500"]`.

- `lowerBound` (_number_): Specifies the start of a range of responses when `matchOperator` is either `IS_BETWEEN` or `IS_NOT_BETWEEN`. For example, `400` to match anything from `400` to `500`.

- `upperBound` (_number_): Specifies the end of a range of responses when `matchOperator` is either `IS_BETWEEN` or `IS_NOT_BETWEEN`. For example, `500` to match anything from `400` to `500`.
