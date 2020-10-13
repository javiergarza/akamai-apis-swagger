---
title: "Other errors"
slug: "other-errors"
hidden: false
createdAt: "2020-06-05T21:29:14.464Z"
updatedAt: "2020-06-05T21:29:14.464Z"
---
This table lists miscellaneous errors:

| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `arl-data-xml-invalid` | XML data is invalid. The response indicates which line caused the parse error. |
| [400](https://httpstatuses.com/400) | `invalid-rule-format` | The specified rule format isn't supported. [Learn more](#getruleformats). |
| [400](https://httpstatuses.com/400) | `toolkit/password-needs-rotation` | The password for the user attached to the given authorization token must be rotated. |
| [404](https://httpstatuses.com/404) | `custom-behavior-not-found` | Unable to locate the requested custom behavior. |
| [404](https://httpstatuses.com/404) | `route-not-found` | Unable to locate the requested resource. |
| [404](https://httpstatuses.com/404) | `user-not-present-to-create-custom-behavior` | Can't create a custom behavior not assigned to a user. |
| [422](https://httpstatuses.com/422) | `custom-behavior-name-in-use` | A custom behavior with that name already exists. |

These fallback errors may occur when modifying a rule tree:

| Type | Description |
| :--- | :--- |
| `unknown_message` | Unknown rule tree validation error. |
| `unknown_validation_type` | Unknown value error. |