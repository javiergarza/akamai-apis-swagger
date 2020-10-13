---
title: "dcpAuthRegexTransformation"
slug: "dcpauthregextransformation"
hidden: false
createdAt: "2020-06-15T21:07:28.500Z"
updatedAt: "2020-06-15T21:07:28.500Z"
---
__Property Manager name__: [Variable Regex Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9060)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. In conjunction with [`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior affects how clients can authenticate themselves to edge servers, and which groups within namespaces are authorized to access topics. It transforms a source string value extracted from the client certificate and stored as a variable, then transforms the string based on a regular expression search pattern, for use in authenticating the client request.

Note that you can apply this regular expression transformation, or either of the [`dcpAuthHMACTransformation`](#dcpauthhmactransformation) or [`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation) behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthRegexTransformation.regexPattern" >

- `regexPattern` (_string_): Specifies a Perl-compatible regular expression with a single grouping to capture the text.  For example, a value of `^.(.{0,10})` omits the first character, but then captures up to 10 characters after that. If the regular expression does not capture a substring, authentication may fail.

</div>

</div>

<div class="feature" data-feature="dcpAuthSubstringTransformation" markdown="1">
