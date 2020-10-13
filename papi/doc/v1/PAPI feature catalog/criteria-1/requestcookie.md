---
title: "requestCookie"
slug: "requestcookie"
hidden: false
createdAt: "2020-06-15T22:25:32.734Z"
updatedAt: "2020-06-15T22:25:32.734Z"
---
__Property Manager name__: [Request Cookie](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match the cookie name or value passed with the request.

__Options__:

- `cookieName` (_string_): The name of the cookie, for example, `visitor` in `visitor:anon`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the cookie `cookieName`     exists.
    - `IS` or `IS_NOT` tests whether the field's `value` string     matches.
    - `IS_BETWEEN` tests whether a numeric cookie `value` falls between     `lowerBound` and `upperBound`.

- `value` (_string_): The cookie's value, for example, `anon` in `visitor:anon`.

- `lowerBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's minimum value.

- `upperBound` (_number_): When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`, this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `cookieName` field.

- `matchCaseSensitiveName` (_boolean_): When enabled, the match is case-sensitive for the `cookieName` field.

- `matchWildcardValue` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `value` field.

- `matchCaseSensitiveValue` (_boolean_): When enabled, the match is case-sensitive for the `value` field.
