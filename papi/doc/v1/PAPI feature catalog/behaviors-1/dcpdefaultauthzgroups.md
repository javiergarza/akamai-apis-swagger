---
title: "dcpDefaultAuthzGroups"
slug: "dcpdefaultauthzgroups"
hidden: false
createdAt: "2020-06-15T21:09:02.775Z"
updatedAt: "2020-06-15T21:09:02.775Z"
---
__Property Manager name__: [Default Authorization Groups](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9067)

The [Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html) product allows connected users and devices to communicate on a publish-subscribe basis within reserved namespaces. This behavior defines a set of default authorization groups to add to each request the property configuration controls.  These groups have access regardless of the authentication method you use, either JWT using the [`verifyJsonWebTokenForDcp`](#verifyjsonwebtokenfordcp) behavior, or mutual authentication using the [`dcpAuthVariableExtractor`](#dcpauthvariableextractor) behavior to control where authorization groups are extracted from within certificates.

__Options__:

<div class="option" markdown="1" id="dcpDefaultAuthzGroups.groupNames" >

- `groupNames` (_array of string values_): Specifies the set of authorization groups to assign to all connecting devices.

</div>

</div>

<div class="feature" data-feature="dcpDevRelations" markdown="1">
