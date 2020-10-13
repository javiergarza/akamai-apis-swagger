---
title: "tokenAuthorization"
slug: "tokenauthorization"
hidden: false
createdAt: "2020-06-15T22:28:26.772Z"
updatedAt: "2020-06-15T22:28:26.772Z"
---
__Property Manager name__: Token Verification Result

Match on Auth Token 2.0 verification results.

__Options__:

- `matchOperator` (_enum string_): Either `IS_SUCCESS` if there are no errors, `IS_CUSTOM_FAILURE` for any errors specified by `statusList`, or `IS_ANY_FAILURE` if there are any errors.

- `statusList` (_array of string values_): Match specific failure cases:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
 EXPIRED_TOKEN
 INVALID_ACL_DELIMITER
 INVALID_DELIMITER
 INVALID_HMAC
 INVALID_HMAC_KEY
 INVALID_IP
 INVALID_TOKEN
 INVALID_URL
 MISSING_EXPIRATION_TIME
 MISSING_TOKEN
 MISSING_URL
 NEED_URL_XOR_ACL
 TOKEN_NOT_VALID_YET
 UNAUTHORIZED_IP
 UNAUTHORIZED_URL
 UNSUPPORTED_VERSION
</pre>
