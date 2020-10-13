---
title: "modifyOutgoingRequestHeader"
slug: "modifyoutgoingrequestheader"
hidden: false
createdAt: "2020-06-15T21:39:32.513Z"
updatedAt: "2020-06-15T21:39:32.513Z"
---
__Property Manager name__: [Modify Outgoing Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9073)

Modify, add, remove, or pass along specific request headers going upstream towards the origin.

Depending on the type of `action` you want to perform, specify the corresponding _standard_ header name, or a `customHeaderName` if the standard name is set to `OTHER`.  The `headerValue` serves as a match condition when the action is `DELETE` or `MODIFY`, and the `newHeaderValue` applies when the action is `ADD` or `MODIFY`. Whole-text replacements apply when the action is `MODIFY`, and substitutions apply when set to `REGEX`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader), [`modifyIncomingResponseHeader`](#modifyincomingresponseheader), and [`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.action" >

- `action` (_enum string_): Either `ADD` or `DELETE` outgoing HTTP request headers, `MODIFY` their fixed values, or specify a `REGEX` pattern to transform them.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_): If the value of `action` is `ADD`, this specifies the name of the field to add, either `USER_AGENT` or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_): If the value of `action` is `DELETE`, this specifies the name of the field to remove, either `PRAGMA`, `USER_AGENT`, `VIA`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_): If the value of `action` is `MODIFY` or `REGEX`, this specifies the name of the field to modify, either `USER_AGENT` or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_): Specifies a custom field name that applies when the relevant _standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_): With the `action` set to `ADD`, specifies the new header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_): With the `action` set to `MODIFY`, specifies an HTTP header replacement value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.regexHeaderMatch" >

- `regexHeaderMatch` (_string; allows [variables](#vf)_): When the `action` is `REGEX`, specifies a Perl-compatible regular expression to match within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.regexHeaderReplace" >

- `regexHeaderReplace` (_string; allows [variables](#vf)_): When the `action` is `REGEX`, specifies text that replaces the `regexHeaderMatch` pattern within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.matchMultiple" >

- `matchMultiple` (_boolean_): When enabled with the `action` set to `REGEX`, replaces all occurrences of the matched regular expression, otherwise only the first match if disabled.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_): When enabled with the `action` set to `MODIFY`, prevents creation of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyOutgoingResponseHeader" markdown="1">
