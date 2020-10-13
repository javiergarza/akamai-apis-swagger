---
title: "requestHeader"
slug: "requestheader"
hidden: false
createdAt: "2020-06-15T22:25:55.441Z"
updatedAt: "2020-06-15T22:25:55.441Z"
---
__Property Manager name__: [Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match HTTP header names or values.

__Options__:

- `headerName` (_string_): The name of the request header, for example `Accept-Language`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the field       `headerName` exists.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's `value`     string matches.

- `values` (_array of string values_): The request header's value, for example `en-US` when the header `headerName` is `Accept-Language`.

- `matchWildcardName` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `headerName` field.

- `matchWildcardValue` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `value` field.

- `matchCaseSensitiveValue` (_boolean_): When enabled, the match is case-sensitive for the `value` field.
