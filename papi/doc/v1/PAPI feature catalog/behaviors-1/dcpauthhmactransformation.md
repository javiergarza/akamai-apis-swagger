---
title: "dcpAuthHMACTransformation"
slug: "dcpauthhmactransformation"
hidden: false
createdAt: "2020-06-15T21:06:52.454Z"
updatedAt: "2020-06-15T21:06:52.454Z"
---
__Property Manager name__: [Variable Hash Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9061)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. In conjunction with [`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior affects how clients can authenticate themselves to edge servers, and which groups within namespaces are authorized to access topics. It transforms a source string value extracted from the client certificate and stored as a variable, then generates a hash value based on the selected algorithm, for use in authenticating the client request.

Note that you can apply this hash transformation, or either of the [`dcpAuthRegexTransformation`](#dcpauthregextransformation) or [`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation) behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthHMACTransformation.hashConversionAlgorithm" >

- `hashConversionAlgorithm` (_enum string_): Choose either `MD5`, `SHA256`, or `SHA384` hash algorithms.

</div>

<div class="option" markdown="1" id="dcpAuthHMACTransformation.hashConversionKey" >

- `hashConversionKey` (_string_): Specifies the key to generate the hash, ideally a long random string to ensure adequate security.

</div>

</div>

<div class="feature" data-feature="dcpAuthRegexTransformation" markdown="1">
