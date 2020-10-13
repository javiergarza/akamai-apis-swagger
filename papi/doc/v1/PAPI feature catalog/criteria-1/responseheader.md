---
title: "responseHeader"
slug: "responseheader"
hidden: false
createdAt: "2020-06-15T22:27:34.809Z"
updatedAt: "2020-06-15T22:27:34.809Z"
---
__Property Manager name__: [Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match HTTP header names or values.

__Options__:

- `headerName` (_string_): The name of the response header, for example `Content-Type`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the HTTP field     `headerName` is present.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's `value`     string matches.
    - `IS_LESS_THAN` or `IS_MORE_THAN` matches ranges when the `value`     is numeric.
    - `IS_BETWEEN` also matches numeric ranges, but considers     `lowerBound` and `upperBound` fields rather than `value`.

- `values` (_array of string values_): The response header's value, for example `application/x-www-form-urlencoded` when the header `headerName` is `Content-Type`.

- `lowerBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's minimum value.

- `upperBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `headerName` field.

- `matchWildcardValue` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `value` field.

- `matchCaseSensitiveValue` (_boolean_): When enabled, the match is case-sensitive for the `value` field.
