---
title: "modifyIncomingRequestHeader"
slug: "modifyincomingrequestheader"
hidden: false
createdAt: "2020-06-15T21:38:43.955Z"
updatedAt: "2020-06-15T21:38:43.955Z"
---
__Property Manager name__: [Modify Incoming Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9062)

Modify, add, remove, or pass along specific request headers coming upstream from the client.

Depending on the type of `action` you want to perform, specify the corresponding _standard_ header name, or a `customHeaderName` if the standard name is set to `OTHER`.  The `headerValue` serves as a match condition when the action is `DELETE` or `MODIFY`, and the `newHeaderValue` applies when the action is `ADD` or `MODIFY`.

See also [`modifyIncomingResponseHeader`](#modifyincomingresponseheader), [`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader), and [`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyIncomingRequestHeader.action" >

- `action` (_enum string_): Either `ADD`, `DELETE`, `MODIFY`, or `PASS` incoming HTTP request headers.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_): If the value of `action` is `ADD`, this specifies the name of the field to add, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_): If the value of `action` is `DELETE`, this specifies the name of the field to remove, either `IF_MODIFIED_SINCE`, `VIA`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_): If the value of `action` is `MODIFY`, this specifies the name of the field to modify, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardPassHeaderName" >

- `standardPassHeaderName` (_enum string_): If the value of `action` is `PASS`, this specifies the name of the field to pass through, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_): Specifies a custom field name that applies when the relevant _standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_): With the `action` set to `ADD`, specifies the new header value.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_): With the `action` set to `MODIFY`, supplies an HTTP header replacement value.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_): When enabled with the `action` set to `MODIFY`, prevents creation of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyIncomingResponseHeader" markdown="1">
