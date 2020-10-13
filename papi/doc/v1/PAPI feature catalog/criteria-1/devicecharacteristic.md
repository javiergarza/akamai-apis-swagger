---
title: "deviceCharacteristic"
slug: "devicecharacteristic"
hidden: false
createdAt: "2020-06-15T22:19:25.024Z"
updatedAt: "2020-06-15T22:19:25.024Z"
---
__Property Manager name__: [Device Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match various aspects of the device or browser making the request.

Based on the value of the `characteristic` option, the expected value is either a boolean, a number, or a string, possibly representing a version number. Each type of value requires a different `value-` field:

- `booleanValue` specifies a boolean value. - `numericValue` specifies a numeric value. - `versionValue` specifies a version number string value. - `stringValue` specifies any other string value, to which the   `valueCase` and `valueWildcard` options apply.

__Options__:

- `characteristic` (_enum string_): Aspect of the device or browser to match. The following values are boolean:

    - `ACCEPT_THIRD_PARTY_COOKIE`
    - `AJAX_SUPPORT_JAVASCRIPT`
    - `COOKIE_SUPPORT`
    - `DUAL_ORIENTATION` (whether the display adapts to portrait/landscape orientation)
    - `FULL_FLASH_SUPPORT`
    - `GIF_ANIMATED`
    - `IS_MOBILE`
    - `IS_TABLET` (subset of `IS_MOBILE`)
    - `IS_WIRELESS_DEVICE`

    The following are numeric values:

    - `PHYSICAL_SCREEN_HEIGHT` (millimeters)
    - `PHYSICAL_SCREEN_WIDTH` (millimeters)
    - `RESOLUTION_HEIGHT` (pixels)
    - `RESOLUTION_WIDTH` (pixels)
    - `XHTML_SUPPORT_LEVEL`

    The following are version string values:

    - `DEVICE_OS_VERSION`
    - `MOBILE_BROWSER_VERSION`

    The following are string values:

    - `BRAND_NAME` (such as `Samsung` or `Apple`)
    - `DEVICE_OS`
    - `MARKETING_NAME` (such as `Samsung Illusion`)
    - `MOBILE_BROWSER`
    - `MODEL_NAME` (such as `SCH-I110`)

- `stringMatchOperator` (_enum string_): When the `characteristic` expects a string value, set this to `MATCHES_ONE_OF` to match against the `stringValue` set, otherwise set to `DOES_NOT_MATCH_ONE_OF` to exclude that set of values.

- `numericMatchOperator` (_enum string_): When the `characteristic` expects a numeric value, compares the specified `numericValue` against the matched client, using the following operators: `IS`, `IS_MORE_THAN_OR_EQUAL`, `IS_MORE_THAN`, `IS_LESS_THAN_OR_EQUAL`, `IS_LESS_THAN`, `IS_NOT`.

- `versionMatchOperator` (_enum string_): When the `characteristic` expects a version string value, compares the specified `versionValue` against the matched client, using the following operators: `IS`, `IS_MORE_THAN_OR_EQUAL`, `IS_MORE_THAN`, `IS_LESS_THAN_OR_EQUAL`, `IS_LESS_THAN`, `IS_NOT`.

- `booleanValue` (_boolean_): When the `characteristic` expects a boolean value, this specifies the value.

- `stringValue` (_array of string values_): When the `characteristic` expects a string, this specifies the set of values.

- `numericValue` (_number_): When the `characteristic` expects a numeric value, this specifies the number.

- `versionValue` (_string_): When the `characteristic` expects a version number, this specifies it as a string.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive for the `stringValue` field.

- `matchWildcard` (_boolean_): When enabled, allows `*` and `?` wildcard matches in the `stringValue` field.
