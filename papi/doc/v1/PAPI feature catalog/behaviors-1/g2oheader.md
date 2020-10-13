---
title: "g2oheader"
slug: "g2oheader"
hidden: false
createdAt: "2020-06-15T21:26:00.744Z"
updatedAt: "2020-06-15T21:26:00.744Z"
---
__Property Manager name__: [Signature Header Authentication](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9054)

The _signature header authentication_ (g2o) security feature provides header-based verification of outgoing origin requests. Edge servers encrypt request data in a pre-defined header, which the origin uses to verify that the edge server processed the request. This behavior configures the request data, header names, encryption algorithm, and shared secret to use for verification.

__Options__:

<div class="option" markdown="1" id="g2oheader.enabled" >

- `enabled` (_boolean_): Enables the g2o verification behavior.

</div>

<div class="option" markdown="1" id="g2oheader.dataHeader" >

- `dataHeader` (_string_): Specifies the name of the header that contains the request data that needs to be encrypted.

</div>

<div class="option" markdown="1" id="g2oheader.signedHeader" >

- `signedHeader` (_string_): Specifies the name of the header containing encrypted request data.

</div>

<div class="option" markdown="1" id="g2oheader.encodingVersion" >

- `encodingVersion` (_numeric enum_): Specifies the version of the encryption algorithm as an integer from `1` through `5`. <!-- `2`, `3`, `4`-->

</div>

<div class="option" markdown="1" id="g2oheader.useCustomSignString" >

- `useCustomSignString` (_boolean_): When disabled, the encrypted string is based on the forwarded URL. If enabled, you can use `customSignString` to customize the set of data to encrypt.

</div>

<div class="option" markdown="1" id="g2oheader.customSignString" >

- `customSignString` (_array of string values_): With `useCustomSignString` enabled, specifies the set of data to be encrypted as a combination of concatenated strings, any of the following values:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
 AK_CLIENT_REAL_IP
 AK_DOMAIN
 AK_EXTENSION
 AK_FILENAME
 AK_HOSTHEADER
 AK_METHOD
 AK_PATH
 AK_QUERY
 AK_SCHEME
 AK_URL
</pre>

</div>

<div class="option" markdown="1" id="g2oheader.secretKey" >

- `secretKey` (_string_): Specifies the shared secret key.

</div>

<div class="option" markdown="1" id="g2oheader.nonce" >

- `nonce` (_string_): Specifies the cryptographic _nonce_ string.

</div>

</div>

<div class="feature" data-feature="globalRequestNumber" markdown="1">
