---
title: "modifyIncomingResponseHeader"
slug: "modifyincomingresponseheader"
hidden: false
createdAt: "2020-06-15T21:39:08.158Z"
updatedAt: "2020-06-15T21:39:08.158Z"
---
__Property Manager name__: [Modify Incoming Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9031)

Modify, add, remove, or pass along specific response headers coming downstream from the origin.

Depending on the type of `action` you want to perform, specify the corresponding _standard_ header name, or a `customHeaderName` if the standard name is set to `OTHER`.  The `headerValue` serves as a match condition when the action is `DELETE` or `MODIFY`, and the `newHeaderValue` applies when the action is `ADD` or `MODIFY`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader), [`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader), and [`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyIncomingResponseHeader.action" >

- `action` (_enum string_): Either `ADD`, `DELETE`, `MODIFY`, or `PASS` incoming HTTP response headers.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_): If the value of `action` is `ADD`, this specifies the name of the field to add, any of the following values:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
 CACHE_CONTROL
 CONTENT_TYPE
 EDGE_CONTROL
 EXPIRES
 LAST_MODIFIED
 OTHER
</pre>

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_): If the value of `action` is `DELETE`, this specifies the name of the field to remove, either `CACHE_CONTROL`, `CONTENT_TYPE`, `VARY`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_): If the value of `action` is `MODIFY`, this specifies the name of the field to modify, either `CACHE_CONTROL`, `CONTENT_TYPE`, `EDGE_CONTROL`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardPassHeaderName" >

- `standardPassHeaderName` (_enum string_): If the value of `action` is `PASS`, this specifies the name of the field to pass through, either `CACHE_CONTROL`, `EXPIRES`, `PRAGMA`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_): Specifies a custom field name that applies when the relevant _standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_): With the `action` set to `ADD`, specifies the header's new value.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_): With the `action` set to `MODIFY`, specifies an HTTP header replacement value.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_): When enabled with the `action` set to `MODIFY`, prevents creation of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyOutgoingRequestHeader" markdown="1">
