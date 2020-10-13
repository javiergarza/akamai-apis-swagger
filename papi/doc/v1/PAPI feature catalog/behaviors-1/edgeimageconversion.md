---
title: "edgeImageConversion"
slug: "edgeimageconversion"
hidden: false
createdAt: "2020-06-15T21:18:56.396Z"
updatedAt: "2020-06-15T21:18:56.396Z"
---
__Property Manager name__: [Image Converter Settings](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9001)

The [Edge Image Converter](http://www.akamai.com/html/technology/image-converter.html) offloads various image manipulation tasks to edge servers.  This behavior specifies various predefined policies to apply.

__Options__:

<div class="option" markdown="1" id="edgeImageConversion.enabled" >

- `enabled` (_boolean_): Enables the edge image conversion behavior.

</div>

<div class="option" markdown="1" id="edgeImageConversion.failover" >

- `failover` (_boolean_): If the request results in a server error, enabling this forwards it to the origin.

</div>

<div class="option" markdown="1" id="edgeImageConversion.usePolicy" >

- `usePolicy` (_boolean_): Enables a specified set of image conversion policies.

</div>

<div class="option" markdown="1" id="edgeImageConversion.policies" >

- `policies` (_array_): With `usePolicy` enabled, specifies commands that when present or not in the query string release an error code.

</div>

<div class="option" markdown="1" id="edgeImageConversion.policyResponses" >

- `policyResponses` (_numeric enum_): Specifies the HTTP error code if any `policies` conditions match, either `400`, `403`, `404`, or `409`.

</div>

</div>

<div class="feature" data-feature="edgeLoadBalancingAdvanced" markdown="1">
