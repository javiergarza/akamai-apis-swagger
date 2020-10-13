---
title: "dcpAuthVariableExtractor"
slug: "dcpauthvariableextractor"
hidden: false
createdAt: "2020-06-15T21:08:34.264Z"
updatedAt: "2020-06-15T21:08:34.264Z"
---
__Property Manager name__: [Mutual Authentication](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9070)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. This behavior affects how clients can authenticate themselves to edge servers, and which groups within namespaces are authorized to access topics. When enabled, this behavior allows end users to authenticate their requests with valid client certificates. Values for client identifiers or access authorization groups are required to make a request valid.

After extracting values from client certificates and storing them as variables, you can then apply any of these behaviors to transform the value: [`dcpAuthHMACTransformation`](#dcpauthhmactransformation), [`dcpAuthRegexTransformation`](#dcpauthregextransformation), or [`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation).

__Options__:

<div class="option" markdown="1" id="dcpAuthVariableExtractor.certificateField" >

- `certificateField` (_enum string_): Choose the field from the certificate to extract from, either `FINGERPRINT_DYN`, `FINGERPRINT_MD5`, `FINGERPRINT_SHA1`, `SUBJECT_DN`, `SERIAL`, `V3_NETSCAPE_COMMENT`, or `V3_SUBJECT_ALT_NAME`.

</div>

<div class="option" markdown="1" id="dcpAuthVariableExtractor.dcpMutualAuthProcessingVariableId" >

- `dcpMutualAuthProcessingVariableId` (_enum string_): Store the value either as `VAR_DCP_CLIENT_ID` or `VAR_DCP_AUTH_GROUP`.

</div>

</div>

<div class="feature" data-feature="dcpDefaultAuthzGroups" markdown="1">
