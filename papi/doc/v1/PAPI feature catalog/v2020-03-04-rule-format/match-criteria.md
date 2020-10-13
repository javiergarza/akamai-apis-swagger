---
title: "Match criteria"
slug: "match-criteria"
hidden: false
createdAt: "2020-06-11T13:12:40.626Z"
updatedAt: "2020-06-15T20:12:45.059Z"
---
The following represents all rule criteria the Property Manager API
supports.  The set available to you is determined by the product and
modules associated with the property, and you can get it by running
the [List available
criteria](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#listavailablecriteria)
operation.

This reference specifies the most recent set of features, that of the
`latest` rule format.  For information on features specified by older
rule formats, see the following:

- [PAPI Feature Catalog Reference, v2015-08-17](https://learn.akamai.com/en-us/api/core_features/property_manager/v2015-08-17.html)
- [PAPI Feature Catalog Reference, v2016-11-15](https://learn.akamai.com/en-us/api/core_features/property_manager/v2016-11-15.html)
- [PAPI Feature Catalog Reference, v2017-06-19](https://learn.akamai.com/en-us/api/core_features/property_manager/v2017-06-19.html)
- [PAPI Feature Catalog Reference, v2018-02-27](https://learn.akamai.com/en-us/api/core_features/property_manager/v2018-02-27.html)
- [PAPI Feature Catalog Reference, v2018-09-12](https://learn.akamai.com/en-us/api/core_features/property_manager/v2018-09-12.html)
- [PAPI Feature Catalog Reference, v2019-07-25](https://learn.akamai.com/en-us/api/core_features/property_manager/v2019-07-25.html)
- [PAPI Feature Catalog Reference, v2020-03-04](https://learn.akamai.com/en-us/api/core_features/property_manager/v2020-03-04.html)

## advancedImMatch

__Property Manager name__:
[Image and Video Manager](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0052)

Matches whether the
[`imageManager`](#imagemanager) behavior already applies to the
current set of requests.

__Options__:

- `matchOperator` (_enum string_):
    2DO: `IS` or `IS_NOT`.

- `matchOn` (_enum string_):
    2DO:
`ANY_IM` or `PRISTINE`.

## bucket

__Property Manager name__:
[Percentage of Clients](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

This [read-only criteria](#ro)
matches a specified percentage of requests when used with the required
accompanying [`spdy`](#spdy) behavior. Contact Akamai Professional
Services for help configuring it.

__Options__:

- `percentage` (_number within 0-100 range_):
    Specifies the
percentage of SPDY requests to match.

## cacheability

__Property Manager name__:
[Response Cacheability](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the current cache
state.  Note that any `NO_STORE` or `BYPASS_CACHE` HTTP headers set on
the origin's content overrides properties'
[`caching`](#caching) instructions, in which case this
criteria does not apply.

__Options__:

- `matchOperator` (_enum string_):
    When
set to `IS`, matches the `value`. If set to `IS_NOT`, reverses the
match so that the cache state does _not_ match the specified
`value`.

- `value` (_enum string_):
    Content's
cache is enabled (`CACHEABLE`) or not (`NO_STORE`), or else is ignored
(`BYPASS_CACHE`).

## chinaCdnRegion

__Property Manager name__:
[ChinaCDN Region](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Identifies traffic
deployed over Akamai's regional ChinaCDN infrastructure.

__Options__:

- `matchOperator` (_enum string_):
    Specify whether the request `IS` or `IS_NOT` deployed over
ChinaCDN.

## clientCertificate

__Property Manager name__:
[Client certificate](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches whether you
have configured a client certificate to authenticate requests to edge
servers.

__Options__:

- `isCertificatePresent` (_boolean_):
    When enabled, executes rule behaviors only if a client certificate
authenticates requests.

- `isCertificateValid` (_enum string_):
    2DO: `IGNORE`, `INVALID`, `VALID`.

## clientIp

__Property Manager name__:
[Client IP](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the IP number of the
requesting client.

__Options__:

- `matchOperator` (_enum string_):
    Matches
the contents of `values` if set to `IS_ONE_OF`, otherwise
`IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_):
    IP or CIDR
block, for example: `71.92.0.0/14`.

- `useHeaders` (_boolean_):
    When
connecting via a proxy server as determined by the `X-Forwarded-For`
header, enabling this option matches the connecting client's IP
address rather than the original end client specified in the header.

## clientIpVersion

__Property Manager name__:
[Client IP Version](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the version of
the IP protocol used by the requesting client.

__Options__:

- `value` (_enum string_):
    The IP
version of the client request, either `IPV4` or `IPV6`.

- `useXForwardedFor` (_boolean_):
    When connecting via a proxy server as determined by the
`X-Forwarded-For` header, enabling this option matches the connecting
client's IP address rather than the original end client specified in
the header.

## cloudletsOrigin

__Property Manager name__:
[Conditional Origin ID](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0027)

Allows Cloudlets
Origins, referenced by label, to define their own criteria to assign
custom origin definitions. The criteria may match, for example, for a
specified percentage of requests defined by the cloudlet to use an
alternative version of a website.

This criteria must be paired with a sibling [`origin`](#origin)
definition.  It should not appear with any other criteria, and an
[`allowCloudletsOrigins`](#allowcloudletsorigins) behavior must
appear within a parent rule.

__Options__:

- `originId` (_string_):
    The Cloudlets Origins identifier, limited to alphanumeric and
underscore characters.

## contentDeliveryNetwork

__Property Manager name__:
CDN Network

A [read-only
criteria](#ro) that specifies the type of Akamai network handling the
request.  Contact Akamai Professional Services for help configuring
it.

__Options__:

- `matchOperator` (_enum string_):
    Matches the specified `network` if set to `IS`, otherwise `IS_NOT`
reverses the match..

- `network` (_enum string_):
    Match requests served from either the `PRODUCTION` or `STAGING`
network.

## contentType

__Property Manager name__:
[Content Type](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the HTTP response
header's `Content-Type`.

__Options__:

- `matchOperator` (_enum string_):
    Matches any `Content-Type` among specified `values` when set to
`IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_):
    `Content-Type` response header value, for example `text/html`.

- `matchWildcard` (_boolean_):
    When
enabled, allows `*` and `?` wildcard matches among the `values`, so
that specifying `text/*` matches both `text/html` and `text/css`.

- `matchCaseSensitive` (_boolean_):
    When enabled, the match is case-sensitive for all `values`.

## deviceCharacteristic

__Property Manager name__:
[Device Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match various
aspects of the device or browser making the request.

Based on the value of the `characteristic` option, the expected value
is either a boolean, a number, or a string, possibly representing a
version number. Each type of value requires a different `value-`
field:

- `booleanValue` specifies a boolean value.
- `numericValue` specifies a numeric value.
- `versionValue` specifies a version number string value.
- `stringValue` specifies any other string value, to which the
  `valueCase` and `valueWildcard` options apply.

__Options__:

- `characteristic` (_enum string_): Aspect of the device or browser to match. The following values are boolean:

    - `ACCEPT_THIRD_PARTY_COOKIE`
    - `AJAX_SUPPORT_JAVASCRIPT`
    - `COOKIE_SUPPORT`
    - `DUAL_ORIENTATION` (whether the display adapts to portrait/landscape orientation)
    - `FULL_FLASH_SUPPORT`
    - `GIF_ANIMATED`
    - `IS_MOBILE`
    - `IS_TABLET` (subset of `IS_MOBILE`)
    - `IS_WIRELESS_DEVICE`

    The following are numeric values:

    - `PHYSICAL_SCREEN_HEIGHT` (millimeters)
    - `PHYSICAL_SCREEN_WIDTH` (millimeters)
    - `RESOLUTION_HEIGHT` (pixels)
    - `RESOLUTION_WIDTH` (pixels)
    - `XHTML_SUPPORT_LEVEL`

    The following are version string values:

    - `DEVICE_OS_VERSION`
    - `MOBILE_BROWSER_VERSION`

    The following are string values:

    - `BRAND_NAME` (such as `Samsung` or `Apple`)
    - `DEVICE_OS`
    - `MARKETING_NAME` (such as `Samsung Illusion`)
    - `MOBILE_BROWSER`
    - `MODEL_NAME` (such as `SCH-I110`)

- `stringMatchOperator` (_enum string_):
    When the `characteristic` expects a string value, set this to
`MATCHES_ONE_OF` to match against the `stringValue` set, otherwise
set to `DOES_NOT_MATCH_ONE_OF` to exclude that set of values.

- `numericMatchOperator` (_enum string_):
    When the `characteristic` expects a numeric value, compares the
specified `numericValue` against the matched client, using the
following operators: `IS`, `IS_MORE_THAN_OR_EQUAL`, `IS_MORE_THAN`,
`IS_LESS_THAN_OR_EQUAL`, `IS_LESS_THAN`, `IS_NOT`.

- `versionMatchOperator` (_enum string_):
    When the `characteristic` expects a version string value, compares
the specified `versionValue` against the matched client, using the
following operators: `IS`, `IS_MORE_THAN_OR_EQUAL`, `IS_MORE_THAN`,
`IS_LESS_THAN_OR_EQUAL`, `IS_LESS_THAN`, `IS_NOT`.

- `booleanValue` (_boolean_):
    When the `characteristic` expects a boolean value, this specifies
the value.

- `stringValue` (_array of string values_):
    When the `characteristic` expects a string, this specifies the set
of values.

- `numericValue` (_number_):
    When the `characteristic` expects a numeric value, this specifies
the number.

- `versionValue` (_string_):
    When the `characteristic` expects a version number, this specifies
it as a string.

- `matchCaseSensitive` (_boolean_):
    When enabled, the match is case-sensitive for the `stringValue`
field.

- `matchWildcard` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the
`stringValue` field.

## edgeWorkersFailure

__Property Manager name__:
[EdgeWorkers Execution Status](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

2DO

__Options__:

- `execStatus` (_enum string_):
    2DO: `FAILURE`,
`SUCCESS`

## fileExtension

__Property Manager name__:
[File Extension](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested
filename's extension, if present.

__Options__:

- `matchOperator` (_enum string_):
    Matches the contents of `values` if set to `IS_ONE_OF`, otherwise
`IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_):
    An array
of file extension strings, with no leading dot characters, for example
`png`, `jpg`, `jpeg`, and `gif`.

- `matchCaseSensitive` (_boolean_):
    When enabled, the match is case-sensitive.

## filename

__Property Manager name__:
[Filename](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested
filename, or test whether it is present.

__Options__:

- `matchOperator` (_enum string_):
    If set
to `IS_ONE_OF` or `IS_NOT_ONE_OF`, matches whether the `value`
matches. If set to `IS_EMPTY` or `IS_NOT_EMPTY`, matches whether the
specified filename is part of the path.

- `values` (_array of string values_):
    Matches the
filename component of the request URL. Wildcards are allowed, where
`?` matches a single character and `*` matches more than one. For
example, specify `filename.*` to accept any extension.

- `matchCaseSensitive` (_boolean_):
    When enabled, the match is case-sensitive for the `value` field.

## hostname

__Property Manager name__:
[Hostname](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested
hostname.

__Options__:

- `matchOperator` (_enum string_):
    Matches
the contents of `values` when set to `IS_ONE_OF`, otherwise
`IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_):
    A list of
hostnames. Wildcards match, so `*.example.com` matches both
`m.example.com` and `www.example.com`.

## matchAdvanced

__Property Manager name__:
Advanced Match

A [read-only criteria](#ro)
that specifies Akamai XML metadata. It can only be configured on your
behalf by Akamai Professional Services.

__Options__:

- `description` (_string_):
    A
human-readable description of what the XML block does.

- `openXml` (_string_):
    An XML
string that opens the relevant block.

- `closeXml` (_string_):
    An XML
string that closes the relevant block.

## matchCpCode

__Property Manager name__:
[Content Provider Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0030)

Match the assigned content
provider code.

__Options__:

- `value` (_object_): Specifies an object that encodes the matching `value`, including an `id` key and a descriptive `name`:

        "value": {
            "id"   : 12345,
            "name" : "my cpcode"
        }

## matchResponseCode

__Property Manager name__:
[Response Status Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match a set or range
of HTTP response codes.

__Options__:

- `matchOperator` (_enum string_):
    Matches the contents of `values` if set to `IS_ONE_OF`, otherwise
`IS_NOT_ONE_OF` reverses the match. If set to `IS_BETWEEN`, matches
the numeric range between `lowerBound` and `upperBound`, otherwise
`IS_NOT_BETWEEN` reverses the match.

- `values` (_array of string values_):
    A set
of response codes to match, for example `["404","500"]`.

- `lowerBound` (_number_):
    Specifies the start of a range of responses when `matchOperator` is
either `IS_BETWEEN` or `IS_NOT_BETWEEN`. For example, `400` to match
anything from `400` to `500`.

- `upperBound` (_number_):
    Specifies the end of a range of responses when `matchOperator` is
either `IS_BETWEEN` or `IS_NOT_BETWEEN`. For example, `500` to match
anything from `400` to `500`.

## matchVariable

__Property Manager name__:
[Variable](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0056)

Matches a built-in
variable, or a custom variable pre-declared within the rule tree by
the [`setVariable`](#setvariable) behavior.  See
[Support for variables](#vf) for more information on this feature.

__Options__:

- `variableName` (_string_):
    The
name of the variable to match.

- `matchOperator` (_enum string_): The type of match, based on which you use different options to specify the match criteria.

    - If set to `IS` or `IS_NOT`, specify a single `variableExpression`       string.
    - If set to `IS_GREATER_THAN`, `IS_LESS_THAN`,       `IS_GREATER_THAN_OR_EQUAL_TO`, or `IS_LESS_THAN_OR_EQUAL_TO`,       specify a single `variableExpression` string.
    - If set to `IS_BETWEEN` or `IS_NOT_BETWEEN`, specify a range       between numeric `lowerBound` and `upperBound` values.
    - If set to `IS_ONE_OF` or `IS_NOT_ONE_OF`, specify an array of       string `variableValues`.
    - If set to `IS_EMPTY` or `IS_NOT_EMPTY`, no other option is       required. These check if a defined variable contains a value.       You can't activate a rule that matches an undefined variable.

- `variableValues` (_array of string values_):
    With `matchOperator` set to either `IS_ONE_OF` or `IS_NOT_ONE_OF`, specifies
an array of matching strings.

- `variableExpression` (_string; allows [variables](#vf)_):
    With `matchOperator` set to either `IS` or `IS_NOT`, specifies a single
matching string.

- `lowerBound` (_string_):
    With
`matchOperator` set to either `IS_BETWEEN` or `IS_NOT_BETWEEN`, specifies the
range's numeric minimum value.

- `upperBound` (_string_):
    With
`matchOperator` set to either `IS_BETWEEN` or `IS_NOT_BETWEEN`, specifies the
range's numeric maximum value.

- `matchWildcard` (_boolean_):
    When matching string expressions, enabling this matches wildcard
metacharacters such as `*` and `?`.

- `matchCaseSensitive` (_boolean_):
    When
matching string expressions, enabling this performs a case-sensitive
match.

## metadataStage

__Property Manager name__:
[Metadata Stage](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches how the current
rule corresponds to low-level syntax elements in translated XML
metadata, indicating progressive stages as each edge server handles
the request and response.  To use this match, you need to be
thoroughly familiar with how Akamai edge servers process requests.
Contact your Akamai Technical representative if you need help, and
test thoroughly on staging before activating on production.

__Options__:

- `matchOperator` (_enum string_):
    Tests
whether the current rule `IS` or `IS_NOT` at the specified metadata
stage.

- `value` (_enum string_): Specifies the metadata stage, one of the following:

    - `content-policy`: This stage calculates whether there is a     property configuration for this request.

    - `client-request`: When the Akamai server receives the request.

    - `client-request-body`: The Akamai server inspects the contents     of the request as a security check.

    - `ipa-response`: Occurs of a response is received from an     intermediate processing agent (IPA) server.

    - `cache-hit`: Content is cacheable and is already cached, but not     yet tested for freshness.

    - `forward-start`: A brief transitory stage while the Akamai     server selects a forward server or persistent connection.

    - `forward-request`: Immediately before the Akamai server tries to     connect to a forward server.

    - `forward-response`: After the forward server responds. Occurs     for content received from an origin server, for example when not     caching it.

    - `client-response`: Occurs prior to constructing a response.

    - `client-done`: Occurs after the response completes.

## originTimeout

__Property Manager name__:
[Origin Timeout](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches when the origin
responds with a timeout error.

__Options__:

- `matchOperator` (_enum string_):
    Specifies a single required `ORIGIN_TIMED_OUT` value.

## path

__Property Manager name__:
[Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the URL's non-hostname
path component.

__Options__:

- `matchOperator` (_enum string_):
    Matches the
contents of `values` when set to `MATCHES_ONE_OF`, otherwise
`DOES_NOT_MATCH_ONE_OF` reverses the match.

- `values` (_array of string values_):
    Matches the URL
path, excluding leading hostname and trailing query parameters. The
path is relative to the server root, for example `/blog`. The `value`
accepts `*` or `?` wildcard characters, for example `/blog/*/2014`.

- `matchCaseSensitive` (_boolean_):
    When
enabled, the match is case-sensitive.

## queryStringParameter

__Property Manager name__:
[Query String Parameter](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches query
string field names or values.

__Options__:

- `parameterName` (_string_):
    The
name of the query field, for example, `q` in `?q=string`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the query field's     `parameterName` is present in the requesting URL.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's     `value` string matches.
    - `IS_LESS_THAN` or `IS_MORE_THAN` matches ranges when the     `value` is numeric.
    - `IS_BETWEEN` also matches numeric ranges, but considers     `lowerBound` and `upperBound` fields rather than `value`.

- `values` (_array of string values_):
    The
value of the query field, for example, `string` in `?q=string`.

- `lowerBound` (_number_):
    When the `value` is numeric and the `matchOperator` is set to
`IS_BETWEEN`, this field specifies the match's minimum value.

- `upperBound` (_number_):
    When the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`,
this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `parameterName`
field.

- `matchCaseSensitiveName` (_boolean_):
    When enabled, the match is case-sensitive for the `parameterName`
field.

- `matchWildcardValue` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `value`
field.

- `matchCaseSensitiveValue` (_boolean_):
    When enabled, the match is case-sensitive for the `value` field.

- `escapeValue` (_boolean_):
    When enabled, matches when the `value` is URL-escaped.

## random

__Property Manager name__:
[Sample Percentage](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0066)

Matches a specified percentage
of requests. Use this match to apply behaviors to a percentage of your
incoming requests that differ from the remainder, useful for A/b
testing, or to offload traffic onto different servers.

__Options__:

- `bucket` (_number within 0-100 range_):
    Specify a percentage of
random requests to which to apply a behavior. Any remainders do not
match.

## regularExpression

__Property Manager name__:
[Regex](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches a regular
expression against a string, especially to apply behaviors flexibly
based on the contents of dynamic [variables](#vf).

__Options__:

- `matchString` (_string; allows [variables](#vf)_):
    The
string to match, typically the contents of a dynamic variable.

- `regex` (_string_):
    The
regular expression (PCRE) to match against the string.

- `caseSensitive` (_boolean_):
    When disabled, the regular expression match is case-insensitive.

## requestCookie

__Property Manager name__:
[Request Cookie](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match the cookie name or
value passed with the request.

__Options__:

- `cookieName` (_string_):
    The name of
the cookie, for example, `visitor` in `visitor:anon`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the cookie `cookieName`     exists.
    - `IS` or `IS_NOT` tests whether the field's `value` string     matches.
    - `IS_BETWEEN` tests whether a numeric cookie `value` falls between     `lowerBound` and `upperBound`.

- `value` (_string_):
    The
cookie's value, for example, `anon` in `visitor:anon`.

- `lowerBound` (_number_):
    When
the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`,
this field specifies the match's minimum value.

- `upperBound` (_number_):
    When
the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`,
this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `cookieName`
field.

- `matchCaseSensitiveName` (_boolean_):
    When
enabled, the match is case-sensitive for the `cookieName` field.

- `matchWildcardValue` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `value`
field.

- `matchCaseSensitiveValue` (_boolean_):
    When enabled, the match is case-sensitive for the `value` field.

## requestHeader

__Property Manager name__:
[Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match HTTP header names
or values.

__Options__:

- `headerName` (_string_):
    The name of
the request header, for example `Accept-Language`.

- `matchOperator` (_enum string_): Narrows the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the field       `headerName` exists.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's `value`     string matches.

- `values` (_array of string values_):
    The request
header's value, for example `en-US` when the header `headerName` is
`Accept-Language`.

- `matchWildcardName` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `headerName`
field.

- `matchWildcardValue` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `value`
field.

- `matchCaseSensitiveValue` (_boolean_):
    When enabled, the match is case-sensitive for the `value` field.

## requestMethod

__Property Manager name__:
[Request Method](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Specify the request's
HTTP verb. Also supports WebDAV methods and common Akamai
operations.

__Options__:

- `matchOperator` (_enum string_):
    Matches the `value` when set to `IS`, otherwise `IS_NOT` reverses
the match.

- `value` (_enum string_):
    Any of the
following HTTP methods:

    - `CONNECT`
    - `COPY`
    - `GET`
    - `HEAD`
    - `HTTP_DELETE` (note the additional prefix)
    - `OPTIONS`
    - `POST`
    - `PUT`
    - `TRACE`

    May also specify the following WebDAV methods:

    - `DAV_ACL`
    - `DAV_CHECKOUT`
    - `DAV_COPY`
    - `DAV_DMCREATE`
    - `DAV_DMINDEX`
    - `DAV_DMMKPATHS`
    - `DAV_DMMKPATH`
    - `DAV_DMOVERLAY`
    - `DAV_DMPATCHPATHS`
    - `DAV_LOCK`
    - `DAV_MERGE`
    - `DAV_MKACTIVITY`
    - `DAV_MKCALENDAR`
    - `DAV_MKCOL`
    - `DAV_MOVE`
    - `DAV_PROPFIND`
    - `DAV_PROPPATCH`
    - `DAV_REPORT`
    - `DAV_SETPROCESS`
    - `DAV_SETREDIRECT`
    - `DAV_TRUTHGET`
    - `DAV_UNLOCK`

    May also specify the following Akamai operations:

    - `AKAMAI_PURGE`
    - `AKAMAI_TRANSLATE`

## requestProtocol

__Property Manager name__:
[Request Protocol](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches whether the
request uses the HTTP or HTTPS protocol.

__Options__:

- `value` (_enum string_):
    Either
`HTTP` or `HTTPS`.

## requestType

__Property Manager name__:
[Request Type](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the basic type of
request.  To use this match, you need to be thoroughly familiar with
how Akamai edge servers process requests.  Contact your Akamai
Technical representative if you need help, and test thoroughly on
staging before activating on production.

__Options__:

- `matchOperator` (_enum string_):
    Specifies whether the request `IS` or `IS_NOT` the type of specified
`value`.

- `value` (_enum string_):
    Specifies the
type of request, either a standard `CLIENT_REQ` or an
`ESI_FRAGMENT`.

## responseHeader

__Property Manager name__:
[Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Match HTTP header
names or values.

__Options__:

- `headerName` (_string_):
    The name of
the response header, for example `Content-Type`.

- `matchOperator` (_enum string_):
    Narrows
the match according to the following criteria:

    - `EXISTS` or `DOES_NOT_EXIST` tests whether the HTTP field     `headerName` is present.
    - `IS_ONE_OF` or `IS_NOT_ONE_OF` tests whether the field's `value`     string matches.
    - `IS_LESS_THAN` or `IS_MORE_THAN` matches ranges when the `value`     is numeric.
    - `IS_BETWEEN` also matches numeric ranges, but considers     `lowerBound` and `upperBound` fields rather than `value`.

- `values` (_array of string values_):
    The
response header's value, for example
`application/x-www-form-urlencoded` when the header `headerName` is
`Content-Type`.

- `lowerBound` (_number_):
    When
the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`,
this field specifies the match's minimum value.

- `upperBound` (_number_):
    When
the `value` is numeric and the `matchOperator` is set to `IS_BETWEEN`,
this field specifies the match's maximum value.

- `matchWildcardName` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `headerName`
field.

- `matchWildcardValue` (_boolean_):
    When enabled, allows `*` and `?` wildcard matches in the `value`
field.

- `matchCaseSensitiveValue` (_boolean_):
    When enabled, the match is case-sensitive for the `value` field.

## time

__Property Manager name__:
[Time Interval](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Specifies ranges of times during
which the request occurred.

__Options__:

- `matchOperator` (_enum string_):
    Specifies
how to define the range of time:

    - `BEGINNING` if the duration is indefinite, using the value of     `beginDate`.
    - `BETWEEN` sets a single range between two dates, using the     values of `beginDate` and `endDate`.
    - `LASTING` also sets a single range, but based on duration     relative to the starting time. It relies on the values of     `lastingDate` and `lastingDuration`.
    - `REPEATING` allows a `LASTING`-style range to repeat at regular     intervals. It relies on the values of `repeatBeginDate`,     `repeatDuration`, and `repeatInterval`.

- `repeatInterval` (_duration string_):
    Sets the
time between each repeating time period's starting points when
`behavior` set to `REPEATING`.

- `repeatDuration` (_duration string_):
    Sets the
duration of each repeating time period with `behavior` set to
`REPEATING`.

- `lastingDuration` (_duration string_):
    With
`behavior` set to `LASTING`, specifies the end of a time period as a
duration relative to the `lastingDate`.

- `lastingDate` (_ISO 8601 format date/time string_):
    Sets the start
of a fixed time period with `behavior` set to `LASTING`.

- `repeatBeginDate` (_ISO 8601 format date/time string_):
    Sets the
start of the initial time period with `behavior` set to `REPEATING`.

- `applyDaylightSavingsTime` (_boolean_):
    Adjusts the start time plus repeat interval to account for daylight
saving time. Applies when the current time and the start time use
different systems, daylight and standard, and the two values are in
conflict.

- `beginDate` (_ISO 8601 format date/time string_):
    Sets the start
of a time period with `behavior` set to `BEGINNING` or `BETWEEN`.

- `endDate` (_ISO 8601 format date/time string_):
    Sets the end of a
fixed time period with `behavior` set to `BETWEEN`.

## tokenAuthorization

__Property Manager name__:
Token Verification Result

Match on Auth Token
2.0 verification results.

__Options__:

- `matchOperator` (_enum string_):
    Either `IS_SUCCESS` if there are no errors, `IS_CUSTOM_FAILURE` for
any errors specified by `statusList`, or `IS_ANY_FAILURE` if there are
any errors.

- `statusList` (_array of string values_):
    Match specific failure cases:

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

## userAgent

__Property Manager name__:
[User Agent](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the user agent string
that helps identify the client browser and device.

__Options__:

- `matchOperator` (_enum string_):
    Matches the specified set of `values` when set to `IS_ONE_OF`,
otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_):
    The `User-Agent` header's
value. For example, `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT
5.1)`.

- `matchWildcard` (_boolean_):
    When
enabled, allows `*` and `?` wildcard matches in the
`value` field. For example, `*Android*`,
`*iPhone5*`, `*Firefox*`, or `*Chrome*`.

- `matchCaseSensitive` (_boolean_):
    When
enabled, the match is case-sensitive for the
`value` field.

## userLocation

__Property Manager name__:
[User Location Data](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

The client browser's
approximate geographic location, determined by looking up the IP
address in a database.

__Options__:

- `field` (_enum string_):
    Indicates
the geographic scope: `CONTINENT`, `COUNTRY`, or `REGION`
for states or provinces within a country.

- `matchOperator` (_enum string_):
    Matches the specified set of values when set to `IS_ONE_OF`,
otherwise `IS_NOT_ONE_OF` reverses the match.

- `countryValues` (_array of string values_):
    ISO 3166-1
country code, such as `US` or `CN`.

- `continentValues` (_array of string values_):
    Continent
code, one of `AF` (Africa), `AS` (Asia), `EU` (Europe), `NA` (North
America), `SA` (South America), `OC` (Oceania), or `OT`
(Antarctica).

- `regionValues` (_array of string values_):
    ISO
3166 country and region codes, for example `US:MA` for Massachusetts
or `JP:13` for Tokyo.

- `checkIps` (_enum string_):
    Specifies which
IP addresses determine the user's location:

    - `CONNECTING` considers the connecting client's IP address.
    - `HEADERS` considers IP addresses specified in the `X-Forwarded-For`     header, succeeding if any of them match.
    - `BOTH` behaves like `HEADERS`, but also considers the connecting     client's IP address.

- `useOnlyFirstXForwardedForIp` (_boolean_):
    When connecting via a proxy server as determined by the
`X-Forwarded-For` header, enabling this option matches the end client
specified in the header. Disabling it matches the connecting client's
IP address.

## userNetwork

__Property Manager name__:
[User Network Data](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches details of the
network over which the request was made, determined by looking up the
IP address in a database.

__Options__:

- `field` (_enum string_):
    The type of
information to match, either `BANDWIDTH`, a specific `NETWORK`, or
a more general `NETWORK_TYPE`.

- `matchOperator` (_enum string_):
    Matches the specified set of values when set to `IS_ONE_OF`,
otherwise `IS_NOT_ONE_OF` reverses the match.

- `networkTypeValues` (_array of string values_):
    Specifies the basic type of network, either `CABLE`, `DIALUP`,
`DSL`, `FIOS`, `ISDN`, `MOBILE`, or `UVERSE`.

- `networkValues` (_array of string values_):
    Any
set of specific networks:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
airtel
alpha_internet
altitudetelecom
aol
arnet
asahi
att
bellcanada
biglobe
bitmailer
bouygues
brighthouse
bskyb
bt
cablevision
cernet
chinamobile
chinanet
chinaunicom
clearwire
colt
comcast
completel
compuserve
covad
dion
dreamnet
dtag
dti
earthlink
easynet
eurociber
fastweb
fibertel
francetelecom
free
freecom
h3g
hinet
ibm
idecnet
iij4u
infosphere
janet
jazztell
justnet
livedoor
mci
mediacom
mediaone
microsoft
mil
nerim
newnet
@nifty
numericable
ocn
odn
ono
panasonic-hi-ho
plala
plusnet
prodigy
qwest
rediris
renater
reserved
retevision
roadrunner
rogers
seednet
seikyo_internet
sfr
shaw
so-net
sprint
suddenlink
talktalk
telefonica
telstra
terramexico
ti
tikitiki
timewarner
tiscali
tmobile
turktelekom
uni2
uninet
upc
uunet
verizon
virginmedia
vodafone
wakwak
wind
windstream
zero
</pre>

- `bandwidthValues` (_array of string values_):
    Bandwidth range in bits per second, either `1`, `57`, `257`, `1000`,
`2000`, or `5000`.

- `checkIps` (_enum string_):
    Specifies
which IP addresses determine the user's network:

    - `CONNECTING` considers the connecting client's IP address.
    - `HEADERS` considers IP addresses specified in the     `X-Forwarded-For` header, succeeding if any of them match.
    - `BOTH` behaves like `HEADERS`, but also considers the connecting     client's IP address.

- `useOnlyFirstXForwardedForIp` (_boolean_):
    When connecting via a proxy server as determined by the
`X-Forwarded-For` header, enabling this option matches the end client
specified in the header. Disabling it matches the connecting client's
IP address.

## variableError

__Property Manager name__:
[Variable Error](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches any runtime
errors that occur on edge servers based on the configuration of a
[`setVariable`](#setvariable) behavior. See
[Support for variables](#vf) section for more information on this
feature.

__Options__:

- `result` (_boolean_): When enabled, matches errors for the specified
set of `variableNames`, otherwise matches errors from variables
outside that set.

- `variableNames` (_string_): The name of the variable whose error
triggers the match, or a space- or comma-delimited list of more than
one variable name. Note that if you define a variable named `VAR`, the
name in this field must appear with its added prefix as
`PMUSER_VAR`. When such a variable is inserted into other fields, it
appears with an additional namespace as `{{user.PMUSER_VAR}}`. See the
[`setVariable`](#setvariable) for details on variable names.
