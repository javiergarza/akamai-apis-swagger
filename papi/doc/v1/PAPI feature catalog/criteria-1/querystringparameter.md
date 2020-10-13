---
title: "queryStringParameter"
slug: "querystringparameter"
hidden: false
createdAt: "2020-06-15T22:24:28.637Z"
updatedAt: "2020-06-15T22:24:28.637Z"
---
__Property Manager name__: [Query String Parameter](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches query string field names or values.

__Options__:

- `parameterName` (_string_): The name of the query field, for example, `q` in `?q=string`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the query field's     `parameterName` is present in the requesting URL.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's     `value` string matches.
    - `IS_LESS_THAN` or `IS_MORE_THAN` matches ranges when the     `value` is numeric.
    - `IS_BETWEEN` also matches numeric ranges, but considers     `lowerBound` and `upperBound` fields rather than `value`.

- `values` (_array of string values_): The value of the query field, for example, `string` in `?q=string`.

- `lowerBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's minimum value.

- `upperBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `parameterName` field.

- `matchCaseSensitiveName` (_boolean_): When enabled, the match is case-sensitive for the `parameterName` field.

- `matchWildcardValue` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `value` field.

- `matchCaseSensitiveValue` (_boolean_): When enabled, the match is case-sensitive for the `value` field.

- `escapeValue` (_boolean_): When enabled, matches when the `value` is URL-escaped.
