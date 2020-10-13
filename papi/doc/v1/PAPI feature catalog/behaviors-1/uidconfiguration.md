---
title: "uidConfiguration"
slug: "uidconfiguration"
hidden: false
createdAt: "2020-06-15T22:07:53.565Z"
updatedAt: "2020-06-15T22:07:53.565Z"
---
__Property Manager name__: [UID Configuration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0084)

This behavior allows you to extract unique identifier (UID) values from live traffic, for use in OTA applications. Note that you are responsible for maintaining the security of any data that may identify individual users.

__Options__:

<div class="option" markdown="1" id="uidConfiguration.enabled" >

- `enabled` (_boolean_): Allows you to extract UIDs from client requests.

</div>

<div class="option" markdown="1" id="uidConfiguration.extractLocation" >

- `extractLocation` (_enum string_): Whether to extract the UID value from a `CLIENT_REQUEST_HEADER`, a `QUERY_STRING`, or from a rule tree `VARIABLE`. (You should mark these variables as [sensitive](https://developer.akamai.com/api/core_features/property_manager/v1.html#82234a11). See also [Support for variables](#vf) above.)

</div>

<div class="option" markdown="1" id="uidConfiguration.headerName" >

- `headerName` (_string_): With `extractLocation` set to `CLIENT_REQUEST_HEADER`, this specifies the name of the HTTP header from which to extract the UID value.

</div>

<div class="option" markdown="1" id="uidConfiguration.queryParameterName" >

- `queryParameterName` (_string_): With `extractLocation` set to `QUERY_STRING`, this specifies the name of the query parameter from which to extract the UID value.

</div>

<div class="option" markdown="1" id="uidConfiguration.variableName" >

- `variableName` (_string_): With `extractLocation` set to `VARIABLE`, this specifies the name of the rule tree variable from which to extract the UID value.

</div>

</div>

<div class="feature" data-feature="validateEntityTag" markdown="1">
