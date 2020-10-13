---
title: "originCharacteristics"
slug: "origincharacteristics"
hidden: false
createdAt: "2020-06-15T21:43:16.738Z"
updatedAt: "2020-06-15T21:43:16.738Z"
---
__Property Manager name__: [Origin Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0059)

Specifies characteristics of the origin. Akamai uses this information to optimize your metadata configuration, which may result in better origin offload and end-user performance.

See also [`clientCharacteristics`](#clientcharacteristics) and various product-specific behaviors whose names are prefixed _contentCharacteristics_.

__Options__:

<div class="option" markdown="1" id="originCharacteristics.country" >

- `country` (_enum string_): Specifies the origin's geographic region, or `UNKNOWN` to defer any optimizations based on geography. Regions include `GLOBAL_MULTI_GEO`, `EUROPE`, `NORDICS`, `GERMANY`, `UNITED_KINGDOM`, `ITALY`, `INDIA`, `JAPAN`, `TAIWAN`, `ASIA_PACIFIC`, `AUSTRALIA`, `LATIN_AMERICA`, `MEXICO`, `SOUTH_AMERICA`, `US_CENTRAL`, `US_EAST`, `US_WEST`, `NORTH_AMERICA`, `OTHER_AMERICAS`, `OTHER_APJ` (Asia, Pacific, Japan), `OTHER_EMEA` (Europe, Middle East, Africa), or `ADC` for Akamai Direct Connection, available to Adaptive Media Delivery customers.

</div>

<div class="option" markdown="1" id="originCharacteristics.directConnectGeo" >

- `directConnectGeo` (_string_): With `country` set to `ADC`, provides a region used by Akamai Direct Connection.

</div>

<div class="option" markdown="1" id="originCharacteristics.authenticationMethod" >

- `authenticationMethod` (_enum string_): Specifies the authentication method, either `AWSV4` (Amazon Web Services), `GCP` (Google Cloud Platform), or `AUTOMATIC`.  With the Adaptive Media Delivery product, choose additional `SIGNATURE_HEADER_AUTHENTICATION` or `MSL_AUTHENTICATION` options.

</div>

<div class="option" markdown="1" id="originCharacteristics.encodingVersion" >

- `encodingVersion` (_numeric enum_): With `authenticationMethod` set to `SIGNATURE_HEADER_AUTHENTICATION`, specifies the version of the encryption algorithm, an integer from `1` to `5`. <!-- `2`, `3`, `4` -->

</div>

<div class="option" markdown="1" id="originCharacteristics.useCustomSignString" >

- `useCustomSignString` (_boolean_): With `authenticationMethod` set to `SIGNATURE_HEADER_AUTHENTICATION`, specifies whether to customize your signed string.

</div>

<div class="option" markdown="1" id="originCharacteristics.customSignString" >

- `customSignString` (_array of string values_): With `useCustomSignString` enabled, specifies the data to be encrypted as a sequence of concatenated strings. The array may include any of the following enumerated values: `AK_CLIENT_REAL_IP`, `AK_DOMAIN`, `AK_EXTENSION`, `AK_FILENAME`, `AK_HOSTHEADER`, `AK_METHOD`, `AK_PATH`, `AK_QUERY`, `AK_SCHEME`, and `AK_URL`. See [Support for variables](#vf) for guidance.

</div>

<div class="option" markdown="1" id="originCharacteristics.secretKey" >

- `secretKey` (_string_): Specifies the shared secret key.

</div>

<div class="option" markdown="1" id="originCharacteristics.nonce" >

- `nonce` (_string_): Specifies the nonce.

</div>

<div class="option" markdown="1" id="originCharacteristics.mslkey" >

- `mslkey` (_string_): With `authenticationMethod` set to `MSL_AUTHENTICATION`, specifies the access key provided by the hosting service.

</div>

<div class="option" markdown="1" id="originCharacteristics.mslname" >

- `mslname` (_string_): With `authenticationMethod` set to `MSL_AUTHENTICATION`, specifies the origin name provided by the hosting service.

</div>

<div class="option" markdown="1" id="originCharacteristics.accessKeyEncryptedStorage" >

- `accessKeyEncryptedStorage` (_boolean_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsAccessKeyVersionGuid" >

- `gcsAccessKeyVersionGuid` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsHmacKeyAccessId" >

- `gcsHmacKeyAccessId` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsHmacKeySecret" >

- `gcsHmacKeySecret` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsAccessKeyVersionGuid" >

- `awsAccessKeyVersionGuid` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsAccessKeyId" >

- `awsAccessKeyId` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsSecretAccessKey" >

- `awsSecretAccessKey` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsRegion" >

- `awsRegion` (_string_): 2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsService" >

- `awsService` (_string_): 2DO

</div>

</div>

<div class="feature" data-feature="originCharacteristicsWsd" markdown="1">
