---
title: "constructResponse"
slug: "constructresponse"
hidden: false
createdAt: "2020-06-15T20:56:39.221Z"
updatedAt: "2020-06-15T20:56:39.221Z"
---
__Property Manager name__: [Construct Response](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0028)

A [read-only behavior](#ro) that constructs an HTTP response, complete with HTTP status code and body, to serve from the edge independently of your origin. Contact Akamai Professional Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="constructResponse.enabled" >

- `enabled` (_boolean_): When enabled, serves the custom response.

</div>

<div class="option" markdown="1" id="constructResponse.body" >

- `body` (_string; allows [variables](#vf)_): HTML response of up to 2000 characters to send to the end-user client.

</div>

<div class="option" markdown="1" id="constructResponse.responseCode" >

- `responseCode` (_numeric enum_): The HTTP response code to send to the end-user client, either `200`, `401`, `403`, `404`, `405`, `500`, `501`, `502`, `503`, or `504`.

</div>

<div class="option" markdown="1" id="constructResponse.forceEviction" >

- `forceEviction` (_boolean_): When enabled, removes the underlying object from the cache, since it is not being served.

</div>

</div>

<div class="feature" data-feature="contentCharacteristics" markdown="1">
