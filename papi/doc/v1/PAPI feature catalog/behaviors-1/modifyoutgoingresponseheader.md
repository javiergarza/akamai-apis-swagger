---
title: "modifyOutgoingResponseHeader"
slug: "modifyoutgoingresponseheader"
hidden: false
createdAt: "2020-06-15T21:39:55.464Z"
updatedAt: "2020-06-15T21:39:55.464Z"
---
__Property Manager name__: [Modify Outgoing Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9052)

Modify, add, remove, or pass along specific response headers going downstream towards the client.

Depending on the type of `action` you want to perform, specify the corresponding _standard_ header name, or a `customHeaderName` if the standard name is set to `OTHER`. The `headerValue` serves as a match condition when the action is `DELETE` or `MODIFY`, and the `newHeaderValue` applies when the action is `ADD` or `MODIFY`. Whole-text replacements apply when the action is `MODIFY`, and substitutions apply when set to `REGEX`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader), [`modifyIncomingResponseHeader`](#modifyincomingresponseheader), and [`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader)

__Options__:

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.action" >

- `action` (_enum string_): Either `ADD` or `DELETE` outgoing HTTP response headers, `MODIFY` their fixed values, or specify a `REGEX` pattern to transform them.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_): If the value of `action` is `ADD`, this specifies the name of the field to add, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
 ACCESS_CONTROL_ALLOW_CREDENTIALS
 ACCESS_CONTROL_ALLOW_HEADERS
 ACCESS_CONTROL_ALLOW_METHODS
 ACCESS_CONTROL_ALLOW_ORIGIN
 ACCESS_CONTROL_EXPOSE_HEADERS
 ACCESS_CONTROL_MAX_AGE
 CACHE_CONTROL
 CONTENT_DISPOSITION
 CONTENT_TYPE
 EDGE_CONTROL
 OTHER
 P3P
 PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_): If the value of `action` is `DELETE`, this specifies the name of the field to remove, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
 ACCESS_CONTROL_ALLOW_CREDENTIALS
 ACCESS_CONTROL_ALLOW_HEADERS
 ACCESS_CONTROL_ALLOW_METHODS
 ACCESS_CONTROL_ALLOW_ORIGIN
 ACCESS_CONTROL_EXPOSE_HEADERS
 ACCESS_CONTROL_MAX_AGE
 CACHE_CONTROL
 CONTENT_DISPOSITION
 CONTENT_TYPE
 EXPIRES
 OTHER
 P3P
 PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_): If the value of `action` is `MODIFY` or `REGEX`, this specifies the name of the field to modify, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
 ACCESS_CONTROL_ALLOW_CREDENTIALS
 ACCESS_CONTROL_ALLOW_HEADERS
 ACCESS_CONTROL_ALLOW_METHODS
 ACCESS_CONTROL_ALLOW_ORIGIN
 ACCESS_CONTROL_EXPOSE_HEADERS
 ACCESS_CONTROL_MAX_AGE
 CACHE_CONTROL
 CONTENT_DISPOSITION
 CONTENT_TYPE
 OTHER
 P3P
 PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_): Specifies a custom field name that applies when the relevant _standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_): Specifies the existing value of the header to match.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_): With the `action` set to `MODIFY`, specifies the new HTTP header replacement value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.regexHeaderMatch" >

- `regexHeaderMatch` (_string_): When the `action` is `REGEX`, specifies a Perl-compatible regular expression to match within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.regexHeaderReplace" >

- `regexHeaderReplace` (_string; allows [variables](#vf)_): When the `action` is `REGEX`, specifies text that replaces the `regexHeaderMatch` pattern within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.matchMultiple" >

- `matchMultiple` (_boolean_): When enabled with the `action` set to `REGEX`, replaces all occurrences of the matched regular expression, otherwise only the first match if disabled.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_): When enabled with the `action` set to `MODIFY`, prevents creation of more than one instance of a header. The last header clobbers others with the same name. This option affects the entire set of outgoing headers, and is not confined to the subset of regular expression matches.

</div>

</div>

<div class="feature" data-feature="modifyViaHeader" markdown="1">
