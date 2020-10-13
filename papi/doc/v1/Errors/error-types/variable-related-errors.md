---
title: "Variable-related errors"
slug: "variable-related-errors"
hidden: false
createdAt: "2020-06-05T21:20:49.156Z"
updatedAt: "2020-06-10T02:53:21.070Z"
---
These errors may be listed within [Rule](#rule) objects, and may prevent you from activating the property version:

| Type | Description |
| :--- | :--- |
| `cannot_validate` | The option can't be validated because the value of its embedded variable can only be known at runtime. |
| `duplicate_variable` | There's more than one declared variable with the same name. |
| `empty_variable_name` | The name of the variable can't be empty. |
| `internal_variable_in_xml` | An advanced behavior specifies a variable that uses a reserved prefix. |
| `no_variable_support` | Your contract doesn't support use of variables. |
| `syntax_error_in_variable_expression.illegal_expression` | There's a format error in a variable expression. |
| `syntax_error_in_variable_expression.illegal_prefix` | There's an illegal prefix in a variable expression. |
| `syntax_error_in_variable_expression.missing_end_token` | There's a missing end token in a variable expression. |
| `unknown_variable_name` | An undeclared variable name was invoked. |