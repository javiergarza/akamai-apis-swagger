---
title: "setVariable"
slug: "setvariable"
hidden: false
createdAt: "2020-06-15T22:01:45.270Z"
updatedAt: "2020-06-15T22:01:45.270Z"
---
__Property Manager name__: [Set Variable](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0008)

Modify a variable to insert into subsequent fields within the rule tree.  Use this behavior to specify the predeclared `variableName` and determine from where to derive its new value. Based on this `valueSource`, you can either generate the value, extract it from some part of the incoming request, assign it from another variable (including a set of built-in system variables), or directly specify its text.  Optionally choose a `transform` function to modify the value once. See [Support for variables](#vf) for more information.

__Options__:

<div class="option" markdown="1" id="setVariable.variableName" >

- `variableName` (_string_): Specifies the predeclared root name of the variable to modify.  When you declare a variable name such as `VAR`, its name is preprended with `PMUSER_` and accessible in a `user` namespace, so that you invoke it in subsequent text fields within the rule tree as `{{ "{{" }}user.PMUSER_VAR}}`. In deployed [XML metadata](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#getaversion), it appears as `%(PMUSER_VAR)`.

</div>

<div class="option" markdown="1" id="setVariable.valueSource" >

- `valueSource` (_enum string_): Determines how you want to set the value: either `GENERATE` it, `EXTRACT` it from another value, or specify your own string `EXPRESSION`.

</div>

<div class="option" markdown="1" id="setVariable.variableValue" >

- `variableValue` (_string; allows [variables](#vf)_): With `valueSource` set to `EXPRESSION`, this directly specifies the value to assign to the variable. The expression may include a mix of static text and other variables, such as `new_filename.{{ "{{" }}builtin.AK_EXTENSION}}` to embed a system variable.

</div>

<div class="option" markdown="1" id="setVariable.extractLocation" >

- `extractLocation` (_enum string_): With `valueSource` set to `EXTRACT`, this specifies from where to get the value, either the `CLIENT_CERTIFICATE`, `CLIENT_REQUEST_HEADER`, `RESPONSE_HEADER`, `COOKIE`, `SET_COOKIE`, `EDGESCAPE` (for location or network data), `PATH_COMPONENT_NAME`, `PATH_COMPONENT_OFFSET`, `PATH_PARAMETER`, `DEVICE_PROFILE` (for client device attributes) or `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="setVariable.certificateFieldName" >

- `certificateFieldName` (_enum string_): With `extractLocation` set to `CLIENT_CERTIFICATE`, specifies the certificate's content, either:

    - `CONTENTS_DER`: The entire DER-encoded certificate, expressed in hex.
    - `CONTENTS_PEM`: The PEM-formatted certificate encoded as a single line of base64 characters.
    - `CONTENTS_PEM_NO_LABELS`: Same as `CONTENTS_PEM`, but not including the certificate's header and footer.
    - `COUNT`: The number of client certificates received.
    - `FINGERPRINT_DYN`: The hex-encoded fingerprint generated based on the `SIGNATURE_ALGORITHM`.
    - `FINGERPRINT_MD5`: The hex-encoded MD5 fingerprint.
    - `FINGERPRINT_SHA1`: The hex-encoded SHA1 fingerprint.
    - `ISSUER_DN`: The _distinguished name_ field for the certificate's issuer.
    - `KEY_LENGTH`: The size of the key in bits.
    - `NOT_AFTER`: The end of the time range, expressed in `YYYY/MM/DD HH:MI:SS ZONE` format, where the zone is optional.
    - `NOT_BEFORE`: The start of the time range, expressed in `YYYY/MM/DD HH:MI:SS ZONE` format, where the zone is optional.
    - `SERIAL`: The serial number, expressed in hex.
    - `SIGNATURE_ALGORITHM`: The algorithm used to generate the certificate's signature.
    - `SIGNATURE`: The certificate's signature, expressed in hex.
    - `STATUS_MSG`: A short message indicating the status of a certificate's validation, such as `ok` or `missing`.
    - `SUBJECT_DN`: The _distinguished name_ field for the user.
    - `VERSION`: The certificate's X509 version number.

</div>

<div class="option" markdown="1" id="setVariable.headerName" >

- `headerName` (_string_): With `extractLocation` set to `CLIENT_REQUEST_HEADER`, specifies the case-insensitive name of the HTTP header to extract.

</div>

<div class="option" markdown="1" id="setVariable.responseHeaderName" >

- `responseHeaderName` (_string_): With `extractLocation` set to `RESPONSE_HEADER`, specifies the case-insensitive name of the HTTP header to extract.

</div>

<div class="option" markdown="1" id="setVariable.setCookieName" >

- `setCookieName` (_string_): With `extractLocation` set to `SET_COOKIE`, specifies the name of the origin's `Set-Cookie` response header.

</div>

<div class="option" markdown="1" id="setVariable.cookieName" >

- `cookieName` (_string_): With `extractLocation` set to `COOKIE`, specifies the name of the cookie to extract.

</div>

<div class="option" markdown="1" id="setVariable.locationId" >

- `locationId` (_enum string_): With `extractLocation` set to `EDGESCAPE`, specifies the `X-Akamai-Edgescape` header's field name. Possible values specify basic geolocation, various geographic standards, and information about the client's network:

    - Two-letter `CONTINENT`, ISO-3166 `COUNTRY_CODE` or       `REGION_CODE`, `COUNTY`, `CITY`, `TIMEZONE`, `AREACODE`, `ZIP`,       `LAT`, and `LONG`.
    - `ASNUM` (Autonomous System Number), `DMA` (Designated Market       Area), `FIPS` (Federal Information Processing System code),       `MSA` (Metropolitan Statistical Area), and `PMSA` (Primary       Metropolitan Statistical Area).
    - `NETWORK` (name), `NETWORK_TYPE`, or tiered level of       `THROUGHPUT` or `BW` (bandwidth).

    For details on EdgeScape header fields, see the
    [EdgeScape User Guide](https://control.akamai.com/dl/customers/ESCAPE/EdgeScape_users_guide.pdf).

</div>

<div class="option" markdown="1" id="setVariable.pathComponentOffset" >

- `pathComponentOffset` (_string_): With `extractLocation` set to `PATH_COMPONENT_OFFSET`, this specifies a portion of the path.  The indexing starts from `1`, so a value of `/path/to/nested/filename.html` and an offset of `1` yields `path`, and `3` yields `nested`. Negative indexes offset from the right, so `-2` also yields `nested`.

</div>

<div class="option" markdown="1" id="setVariable.queryParameterName" >

- `queryParameterName` (_string_): With `extractLocation` set to `QUERY_STRING`, specifies the name of the query parameter from which to extract the value.

</div>

<div class="option" markdown="1" id="setVariable.generator" >

- `generator` (_enum string_): With `valueSource` set to `GENERATE`, this specifies the type of value to generate: either `RAND` for a random number, or `HEXRAND` for a random hex sequence.

</div>

<div class="option" markdown="1" id="setVariable.numberOfBytes" >

- `numberOfBytes` (_number within 1-16 range_): With `valueSource` set to `GENERATE` and the `generator` set to `HEXRAND`, this specifies the number of random hex bytes to generate.

</div>

<div class="option" markdown="1" id="setVariable.minRandomNumber" >

- `minRandomNumber` (_string; allows [variables](#vf)_): With `valueSource` set to `GENERATE` and the `generator` set to `RAND`, this specifies the lower bound of the random number.

</div>

<div class="option" markdown="1" id="setVariable.maxRandomNumber" >

- `maxRandomNumber` (_string; allows [variables](#vf)_): With `valueSource` set to `GENERATE` and the `generator` set to `RAND`, this specifies the upper bound of the random number.

</div>

<div class="option" markdown="1" id="setVariable.transform" >

- `transform` (_enum string_): Specifies a function to transform the value, either `NONE` for no transformation, or any from the following categories:

    - Arithmetic: `ADD`, `SUBTRACT`, `MINUS` (reverse sign),       `MULTIPLY`, `DIVIDE`, and `MODULO` (get remainder).
    - Strings: `SUBSTITUTE`, `LOWER`, `UPPER`, `SUBSTRING`,       `STRING_INDEX` (locate a substring), `STRING_LENGTH`,       `REMOVE_WHITESPACE`, `TRIM` (surrounding whitespace), and       `EXTRACT_PARAM`.
    - String conversions: `HEX_ENCODE`/`HEX_DECODE`,       `XML_ENCODE`/`XML_DECODE`.       `URL_ENCODE`/`URL_DECODE`/`URL_DECODE_UNI` (Unicode),       `NORMALIZE_PATH_WIN` (convert Windows paths to Unix format and       remove relative path syntax)
    - Bitwise operations: `BITWISE_AND`, `BITWISE_OR`, `BITWISE_XOR`,       and `BITWISE_NOT`.
    - Numeric conversion: `DECIMAL_TO_HEX`, `HEX_TO_DECIMAL`.
    - Encoding/decoding: `DECRYPT`/`ENCRYPT`,       `BASE_64_ENCODE`/`BASE_64_DECODE`.
    - Generate digests: `SHA_1`, `SHA_256`, `MD5`, a base64-encoded       `HMAC` key, or a simple `HASH` integer.
    - Time formats: `UTC_SECONDS` (epoch time), `EPOCH_TO_STRING`, and       `STRING_TO_EPOCH`.
    - Networking: `NETMASK` (apply a netmask to an IP address to specify the       network's available hosts).

    For more details on each transform function, see
    [Set Variable: Operations](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0087).

</div>

<div class="option" markdown="1" id="setVariable.operandOne" >

- `operandOne` (_string; allows [variables](#vf)_): Specifies an additional operand when the `transform` function is set to various arithmetic functions (`ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, or `MODULO`) or bitwise functions (`BITWISE_AND`, `BITWISE_OR`, or `BITWISE_XOR`).

</div>

<div class="option" markdown="1" id="setVariable.algorithm" >

- `algorithm` (_enum string_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, this specifies the algorithm to apply, either `ALG_AES128` or `ALG_AES256` (Advanced Encryption Standard, 128 or 256 bits), or `ALG_3DES` (Triple DES).

</div>

<div class="option" markdown="1" id="setVariable.encryptionKey" >

- `encryptionKey` (_string; allows [variables](#vf)_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, this specifies the encryption hex key. For `ALG_3DES` it must be 48 characters long, 32 characters for `ALG_AES128`, and 64 characters for `ALG_AES256`.

</div>

<div class="option" markdown="1" id="setVariable.initializationVector" >

- `initializationVector` (_string_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, specifies a one-time number as an initialization vector.  It must be 15 characters long for `ALG_3DES`, and 32 characters for both `ALG_AES128` and `ALG_AES256`.

</div>

<div class="option" markdown="1" id="setVariable.encryptionMode" >

- `encryptionMode` (_enum string_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, specifies either `CBC` (Cipher Block Chaining) or `ECB` (Electronic Codebook) encryption modes.

</div>

<div class="option" markdown="1" id="setVariable.nonce" >

- `nonce` (_string; allows [variables](#vf)_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, specifies the one-time number used for encryption.

</div>

<div class="option" markdown="1" id="setVariable.prependBytes" >

- `prependBytes` (_boolean_): With the `transform` function set to either `ENCRYPT` or `DECRYPT`, specifies a number of random bytes to prepend to the key.

</div>

<div class="option" markdown="1" id="setVariable.formatString" >

- `formatString` (_string_): With the `transform` function set to either `EPOCH_TO_STRING` or `STRING_TO_EPOCH`, this specifies an optional format string for the conversion, using format codes such as `%m/%d/%y` as specified by [`strftime`](http://man7.org/linux/man-pages/man3/strftime.3.html). A blank value defaults to RFC-2616 format.

</div>

<div class="option" markdown="1" id="setVariable.paramName" >

- `paramName` (_string; allows [variables](#vf)_): With the `transform` function set to `EXTRACT_PARAM`, this extracts the value for the specified parameter name from a string that contains key/value pairs. (Use `separator` below to parse them.)

</div>

<div class="option" markdown="1" id="setVariable.separator" >

- `separator` (_string_): With the `transform` function set to `EXTRACT_PARAM`, this specifies the character that separates pairs of values within the string.

</div>

<div class="option" markdown="1" id="setVariable.min" >

- `min` (_number_): With the `transform` function set to `HASH`, specifies a minimum value for the generated integer.

</div>

<div class="option" markdown="1" id="setVariable.max" >

- `max` (_number_): With the `transform` function set to `HASH`, specifies a maximum value for the generated integer

</div>

<div class="option" markdown="1" id="setVariable.hmacKey" >

- `hmacKey` (_string; allows [variables](#vf)_): With the `transform` function set to `HMAC`, specifies the secret to use in generating the base64-encoded digest.

</div>

<div class="option" markdown="1" id="setVariable.hmacAlgorithm" >

- `hmacAlgorithm` (_enum string_): With the `transform` function set to `HMAC`, specifies the algorithm to use to generate the base64-encoded digest, either `MD5`, `SHA1`, or `SHA256`.

</div>

<div class="option" markdown="1" id="setVariable.ipVersion" >

- `ipVersion` (_enum string_): With the `transform` function set to `NETMASK`, this specifies the IP version under which a subnet mask generates, either `IPV4` or `IPV6`.

</div>

<div class="option" markdown="1" id="setVariable.ipv6Prefix" >

- `ipv6Prefix` (_number within 0-128 range_): With the `transform` function set to `NETMASK` and the `ipVersion` set to `IPV6`, specifies the prefix of the IPV6 address, a value between 0 and 128.

</div>

<div class="option" markdown="1" id="setVariable.ipv4Prefix" >

- `ipv4Prefix` (_number within 0-32 range_): With the `transform` function set to `NETMASK` and the `ipVersion` set to `IPV4`, specifies the prefix of the IPV4 address, a value between 0 and 32.

</div>

<div class="option" markdown="1" id="setVariable.subString" >

- `subString` (_string; allows [variables](#vf)_): With the `transform` function set to `STRING_INDEX`, specifies a substring for which the returned value represents a zero-based offset of where it appears in the original string, or `-1` if there's no match.

</div>

<div class="option" markdown="1" id="setVariable.regex" >

- `regex` (_string_): With the `transform` function set to `SUBSTITUTE`, this specifies the regular expression pattern (PCRE) to match the value.

</div>

<div class="option" markdown="1" id="setVariable.replacement" >

- `replacement` (_string; allows [variables](#vf)_): With the `transform` function set to `SUBSTITUTE`, this specifies the replacement string. Reinsert grouped items from the match into the replacement using `$1`, `$2` ... `$n`.

</div>

<div class="option" markdown="1" id="setVariable.caseSensitive" >

- `caseSensitive` (_boolean_): With the `transform` function set to `SUBSTITUTE`, enabling this makes all matches case sensitive.

</div>

<div class="option" markdown="1" id="setVariable.globalSubstitution" >

- `globalSubstitution` (_boolean_): With the `transform` function set to `SUBSTITUTE`, enabling this replaces all matches in the string, not just the first.

</div>

<div class="option" markdown="1" id="setVariable.startIndex" >

- `startIndex` (_string; allows [variables](#vf)_): With the `transform` function set to `SUBSTRING`, specifies the zero-based character offset at the start of the substring. Negative indexes specify the offset from the end of the string.

</div>

<div class="option" markdown="1" id="setVariable.endIndex" >

- `endIndex` (_string; allows [variables](#vf)_): With the `transform` function set to `SUBSTRING`, specifies the zero-based character offset at the end of the substring, without including the character at that index position. Negative indexes specify the offset from the end of the string.

</div>

<div class="option" markdown="1" id="setVariable.exceptChars" >

- `exceptChars` (_string_): With the `transform` function set to `URL_ENCODE`, specifies characters _not_ to encode, possibly overriding the default set.

</div>

<div class="option" markdown="1" id="setVariable.forceChars" >

- `forceChars` (_string_): With the `transform` function set to `URL_ENCODE`, specifies characters to encode, possibly overriding the default set.

</div>

<div class="option" markdown="1" id="setVariable.deviceProfile" >

- `deviceProfile` (_enum string_): With `extractLocation` set to `DEVICE_PROFILE`, specifies the client device attribute. Possible values specify information about the client device, including device type, size and browser:

    - `IS_MOBILE`, `IS_TABLET` and `IS_WIRELESS_DEVICE`; basic device       attributes; returns 'true' or 'false'
    - `PHYSICAL_SCREEN_HEIGHT`, `PHYSICAL_SCREEN_WIDTH` and       `VIEWPORT_WIDTH`; device screen and viewport size in millimeters
    - `RESOLUTION_HEIGHT` and `RESOLUTION_WIDTH`; device       screen size in pixels
    - `BRAND_NAME`, `DEVICE_OS`, `DEVICE_OS_VERSION`,       `MOBILE_BROWSER` and `MOBILE_BROWSER_VERSION`; basic device       attributes; returns string values
    - `MAX_IMAGE_HEIGHT` and `MAX_IMAGE_WIDTH`; maximum image size       that can be displayed, in pixels
    - `DUAL_ORIENTATION`, `PDF_SUPPORT` and `COOKIE_SUPPORT`; device       support capabilities; returns 'true' or 'false'

    For details on Device Characterization fields, see the
    [Device Characterization Online Help](https://control.akamai.com/dl/EDC/Output/EDC_Config_Help/EDCConfiguration.htm).

</div>

</div>

<div class="feature" data-feature="shutr" markdown="1">
