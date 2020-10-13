---
title: "Option value errors"
slug: "option-value-errors"
hidden: false
createdAt: "2020-06-05T21:20:09.499Z"
updatedAt: "2020-06-10T02:53:21.077Z"
---
These errors may be listed within [Rule](#rule) objects, and may prevent you from activating the property version:

| Type | Description |
| :--- | :--- |
| `generic_behavior_issue.table_option_dup_row` | The option specifies duplicated items. |
| `illegal_option_value_format.features` | A behavior option's data type is invalid. |
| `illegal_option_value_format.matches` | A criteria option's data type is invalid. |
| `insecure_string_value` | Option values may not specify `%(` text. |
| `non_ascii` | The option specifies non-ASCII characters. |
| `option_empty` | The option may not specify an empty value. |
| `option_required.features` | The behavior is missing a required option. |
| `option_required.matches` | The criteria is missing a required option. |
| `option_required_when.features` | The behavior is missing an option that's required when another of its options is set to a specific value. |
| `option_required_when.matches` | The criteria is missing an option that's required when another of its options is set to a specific value. |