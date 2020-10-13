---
title: "globalRequestNumber"
slug: "globalrequestnumber"
hidden: false
createdAt: "2020-06-15T21:27:07.386Z"
updatedAt: "2020-06-15T21:27:07.386Z"
---
__Property Manager name__: [Global Request Number](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9038)

Generates a unique identifier for each request on the Akamai edge network, for use in logging and debugging. GRN identifiers follow the same format as Akamai's error reference strings, for example: `0.05313217.1567801841.1457a3`.  You can use the Diagnostic Tools API's [Translate an Error](https://developer.akamai.com/api/core_features/diagnostic_tools/v2.html#gettranslatederror) operation to get low-level details about any request.

__Options__:

<div class="option" markdown="1" id="globalRequestNumber.outputOption" >

- `outputOption` (_enum string_): Specifies how to report the GRN value, either as a `RESPONSE_HEADER` to the client, a `REQUEST_HEADER` to the origin, `BOTH_HEADERS`, or `ASSIGN_VARIABLE` to process the value in some other way as a [variable](#vf).

</div>

<div class="option" markdown="1" id="globalRequestNumber.headerName" >

- `headerName` (_string_): With `outputOption` set to specify any set of headers, this specifies the name of the header to report the GRN value.

</div>

<div class="option" markdown="1" id="globalRequestNumber.variableName" >

- `variableName` (_string_): With `outputOption` set to `ASSIGN_VARIABLE`, this specifies the name of the variable to assign the GRN value to. You need to pre-declare any [variable](#vf) you specify within the rule tree.

</div>

</div>

<div class="feature" data-feature="gzipResponse" markdown="1">
