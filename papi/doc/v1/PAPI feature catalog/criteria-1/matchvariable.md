---
title: "matchVariable"
slug: "matchvariable"
hidden: false
createdAt: "2020-06-15T22:22:11.458Z"
updatedAt: "2020-06-15T22:22:11.458Z"
---
__Property Manager name__: [Variable](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0056)

Matches a built-in variable, or a custom variable pre-declared within the rule tree by the [`setVariable`](#setvariable) behavior.  See [Support for variables](#vf) for more information on this feature.

__Options__:

- `variableName` (_string_): The name of the variable to match.

- `matchOperator` (_enum string_): The type of match, based on which you use different options to specify the match criteria.

    - If set to `IS` or `IS_NOT`, specify a single `variableExpression`       string.
    - If set to `IS_GREATER_THAN`, `IS_LESS_THAN`,       `IS_GREATER_THAN_OR_EQUAL_TO`, or `IS_LESS_THAN_OR_EQUAL_TO`,       specify a single `variableExpression` string.
    - If set to `IS_BETWEEN` or `IS_NOT_BETWEEN`, specify a range       between numeric `lowerBound` and `upperBound` values.
    - If set to `IS_ONE_OF` or `IS_NOT_ONE_OF`, specify an array of       string `variableValues`.
    - If set to `IS_EMPTY` or `IS_NOT_EMPTY`, no other option is       required. These check if a defined variable contains a value.       You can't activate a rule that matches an undefined variable.

- `variableValues` (_array of string values_): With `matchOperator` set to either `IS_ONE_OF` or `IS_NOT_ONE_OF`, specifies an array of matching strings.

- `variableExpression` (_string; allows [variables](#vf)_): With `matchOperator` set to either `IS` or `IS_NOT`, specifies a single matching string.

- `lowerBound` (_string_): With `matchOperator` set to either `IS_BETWEEN` or `IS_NOT_BETWEEN`, specifies the range's numeric minimum value.

- `upperBound` (_string_): With `matchOperator` set to either `IS_BETWEEN` or `IS_NOT_BETWEEN`, specifies the range's numeric maximum value.

- `matchWildcard` (_boolean_): When matching string expressions, enabling this matches wildcard metacharacters such as `*` and `?`.

- `matchCaseSensitive` (_boolean_): When matching string expressions, enabling this performs a case-sensitive match.
