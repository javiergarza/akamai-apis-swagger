---
title: "dcpAuthSubstringTransformation"
slug: "dcpauthsubstringtransformation"
hidden: false
createdAt: "2020-06-15T21:07:59.155Z"
updatedAt: "2020-06-15T21:07:59.155Z"
---
__Property Manager name__: [Variable Substring Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9074)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. In conjunction with [`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior affects how clients can authenticate themselves to edge servers, and which groups within namespaces are authorized to access topics. It transforms a source string value extracted from the client certificate and stored as a variable, then extracts a substring, for use in authenticating the client request.

Note that you can apply this substring transformation, or either of the [`dcpAuthHMACTransformation`](#dcpauthhmactransformation) or [`dcpAuthRegexTransformation`](#dcpauthregextransformation) behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthSubstringTransformation.substringStart" >

- `substringStart` (_string_): The zero-based index offset of the first character to extract. If the index is out of bound from the string's length, authentication may fail.

</div>

<div class="option" markdown="1" id="dcpAuthSubstringTransformation.substringEnd" >

- `substringEnd` (_string_): The zero-based index offset of the last character to extract, where `-1` selects the remainder of the string. If the index is out of bound from the string's length, authentication may fail.

</div>

</div>

<div class="feature" data-feature="dcpAuthVariableExtractor" markdown="1">
