---
title: "Behaviors"
slug: "behaviors-2"
hidden: false
createdAt: "2020-06-11T13:12:52.357Z"
updatedAt: "2020-06-15T20:13:56.242Z"
---
# Behaviors

The following represents all rule behaviors the Property Manager API
supports.  The set available to you is determined by the product and
modules associated with the property, and you can get it by running
the
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#listavailablebehaviors)
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

<div class="feature" data-feature="adaptiveAcceleration" markdown="1">

## adaptiveAcceleration

__Property Manager name__:
[Adaptive Acceleration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0120)

With the
[`http2`](#http2) and [`realUserMonitoring`](#realusermonitoring)
features enabled, uses HTTP/2 server push to pre-position content and
improve the performance of HTML page loading based on Real User
Monitoring (RUM) timing data. Also use this feature to allow browsers
to preconnect to content likely needed for upcoming requests.  Use the
[Adaptive Acceleration API](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html)
to report on the set of assets this feature optimizes.

__Options__:

<div class="option" markdown="1" id="adaptiveAcceleration.source" >

- `source` (_string_):
    With
`enablePreconnect` or `enablePush` on, specifies the type of data that
anticipates optimal connections. If you specify a value of `Real User
Monitoring`, make sure to enable the corresponding
[`realUserMonitoring`](#realusermonitoring) behavior.
If you specify `mPulse`, enable the [`mPulse`](#mpulse) behavior.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enablePush" >

- `enablePush` (_boolean_):
    Enables adaptive acceleration's HTTP/2 server push feature.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enablePreconnect" >

- `enablePreconnect` (_boolean_):
    When enabled, allows browsers to open TCP connections to web
pages before making requests.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.preloadEnable" >

- `preloadEnable` (_boolean_):
    With the beacon `source` set to `mPulse`, allows fonts to preload.

</div>

<div class="option" markdown="1" id="adaptiveAcceleration.enableRo" >

- `enableRo` (_boolean_):
    Enables the Resource Optimizer, which compresses common file
components such as scripts, fonts, and CSS, and caches them on the
Akamai network.

</div>

</div>

<div class="feature" data-feature="adaptiveImageCompression" markdown="1">

## adaptiveImageCompression

__Property Manager name__:
[Adaptive Image Compression](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0114)

The Adaptive
Image Compression feature compresses JPEG images depending on the
requesting network's performance, thus improving response time. The
behavior specifies three performance tiers based on round-trip tests:
1 for excellent, 2 for good, and 3 for poor. It assigns separate
performance criteria for mobile (cellular) and non-mobile networks,
which the `compressMobile` and `compressStandard` options enable
independently.

There are six `method` options, one for each tier and type of network.
If the `method` is `COMPRESS`, choose from among the six corresponding
`slider` options to specify a percentage. As an alternative to
compression, setting the `method` to `STRIP` removes unnecessary
application-generated metadata from the image. Setting the `method` to
`BYPASS` serves clients the original image.

The behavior serves `ETags` headers as a data signature for each
adapted variation. In case of error or if the file size increases, the
behavior serves the original image file. Flushing the original image
from the edge cache also flushes adapted variants. The behavior
applies to the following image file extensions: `jpg`, `jpeg`, `jpe`,
`jif`, `jfif`, and `jfi`.

__Options__:

<div class="option" markdown="1" id="adaptiveImageCompression.compressMobile" >

- `compressMobile` (_boolean_):
    When enabled, adapts images served over cellular mobile networks.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.compressStandard" >

- `compressStandard` (_boolean_):
    When enabled, adapts images served over non-cellular networks.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1StandardCompressionMethod" >

- `tier1StandardCompressionMethod` (_enum string_):
    Specifies tier-1 non-cellular network behavior, either `COMPRESS`,
`STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1StandardCompressionValue" >

- `tier1StandardCompressionValue` (_number within 0-100 range_):
    With `tier1StandardCompressionMethod` set to `COMPRESS`, this specifies
the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2StandardCompressionMethod" >

- `tier2StandardCompressionMethod` (_enum string_):
    Specifies tier-2 non-cellular network behavior, either `COMPRESS`,
`STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2StandardCompressionValue" >

- `tier2StandardCompressionValue` (_number within 0-100 range_):
    With `tier2StandardCompressionMethod` set to `COMPRESS`, this specifies
the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3StandardCompressionMethod" >

- `tier3StandardCompressionMethod` (_enum string_):
    Specifies tier-5 non-cellular network behavior, either `COMPRESS`,
`STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3StandardCompressionValue" >

- `tier3StandardCompressionValue` (_number within 0-100 range_):
    With `tier3StandardCompressionMethod` set to `COMPRESS`, this specifies
the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1MobileCompressionMethod" >

- `tier1MobileCompressionMethod` (_enum string_):
    Specifies tier-1 behavior, either `COMPRESS`, `STRIP`, or
`BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1MobileCompressionValue" >

- `tier1MobileCompressionValue` (_number within 0-100 range_):
    With `tier1MobileCompressionMethod` set to `COMPRESS`, this specifies the
compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2MobileCompressionMethod" >

- `tier2MobileCompressionMethod` (_enum string_):
    Specifies tier-2 cellular-network behavior, either `COMPRESS`,
`STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2MobileCompressionValue" >

- `tier2MobileCompressionValue` (_number within 0-100 range_):
    With `tier2MobileCompressionMethod` set to `COMPRESS`, this specifies the
compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3MobileCompressionMethod" >

- `tier3MobileCompressionMethod` (_enum string_):
    Specifies tier-5 cellular-network behavior, either `COMPRESS`,
`STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3MobileCompressionValue" >

- `tier3MobileCompressionValue` (_number within 0-100 range_):
    With `tier3MobileCompressionMethod` set to `COMPRESS`, this specifies the
compression percentage.

</div>

</div>

<div class="feature" data-feature="advanced" markdown="1">

## advanced

__Property Manager name__:
[Advanced](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0119)

A [read-only behavior](#ro) that
specifies Akamai XML metadata. It can only be configured on your
behalf by Akamai Professional Services.

__Options__:

<div class="option" markdown="1" id="advanced.description" >

- `description` (_string_):
    Human-readable
description of what the XML block does.

</div>

<div class="option" markdown="1" id="advanced.xml" >

- `xml` (_string_):
    Akamai XML metadata.

</div>

</div>

<div class="feature" data-feature="aggregatedReporting" markdown="1">

## aggregatedReporting

__Property Manager name__:
[Aggregated Reporting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0010)

Configure attributes
for your custom aggregated reports. You can configure up to four
attributes.

__Options__:

<div class="option" markdown="1" id="aggregatedReporting.enabled" >

- `enabled` (_boolean_):
    Enables aggregated reporting.

</div>

<div class="option" markdown="1" id="aggregatedReporting.reportName" >

- `reportName` (_string_):
    The unique name of the aggregated report within the property. If you
reconfigure any attributes or variables in the aggregated reporting
behavior, update this field to a unique value to enable logging data
in a new instance of the report.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attributesCount" >

- `attributesCount` (_number within 1-4 range_):
    Select the number of attributes by which your report is grouped. You
can add up to four attributes.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute1" >

- `attribute1` (_string; allows [variables](#vf)_):
    Select a previously user-defined variable to be an attribute for the
report. The values extracted for all attributes range from 0 to 20
characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute2" >

- `attribute2` (_string; allows [variables](#vf)_):
    Select a previously user-defined variable to be an attribute for the
report. The values extracted for all attributes range from 0 to 20
characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute3" >

- `attribute3` (_string; allows [variables](#vf)_):
    Select a previously user-defined variable to be an attribute for the
report. The values extracted for all attributes range from 0 to 20
characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute4" >

- `attribute4` (_string; allows [variables](#vf)_):
    Select a previously user-defined variable to be an attribute for the
report. The values extracted for all attributes range from 0 to 20
characters.

</div>

</div>

<div class="feature" data-feature="akamaizer" markdown="1">

## akamaizer

__Property Manager name__:
[Akamaizer](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9047)

This [read-only behavior](#ro)
allows you to run regular expression substitutions over web pages.
To apply this behavior, you need to match on a
[`contentType`](#contenttype).
Contact Akamai Professional Services for help configuring the
Akamaizer. See also the [`akamaizerTag`](#akamaizertag) behavior.

__Options__:

<div class="option" markdown="1" id="akamaizer.enabled" >

- `enabled` (_boolean_):
    Enables the Akamaizer
behavior.

</div>

</div>

<div class="feature" data-feature="akamaizerTag" markdown="1">

## akamaizerTag

__Property Manager name__:
[Akamaize Tag](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9075)

This [read-only behavior](#ro)
specifies HTML tags and replacement rules for hostnames
used in conjunction with the [`akamaizer`](#akamaizer)
behavior. Contact Akamai Professional Services for help configuring
the Akamaizer.

__Options__:

<div class="option" markdown="1" id="akamaizerTag.matchHostname" >

- `matchHostname` (_string_):
    Specifies the hostname to match on as a Perl-compatible regular
expression.

</div>

<div class="option" markdown="1" id="akamaizerTag.replacementHostname" >

- `replacementHostname` (_string_):
    Specifies the replacement hostname for the tag to use.

</div>

<div class="option" markdown="1" id="akamaizerTag.scope" >

- `scope` (_enum string_):
    Specifies the
part of HTML content the `tagsAttribute` refers to:

    - `ATTRIBUTE` for when `tagsAttribute` refers to a     tag/attribute pair, the match only applies to the attribute.
    - `URL_ATTRIBUTE` is the same as `ATTRIBUTE`, but applies when the attribute     value is a URL. In that case, it converts to an absolute URL     prior to substitution.
    - `BLOCK` substitutes within the tag's contents, but not within     any nested tags.
    - `PAGE` ignores the `tagsAttribute` field     and performs the substitution on the entire page.

</div>

<div class="option" markdown="1" id="akamaizerTag.tagsAttribute" >

- `tagsAttribute` (_enum string_):
    Specifies
the tag or tag/attribute combination to operate on, any of the
following:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
A
A_HREF
AREA
AREA_HREF
BASE
BASE_HREF
FORM
FORM_ACTION
IFRAME
IFRAME_SRC
IMG
IMG_SRC
LINK
LINK_HREF
SCRIPT
SCRIPT_SRC
TABLE
TABLE_BACKGROUND
TD
TD_BACKGROUND
</pre>

</div>

<div class="option" markdown="1" id="akamaizerTag.replaceAll" >

- `replaceAll` (_boolean_):
    Replaces
all matches when enabled, otherwise replaces only the first match.

</div>

<div class="option" markdown="1" id="akamaizerTag.includeTagsAttribute" >

- `includeTagsAttribute` (_boolean_):
    Whether to include the `tagsAttribute` value.

</div>

</div>

<div class="feature" data-feature="allHttpInCacheHierarchy" markdown="1">

## allHttpInCacheHierarchy

__Property Manager name__:
[Allow All Methods on Parent Servers](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9071)

Allow all HTTP
request methods to be used for the edge's parent servers, useful to
implement features such as
[Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html),
[SureRoute](http://www.akamai.com/dl/feature_sheets/fs_edgesuite_sureroute.pdf),
and Tiered Distribution. (See the [`siteShield`](#siteshield),
[`sureRoute`](#sureroute), and
[`tieredDistribution`](#tiereddistribution) behaviors.)

__Options__:

<div class="option" markdown="1" id="allHttpInCacheHierarchy.enabled" >

- `enabled` (_boolean_):
    Enables all HTTP requests for parent servers in the cache
hierarchy.

</div>

</div>

<div class="feature" data-feature="allowCloudletsOrigins" markdown="1">

## allowCloudletsOrigins

__Property Manager name__:
[Allow Conditional Origins](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0014)

Allows
Cloudlets Origins to determine the criteria, separately from the
Property Manager, under which alternate [`origin`](#origin)
definitions are assigned.

This behavior must appear alone within its own rule. When enabled, it
allows any [`cloudletsOrigin`](#cloudletsorigin) criteria
within sub-rules to override the prevailing origin.

__Options__:

<div class="option" markdown="1" id="allowCloudletsOrigins.enabled" >

- `enabled` (_boolean_):
    Allows you to assign custom origin definitions referenced in
sub-rules by [`cloudletsOrigin`](#cloudletsorigin) labels.
If disabled, all sub-rules are ignored.

</div>

<div class="option" markdown="1" id="allowCloudletsOrigins.honorBaseDirectory" >

- `honorBaseDirectory` (_boolean_):
    If enabled, prefixes any Cloudlet-generated origin path with a
path defined by an Origin Base Path behavior. If no path is defined,
it has no effect. If another Cloudlet policy already prepends the same
Origin Base Path, the path is not duplicated.

</div>

<div class="option" markdown="1" id="allowCloudletsOrigins.purgeOriginQueryParameter" >

- `purgeOriginQueryParameter` (_string_):
    When purging content from a Cloudlets Origin, this specifies a
query parameter name whose value is the specific named origin to
purge.  Note that this only applies to content purge requests, for
example when using the
[Content Control Utility API](https://learn.akamai.com/en-us/api/web_performance/content_control_utility/v2.html).

</div>

</div>

<div class="feature" data-feature="allowDelete" markdown="1">

## allowDelete

__Property Manager name__:
[Allow DELETE](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0011)

Allow HTTP requests using the
DELETE method. By default, only GET and HEAD requests are allowed, and
all other methods result in a 403 error. Such content does not cache,
and any DELETE requests pass to the origin.
See also the
[`allowOptions`](#allowoptions),
[`allowPatch`](#allowpatch),
[`allowPost`](#allowpost),
and
[`allowPut`](#allowput)
behaviors.

__Options__:

<div class="option" markdown="1" id="allowDelete.enabled" >

- `enabled` (_boolean_):
    When enabled,
allows DELETE requests. Content does _not_ cache.

</div>

<div class="option" markdown="1" id="allowDelete.allowBody" >

- `allowBody` (_boolean_):
    When
enabled, allows data in the body of the DELETE request.

</div>

</div>

<div class="feature" data-feature="allowHTTPSCacheKeySharing" markdown="1">

## allowHTTPSCacheKeySharing

__Property Manager name__:
[HTTPS Cache Key Sharing](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9025)

HTTPS cache key
sharing allows HTTP requests to be served from an HTTPS cache.

__Options__:

<div class="option" markdown="1" id="allowHTTPSCacheKeySharing.enabled" >

- `enabled` (_boolean_):
    Enables HTTPS cache key sharing.

</div>

</div>

<div class="feature" data-feature="allowHTTPSDowngrade" markdown="1">

## allowHTTPSDowngrade

__Property Manager name__:
[Protocol Downgrade](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5004)

Passes HTTPS requests
to origin as HTTP. This is useful when incorporating Standard TLS or
Akamai's shared certificate delivery security with an origin that
serves HTTP traffic.

__Options__:

<div class="option" markdown="1" id="allowHTTPSDowngrade.enabled" >

- `enabled` (_boolean_):
    Downgrades to HTTP protocol for the origin server.

</div>

</div>

<div class="feature" data-feature="allowOptions" markdown="1">

## allowOptions

__Property Manager name__:
[Allow OPTIONS](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0013)

Allow HTTP requests using
the OPTIONS method. By default, only GET and HEAD requests are
allowed, and all other methods result in a 403 error. Such content
does not cache, and any OPTIONS requests pass to the origin.
See also the
[`allowDelete`](#allowdelete),
[`allowPatch`](#allowpatch),
[`allowPost`](#allowpost),
and
[`allowPut`](#allowput)
behaviors.

__Options__:

<div class="option" markdown="1" id="allowOptions.enabled" >

- `enabled` (_boolean_):
    When
enabled, allows OPTIONS requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowPatch" markdown="1">

## allowPatch

__Property Manager name__:
[Allow PATCH](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9016)

Allow HTTP requests using the
PATCH method. By default, only GET and HEAD requests are allowed, and
all other methods result in a 403 error. Such content does not cache,
and any PATCH requests pass to the origin.
See also the
[`allowDelete`](#allowdelete),
[`allowOptions`](#allowoptions),
[`allowPost`](#allowpost),
and
[`allowPut`](#allowput)
behaviors.

__Options__:

<div class="option" markdown="1" id="allowPatch.enabled" >

- `enabled` (_boolean_):
    When enabled,
allows PATCH requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowPost" markdown="1">

## allowPost

__Property Manager name__:
[Allow POST](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0012)

Allow HTTP requests using the
POST method. By default, only GET and HEAD are allowed, and all other
methods result in a 403 error.
See also the
[`allowDelete`](#allowdelete),
[`allowOptions`](#allowoptions),
[`allowPatch`](#allowpatch),
and
[`allowPut`](#allowput)
behaviors.

__Options__:

<div class="option" markdown="1" id="allowPost.enabled" >

- `enabled` (_boolean_):
    When enabled,
allows POST requests.

</div>

<div class="option" markdown="1" id="allowPost.allowWithoutContentLength" >

- `allowWithoutContentLength` (_boolean_):
    By default, POST requests also require a `Content-Length` header,
or they result in a 411 error. With this option enabled with no
specified `Content-Length`, the edge server relies on a
`Transfer-Encoding` header to chunk the data. If neither header is
present, it assumes the request has no body, and it adds a header with
a `0` value to the forward request.

</div>

</div>

<div class="feature" data-feature="allowPut" markdown="1">

## allowPut

__Property Manager name__:
[Allow PUT](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0013)

Allow HTTP requests using the
PUT method.  By default, only GET and HEAD are allowed, and all other
methods result in a 403 error. Such content does not cache, and any
PUT requests pass to the origin.
See also the
[`allowDelete`](#allowdelete),
[`allowOptions`](#allowoptions),
[`allowPatch`](#allowpatch),
and
[`allowPost`](#allowpost)
behaviors.

__Options__:

<div class="option" markdown="1" id="allowPut.enabled" >

- `enabled` (_boolean_):
    When enabled, allows PUT
requests. Content does _not_ cache.

</div>

</div>

<div class="feature" data-feature="allowTransferEncoding" markdown="1">

## allowTransferEncoding

__Property Manager name__:
[Chunked Transfer Encoding](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0015)

Controls whether to
allow or deny Chunked Transfer Encoding (CTE) requests to pass to your
origin. If your origin supports CTE, you should enable this behavior.
This behavior also protects against a known issue when pairing
[`http2`](#http2) and [`webdav`](#webdav) behaviors within the same
rule tree, in which case it is required.

__Options__:

<div class="option" markdown="1" id="allowTransferEncoding.enabled" >

- `enabled` (_boolean_):
    Allows Chunked Transfer Encoding requests.

</div>

</div>

<div class="feature" data-feature="apiPrioritization" markdown="1">

## apiPrioritization

__Property Manager name__:
[API Prioritization Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0016)

Enables the API
Prioritization Cloudlet, which maintains continuity in user experience
by serving an alternate static response when load is too high. You can
configure rules using either the Cloudlets Policy Manager application
or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).
The feature is designed to serve static API content, such as fallback
JSON data.  To serve non-API HTML content, use the
[`visitorPrioritization`](#visitorprioritization) behavior.

__Options__:

<div class="option" markdown="1" id="apiPrioritization.enabled" >

- `enabled` (_boolean_):
    Activates the API Prioritization feature.

</div>

<div class="option" markdown="1" id="apiPrioritization.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="apiPrioritization.label" >

- `label` (_string_):
    A
label to distinguish this API Prioritization policy from any others in
the same property.

</div>

<div class="option" markdown="1" id="apiPrioritization.useThrottledCpCode" >

- `useThrottledCpCode` (_boolean_):
    Specifies whether to apply an alternative CP code for requests
served the alternate response.

</div>

<div class="option" markdown="1" id="apiPrioritization.throttledCpCode" >

- `throttledCpCode` (_object_):
    With `useThrottledCpCode` enabled, this specifies the CP code as
an object:

        "throttledCpCode": {
            "id"   : 12345,
            "name" : "sent to waiting room"
        }

</div>

<div class="option" markdown="1" id="apiPrioritization.useThrottledStatusCode" >

- `useThrottledStatusCode` (_boolean_):
    When enabled, allows you to assign a specific HTTP response code
to a throttled request.

</div>

<div class="option" markdown="1" id="apiPrioritization.throttledStatusCode" >

- `throttledStatusCode` (_number_):
    With `change_response_code` enabled, specifies the HTTP response
code for requests that receive the alternate response.

</div>

<div class="option" markdown="1" id="apiPrioritization.netStorage" >

- `netStorage` (_object_):
    Specify the NetStorage domain that contains the alternate
response. For example:

        "netStorage": {
            "id"                 : "netstorage_id",
            "name"               : "Waiting Room",
            "downloadDomainName" : "example.wait.akamai.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="apiPrioritization.netStoragePath" >

- `netStoragePath` (_string_):
    Specify the full NetStorage path for the alternate response,
including trailing file name.

</div>

<div class="option" markdown="1" id="apiPrioritization.alternateResponseCacheTtl" >

- `alternateResponseCacheTtl` (_number within 5-30 range_):
    Specifies the alternate response's time to live in the cache, `5`
minutes by default.

</div>

</div>

<div class="feature" data-feature="applicationLoadBalancer" markdown="1">

## applicationLoadBalancer

__Property Manager name__:
[Application Load Balancer Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0017)

Enables the
Application Load Balancer Cloudlet, which automates load balancing
based on configurable criteria. To configure this behavior, use either
the Cloudlets Policy Manager or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html)
to set up a policy.

__Options__:

<div class="option" markdown="1" id="applicationLoadBalancer.enabled" >

- `enabled` (_boolean_):
    Activates the Application Load Balancer Cloudlet.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique
numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.label" >

- `label` (_string_):
    A
label to distinguish this Application Load Balancer policy from any
others within the same property.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieType" >

- `stickinessCookieType` (_enum string_):
    Determines how a cookie persistently associates the client with a
load-balanced origin.  Specify an overall `DURATION` or a `FIXED_DATE`
for when the cookie expires.  Specify `ON_BROWSER_CLOSE` to limit the
cookie duration to browser sessions, or to when the `ORIGIN_SESSION`
terminates.  (After the cookie expires, the cookie type re-evaluates.)
To preserve the cookie indefinitely, specify `NEVER`.  To dynamically
reassign different load-balanced origins for each request, specify
`NONE`.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessExpirationDate" >

- `stickinessExpirationDate` (_ISO 8601 format date/time string_):
    With `stickinessCookieType` set to `FIXED_DATE`, this specifies
when the cookie expires.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessDuration" >

- `stickinessDuration` (_duration string_):
    With `stickinessCookieType` set to `DURATION`, sets how long it is
before the cookie expires.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessRefresh" >

- `stickinessRefresh` (_boolean_):
    With `stickinessCookieType` set to `DURATION`, enabling this
extends the duration of the cookie with each new request. When
enabled, the `DURATION` thus specifies the latency between requests
that would cause the cookie to expire.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.originCookieName" >

- `originCookieName` (_string_):
    Specifies the name for your session cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.specifyStickinessCookieDomain" >

- `specifyStickinessCookieDomain` (_boolean_):
    Specifies whether to use a cookie domain with the stickiness
cookie, to tell the browser to which domain to send the cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieDomain" >

- `stickinessCookieDomain` (_string_):
    With `specifyStickinessCookieDomain` enabled, specifies the domain
to track the stickiness cookie.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieAutomaticSalt" >

- `stickinessCookieAutomaticSalt` (_boolean_):
    Sets whether to assign a _salt_ value automatically to the cookie
to prevent manipulation by the user. You should not enable this if
sharing the population cookie across more than one property.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSalt" >

- `stickinessCookieSalt` (_string_):
    With `stickinessCookieAutomaticSalt` disabled, specifies the
stickiness cookie's salt value. Use this option to share the cookie
across many properties.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSetHttpOnlyFlag" >

- `stickinessCookieSetHttpOnlyFlag` (_boolean_):
    Ensures the cookie is transmitted only over HTTP.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.stickinessCookieSetSecureFlag" >

- `stickinessCookieSetSecureFlag` (_boolean_):
    Deploys the stickiness cookie as secure.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownNetStorage" >

- `allDownNetStorage` (_object_):
    Specifies a NetStorage account for a static maintenance page as a
fallback when no origins are available. This example shows the
object's structure:

        "allDownNetStorage": {
            "id"                 : "uniq_id",
            "name"               : "Download Area",
            "downloadDomainName" : "download.example.akamai.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownNetStorageFile" >

- `allDownNetStorageFile` (_string_):
    Specifies the fallback maintenance page's filename, expressed as a
full path from the root of the NetStorage server.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allDownStatusCode" >

- `allDownStatusCode` (_string_):
    Specifies the HTTP response code when all load-balancing origins
are unavailable.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverStatusCodes" >

- `failoverStatusCodes` (_array of string values_):
    Specifies a set of HTTP status codes that signal a failure on the
origin, in which case the cookie that binds the client to that origin
is invalidated and the client is rerouted to another available
origin.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverMode" >

- `failoverMode` (_enum string_):
    Determines what to do if an origin fails. If set to `AUTOMATIC`,
automatically determines which origin in the policy to try next.  If
set to `MANUAL`, you define a sequence of failover origins.  (If
failover runs out of origins, requests are sent to NetStorage.)
Setting `DISABLED` turns off failover, but maintains origin stickiness
even when the origin goes down.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverOriginMap" >

- `failoverOriginMap` (_array_):
    With `failoverMode` set to `MANUAL`, this specifies a fixed set of
failover mapping rules.  If the origin identified by `fromOriginId`
fails, requests stuck to that origin retry for each alternate origin
`toOriginIds` specifies, until one succeeds:

        "failoverOriginMap" : [
            {
                "fromOriginId": "origin1",
                "toOriginIds": [ "origin2", "origin3" ]
            }
        ]

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.failoverAttemptsThreshold" >

- `failoverAttemptsThreshold` (_number_):
    Sets the number of failed requests that would trigger the failover
process.

</div>

<div class="option" markdown="1" id="applicationLoadBalancer.allowCachePrefresh" >

- `allowCachePrefresh` (_boolean_):
    When enabled, allows the cache to prefresh.  Only appropriate if
all origins serve the same content for the same URL.

</div>

</div>

<div class="feature" data-feature="audienceSegmentation" markdown="1">

## audienceSegmentation

__Property Manager name__:
[Audience Segmentation Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0018)

Allows you to divide
your users into different segments based on a persistent cookie. You
can configure rules using either the Cloudlets Policy Manager
application or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).

__Options__:

<div class="option" markdown="1" id="audienceSegmentation.enabled" >

- `enabled` (_boolean_):
    Enables the Audience Segmentation cloudlet feature.

</div>

<div class="option" markdown="1" id="audienceSegmentation.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="audienceSegmentation.label" >

- `label` (_string_):
    Specifies a suffix to append to the cookie name. This helps
distinguish this audience segmentation policy from any others within
the same property.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingMethod" >

- `segmentTrackingMethod` (_enum string_):
    Specifies the method to pass segment information to the origin.
The Cloudlet passes the rule applied to a given request either
`IN_COOKIE_HEADER`, `IN_QUERY_PARAM`, `IN_CUSTOM_HEADER`, or the
default, `NONE`.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingQueryParam" >

- `segmentTrackingQueryParam` (_string_):
    With `segmentTrackingMethod` set to `IN_QUERY_PARAM`, this query
parameter specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingCookieName" >

- `segmentTrackingCookieName` (_string_):
    With `segmentTrackingMethod` set to `IN_COOKIE_HEADER`, this
cookie name specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.segmentTrackingCustomHeader" >

- `segmentTrackingCustomHeader` (_string_):
    With `segmentTrackingMethod` set to `IN_CUSTOM_HEADER`, this
custom HTTP header specifies the name of the segmentation rule.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieType" >

- `populationCookieType` (_enum string_):
    Specifies when the segmentation cookie expires, either
`ON_BROWSER_CLOSE`, `NEVER`, or based on a specific `DURATION`.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationDuration" >

- `populationDuration` (_duration string_):
    With `populationCookieType` set to `DURATION`, specifies the
lifetime of the segmentation cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationRefresh" >

- `populationRefresh` (_boolean_):
    If disabled, sets the expiration time only if the cookie is not
yet present in the request.

</div>

<div class="option" markdown="1" id="audienceSegmentation.specifyPopulationCookieDomain" >

- `specifyPopulationCookieDomain` (_boolean_):
    Whether to specify a cookie domain with the population cookie. It
tells the browser to which domain to send the cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieDomain" >

- `populationCookieDomain` (_string_):
    With `specifyPopulationCookieDomain` enabled, specifies the domain
to track the population cookie.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieAutomaticSalt" >

- `populationCookieAutomaticSalt` (_boolean_):
    Whether to assign a _salt_ value automatically to the cookie to
prevent manipulation by the user. You should not enable if sharing the
population cookie across more than one property.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieSalt" >

- `populationCookieSalt` (_string_):
    With `populationCookieAutomaticSalt` disabled, specifies the
cookie's salt value. Use this option to share the cookie across many
properties.

</div>

<div class="option" markdown="1" id="audienceSegmentation.populationCookieIncludeRuleName" >

- `populationCookieIncludeRuleName` (_boolean_):
    When enabled, includes in the session cookie the name of the rule
in which this behavior appears.

</div>

</div>

<div class="feature" data-feature="autoDomainValidation" markdown="1">

## autoDomainValidation

__Property Manager name__:
[Auto Domain Validation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0202)

This behavior allows
standard TLS domain validated certificates to renew automatically.
Apply it after using the
[Certificate Provisioning System](https://learn.akamai.com/en-us/products/core_features/certificate_provisioning_system.html)
to request a certificate for a hostname.  To provision certificates
programmatically, see the
[Certificate Provisioning System API](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html).

This behavior does not affect hostnames that use enhanced TLS
certificates.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="baseDirectory" markdown="1">

## baseDirectory

__Property Manager name__:
[Origin Base Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0203)

Prefix URLs sent to the origin
with a base path.

For example, with an origin of `example.com`, setting the `value` to
`/images` sets the origin's base path to `example.com/images`. Any
request for a `my_pics/home.jpg` file resolves on the origin server to
`example.com/images/my_pics/home.jpg`.

Note that changing the origin's base path also causes a change to the
cache key. Until that resolves, it may cause a traffic spike to your
origin server.

__Options__:

<div class="option" markdown="1" id="baseDirectory.value" >

- `value` (_string; allows [variables](#vf)_):
    Specifies the
base path of content on your origin server. The value must begin and
end with a slash (`/`) character, for example `/parent/child/`.

</div>

</div>

<div class="feature" data-feature="bossBeaconing" markdown="1">

## bossBeaconing

__Property Manager name__:
[Diagnostic data beacons](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9066)

Triggers diagnostic data
beacons for use with BOSS, Akamai's monitoring and diagnostics
system.

__Options__:

<div class="option" markdown="1" id="bossBeaconing.enabled" >

- `enabled` (_boolean_):
    Enable
diagnostic data beacons.

</div>

<div class="option" markdown="1" id="bossBeaconing.cpcodes" >

- `cpcodes` (_string_):
    The
space-separated list of CP codes that trigger the beacons. You need to
specify the same set of CP codes within BOSS.

</div>

<div class="option" markdown="1" id="bossBeaconing.requestType" >

- `requestType` (_enum string_):
    Specify
whether to trigger a beacon for `EDGE` requests only, or
`EDGE_MIDGRESS` to include midgress requests.

</div>

<div class="option" markdown="1" id="bossBeaconing.forwardType" >

- `forwardType` (_enum string_):
    Specify
whether to trigger a beacon for internal `MIDGRESS` forwards only,
`ORIGIN` forwards only, or `MIDGRESS_ORIGIN` for both.

</div>

<div class="option" markdown="1" id="bossBeaconing.samplingFrequency" >

- `samplingFrequency` (_enum string_):
    Specifies `SAMPLING_FREQ_0_1` as a sampling frequency, or
`SAMPLING_FREQ_0_0` to disable beacons altogether.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalSamplingFrequency" >

- `conditionalSamplingFrequency` (_enum string_):
    Specifies either `CONDITIONAL_SAMPLING_FREQ_0_1`,
`CONDITIONAL_SAMPLING_FREQ_0_2`, `CONDITIONAL_SAMPLING_FREQ_0_3`, or
`CONDITIONAL_SAMPLING_FREQ_0_0` to disable beacons altogether.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalHTTPStatus" >

- `conditionalHTTPStatus` (_array of string values_):
    Specifies the set of response status codes or ranges that trigger
the beacon. You can combine any of these values: `0xx`, `302`, `304`,
`3xx`, `401`, `403`, `404`, `408`, `4xx`, `500`, `503`, `5xx`,
`6xx`.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalErrorPattern" >

- `conditionalErrorPattern` (_string_):
    A space-separated set of error patterns that trigger beacons to
conditional feeds. Each pattern can include wildcards, such as
`*CONNECT* *DENIED*`.

</div>

</div>

<div class="feature" data-feature="breadcrumbs" markdown="1">

## breadcrumbs

__Property Manager name__:
[Breadcrumbs](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5025)

2DO

__Options__:

<div class="option" markdown="1" id="breadcrumbs.enabled" >

- `enabled` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="breadcrumbs.optMode" >

- `optMode` (_boolean_):
    2DO

</div>

</div>

<div class="feature" data-feature="breakConnection" markdown="1">

## breakConnection

__Property Manager name__:
[Break Forward Connection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9078)

A [read-only behavior](#ro)
that simulates an origin connection problem, typically to test an
accompanying [`failAction`](#failaction) policy.

__Options__:

<div class="option" markdown="1" id="breakConnection.enabled" >

- `enabled` (_boolean_):
    Enables the break
connection behavior.

</div>

</div>

<div class="feature" data-feature="brotli" markdown="1">

## brotli

__Property Manager name__:
[Brotli Support](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0123)

When enabled, applies Brotli
compression, converting your origin content to cache on edge
servers.

__Options__:

<div class="option" markdown="1" id="brotli.enabled" >

- `enabled` (_boolean_):
    Enables Brotli
compression.

</div>

</div>

<div class="feature" data-feature="cacheError" markdown="1">

## cacheError

__Property Manager name__:
[Cache HTTP Error Responses](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0020)

Caches the origin's error responses to
decrease server load. Applies for 10 seconds by default to the
following HTTP codes: `204`, `305`, `400`, `404`, `405`, `501`, `502`,
`503`, `504`, and `505`.

__Options__:

<div class="option" markdown="1" id="cacheError.enabled" >

- `enabled` (_boolean_):
    When enabled, activates
the error-caching behavior.

</div>

<div class="option" markdown="1" id="cacheError.ttl" >

- `ttl` (_duration string_):
    Overrides the default
caching duration of `10s`. Note that if set to `0`, it is equivalent
to `no-cache`, which forces revalidation and may cause a traffic
spike. This can be counterproductive when, for example, the origin is
producing an error code of `500`.

</div>

<div class="option" markdown="1" id="cacheError.preserveStale" >

- `preserveStale` (_boolean_):
    When enabled, the
edge server preserves stale cached objects when the origin returns
`400`, `500`, `502`, `503`, and `504` error codes. This avoids
re-fetching and re-caching content after transient errors.

</div>

</div>

<div class="feature" data-feature="cacheId" markdown="1">

## cacheId

__Property Manager name__:
[Cache ID Modification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9050)

Controls which query parameters,
headers, and cookies are included in or excluded from the cache key
identifier.

Note that this behavior executes differently than usual within rule
trees.  Applying a set of `cacheId` behaviors within the same rule
results in a system of forming cache keys that applies independently
to the rule's content.  If any `cacheId` behaviors are present in a
rule, any others specified in parent rules or prior executing sibling
rules no longer apply. Otherwise for any rule that lacks a `cacheId`
behavior, the set of behaviors specified in an ancestor or prior
sibling rule determines how to form cache keys for that content.

__Options__:

<div class="option" markdown="1" id="cacheId.rule" >

- `rule` (_enum string_):
    Specifies how to
modify the cache ID:

    - `INCLUDE_HEADERS` includes specified HTTP headers in the cache ID.
    - `INCLUDE_COOKIES` includes specified cookies in the cache ID.
    - `INCLUDE_ALL_QUERY_PARAMS` includes all query parameters     when forming a cache ID.
    - `INCLUDE_QUERY_PARAMS` includes the specified set of     query parameters when forming a cache ID.
    - `EXCLUDE_QUERY_PARAMS` excludes the specified set of     query parameters when forming a cache ID.
    - `INCLUDE_VARIABLE` includes a specific [user variable](#vf)     in the cache ID.
    - `INCLUDE_URL` includes the full URL, the same as the default     without the `cacheid` behavior.

</div>

<div class="option" markdown="1" id="cacheId.includeValue" >

- `includeValue` (_boolean_):
    When
enabled, includes the value of the specified elements in the cache ID.
Otherwise only their names are included.

</div>

<div class="option" markdown="1" id="cacheId.optional" >

- `optional` (_boolean_):
    When enabled,
requires the behavior's specified elements to be present for content
to cache. When disabled, requests that lack the specified elements are
still cached.  This option only applies when the `type` is
`INCLUDE_COOKIES`, `INCLUDE_QUERY_PARAMS`, `INCLUDE_HEADERS`, or
`EXCLUDE_QUERY_PARAMS`.

</div>

<div class="option" markdown="1" id="cacheId.elements" >

- `elements` (_array of string values_):
    Specifies the
names of the query parameters, cookies, or headers to include or
exclude from the cache ID. This only applies when the `rule` is
`INCLUDE_COOKIES`, `INCLUDE_HEADERS`, `INCLUDE_QUERY_PARAMS`, or
`EXCLUDE_QUERY_PARAMS`.

</div>

<div class="option" markdown="1" id="cacheId.variableName" >

- `variableName` (_string_):
    With `rule`
set to `INCLUDE_VARIABLE`, specifies the name of the variable you want
to include in the cache key.

</div>

</div>

<div class="feature" data-feature="cacheKeyIgnoreCase" markdown="1">

## cacheKeyIgnoreCase

__Property Manager name__:
[Ignore Case In Cache Key](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0021)

By default, cache keys
are generated under the assumption that path and filename components
are case-sensitive, so that `File.html` and `file.html` use separate
cache keys. Enabling this behavior forces URL components whose case
varies to resolve to the same cache key. Enable this behavior if your
origin server is already case-insensitive, such as those based on
Microsoft IIS.

With this behavior enabled, make sure any child rules do not match
case-sensitive path components, or you may apply different settings to
the same cached object.

Note that if already enabled, disabling this behavior potentially
results in new sets of cache keys. Until these new caches are built,
your origin server may experience traffic spikes as requests pass
through. It may also result in _cache pollution_, excess cache space
taken up with redundant content.

If you are using
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
in conjunction with this behavior, enable its __Force Case__ option to
match it, and make sure you name the original files consistently as
either upper- or lowercase.

__Options__:

<div class="option" markdown="1" id="cacheKeyIgnoreCase.enabled" >

- `enabled` (_boolean_):
    When
enabled, ignores case when forming cache keys.

</div>

</div>

<div class="feature" data-feature="cacheKeyQueryParams" markdown="1">

## cacheKeyQueryParams

__Property Manager name__:
[Cache Key Query Parameters](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0022)

By default, cache
keys are formed as URLs with full query strings. This behavior allows
you to consolidate cached objects based on specified sets of query
parameters.

Note also that whenever you apply behavior that generates new cache
keys, your origin server may experience traffic spikes before the new
cache starts to serve out.

__Options__:

<div class="option" markdown="1" id="cacheKeyQueryParams.behavior" >

- `behavior` (_enum string_):
    Configures how sets of query string parameters translate to cache
keys:

    - `IGNORE_ALL` causes query string parameters to be ignored when     forming cache keys.
    - `IGNORE` or `INCLUDE` makes the key depend on the sequence of     values in the `parameters`     field.
    - `INCLUDE_ALL_PRESERVE_ORDER` forms a separate key for the entire     set of query parameters, but sensitive to the order in which they     appear. (For example, `?q=akamai&state=ma` and     `?state=ma&q=akamai` cache separately.)
    - `INCLUDE_ALL_ALPHABETIZE_ORDER` forms keys for the entire set of     parameters, but the order doesn't matter. The examples above     both use the same cache key.

    Be careful when applying `behavior`
    not to ignore any parameters that result in substantially different
    content, as it is _not_ reflected in the cached object.

</div>

<div class="option" markdown="1" id="cacheKeyQueryParams.parameters" >

- `parameters` (_array of string values_):
    With `behavior` set to `INCLUDE` or `IGNORE`, `parameters` specifies
the set of parameter field names to include in or exclude from the
cache key. By default, these match the field names as string
prefixes.

</div>

<div class="option" markdown="1" id="cacheKeyQueryParams.exactMatch" >

- `exactMatch` (_boolean_):
    When enabled, `parameters` must match exactly. Keep disabled to
match string prefixes.

</div>

</div>

<div class="feature" data-feature="cacheKeyRewrite" markdown="1">

## cacheKeyRewrite

__Property Manager name__:
[Cache Key Path Rewrite](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9010)

This [read-only behavior](#ro)
rewrites a default cache key's path. Contact Akamai Professional
Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="cacheKeyRewrite.purgeKey" >

- `purgeKey` (_string_):
    Specifies the new
cache key path as an alphanumeric value.

</div>

</div>

<div class="feature" data-feature="cachePost" markdown="1">

## cachePost

__Property Manager name__:
[Cache POST Responses](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9019)

By default, POST requests are
passed to the origin. This behavior overrides the default, and allows
you to cache POST responses.

__Options__:

<div class="option" markdown="1" id="cachePost.enabled" >

- `enabled` (_boolean_):
    Enables caching of POST
responses.

</div>

<div class="option" markdown="1" id="cachePost.useBody" >

- `useBody` (_enum string_):
    Define how and whether
to use the POST message body as a cache key:

    - `IGNORE` uses only the URL to cache the response.
    - `MD5` adds a string digest of the data as a query parameter to the     cache URL.
    - `QUERY` adds the raw request body as a query parameter to the     cache key, but only if the POST request's `Content-Type` is     `application/x-www-form-urlencoded`. (Use this in conjunction     with [`cacheId`](#cacheid) to define relevant query     parameters.)

</div>

</div>

<div class="feature" data-feature="cacheRedirect" markdown="1">

## cacheRedirect

__Property Manager name__:
[Cache HTTP Redirects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0023)

Caches HTTP 302 redirect
responses. By default, Akamai edge servers cache HTTP 302 redirects
depending on their `Cache-Control` or `Expires` headers. Enabling this
behavior instructs edge servers to cache 302 redirects the same as
they would for HTTP 200 responses.

__Options__:

<div class="option" markdown="1" id="cacheRedirect.enabled" >

- `enabled` (_boolean_):
    Enables the redirect
caching behavior.

</div>

</div>

<div class="feature" data-feature="cacheTagVisible" markdown="1">

## cacheTagVisible

__Property Manager name__:
Cache Tag Visibility

Cache tags are
comma-separated string values you define within an `Edge-Cache-Tag`
header. You can use them to flexibly fast purge tagged segments of
your cached content. You can either define these headers at the
origin server level, or use the
[`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader)
behavior to configure them at the edge.  Apply this behavior to
confirm you're deploying the intended set of cache tags to your
content.

See
[Fast Purge](https://learn.akamai.com/en-us/webhelp/fast-purge/fast-purge/)
for guidance on best practices to deploy cache tags. Use the
[Fast Purge API](https://developer.akamai.com/api/core_features/fast_purge/v3.html)
to purge by cache tag programmatically.

__Options__:

<div class="option" markdown="1" id="cacheTagVisible.behavior" >

- `behavior` (_enum string_):
    Specify
`ALWAYS` to include the `Edge-Cache-Tag` header in all responses.
Specify `NEVER` to match edge servers' default response, stripping out
the header.  Otherwise if you specify `PRAGMA_HEADER`, edge servers
respond with the `Edge-Cache-Tag` header only when you pass in a
`Pragma: akamai-x-get-cache-tags` header as part of the request.

</div>

</div>

<div class="feature" data-feature="caching" markdown="1">

## caching

__Property Manager name__:
[Caching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0024)

Control content caching on edge
servers: whether or not to cache, whether to honor the origin's
caching headers, and for how long to cache.  Note that any `NO_STORE`
or `BYPASS_CACHE` HTTP headers set on the origin's content overrides
this behavior.

__Options__:

<div class="option" markdown="1" id="caching.behavior" >

- `behavior` (_enum string_):
    Specify the caching
option:

    - `NO_STORE` clears the cache and serves from the origin.
    - `BYPASS_CACHE` retains the cache but serves from the origin.
    - Honor the origin's `MAX_AGE` header
    - Honor the origin's `CACHE_CONTROL` header
    - Honor the origin's `EXPIRES` header
    - Honor `CACHE_CONTROL_AND_EXPIRES` the origin's `CACHE_CONTROL`     or `EXPIRES` header, whichever comes last.

    __Note__. New `CACHE_CONTROL_BETA` and
    `CACHE_CONTROL_AND_EXPIRES_BETA` values add support for the
    `s-maxage` response directive specified in
    [RFC 7234](https://tools.ietf.org/html/rfc7234).
    Use these alternative values to instruct a downstream CDN how long
    to cache content.

</div>

<div class="option" markdown="1" id="caching.mustRevalidate" >

- `mustRevalidate` (_boolean_):
    Determines what to
do once the cached content has expired, by which time the Akamai platform
should have re-fetched and validated content from the origin. If
enabled, only allows the re-fetched content to be served. If disabled,
may serve stale content if the origin is unavailable.

</div>

<div class="option" markdown="1" id="caching.ttl" >

- `ttl` (_duration string_):
    The maximum time
content may remain cached. Setting the value to `0` is the same as
setting a `no-cache` header, which forces content to revalidate.

</div>

<div class="option" markdown="1" id="caching.defaultTtl" >

- `defaultTtl` (_duration string_):
    Set the `MAX_AGE` header
for the cached content.

</div>

<div class="option" markdown="1" id="caching.honorPrivateEnabled" >

- `honorPrivateEnabled` (_boolean_):
    With
the `behavior` set to either `CACHE_CONTROL` or
`CACHE_CONTROL_AND_EXPIRES`, enabling this instructs edge servers to
honor `Cache-Control: private` headers.

</div>

<div class="option" markdown="1" id="caching.honorMustrevalidateEnabled" >

- `honorMustrevalidateEnabled` (_boolean_):
    With the `behavior` set to either `CACHE_CONTROL` or
`CACHE_CONTROL_AND_EXPIRES`, enabling this instructs edge servers to
honor `Cache-Control: must-revalidate` headers.

</div>

</div>

<div class="feature" data-feature="centralAuthorization" markdown="1">

## centralAuthorization

__Property Manager name__:
[Centralized Authorization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0025)

Forward client
requests to the origin server for authorization, along with optional
`Set-Cookie` headers, useful when you need to maintain tight access
control. The edge server forwards an `If-Modified-Since` header, to
which the origin needs to respond with a `304` (Not-Modified) HTTP
status when authorization succeeds. If so, the edge server responds to
the client with the cached object, since it does not need to be
re-acquired from the origin.

__Options__:

<div class="option" markdown="1" id="centralAuthorization.enabled" >

- `enabled` (_boolean_):
    Enables the centralized authorization behavior.

</div>

</div>

<div class="feature" data-feature="chaseRedirects" markdown="1">

## chaseRedirects

__Property Manager name__:
[Chase Redirects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9037)

Controls whether the edge server
chases any redirects served from the origin.

__Options__:

<div class="option" markdown="1" id="chaseRedirects.enabled" >

- `enabled` (_boolean_):
    When enabled, allows
edge servers to chase redirects.

</div>

<div class="option" markdown="1" id="chaseRedirects.limit" >

- `limit` (_string_):
    Specifies, as a
string, the maximum number of redirects to follow.

</div>

<div class="option" markdown="1" id="chaseRedirects.serve404" >

- `serve404` (_boolean_):
    Once the
redirect `limit` is reached, enabling this
option serves an HTTP `404` (Not Found) error instead of the last
redirect.

</div>

</div>

<div class="feature" data-feature="clientCharacteristics" markdown="1">

## clientCharacteristics

__Property Manager name__:
[Client Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0026)

Specifies
characteristics of the client ecosystem. Akamai uses this information
to optimize your metadata configuration, which may result in better
end-user performance.

See also [`originCharacteristics`](#origincharacteristics) and
various product-specific behaviors whose names are prefixed
_contentCharacteristics_.

__Options__:

<div class="option" markdown="1" id="clientCharacteristics.country" >

- `country` (_enum string_):
    Specifies the client request's geographic region, or `UNKNOWN` to
defer any optimizations based on geography. Possible global regions
are `GLOBAL`, `GLOBAL_ASIA_CENTRIC`, `GLOBAL_EU_CENTRIC`, or
`GLOBAL_US_CENTRIC`. More specific regions include `ASIA_PACIFIC`,
`AUSTRALIA`, `EUROPE`, `GERMANY`, `INDIA`, `ITALY`, `JAPAN`,
`NORDICS`, `NORTH_AMERICA`, `SOUTH_AMERICA`, `TAIWAN`, or
`UNITED_KINGDOM`. Specify `OTHER` as a fallback value.

</div>

</div>

<div class="feature" data-feature="constructResponse" markdown="1">

## constructResponse

__Property Manager name__:
[Construct Response](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0028)

A [read-only behavior](#ro)
that constructs an HTTP response, complete with HTTP status code and
body, to serve from the edge independently of your origin. Contact
Akamai Professional Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="constructResponse.enabled" >

- `enabled` (_boolean_):
    When
enabled, serves the custom response.

</div>

<div class="option" markdown="1" id="constructResponse.body" >

- `body` (_string; allows [variables](#vf)_):
    HTML
response of up to 2000 characters to send to the end-user client.

</div>

<div class="option" markdown="1" id="constructResponse.responseCode" >

- `responseCode` (_numeric enum_):
    The HTTP response code to send to the end-user client, either `200`,
`401`, `403`, `404`, `405`, `500`, `501`, `502`, `503`, or `504`.

</div>

<div class="option" markdown="1" id="constructResponse.forceEviction" >

- `forceEviction` (_boolean_):
    When enabled, removes the underlying object from the cache, since it
is not being served.

</div>

</div>

<div class="feature" data-feature="contentCharacteristics" markdown="1">

## contentCharacteristics

__Property Manager name__:
[Content Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0029)

Specifies
characteristics of the delivered content. Akamai uses this information
to optimize your metadata configuration, which may result in better
origin offload and end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristics.objectSize" >

- `objectSize` (_enum string_):
    Optimize based on the size of the object retrieved from the origin,
either `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, or
`UNKNOWN` to defer this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristics.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristics.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristics.contentType" >

- `contentType` (_enum string_):
    Optimize based on the type of content, either `SOFTWARE`, `IMAGES`,
`WEB_OBJECTS` (generally, media delivered for websites),
`USER_GENERATED` (generally, user-generated media), `OTHER_OBJECTS`
for content that doesn't fall under any of these categories, or
`UNKNOWN`, to defer this optimization.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsAMD" markdown="1">

## contentCharacteristicsAMD

__Property Manager name__:
[Content Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0029)

Specifies
characteristics of the delivered content. Akamai uses this information
to optimize your metadata configuration, which may result in better
origin offload and end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsAMD.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.  Specify `OTHER` to customize the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.contentType" >

- `contentType` (_enum string_):
    Optimize based on the quality of media content, either `SD`
(standard definition), `HD` (high definition), `ULTRA_HD`, `OTHER` for
more than one level of quality, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.  Specify `OTHER` to customize
the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.hls" >

- `hls` (_boolean_):
    Enable delivery of HLS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationHLS" >

- `segmentDurationHLS` (_enum string_):
    With the `hls` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.  Specify `OTHER` to customize the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationHLSCustom" >

- `segmentDurationHLSCustom` (_number_):
    With `segmentDurationHLS` set to `OTHER`, customizes the number of
seconds for the segment.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentSizeHLS" >

- `segmentSizeHLS` (_enum string_):
    With the `hls` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.hds" >

- `hds` (_boolean_):
    Enable delivery of HDS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationHDS" >

- `segmentDurationHDS` (_enum string_):
    With the `hds` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.  Specify `OTHER` to customize the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationHDSCustom" >

- `segmentDurationHDSCustom` (_number_):
    With `segmentDurationHDS` set to `OTHER`, customizes the number of
seconds for the fragment.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentSizeHDS" >

- `segmentSizeHDS` (_enum string_):
    With the `hds` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.dash" >

- `dash` (_boolean_):
    Enable delivery of DASH media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationDASH" >

- `segmentDurationDASH` (_enum string_):
    With the `dash` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.  Specify `OTHER` to customize the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationDASHCustom" >

- `segmentDurationDASHCustom` (_number_):
    With `segmentDurationDASH` set to `OTHER`, customizes the number
of seconds for the segment.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentSizeDASH" >

- `segmentSizeDASH` (_enum string_):
    With the `dash` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.smooth" >

- `smooth` (_boolean_):
    Enable delivery of Smooth media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationSmooth" >

- `segmentDurationSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.  Specify `OTHER` to customize the value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentDurationSmoothCustom" >

- `segmentDurationSmoothCustom` (_number_):
    With `segmentDurationSmooth` set to `OTHER`, customizes the number
of seconds for the fragment.

</div>

<div class="option" markdown="1" id="contentCharacteristicsAMD.segmentSizeSmooth" >

- `segmentSizeSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsDD" markdown="1">

## contentCharacteristicsDD

__Property Manager name__:
[Content Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0029)

Specifies
characteristics of the delivered content. Akamai uses this information
to optimize your metadata configuration, which may result in better
origin offload and end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsDD.objectSize" >

- `objectSize` (_enum string_):
    Optimize based on the size of the object retrieved from the origin,
either `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`,
`GREATER_THAN_100MB`, or `UNKNOWN` to defer this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.
Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.contentType" >

- `contentType` (_enum string_):
    Optimize based on the type of content, either `VIDEO`, `SOFTWARE`,
`SOFTWARE_PATCH`, `GAME`, `GAME_PATCH`, `OTHER_DOWNLOADS`, or
`UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.optimizeOption" >

- `optimizeOption` (_boolean_):
    When enabled, optimizes the delivery throughput and download times
for large files.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsWsdLargeFile" markdown="1">

## contentCharacteristicsWsdLargeFile

__Property Manager name__:
[Content Characteristics - Large File](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5010)

Specifies characteristics of the delivered content, specifically
targeted to delivering large files. Akamai uses this information to
optimize your metadata configuration, which may result in better
origin offload and end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsWsdLargeFile.objectSize" >

- `objectSize` (_enum string_):
    Optimize based on the size of the object retrieved from the
origin, either `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`,
`TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLargeFile.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLargeFile.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLargeFile.contentType" >

- `contentType` (_enum string_):
    Optimize based on the type of content, either `VIDEO`, `SOFTWARE`,
`SOFTWARE_PATCH`, `GAME`, `GAME_PATCH`, `OTHER_DOWNLOADS`, or
`UNKNOWN` to defer this optimization.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsWsdLive" markdown="1">

## contentCharacteristicsWsdLive

__Property Manager name__:
[Content Characteristics - Streaming Video Live](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9056)

Specifies
characteristics of the delivered content, specifically targeted to
delivering live video. Akamai uses this information to optimize your
metadata configuration, which may result in better origin offload and
end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.contentType" >

- `contentType` (_enum string_):
    Optimize based on the quality of media content, either `SD`
(standard definition), `HD` (high definition), `ULTRA_HD`, `OTHER` for
more than one level of quality, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.hls" >

- `hls` (_boolean_):
    Enable delivery of HLS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentDurationHLS" >

- `segmentDurationHLS` (_enum string_):
    With the `hls` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentSizeHLS" >

- `segmentSizeHLS` (_enum string_):
    With the `hls` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.hds" >

- `hds` (_boolean_):
    Enable delivery of HDS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentDurationHDS" >

- `segmentDurationHDS` (_enum string_):
    With the `hds` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentSizeHDS" >

- `segmentSizeHDS` (_enum string_):
    With the `hds` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.dash" >

- `dash` (_boolean_):
    Enable delivery of DASH media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentDurationDASH" >

- `segmentDurationDASH` (_enum string_):
    With the `dash` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentSizeDASH" >

- `segmentSizeDASH` (_enum string_):
    With the `dash` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.smooth" >

- `smooth` (_boolean_):
    Enable delivery of Smooth media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentDurationSmooth" >

- `segmentDurationSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdLive.segmentSizeSmooth" >

- `segmentSizeSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsWsdVod" markdown="1">

## contentCharacteristicsWsdVod

__Property Manager name__:
[Content Characteristics - Streaming Video On-demand](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5009)

Specifies
characteristics of the delivered content, specifically targeted to
delivering on-demand video. Akamai uses this information to optimize
your metadata configuration, which may result in better origin offload
and end-user performance.

Along with other behaviors whose names are prefixed
_contentCharacteristics_, this behavior is customized for a specific
product set.  Use PAPI's
[List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors)
operation to determine the set available to you. See also the
related [`clientCharacteristics`](#clientcharacteristics) and
[`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.catalogSize" >

- `catalogSize` (_enum string_):
    Optimize based on the total size of the content library delivered,
either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE`
(1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer
this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.contentType" >

- `contentType` (_enum string_):
    Optimize based on the quality of media content, either `SD`
(standard definition), `HD` (high definition), `ULTRA_HD`, `OTHER` for
more than one level of quality, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.popularityDistribution" >

- `popularityDistribution` (_enum string_):
    Optimize based on the content's expected popularity, either
`ALL_POPULAR` for a high volume of requests over a short period,
`LONG_TAIL` for a low volume of requests over a long period, or
`UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.hls" >

- `hls` (_boolean_):
    Enable delivery of HLS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationHLS" >

- `segmentDurationHLS` (_enum string_):
    With the `hls` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeHLS" >

- `segmentSizeHLS` (_enum string_):
    With the `hls` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.hds" >

- `hds` (_boolean_):
    Enable delivery of HDS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationHDS" >

- `segmentDurationHDS` (_enum string_):
    With the `hds` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeHDS" >

- `segmentSizeHDS` (_enum string_):
    With the `hds` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.dash" >

- `dash` (_boolean_):
    Enable delivery of DASH media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationDASH" >

- `segmentDurationDASH` (_enum string_):
    With the `dash` option enabled, specifies the duration of
individual segments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeDASH" >

- `segmentSizeDASH` (_enum string_):
    With the `dash` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.smooth" >

- `smooth` (_boolean_):
    Enable delivery of Smooth media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationSmooth" >

- `segmentDurationSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the duration of
individual fragments, either `SEGMENT_DURATION_2S`,
`SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`,
or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeSmooth" >

- `segmentSizeSmooth` (_enum string_):
    With the `smooth` option enabled, specifies the size of the media
object retrieved from the origin, either: `LESS_THAN_1MB`,
`ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER`
for sizes that straddle these ranges, or `UNKNOWN` to defer this
optimization.

</div>

</div>

<div class="feature" data-feature="contentTargetingProtection" markdown="1">

## contentTargetingProtection

__Property Manager name__:
[Content Targeting - Protection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5003)

Content
Targeting is based on
[EdgeScape](https://developer.akamai.com/edgescape), Akamai's
location-based access control system.  You can use it to allow or deny
access to a set of geographic regions or IP addresses.

__Options__:

<div class="option" markdown="1" id="contentTargetingProtection.enabled" >

- `enabled` (_boolean_):
    Enables the Content Targeting feature.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableGeoProtection" >

- `enableGeoProtection` (_boolean_):
    When enabled, verifies IP addresses are unique to specific
geographic regions.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.geoProtectionMode" >

- `geoProtectionMode` (_enum string_):
    With `enableGeoProtection` enabled, specifies whether to `ALLOW` or
`DENY` requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.countries" >

- `countries` (_array of string values_):
    With `enableGeoProtection` enabled, specifies a set of
two-character ISO 3166 country codes from which to allow or deny
traffic. See
[EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp)
for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.regions" >

- `regions` (_array of string values_):
    With `enableGeoProtection` enabled, specifies a set of ISO 3166-2
regional codes from which to allow or deny traffic. See
[EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp)
for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.dmas" >

- `dmas` (_array of string values_):
    With `enableGeoProtection` enabled, specifies the set of Designated
Market Area codes from which to allow or deny traffic.  See
[EdgeScape Data Codes](https://control.akamai.com/portal/content/akaServiceSupport/edgescape/shared/ES_datacodes.jsp)
for a list.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.overrideIPAddresses" >

- `overrideIPAddresses` (_array of string values_):
    With `enableGeoProtection` enabled, specify a set of IP addresses
or CIDR blocks that exceptions to the set of included or excluded
areas.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableGeoRedirectOnDeny" >

- `enableGeoRedirectOnDeny` (_boolean_):
    When enabled, redirects denied requests rather than responding
with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.geoRedirectUrl" >

- `geoRedirectUrl` (_string_):
    With `enableGeoRedirectOnDeny` enabled, this specifies the full
URL to the redirect page for denied requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableIPProtection" >

- `enableIPProtection` (_boolean_):
    When enabled, allows you to control access to your content from
specific sets of IP addresses and CIDR blocks.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipProtectionMode" >

- `ipProtectionMode` (_enum string_):
    With `enableIPProtection` enabled, specifies whether to `ALLOW` or
`DENY` requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipAddresses" >

- `ipAddresses` (_array of string values_):
    With `enableIPProtection` enabled, specify a set of IP addresses
or CIDR blocks to allow or deny.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableIPRedirectOnDeny" >

- `enableIPRedirectOnDeny` (_boolean_):
    When enabled, redirects denied requests rather than responding
with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.ipRedirectUrl" >

- `ipRedirectUrl` (_string_):
    With `enableIPRedirectOnDeny` enabled, this specifies the full URL
to the redirect page for denied requests.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableReferrerProtection" >

- `enableReferrerProtection` (_boolean_):
    When enabled, allows you allow traffic from certain referring
websites, and disallow traffic from unauthorized sites that hijack
those links.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerProtectionMode" >

- `referrerProtectionMode` (_enum string_):
    With `enableReferrerProtection` enabled, specify whether to
`ALLOW` or `DENY` traffic from specified domains.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerDomains" >

- `referrerDomains` (_array of string values_):
    With `enableReferrerProtection` enabled, specifies the set of
domains from which to allow or deny traffic.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.enableReferrerRedirectOnDeny" >

- `enableReferrerRedirectOnDeny` (_boolean_):
    When enabled, redirects denied requests rather than responding
with an error code.

</div>

<div class="option" markdown="1" id="contentTargetingProtection.referrerRedirectUrl" >

- `referrerRedirectUrl` (_string_):
    With `enableReferrerRedirectOnDeny` enabled, this specifies the
full URL to the redirect page for denied requests.

</div>

</div>

<div class="feature" data-feature="corsSupport" markdown="1">

## corsSupport

__Property Manager name__:
[](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_7000)

2DO.

__Options__:

<div class="option" markdown="1" id="corsSupport.enabled" >

- `enabled` (_boolean_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.allowOrigins" >

- `allowOrigins` (_enum string_):
    2DO:
`ANY`, `SPECIFIED`.

</div>

<div class="option" markdown="1" id="corsSupport.origins" >

- `origins` (_array of string values_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.allowCredentials" >

- `allowCredentials` (_boolean_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.allowHeaders" >

- `allowHeaders` (_enum string_):
    2DO:
`ANY`, `SPECIFIED`.

</div>

<div class="option" markdown="1" id="corsSupport.headers" >

- `headers` (_array of string values_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.methods" >

- `methods` (_array of string values_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.exposeHeaders" >

- `exposeHeaders` (_array of string values; allows [variables](#vf)_):
    2DO.

</div>

<div class="option" markdown="1" id="corsSupport.preflightMaxAge" >

- `preflightMaxAge` (_duration string_):
    2DO.

</div>

</div>

<div class="feature" data-feature="cpCode" markdown="1">

## cpCode

__Property Manager name__:
[Content Provider Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0030)

Content Provider Codes (CP codes)
allow you to distinguish various reporting and billing segments. You
receive a CP code when purchasing Akamai service, and you need it to
access properties. This behavior allows you to apply any valid CP
code, including additional ones you may request from Akamai
Professional Services. For a CP code to be valid, it must belong to
the same contract and be associated with the same product as the
property, and the group must have access to it.

__Options__:

<div class="option" markdown="1" id="cpCode.value" >

- `value` (_object_):
    Specifies a
`value` object, which includes an `id` key and a descriptive `name`:

        "value": {
            "id"   : 12345,
            "name" : "my cpcode"
        }

</div>

</div>

<div class="feature" data-feature="customBehavior" markdown="1">

## customBehavior

__Property Manager name__:
[Custom Behavior](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0031)

Allows you to insert a
customized XML metadata behavior into any property's rule tree.  Talk
to your Akamai representative to implement the customized behavior.
Once it's ready, run PAPI's
[List custom behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#getcustombehaviors)
operation, then apply the relevant `behaviorId` value from the
response within the current `customBehavior`.
See
[Custom behaviors and overrides](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#custombehaviors)
for guidance on custom metadata behaviors.

__Options__:

<div class="option" markdown="1" id="customBehavior.behaviorId" >

- `behaviorId` (_string_):
    The
unique identifier for the predefined custom behavior you want to
insert into the current rule.

</div>

</div>

<div class="feature" data-feature="datastream" markdown="1">

## datastream

__Property Manager name__:
[DataStream](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9005)

The
[DataStream](https://learn.akamai.com/en-us/products/web_performance/datastream.html)
reporting service provides real-time logs on application activity,
including aggregated metrics on complete request and response cycles
and origin response times.  Apply this behavior to report on this set
of traffic.  Use the
[DataStream API](https://developer.akamai.com/api/web_performance/datastream/v1.html)
to aggregate the data.

__Options__:

<div class="option" markdown="1" id="datastream.streamType" >

- `streamType` (_enum string_):
    2DO:
`BEACON`, `BEACON_AND_LOG`, `LOG`

</div>

<div class="option" markdown="1" id="datastream.enabled" >

- `enabled` (_boolean_):
    Enables
DataStream reporting.

</div>

<div class="option" markdown="1" id="datastream.datastreamIds" >

- `datastreamIds` (_string_):
    A set of
dash-separated DataStream ID values to limit the scope of reported
data. By default, all active streams report. Use the DataStream
application to gather stream ID values that apply to this property
configuration. Specifying IDs for any streams that don't apply to this
property has no effect, and results in no data reported.

</div>

<div class="option" markdown="1" id="datastream.logEnabled" >

- `logEnabled` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="datastream.logStreamName" >

- `logStreamName` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="datastream.samplingPercentage" >

- `samplingPercentage` (_number_):
    2DO

</div>

</div>

<div class="feature" data-feature="dcp" markdown="1">

## dcp

__Property Manager name__:
[IoT Edge Connect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9024)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
(The
[IoT Edge Connect API](https://developer.akamai.com/api/web_performance/iot_edge_connect/v1.html)
allows programmatic access.)
This behavior allows you to select previously reserved namespaces and
set the protocols for users to publish and receive messages within
these namespaces.  Use the
[`verifyJsonWebTokenForDcp`](#verifyjsonwebtokenfordcp) behavior to
control access.

__Options__:

<div class="option" markdown="1" id="dcp.enabled" >

- `enabled` (_boolean_):
    Enables IoT Edge
Connect.

</div>

<div class="option" markdown="1" id="dcp.namespaceId" >

- `namespaceId` (_string_):
    Specifies the
globally reserved name for a specific configuration. It includes
authorization rules over publishing and subscribing to logical
categories known as _topics_. This provides a root path for all topics
defined within a namespace configuration.  You can use the
[IoT Edge Connect API](https://developer.akamai.com/api/web_performance/iot_edge_connect/v1.html)
to configure access control lists for your namespace configuration.

</div>

<div class="option" markdown="1" id="dcp.tlsenabled" >

- `tlsenabled` (_boolean_):
    When enabled, you
can publish and receive messages over a secured MQTT connection on
port 8883.

</div>

<div class="option" markdown="1" id="dcp.wsenabled" >

- `wsenabled` (_boolean_):
    When enabled, you
can publish and receive messages through a secured MQTT connection
over WebSockets on port 443.

</div>

<div class="option" markdown="1" id="dcp.gwenabled" >

- `gwenabled` (_boolean_):
    When enabled, you
can publish and receive messages over a secured HTTP connection on
port 443.

</div>

</div>

<div class="feature" data-feature="dcpAuthHMACTransformation" markdown="1">

## dcpAuthHMACTransformation

__Property Manager name__:
[Variable Hash Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9061)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
In conjunction with
[`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior
affects how clients can authenticate themselves to edge servers, and
which groups within namespaces are authorized to access topics.
It transforms a source string value extracted from the client
certificate and stored as a variable, then generates a hash value
based on the selected algorithm, for use in authenticating the client request.

Note that you can apply this hash transformation, or either of the
[`dcpAuthRegexTransformation`](#dcpauthregextransformation) or
[`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation)
behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthHMACTransformation.hashConversionAlgorithm" >

- `hashConversionAlgorithm` (_enum string_):
    Choose either `MD5`, `SHA256`, or `SHA384` hash algorithms.

</div>

<div class="option" markdown="1" id="dcpAuthHMACTransformation.hashConversionKey" >

- `hashConversionKey` (_string_):
    Specifies the key to generate the hash, ideally a long random
string to ensure adequate security.

</div>

</div>

<div class="feature" data-feature="dcpAuthRegexTransformation" markdown="1">

## dcpAuthRegexTransformation

__Property Manager name__:
[Variable Regex Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9060)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
In conjunction with
[`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior
affects how clients can authenticate themselves to edge servers, and
which groups within namespaces are authorized to access topics.
It transforms a source string value extracted from the client
certificate and stored as a variable,
then transforms the string based on a regular expression search
pattern, for use in authenticating the client request.

Note that you can apply this regular expression transformation, or
either of the
[`dcpAuthHMACTransformation`](#dcpauthhmactransformation) or
[`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation)
behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthRegexTransformation.regexPattern" >

- `regexPattern` (_string_):
    Specifies a Perl-compatible regular expression with a single
grouping to capture the text.  For example, a value of `^.(.{0,10})`
omits the first character, but then captures up to 10 characters after
that. If the regular expression does not capture a substring,
authentication may fail.

</div>

</div>

<div class="feature" data-feature="dcpAuthSubstringTransformation" markdown="1">

## dcpAuthSubstringTransformation

__Property Manager name__:
[Variable Substring Transformation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9074)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
In conjunction with
[`dcpAuthVariableExtractor`](#dcpauthvariableextractor), this behavior
affects how clients can authenticate themselves to edge servers, and
which groups within namespaces are authorized to access topics.
It transforms a source string value extracted from the client
certificate and stored as a variable, then extracts a substring, for
use in authenticating the client request.

Note that you can apply this substring transformation, or either of
the [`dcpAuthHMACTransformation`](#dcpauthhmactransformation) or
[`dcpAuthRegexTransformation`](#dcpauthregextransformation)
behaviors.

__Options__:

<div class="option" markdown="1" id="dcpAuthSubstringTransformation.substringStart" >

- `substringStart` (_string_):
    The zero-based index offset of the first character to extract.
If the index is out of bound from the string's length,
authentication may fail.

</div>

<div class="option" markdown="1" id="dcpAuthSubstringTransformation.substringEnd" >

- `substringEnd` (_string_):
    The zero-based index offset of the last character to extract,
where `-1` selects the remainder of the string.
If the index is out of bound from the string's length,
authentication may fail.

</div>

</div>

<div class="feature" data-feature="dcpAuthVariableExtractor" markdown="1">

## dcpAuthVariableExtractor

__Property Manager name__:
[Mutual Authentication](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9070)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
This behavior affects how clients can authenticate themselves to edge
servers,
and which groups within namespaces are authorized to access topics.
When enabled, this behavior allows end users to authenticate their
requests with valid client certificates.
Values for client identifiers or access authorization groups are
required to make a request valid.

After extracting values from client certificates and storing them as
variables, you can then apply any of these behaviors to transform the
value: [`dcpAuthHMACTransformation`](#dcpauthhmactransformation),
[`dcpAuthRegexTransformation`](#dcpauthregextransformation), or
[`dcpAuthSubstringTransformation`](#dcpauthsubstringtransformation).

__Options__:

<div class="option" markdown="1" id="dcpAuthVariableExtractor.certificateField" >

- `certificateField` (_enum string_):
    Choose the field from the certificate to extract from, either
`FINGERPRINT_DYN`, `FINGERPRINT_MD5`, `FINGERPRINT_SHA1`,
`SUBJECT_DN`, `SERIAL`, `V3_NETSCAPE_COMMENT`, or
`V3_SUBJECT_ALT_NAME`.

</div>

<div class="option" markdown="1" id="dcpAuthVariableExtractor.dcpMutualAuthProcessingVariableId" >

- `dcpMutualAuthProcessingVariableId` (_enum string_):
    Store the value either as `VAR_DCP_CLIENT_ID` or
`VAR_DCP_AUTH_GROUP`.

</div>

</div>

<div class="feature" data-feature="dcpDefaultAuthzGroups" markdown="1">

## dcpDefaultAuthzGroups

__Property Manager name__:
[Default Authorization Groups](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9067)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
This behavior defines a set of default authorization groups to add to
each request the property configuration controls.  These groups have
access regardless of the authentication method you use, either JWT
using the [`verifyJsonWebTokenForDcp`](#verifyjsonwebtokenfordcp)
behavior, or mutual authentication using the
[`dcpAuthVariableExtractor`](#dcpauthvariableextractor) behavior to
control where authorization groups are extracted from within
certificates.

__Options__:

<div class="option" markdown="1" id="dcpDefaultAuthzGroups.groupNames" >

- `groupNames` (_array of string values_):
    Specifies the set of authorization groups to assign to all
connecting devices.

</div>

</div>

<div class="feature" data-feature="dcpDevRelations" markdown="1">

## dcpDevRelations

__Property Manager name__:
[IoT Edge Connect Dev Relations](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9012)

The
[Internet of Things: Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html)
product allows connected users and devices to communicate on a
publish-subscribe basis within reserved namespaces.
This behavior allows Akamai-external clients to use developer test
accounts in a shared environment. In conjunction with
[`verifyJsonWebTokenForDcp`](#verifyjsonwebtokenfordcp), this behavior
allows you to use your own JWTs in your requests, or those generated
by Akamai. It lets you either enable the default JWT server for your
test configuration by setting the authentication endpoint to a default
path, or specify custom settings for your JWT server and the
authentication endpoint.

__Options__:

<div class="option" markdown="1" id="dcpDevRelations.enabled" >

- `enabled` (_boolean_):
    Enables
the default JWT server and sets the authentication endpoint to a
default path.

</div>

<div class="option" markdown="1" id="dcpDevRelations.customValues" >

- `customValues` (_boolean_):
    When
enabled, allows you to specify custom JWT server connection values.

</div>

<div class="option" markdown="1" id="dcpDevRelations.hostname" >

- `hostname` (_string_):
    With
`customValues` enabled, specifies the JWT server's hostname.

</div>

<div class="option" markdown="1" id="dcpDevRelations.path" >

- `path` (_string_):
    With
`customValues` enabled, specifies the path to your JWT server's
authentication endpoint. This lets you generate JWTs to sign your
requests.

</div>

</div>

<div class="feature" data-feature="deliveryReceipt" markdown="1">

## deliveryReceipt

__Property Manager name__:
[Cloud Monitor Data Delivery](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9011)

A static behavior that's
required when specifying the
[Cloud Monitor](http://www.akamai.com/html/technology/cloud-monitor.html)
module's ([`edgeConnect`](#edgeconnect)) behavior. You can only apply
this behavior if the property is marked as secure. See
[Secure property requirements](#sf) for guidance.

__Options__:

<div class="option" markdown="1" id="deliveryReceipt.enabled" >

- `enabled` (_read-only string_):
    When `on`,
enables the behavior.

</div>

</div>

<div class="feature" data-feature="denyAccess" markdown="1">

## denyAccess

__Property Manager name__:
[Control Access](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0032)

Assuming a condition in the
rule matches, this denies access to the requested content. For
example, a [`userLocation`](#userlocation) match paired
with the `denyaccess` behavior would deny requests from a specified
part of the world.

By keying on the value of the `reason` option, `denyaccess` behaviors
may override each other when called from nested rules. For example, a
parent rule might deny access to a certain geographic area, citing
`"location"` as the `reason`, but another nested rule can then allow
access for a set of IPs within that area, so long as the `reason`
matches.

__Options__:

<div class="option" markdown="1" id="denyAccess.enabled" >

- `enabled` (_boolean_):
    Denies access
when enabled.

</div>

<div class="option" markdown="1" id="denyAccess.reason" >

- `reason` (_string_):
    Text message
that keys why access is denied. Any subsequent `denyaccess` behaviors
within the rule tree may refer to the same `reason` key to override
the current behavior.

</div>

</div>

<div class="feature" data-feature="denyDirectFailoverAccess" markdown="1">

## denyDirectFailoverAccess

__Property Manager name__:
[Security Failover Protection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9020)

A static
behavior required for all properties that implement a failover under
the Cloud Security Failover product.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="deviceCharacteristicCacheId" markdown="1">

## deviceCharacteristicCacheId

__Property Manager name__:
[Device Characterization - Define Cached Content](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0033)

By default,
source URLs serve as cache IDs on edge servers. Electronic Data
Capture allows you to specify an additional set of device
characteristics to generate separate cache keys. Use this in
conjunction with the
[`deviceCharacteristicHeader`](#devicecharacteristicheader)
behavior.

__Options__:

<div class="option" markdown="1" id="deviceCharacteristicCacheId.elements" >

- `elements` (_array of string values_):
    Specifies a set of information about the device with which to
generate a separate cache key, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ACCEPT_THIRD_PARTY_COOKIE
AJAX_PREFERRED_GEOLOC_API
AJAX_SUPPORT_JAVASCRIPT
BRAND_NAME
COOKIE_SUPPORT
DEVICE_OS
DEVICE_OS_VERSION
DUAL_ORIENTATION
FLASH_LITE_VERSION
FULL_FLASH_SUPPORT
GIF_ANIMATED
HTML_PREFERRED_DTD
IS_MOBILE
IS_TABLET
IS_WIRELESS_DEVICE
JPG
MARKETING_NAME
MAX_IMAGE_HEIGHT
MAX_IMAGE_WIDTH
MOBILE_BROWSER
MOBILE_BROWSER_VERSION
MODEL_NAME
PDF_SUPPORT
PHYSICAL_SCREEN_HEIGHT
PHYSICAL_SCREEN_WIDTH
PNG
PREFERRED_MARKUP
RESOLUTION_HEIGHT
RESOLUTION_WIDTH
VIEWPORT_INITIAL_SCALE
VIEWPORT_WIDTH
XHTML_FILE_UPLOAD
XHTML_PREFERRED_CHARSET
XHTML_SUPPORT_LEVEL
XHTML_SUPPORTS_IFRAME
XHTML_SUPPORTS_TABLE_FOR_LAYOUT
XHTML_TABLE_SUPPORT
XHTMLMP_PREFERRED_MIME_TYPE
</pre>

</div>

</div>

<div class="feature" data-feature="deviceCharacteristicHeader" markdown="1">

## deviceCharacteristicHeader

__Property Manager name__:
[Device Characterization - Forward in Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0033)

Sends selected
information about requesting devices to the origin server, in the form
of an `X-Akamai-Device-Characteristics` HTTP header. Use in
conjunction with the
[`deviceCharacteristicCacheId`](#devicecharacteristiccacheid)
behavior.

__Options__:

<div class="option" markdown="1" id="deviceCharacteristicHeader.elements" >

- `elements` (_array of string values_):
    Specifies the set of information about the requesting device to
send to the origin server, any of the following:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ACCEPT_THIRD_PARTY_COOKIE
AJAX_PREFERRED_GEOLOC_API
AJAX_SUPPORT_JAVASCRIPT
BRAND_NAME
COOKIE_SUPPORT
DEVICE_OS
DEVICE_OS_VERSION
DUAL_ORIENTATION
FLASH_LITE_VERSION
FULL_FLASH_SUPPORT
GIF_ANIMATED
HTML_PREFERRED_DTD
IS_MOBILE
IS_TABLET
IS_WIRELESS_DEVICE
JPG
MARKETING_NAME
MAX_IMAGE_HEIGHT
MAX_IMAGE_WIDTH
MOBILE_BROWSER
MOBILE_BROWSER_VERSION
MODEL_NAME
PDF_SUPPORT
PHYSICAL_SCREEN_HEIGHT
PHYSICAL_SCREEN_WIDTH
PNG
PREFERRED_MARKUP
RESOLUTION_HEIGHT
RESOLUTION_WIDTH
VIEWPORT_INITIAL_SCALE
VIEWPORT_WIDTH
XHTML_FILE_UPLOAD
XHTML_PREFERRED_CHARSET
XHTML_SUPPORT_LEVEL
XHTML_SUPPORTS_IFRAME
XHTML_SUPPORTS_TABLE_FOR_LAYOUT
XHTML_TABLE_SUPPORT
XHTMLMP_PREFERRED_MIME_TYPE
</pre>

</div>

</div>

<div class="feature" data-feature="dnsAsyncRefresh" markdown="1">

## dnsAsyncRefresh

__Property Manager name__:
[DNS Asynchronous Refresh](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0112)

Allow an edge server to
use an expired DNS record when forwarding a request to your origin.
The _type A_ DNS record refreshes _after_ content is served to the end
user, so there is no wait for the DNS resolution. Avoid this behavior
if you want to be able to disable a server immediately after its DNS
record expires.

__Options__:

<div class="option" markdown="1" id="dnsAsyncRefresh.enabled" >

- `enabled` (_boolean_):
    When
enabled, allows edge servers to refresh an expired DNS record after
serving content.

</div>

<div class="option" markdown="1" id="dnsAsyncRefresh.timeout" >

- `timeout` (_duration string_):
    Set the
maximum allowed time an expired DNS record may be active.

</div>

</div>

<div class="feature" data-feature="dnsPrefresh" markdown="1">

## dnsPrefresh

__Property Manager name__:
[DNS Prefresh](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0034)

A [read-only behavior](#ro)
that allows edge servers to refresh your origin's DNS record
independently from end-user requests. The _type A_ DNS record
refreshes before the origin's DNS record expires.

__Options__:

<div class="option" markdown="1" id="dnsPrefresh.enabled" >

- `enabled` (_boolean_):
    When enabled,
allows edge servers to refresh DNS records before they expire.

</div>

<div class="option" markdown="1" id="dnsPrefresh.delay" >

- `delay` (_duration string_):
    Specifies the
amount of time following a DNS record's expiration to asynchronously
prefresh it.

</div>

<div class="option" markdown="1" id="dnsPrefresh.timeout" >

- `timeout` (_duration string_):
    Specifies the
amount of time to prefresh a DNS entry if there have been no requests
to the domain name.

</div>

</div>

<div class="feature" data-feature="downgradeProtocol" markdown="1">

## downgradeProtocol

__Property Manager name__:
[Protocol Downgrade](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0035)

Serve static objects to the
end-user client over HTTPS, but fetch them from the origin via HTTP.

__Options__:

<div class="option" markdown="1" id="downgradeProtocol.enabled" >

- `enabled` (_boolean_):
    Enables the
protocol downgrading behavior.

</div>

</div>

<div class="feature" data-feature="downloadCompleteMarker" markdown="1">

## downloadCompleteMarker

__Property Manager name__:
[Download Complete Marker](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0036)

The
[Internet of Things: OTA Updates](https://learn.akamai.com/en-us/webhelp/iot/internet-of-things-over-the-air-user-guide/)
product allows customers to securely distribute firmware to devices
over cellular networks.  Based on match criteria that executes a rule,
this behavior logs requests to the OTA servers as completed in
aggregated and individual reports.

See also the [`downloadNotification`](#downloadnotification) and
[`requestTypeMarker`](#requesttypemarker) behaviors.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="downloadNotification" markdown="1">

## downloadNotification

__Property Manager name__:
[Download Notification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0037)

The
[Internet of Things: OTA Updates](https://learn.akamai.com/en-us/webhelp/iot/internet-of-things-over-the-air-user-guide/)
product allows customers to securely distribute firmware to devices
over cellular networks.
Based on match criteria that executes a rule, this behavior allows
requests to the
[OTA Updates API](https://developer.akamai.com/api/web_performance/iot_ota_updates/v1.html)
for a list of completed downloads to individual vehicles.

See also the [`downloadCompleteMarker`](#downloadcompletemarker)
behavior.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="downstreamCache" markdown="1">

## downstreamCache

__Property Manager name__:
[Downstream Cacheability](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0038)

Specify the caching
instructions the edge server sends to the end user's client or client
proxies. By default, the cache's duration is whichever is less: the
remaining lifetime of the edge cache, or what the origin's header
specifies. If the origin is set to `no-store` or `bypass-cache`, edge
servers send _cache-busting_ headers downstream to prevent downstream
caching.

__Options__:

<div class="option" markdown="1" id="downstreamCache.behavior" >

- `behavior` (_enum string_):
    Specify the
caching instructions the edge server sends to the end user's client.
It accepts the following values:

    - `ALLOW`: The value of `allowBehavior` chooses the caching     method and headers to send to the client.
    - `MUST_REVALIDATE`: This equates to a `Cache-Control: no-cache`     header, which allows caching but forces the client browser to send     an `if-modified-since` request each time it requests the object.
    - `BUST`: Sends cache-busting headers downstream.
    - `TUNNEL_ORIGIN`: This passes `Cache-Control` and `Expires` headers     from the origin to the downstream client.
    - `NONE`: Don't send any caching headers. Allow client browsers to     cache content according to their own default settings.

</div>

<div class="option" markdown="1" id="downstreamCache.allowBehavior" >

- `allowBehavior` (_enum string_):
    Specify how the edge server calculates the downstream cache by
setting the value of the `Expires` header:

    - `FROM_VALUE` sends the value of the edge cache's duration.
    - `FROM_MAX_AGE` sends the `cache:max-age` value applied to the     object, without evaluating the cache's duration.
    - `LESSER` sends the lesser value of what the origin specifies and     the edge cache's remaining duration. This is the default behavior.
    - `GREATER` sends the greater value of what the origin specifies and     the edge cache's remaining duration.
    - `REMAINING_LIFETIME` sends the value of the edge cache's remaining     duration, without comparing it to the origin's headers.
    - `PASS_ORIGIN` sends the value of the origin's header, without     evaluating the edge cache's duration.

</div>

<div class="option" markdown="1" id="downstreamCache.ttl" >

- `ttl` (_duration string_):
    Set the
duration of the cache. Setting the value to `0` equates to a
`no-cache` header that forces revalidation.

</div>

<div class="option" markdown="1" id="downstreamCache.sendHeaders" >

- `sendHeaders` (_enum string_):
    Specifies the HTTP headers to include in the response to the client:

    - `PASS_ORIGIN` sends the same set of `Cache-Control` and `Expires`     headers received from the origin.
    - `CACHE_CONTROL` sends only the origin's `Cache-Control` header.
    - `EXPIRES` sends only the origin's `Expires` header.
    - `CACHE_CONTROL_AND_EXPIRES` sends both `Cache-Control` and `Expires` header.
    - `NONE` strips both headers.

</div>

<div class="option" markdown="1" id="downstreamCache.sendPrivate" >

- `sendPrivate` (_boolean_):
    When
enabled, adds a `Cache-Control: private` header to prevent objects
from being cached in a shared caching proxy.

</div>

</div>

<div class="feature" data-feature="dynamicAdInsertion" markdown="1">

## dynamicAdInsertion

__Property Manager name__:
[Dynamic Ad Insertion](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5024)

2DO

__Options__:

<div class="option" markdown="1" id="dynamicAdInsertion.enableDai" >

- `enableDai` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="dynamicAdInsertion.daiPartner" >

- `daiPartner` (_enum string_):
    2DO: `YOSPACE`

</div>

<div class="option" markdown="1" id="dynamicAdInsertion.daiPolicy" >

- `daiPolicy` (_string_):
    2DO

</div>

</div>

<div class="feature" data-feature="dynamicThroughtputOptimization" markdown="1">

## dynamicThroughtputOptimization

__Property Manager name__:
[Quick Retry](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5015)

Enables
_quick retry_, which detects slow forward throughput while fetching an
object, and attempts a different forward connection path to avoid
congestion. By default, connections under 5 mbps trigger this
behavior.  Contact Akamai Professional Services to override this
threshold.

__Options__:

<div class="option" markdown="1" id="dynamicThroughtputOptimization.enabled" >

- `enabled` (_boolean_):
    Enables the quick retry feature.

</div>

</div>

<div class="feature" data-feature="dynamicWebContent" markdown="1">

## dynamicWebContent

__Property Manager name__:
[Content Characteristics - Dynamic Web Content](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5008)

In conjunction with the
[`subCustomer`](#subcustomer) behavior, this optional behavior allows
you to control how dynamic web content behaves for your subcustomers
using
[Akamai Cloud Embed](https://learn.akamai.com/en-us/products/media_delivery/cloud_embed.html).

__Options__:

<div class="option" markdown="1" id="dynamicWebContent.sureRoute" >

- `sureRoute` (_boolean_):
    Optimizes how subcustomer traffic routes from origin to edge
servers.  See the [`sureRoute`](#sureroute) behavior for more
information.

</div>

<div class="option" markdown="1" id="dynamicWebContent.prefetch" >

- `prefetch` (_boolean_):
    Allows
subcustomer content to prefetch over HTTP/2.

</div>

<div class="option" markdown="1" id="dynamicWebContent.realUserMonitoring" >

- `realUserMonitoring` (_boolean_):
    Allows Real User Monitoring (RUM) to collect performance data for
subcustomer content. See the
[`realUserMonitoring`](#realusermonitoring) behavior for more
information.

</div>

<div class="option" markdown="1" id="dynamicWebContent.imageCompression" >

- `imageCompression` (_boolean_):
    Enables image compression for subcustomer content.

</div>

</div>

<div class="feature" data-feature="edgeConnect" markdown="1">

## edgeConnect

__Property Manager name__:
[Cloud Monitor Instrumentation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9021)

Configures traffic logs for
the
[Cloud Monitor](http://www.akamai.com/html/technology/cloud-monitor.html)
push API.

__Options__:

<div class="option" markdown="1" id="edgeConnect.enabled" >

- `enabled` (_boolean_):
    Enables Cloud
Monitor's log-publishing behavior.

</div>

<div class="option" markdown="1" id="edgeConnect.apiConnector" >

- `apiConnector` (_enum string_):
    Describes the API connector type, either `DEFAULT`, `BMC_APM`, or
`SIEM_JSON`.

</div>

<div class="option" markdown="1" id="edgeConnect.apiDataElements" >

- `apiDataElements` (_array of string values_):
    Specifies the data set to log, any of the following values:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
APM
GEO
HTTP
NETWORK_PERFORMANCE
NETWORK_V1
REQUEST_HEADER
RESPONSE_HEADER
SEC_APP_V2
SEC_RATE_DENY_V2
SEC_RATE_WARN_V2
</pre>

</div>

<div class="option" markdown="1" id="edgeConnect.destinationHostname" >

- `destinationHostname` (_string_):
    Specifies
the target hostname accepting push API requests.

</div>

<div class="option" markdown="1" id="edgeConnect.destinationPath" >

- `destinationPath` (_string_):
    Specifies
the push API's endpoint.

</div>

<div class="option" markdown="1" id="edgeConnect.overrideAggregateSettings" >

- `overrideAggregateSettings` (_boolean_):
    When enabled, overrides default log settings.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateTime" >

- `aggregateTime` (_duration string_):
    With
`overrideAggregateSettings` enabled, specifies how often logs are
generated.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateLines" >

- `aggregateLines` (_string_):
    With
`overrideAggregateSettings` enabled, specifies the maximum number of
lines to include in each log.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateSize" >

- `aggregateSize` (_string_):
    With
`overrideAggregateSettings` enabled, specifies the log's maximum
size.

</div>

</div>

<div class="feature" data-feature="edgeImageConversion" markdown="1">

## edgeImageConversion

__Property Manager name__:
[Image Converter Settings](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9001)

The
[Edge Image Converter](http://www.akamai.com/html/technology/image-converter.html)
offloads various image manipulation tasks to edge servers.  This
behavior specifies various predefined policies to apply.

__Options__:

<div class="option" markdown="1" id="edgeImageConversion.enabled" >

- `enabled` (_boolean_):
    Enables the edge image conversion behavior.

</div>

<div class="option" markdown="1" id="edgeImageConversion.failover" >

- `failover` (_boolean_):
    If the request results in a server error, enabling this forwards it
to the origin.

</div>

<div class="option" markdown="1" id="edgeImageConversion.usePolicy" >

- `usePolicy` (_boolean_):
    Enables a specified set of image conversion policies.

</div>

<div class="option" markdown="1" id="edgeImageConversion.policies" >

- `policies` (_array_):
    With `usePolicy` enabled, specifies commands that when present or
not in the query string release an error code.

</div>

<div class="option" markdown="1" id="edgeImageConversion.policyResponses" >

- `policyResponses` (_numeric enum_):
    Specifies the HTTP error code if any `policies` conditions
match, either `400`, `403`, `404`, or `409`.

</div>

</div>

<div class="feature" data-feature="edgeLoadBalancingAdvanced" markdown="1">

## edgeLoadBalancingAdvanced

__Property Manager name__:
[Edge Load Balancing: Advanced Metadata](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9072)

A [read-only
behavior](#ro) that implements customized
[Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf)
features. Contact Akamai Professional Services for help configuring
it.

__Options__:

<div class="option" markdown="1" id="edgeLoadBalancingAdvanced.description" >

- `description` (_string_):
    A
description of what the `xml` block does.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingAdvanced.xml" >

- `xml` (_string_):
    A block of
Akamai XML metadata.

</div>

</div>

<div class="feature" data-feature="edgeLoadBalancingDataCenter" markdown="1">

## edgeLoadBalancingDataCenter

__Property Manager name__:
[Edge Load Balancing: Data Center](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0039)

The
[Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf)
module allows you to specify groups of data centers that implement
load balancing, session persistence, and real-time dynamic failover.
Enabling ELB routes requests contextually based on location, device,
or network, along with optional rules you specify.

This behavior specifies details about a data center, and must be
paired in the same rule with an
[`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior, which
specifies its origin. An _origin_ is an abstraction that helps group a
logical set of a website or application. It potentially includes
information about many data centers and cloud providers, as well as
many end points or IP addresses for each data center. More than one
data center can thus refer to the same origin.

__Options__:

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.originId" >

- `originId` (_string_):
    Corresponds to the `id` specified by the
[`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior
associated with this data center.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.description" >

- `description` (_string_):
    Provides a description for the ELB data center, for your own
reference.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.hostname" >

- `hostname` (_string_):
    Specifies the data center's hostname.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.cookieName" >

- `cookieName` (_string_):
    If using session persistence, this specifies the value of the
cookie named in the corresponding
[`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior's
`cookie_name` option.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.enableFailover" >

- `enableFailover` (_boolean_):
    When enabled, allows you to specify failover rules.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.ip" >

- `ip` (_string_):
    With `enableFailover` enabled, specifies this data center's IP
address.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingDataCenter.failoverRules" >

- `failoverRules` (_array_):
    With `enableFailover` enabled, provides up to four failover
rules to apply in the specified order. These rules appear as
objects with the following fields:

    - `modify_request` (_boolean_): When enabled, allows you to modify     the request's hostname or path.

    - `override_hostname` (_boolean_): When enabled, overrides the     request's hostname with the `failover_hostname`.

    - `failover_hostname`: The hostname of the data center to fail over     to.

    - `context_root`: Specifies the path to use in the forwarding     request, typically the root (`/`) when failing over to a different     data center, or a full path such as `/static/error.html` when     failing over to an error page.

    - `absolute_path` (_boolean_): If enabled, the path specified by     `context_root` is interpreted as an absolute server path, for     example to reference a site-down page. If disabled, the path is     appended to the request.

</div>

</div>

<div class="feature" data-feature="edgeLoadBalancingOrigin" markdown="1">

## edgeLoadBalancingOrigin

__Property Manager name__:
[Edge Load Balancing: Origin Definition](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0040)

The
[Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf)
module allows you to implement groups of data centers featuring load
balancing, session persistence, and real-time dynamic failover.
Enabling ELB routes requests contextually based on location, device,
or network, along with optional rules you specify.

This behavior specifies the data center's origin, and must be paired
in the same rule with at least one
[`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter)
behavior, which provides details about a particular data center. An
_origin_ is an abstraction that helps group a logical set of a website
or application. It potentially includes information about many data
centers and cloud providers, as well as many end points or IP
addresses for each data center. To specify an ELB origin, you must
have configured an [`origin`](#origin) behavior whose `type` is set to
`elb_origin_group`.

__Options__:

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.id" >

- `id` (_string_):
    Specifies a unique descriptive string for this ELB origin. The value
must match the `origin_id` specified by the
[`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter) behavior
associated with this origin.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.description" >

- `description` (_string_):
    Provides a description for the ELB origin, for your own reference.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.hostname" >

- `hostname` (_string_):
    Specifies the hostname associated with the ELB rule.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.enableSessionPersistence" >

- `enableSessionPersistence` (_boolean_):
    When enabled, allows you to specify a cookie to pin the user's
browser session to one data center. When disabled, ELB's default load
balancing may send users to various data centers within the same
session.

</div>

<div class="option" markdown="1" id="edgeLoadBalancingOrigin.cookieName" >

- `cookieName` (_string_):
    With `enableSessionPersistence` enabled, this specifies the name of
the cookie that marks users' persistent sessions. The accompanying
[`edgeLoadBalancingDataCenter`](#edgeloadbalancingdatacenter)
behavior's `description` option specifies the cookie's value.

</div>

</div>

<div class="feature" data-feature="edgeOriginAuthorization" markdown="1">

## edgeOriginAuthorization

__Property Manager name__:
[Edge Server Identification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0041)

Allows the origin
server to use a cookie to ensure requests from Akamai servers are
genuine.

This behavior requires that you specify the cookie's domain name, so
it is best to deploy within a match of the hostname.  It does not work
properly when the origin server accepts more than one hostname (for
example, using virtual servers) that do not share the same top-level
domain.

__Options__:

<div class="option" markdown="1" id="edgeOriginAuthorization.enabled" >

- `enabled` (_boolean_):
    Enables the cookie-authorization behavior.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.cookieName" >

- `cookieName` (_string_):
    Specifies the name of the cookie to use for authorization.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.value" >

- `value` (_string_):
    Specifies the value of the authorization cookie.

</div>

<div class="option" markdown="1" id="edgeOriginAuthorization.domain" >

- `domain` (_string_):
    Specify the cookie's domain, which must match the top-level domain
of the `Host` header the origin server receives.

</div>

</div>

<div class="feature" data-feature="edgeRedirector" markdown="1">

## edgeRedirector

__Property Manager name__:
[Edge Redirector Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0042)

This behavior enables the
[Edge Redirector Cloudlet](http://www.akamai.com/html/technology/edge-redirector.html)
application, which is designed to help you manage large numbers of
redirects. With cloudlets available on your contract, choose
__Your services__ &rArr; __Edge logic Cloudlets__
to control the Edge Redirector within
[Control Center](https://control.akamai.com).
Otherwise use the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html)
to configure it programmatically.

__Options__:

<div class="option" markdown="1" id="edgeRedirector.enabled" >

- `enabled` (_boolean_):
    Enables
the Edge Redirector Cloudlet.

</div>

<div class="option" markdown="1" id="edgeRedirector.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Specifies the Cloudlet policy as an object containing two members: a
descriptive `name` string and an integer `id` set by the Cloudlet
application.

</div>

</div>

<div class="feature" data-feature="edgeScape" markdown="1">

## edgeScape

__Property Manager name__:
[Content Targeting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0043)

[EdgeScape](https://control.akamai.com/dl/customers/ESCAPE/EdgeScape_users_guide.pdf)
allows you to customize content based on the end user's geographic
location or connection speed. When enabled, the edge server sends a
special `X-Akamai-Edgescape` header to the origin server encoding
relevant details about the end-user client as key-value pairs.

__Options__:

<div class="option" markdown="1" id="edgeScape.enabled" >

- `enabled` (_boolean_):
    When enabled,
sends the `X-Akamai-Edgescape` request header to the origin.

</div>

</div>

<div class="feature" data-feature="edgeSideIncludes" markdown="1">

## edgeSideIncludes

__Property Manager name__:
[ESI](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0094)

Allows edge servers to
process
[edge side include (ESI)](http://www.akamai.com/html/support/esi.html)
code to generate dynamic content. To apply this behavior, you need to
match on a [`contentType`](#contenttype), [`path`](#path), or
[`filename`](#filename). Since this behavior requires more parsing
time, you should not apply it to pages that lack ESI code, or to any
non-HTML content.

__Options__:

<div class="option" markdown="1" id="edgeSideIncludes.enabled" >

- `enabled` (_boolean_):
    Enables
ESI processing.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.enableViaHttp" >

- `enableViaHttp` (_boolean_):
    Enable ESI only for content featuring the following HTTP response
header: `Edge-control: dca=esi`

</div>

<div class="option" markdown="1" id="edgeSideIncludes.passSetCookie" >

- `passSetCookie` (_boolean_):
    When enabled, allows edge servers to pass your origin server's
cookies to the ESI processor.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.passClientIp" >

- `passClientIp` (_boolean_):
    When enabled, allows edge servers to pass the client IP header to
the ESI processor.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.i18nStatus" >

- `i18nStatus` (_boolean_):
    When
enabled, provides internationalization support for ESI.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.i18nCharset" >

- `i18nCharset` (_array of string values_):
    With
`i18nStatus` enabled, specifies the character sets to use when
transcoding the ESI language, `UTF-8` and `ISO-8859-1` for example.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.detectInjection" >

- `detectInjection` (_boolean_):
    When enabled, denies attempts to inject ESI code.

</div>

</div>

<div class="feature" data-feature="enhancedAkamaiProtocol" markdown="1">

## enhancedAkamaiProtocol

__Property Manager name__:
[Enhanced Akamai Protocol](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0044)

Enables the
[Enhanced Akamai Protocol](http://www.akamai.com/dl/feature_sheets/DSA_Premier_Edition_Feature_Sheet.pdf),
a suite of advanced routing and transport optimizations that increase
your website's performance and reliability. It is only available to
specific applications, and requires a special routing from edge to
origin.

> __WARNING__: Disabling this behavior may significantly reduce a
property's performance.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="enhancedProxyDetection" markdown="1">

## enhancedProxyDetection

__Property Manager name__:
[Enhanced Proxy Detection with GeoGuard](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5006)

This behavior
allows you to apply proxy detection and location spoofing protection
from Akamai's data provider, GeoGuard. Configure it to identify
unwanted requests redirected from four types of proxy: anonymous VPN,
public proxy, The Onion Router (Tor) exit node, and smart DNS
proxy. Configure your edge content to deny or redirect requests, or
allow them to pass through so that you can log and audit the
traffic.

__Options__:

<div class="option" markdown="1" id="enhancedProxyDetection.enabled" >

- `enabled` (_boolean_):
    Applies GeoGuard proxy detection.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.enableConfigurationMode" >

- `enableConfigurationMode` (_enum string_):
    Sets either a default `BEST_PRACTICE` mode to apply a single
action to the four different categories of traffic, or `ADVANCED` to
configure them separately. Choose the latter only if you are
thoroughly familiar in GeoGuard proxy detection.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.bestPracticeAction" >

- `bestPracticeAction` (_enum string_):
    With `enableConfigurationMode` set to `BEST_PRACTICE`, specifies
whether to `ALLOW`, `DENY`, or `REDIRECT` the proxy request.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.bestPracticeRedirecturl" >

- `bestPracticeRedirecturl` (_string_):
    With `bestPracticeAction` set to `REDIRECT`, this specifies the
URL to which to redirect requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpn" >

- `detectAnonymousVpn` (_boolean_):
    With `enableConfigurationMode` set to `ADVANCED`, this enables
detection of requests from anonymous VPNs.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpnAction" >

- `detectAnonymousVpnAction` (_enum string_):
    With `detectAnonymousVpn` enabled, specifies whether to `ALLOW`,
`DENY`, or `REDIRECT` anonymous VPN requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpnRedirecturl" >

- `detectAnonymousVpnRedirecturl` (_string_):
    With `detectAnonymousVpnAction` set to `REDIRECT`, this specifies
the URL to which to redirect anonymous VPN requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxy" >

- `detectPublicProxy` (_boolean_):
    With `enableConfigurationMode` set to `ADVANCED`, this enables
detection of requests from public proxies.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxyAction" >

- `detectPublicProxyAction` (_enum string_):
    With `detectPublicProxy` enabled, specifies whether to `ALLOW`,
`DENY`, or `REDIRECT` public proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxyRedirecturl" >

- `detectPublicProxyRedirecturl` (_string_):
    With `detectPublicProxyAction` set to `REDIRECT`, this specifies
the URL to which to redirect public proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNode" >

- `detectTorExitNode` (_boolean_):
    With `enableConfigurationMode` set to `ADVANCED`, this enables
detection of requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNodeAction" >

- `detectTorExitNodeAction` (_enum string_):
    With `detectTorExitNode` enabled, specifies whether to `DENY`,
`ALLOW`, or `REDIRECT` requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNodeRedirecturl" >

- `detectTorExitNodeRedirecturl` (_string_):
    With `detectTorExitNodeAction` set to `REDIRECT`, this specifies
the URL to which to redirect requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxy" >

- `detectSmartDNSProxy` (_boolean_):
    With `enableConfigurationMode` set to `ADVANCED`, this enables
detection of requests from smart DNS proxies.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxyAction" >

- `detectSmartDNSProxyAction` (_enum string_):
    With `detectSmartDNSProxy` enabled, specifies whether to `DENY`,
`ALLOW`, or `REDIRECT` smart DNS proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxyRedirecturl" >

- `detectSmartDNSProxyRedirecturl` (_string_):
    With `detectSmartDNSProxyAction` set to `REDIRECT`, this specifies
the URL to which to redirect DNS proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenter" >

- `detectVpnDataCenter` (_boolean_):
    With `enableConfigurationMode` set to `ADVANCED`, this enables
detection of requests from VPN data centers. You should learn more
about this GeoGuard category before enabling it.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenterAction" >

- `detectVpnDataCenterAction` (_enum string_):
    With `detectVpnDataCenter` enabled, specifies whether to `DENY`,
`ALLOW`, or `REDIRECT` requests from VPN data centers.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenterRedirecturl" >

- `detectVpnDataCenterRedirecturl` (_string_):
    With `detectVpnDataCenterAction` set to `REDIRECT`, this specifies
the URL to which to redirect requests from VPN data centers. ...

</div>

</div>

<div class="feature" data-feature="failAction" markdown="1">

## failAction

__Property Manager name__:
[Site Failover](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9017)

Specifies how to respond when
the origin is not available: by serving stale content, by serving an
error page, or by redirecting.  To apply this behavior, you should
match on an [`originTimeout`](#origintimeout) or
[`matchResponseCode`](#matchresponsecode).

__Options__:

<div class="option" markdown="1" id="failAction.enabled" >

- `enabled` (_boolean_):
    When enabled in
case of a failure to contact the origin, the current behavior
applies.

</div>

<div class="option" markdown="1" id="failAction.actionType" >

- `actionType` (_enum string_):
    Specifies the
basic action to take when there is a failure to contact the origin:

    - `SERVE_STALE` serves content that is already in the cache.
    - `REDIRECT` specifies a redirect action. (Use with these options:     `redirectHostnameType`, `redirectHostname`, `redirectCustomPath`,     `redirectPath`, `redirectMethod`, `modifyProtocol`, and `protocol`.)
    - `RECREATED_CEX` serves alternate content from an external     network.  (Use with these options: `cexHostname`, `cexCustomPath`,     and `cexPath`.)
    - `RECREATED_CO` serves alternate content from your network.  (Use     with these options: `contentHostname`, `contentCustomPath`, and `contentPath`.)
    - `RECREATED_NS` serves     [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)     content. (Use with these options: `netStorageHostname`,     `netStoragePath`, and `cpCode`.)
    - `DYNAMIC` allows you to serve dynamic SaaS content if SaaS     acceleration is available on your contract.  (Use with these     options: `dynamicMethod`, `dynamicCustomPath`, `saasType`,     `saasSuffix`, `saasRegex`, and `saasReplace`.)

</div>

<div class="option" markdown="1" id="failAction.statusCode" >

- `statusCode` (_numeric enum_):
    Assigns a
new HTTP status code to the failure response.  <!-- `100`, `101`,
`102`, `103`, `122`, `200`, `201`, `202`, `203`, `204`, `205`, `206`,
`207`, `226`, `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`,
`408`, `409`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`,
`422`, `423`, `424`, `425`, `426`, `428`, `429`, `431`, `444`, `449`,
`450`, `499`, `500`, `501`, `502`, `503`, `504`, `505`, `506`, `507`,
`509`, `510`, `511`, `598`, `599`-->

</div>

<div class="option" markdown="1" id="failAction.cpCode" >

- `cpCode` (_object_):
    When
`actionType` is `RECREATED_NS`, this specifies a _cpcode_ for which to
log errors for the NetStorage location. It appears as an object that
includes an `id` key and a descriptive `name`:

        "cpCode": {
            "id"   : 12345,
            "name" : "my cpcode"
        }

</div>

<div class="option" markdown="1" id="failAction.netStorageHostname" >

- `netStorageHostname` (_object_):
    When the `actionType` is `RECREATED_NS`, specifies the
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
origin to serve the alternate content, as in the example below.
Contact Akamai Professional Services for your NetStorage origin's
`id`.

        "netStorageHostname": {
            "id"                 : "netstorage_id",
            "name"               : "Example Downloads",
            "downloadDomainName" : "download.example.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="failAction.netStoragePath" >

- `netStoragePath` (_string; allows [variables](#vf)_):
    When
the `actionType` is `RECREATED_NS`, specifies the path for the
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
request.

</div>

<div class="option" markdown="1" id="failAction.redirectMethod" >

- `redirectMethod` (_numeric enum_):
    When
the `actionType` is `REDIRECT`, specifies the HTTP response code, either
`301` or `302`.

</div>

<div class="option" markdown="1" id="failAction.redirectHostnameType" >

- `redirectHostnameType` (_enum string_):
    When the `actionType` is `REDIRECT`, this specifies whether to preserve
the `ORIGINAL` hostname in the redirect, or whether to use an
`ALTERNATE` hostname specified with `redirectHostname`.

</div>

<div class="option" markdown="1" id="failAction.redirectHostname" >

- `redirectHostname` (_string; allows [variables](#vf)_):
    When
the `actionType` is `REDIRECT` and the `redirectHostnameType` is
`ALTERNATE`, this specifies the hostname for the redirect.

</div>

<div class="option" markdown="1" id="failAction.redirectCustomPath" >

- `redirectCustomPath` (_boolean_):
    When the `actionType` is `REDIRECT`, enabling this allows you use
`redirectPath` to customize a new path.

</div>

<div class="option" markdown="1" id="failAction.redirectPath" >

- `redirectPath` (_string; allows [variables](#vf)_):
    When the
`actionType` is `REDIRECT`, this specifies a new path.

</div>

<div class="option" markdown="1" id="failAction.modifyProtocol" >

- `modifyProtocol` (_boolean_):
    When
the `actionType` is `REDIRECT`, or if the `dynamicMethod` is either
`SERVE_301` or `SERVE_302`, enabling this allows you to modify the
redirect's protocol using the value of the `protocol` field.

</div>

<div class="option" markdown="1" id="failAction.protocol" >

- `protocol` (_enum string_):
    When the
`actionType` is `REDIRECT` and `modifyProtocol` is enabled, this
specifies the redirect's protocol, either `HTTP` or `HTTPS`.

</div>

<div class="option" markdown="1" id="failAction.preserveQueryString" >

- `preserveQueryString` (_boolean_):
    When using either `contentCustomPath`, `cexCustomPath`,
`dynamicCustomPath`, or `redirectCustomPath` to specify a custom path,
enabling this passes in the original request's query string as part of
the path.

</div>

<div class="option" markdown="1" id="failAction.cexHostname" >

- `cexHostname` (_string; allows [variables](#vf)_):
    When
`actionType` is `RECREATED_CEX`, this specifies a hostname.

</div>

<div class="option" markdown="1" id="failAction.cexCustomPath" >

- `cexCustomPath` (_boolean_):
    When
`actionType` is `RECREATED_CEX`, enabling this allows you to specify a
custom path.

</div>

<div class="option" markdown="1" id="failAction.cexPath" >

- `cexPath` (_string; allows [variables](#vf)_):
    When
`actionType` is `RECREATED_CEX` and `cexCustomPath` is enabled, this
specifies a custom path.

</div>

<div class="option" markdown="1" id="failAction.contentHostname" >

- `contentHostname` (_string; allows [variables](#vf)_):
    When the
`actionType` is `RECREATED_CO`, specifies the static hostname for the
alternate redirect.

</div>

<div class="option" markdown="1" id="failAction.contentCustomPath" >

- `contentCustomPath` (_boolean_):
    When
the `actionType` is `RECREATED_CO`, enabling this allows you to
specify a custom redirect path.

</div>

<div class="option" markdown="1" id="failAction.contentPath" >

- `contentPath` (_string; allows [variables](#vf)_):
    When the
`actionType` is `RECREATED_CO` and `contentCustomPath` is enabled,
this specifies a custom redirect path.

</div>

<div class="option" markdown="1" id="failAction.dynamicMethod" >

- `dynamicMethod` (_enum string_):
    With the
`actionType` set to `DYNAMIC`, specifies the redirect method, either
`SERVE_301`, `SERVE_302`, or `SERVE_ALTERNATE`.

</div>

<div class="option" markdown="1" id="failAction.dynamicCustomPath" >

- `dynamicCustomPath` (_boolean_):
    When
enabled, allows you to modify the original requested path.

</div>

<div class="option" markdown="1" id="failAction.dynamicPath" >

- `dynamicPath` (_string; allows [variables](#vf)_):
    With
`dynamicCustomPath` enabled, specifies the new path.

</div>

<div class="option" markdown="1" id="failAction.saasType" >

- `saasType` (_enum string_):
    Identifies
the component of the request that identifies the SaaS dynamic
failaction: either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="failAction.saasSuffix" >

- `saasSuffix` (_string; allows [variables](#vf)_):
    With
`actionType` set to `DYNAMIC`, specifies the static portion of the SaaS
dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasRegex" >

- `saasRegex` (_string_):
    With `actionType`
set to `DYNAMIC`, specifies the substitution pattern (a
Perl-compatible regular expression) that defines the SaaS dynamic
failaction.

</div>

<div class="option" markdown="1" id="failAction.saasReplace" >

- `saasReplace` (_string; allows [variables](#vf)_):
    With
`actionType` set to `DYNAMIC`, specifies the replacement pattern that
defines the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCnameEnabled" >

- `saasCnameEnabled` (_boolean_):
    With the `saasType` set to `HOSTNAME`, specifies whether to use a
CNAME chain to determine the hostname for the SaaS dynamic
failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCnameLevel" >

- `saasCnameLevel` (_number_):
    With
`saasCnameEnabled` on, specifies the number of elements in the CNAME
chain backwards from the edge hostname that determines the hostname
for the SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasCookie" >

- `saasCookie` (_string; allows [variables](#vf)_):
    With
`saasType` set to `COOKIE`, specifies the name of the cookie that
identifies this SaaS dynamic failaction.

</div>

<div class="option" markdown="1" id="failAction.saasQueryString" >

- `saasQueryString` (_string; allows [variables](#vf)_):
    With
`saasType` set to `QUERY_STRING`, specifies the name of the query
parameter that identifies this SaaS dynamic failaction.

</div>

</div>

<div class="feature" data-feature="fastInvalidate" markdown="1">

## fastInvalidate

__Property Manager name__:
[Fast Invalidate](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9076)

Applies Akamai's _Fast
Purge_ feature to selected edge content, invalidating it within
approximately five seconds.  This behavior sends an
`If-Modified-Since` request to the origin for subsequent requests,
replacing it with origin content if its timestamp is more recent.
Otherwise if the origin lacks a `Last-Modified` header, it sends a
simple GET request. Note that this behavior does not simply delete
content if more recent origin content is unavailable.  See the
[Fast Purge API](https://learn.akamai.com/en-us/api/core_features/fast_purge/v3.html)
for an independent way to invalidate selected sets of content, and for
more information on the feature.

__Options__:

<div class="option" markdown="1" id="fastInvalidate.enabled" >

- `enabled` (_boolean_):
    When
enabled, forces a validation test for all edge content to which the
behavior applies.

</div>

</div>

<div class="feature" data-feature="firstPartyMarketing" markdown="1">

## firstPartyMarketing

__Property Manager name__:
[Cloud Marketing Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0045)

Enables the
[Cloud Marketing Cloudlet](https://learn.akamai.com/pdf/CloudMarketing-CS.pdf),
which helps MediaMath customers collect usage data and place
corresponding tags for use in online advertising.  You can configure
tags using either the Cloudlets Policy Manager application or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).
See also the [`firstPartyMarketingPlus`](#firstpartymarketingplus)
behavior, which is designed to integrate better with both MediaMath
and its partners. Both behaviors support the same set of options.

__Options__:

<div class="option" markdown="1" id="firstPartyMarketing.enabled" >

- `enabled` (_boolean_):
    Enables the Cloud Marketing Cloudlet.

</div>

<div class="option" markdown="1" id="firstPartyMarketing.javaScriptInsertionRule" >

- `javaScriptInsertionRule` (_enum string_):
    Select how to insert the MediaMath JavaScript reference script,
either `NEVER` if inserting it at the origin, `ALWAYS` to insert it
for all edge requests, or `POLICY` to allow the Cloudlet policy to
determine when to insert it.

</div>

<div class="option" markdown="1" id="firstPartyMarketing.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="firstPartyMarketing.mediaMathPrefix" >

- `mediaMathPrefix` (_string_):
    Specify the URL path prefix that distinguishes Cloud Marketing
requests from your other web traffic. Include the leading slash
character, but no trailing slash.  For example, if the path prefix is
`/mmath`, and the request is for `www.example.com/dir`, the new URL is
`www.example.com/mmath/dir`.

</div>

</div>

<div class="feature" data-feature="firstPartyMarketingPlus" markdown="1">

## firstPartyMarketingPlus

__Property Manager name__:
[Cloud Marketing Plus Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0046)

Enables the
[Cloud Marketing Plus Cloudlet](https://learn.akamai.com/pdf/CloudMarketing-CS.pdf),
which helps MediaMath customers collect usage data and place
corresponding tags for use in online advertising.  You can configure
tags using either the Cloudlets Policy Manager application or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).
See also the [`firstPartyMarketing`](#firstpartymarketing) behavior,
which integrates with MediaMath but not its partners. Both behaviors
support the same set of options.

__Options__:

<div class="option" markdown="1" id="firstPartyMarketingPlus.enabled" >

- `enabled` (_boolean_):
    Enables the Cloud Marketing Plus Cloudlet.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.javaScriptInsertionRule" >

- `javaScriptInsertionRule` (_enum string_):
    Select how to insert the MediaMath JavaScript reference script,
either `NEVER` if inserting it at the origin, `ALWAYS` to insert it
for all edge requests, or `POLICY` to allow the Cloudlet policy to
determine when to insert it.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique
numeric `id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="firstPartyMarketingPlus.mediaMathPrefix" >

- `mediaMathPrefix` (_string_):
    Specify the URL path prefix that distinguishes Cloud Marketing
requests from your other web traffic. Include the leading slash
character, but no trailing slash.  For example, if the path prefix is
`/mmath`, and the request is for `www.example.com/dir`, the new URL is
`www.example.com/mmath/dir`.

</div>

</div>

<div class="feature" data-feature="forwardRewrite" markdown="1">

## forwardRewrite

__Property Manager name__:
[Forward Rewrite Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0047)

The Forward Rewrite
Cloudlet allows you to conditionally modify the forward path in edge
content without affecting the URL that displays in the user's address
bar. If cloudlets are available on your contract, choose
__Your services__ &rArr; __Edge logic Cloudlets__
to control how this feature works within
[Control Center](https://control.akamai.com),
or use the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html) to
configure it programmatically.

__Options__:

<div class="option" markdown="1" id="forwardRewrite.enabled" >

- `enabled` (_boolean_):
    Enables
the Forward Rewrite Cloudlet behavior.

</div>

<div class="option" markdown="1" id="forwardRewrite.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

</div>

<div class="feature" data-feature="frontEndOptimization" markdown="1">

## frontEndOptimization

__Property Manager name__:
[Front-End Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0048)

This behavior
enables
[Front End Optimization](http://www.akamai.com/html/resources/front-end-optimization-feo.html),
a suite of performance enhancements that accelerate page rendering and
reduce download times, for example by _minifying_ JavaScript and
CSS.

__Options__:

<div class="option" markdown="1" id="frontEndOptimization.enabled" >

- `enabled` (_boolean_):
    Enables the front-end optimization behavior.

</div>

</div>

<div class="feature" data-feature="g2oheader" markdown="1">

## g2oheader

__Property Manager name__:
[Signature Header Authentication](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9054)

The _signature header
authentication_ (g2o) security feature provides header-based
verification of outgoing origin requests. Edge servers encrypt request
data in a pre-defined header, which the origin uses to verify that the
edge server processed the request. This behavior configures the
request data, header names, encryption algorithm, and shared secret to
use for verification.

__Options__:

<div class="option" markdown="1" id="g2oheader.enabled" >

- `enabled` (_boolean_):
    Enables the g2o
verification behavior.

</div>

<div class="option" markdown="1" id="g2oheader.dataHeader" >

- `dataHeader` (_string_):
    Specifies
the name of the header that contains the request data that needs to be
encrypted.

</div>

<div class="option" markdown="1" id="g2oheader.signedHeader" >

- `signedHeader` (_string_):
    Specifies
the name of the header containing encrypted request data.

</div>

<div class="option" markdown="1" id="g2oheader.encodingVersion" >

- `encodingVersion` (_numeric enum_):
    Specifies the version of the encryption algorithm as an integer
from `1` through `5`. <!-- `2`, `3`, `4`-->

</div>

<div class="option" markdown="1" id="g2oheader.useCustomSignString" >

- `useCustomSignString` (_boolean_):
    When disabled, the encrypted string is based on the forwarded URL.
If enabled, you can use `customSignString` to customize the set of
data to encrypt.

</div>

<div class="option" markdown="1" id="g2oheader.customSignString" >

- `customSignString` (_array of string values_):
    With
`useCustomSignString` enabled, specifies the set of data to be
encrypted as a combination of concatenated strings, any of the
following values:

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

- `secretKey` (_string_):
    Specifies
the shared secret key.

</div>

<div class="option" markdown="1" id="g2oheader.nonce" >

- `nonce` (_string_):
    Specifies the
cryptographic _nonce_ string.

</div>

</div>

<div class="feature" data-feature="globalRequestNumber" markdown="1">

## globalRequestNumber

__Property Manager name__:
[Global Request Number](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9038)

Generates a unique
identifier for each request on the Akamai edge network, for use in
logging and debugging. GRN identifiers follow the same format as
Akamai's error reference strings, for example:
`0.05313217.1567801841.1457a3`.  You can use the Diagnostic Tools API's
[Translate an Error](https://developer.akamai.com/api/core_features/diagnostic_tools/v2.html#gettranslatederror)
operation to get low-level details about any request.

__Options__:

<div class="option" markdown="1" id="globalRequestNumber.outputOption" >

- `outputOption` (_enum string_):
    Specifies how to report the GRN value, either as a `RESPONSE_HEADER`
to the client, a `REQUEST_HEADER` to the origin, `BOTH_HEADERS`, or
`ASSIGN_VARIABLE` to process the value in some other way as a
[variable](#vf).

</div>

<div class="option" markdown="1" id="globalRequestNumber.headerName" >

- `headerName` (_string_):
    With `outputOption` set to specify any set of headers, this
specifies the name of the header to report the GRN value.

</div>

<div class="option" markdown="1" id="globalRequestNumber.variableName" >

- `variableName` (_string_):
    With `outputOption` set to `ASSIGN_VARIABLE`, this specifies the
name of the variable to assign the GRN value to. You need to
pre-declare any [variable](#vf) you specify within the rule tree.

</div>

</div>

<div class="feature" data-feature="gzipResponse" markdown="1">

## gzipResponse

__Property Manager name__:
[Last Mile Acceleration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0049)

Apply _gzip_ compression to
speed transfer time. This behavior applies best to text-based content
such as HTML, CSS, and JavaScript, especially once files exceed about
10KB. Do not apply it to already compressed image formats, or to small
files that would add more time to uncompress. To apply this behavior,
you should match on [`contentType`](#contenttype) or the content's
[`cacheability`](#cacheability).

__Options__:

<div class="option" markdown="1" id="gzipResponse.behavior" >

- `behavior` (_enum string_):
    Specify
when to compress responses, either `ALWAYS`, `NEVER`, or
`ORIGIN_RESPONSE` to clients that send an `Accept-Encoding: gzip`
header.

</div>

</div>

<div class="feature" data-feature="hdDataAdvanced" markdown="1">

## hdDataAdvanced

__Property Manager name__:
[HD Data Override: Advanced Metadata](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9064)

A [read-only behavior](#ro)
that specifies Akamai XML metadata that can only be configured on your
behalf by Akamai Professional Services.  Unlike the
[`advanced`](#advanced) behavior, this may apply a different set of
overriding metadata that executes in a post-processing phase.

__Options__:

<div class="option" markdown="1" id="hdDataAdvanced.description" >

- `description` (_string_):
    Human-readable
description of what the XML block does.

</div>

<div class="option" markdown="1" id="hdDataAdvanced.xml" >

- `xml` (_string_):
    A block of
Akamai XML metadata.

</div>

</div>

<div class="feature" data-feature="healthDetection" markdown="1">

## healthDetection

__Property Manager name__:
[Origin Health Detection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0113)

Monitors the health of
your origin server by tracking unsuccessful attempts to contact
it. Use this behavior to keep end users from having to wait several
seconds before a forwarded request times out, or to reduce requests on
the origin server when it is unavailable.

When client requests are forwarded to the origin, the edge server
tracks the number of attempts to connect to each IP address. It cycles
through IP addresses in least-recently-tested order to avoid hitting
the same one twice in a row. If the number of consecutive
unsuccessful tests reaches a threshold you specify, the behavior
identifies the address as faulty and stops sending requests. The edge
server returns an error message to the end user or else triggers any
[`failAction`](#failaction) behavior you specify.

__Options__:

<div class="option" markdown="1" id="healthDetection.retryCount" >

- `retryCount` (_number_):
    The
number of consecutive connection failures that mark an IP address as
faulty.

</div>

<div class="option" markdown="1" id="healthDetection.retryInterval" >

- `retryInterval` (_duration string_):
    Specifies the amount of time the edge server will wait before trying
to reconnect to an IP address it has already identified as faulty.

</div>

<div class="option" markdown="1" id="healthDetection.maximumReconnects" >

- `maximumReconnects` (_number_):
    Specifies the maximum number of times the edge server will contact
your origin server. If your origin is associated with several IP
addresses, `maximumReconnects` effectively overrides the value of
`retryCount`.

</div>

</div>

<div class="feature" data-feature="http2" markdown="1">

## http2

__Property Manager name__:
[HTTP/2](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0050)

Enables the HTTP/2 protocol, which
reduces latency and improves efficiency. You can only apply this
behavior if the property is marked as secure.  See
[Secure property requirements](#sf) for guidance.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="httpStrictTransportSecurity" markdown="1">

## httpStrictTransportSecurity

__Property Manager name__:
[HTTP Strict Transport Security](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_1000)

Applies HTTP
Strict Transport Security (HSTS), disallowing insecure HTTP traffic.
Apply this to hostnames managed with Standard TLS or Enhanced TLS
certificates.

__Options__:

<div class="option" markdown="1" id="httpStrictTransportSecurity.enable" >

- `enable` (_boolean_):
    Applies HSTS to this set of requests.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.maxAge" >

- `maxAge` (_enum string_):
    Specifies the duration for which to apply HSTS for new browser
connections, either `TEN_MINS`, `ONE_DAY`, `ONE_MONTH`,
`THREE_MONTHS`, `SIX_MONTHS`, or `ONE_YEAR`.  A value of `ZERO_MINS`
effectively disables HSTS, without affecting any existing browser
connections.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.includeSubDomains" >

- `includeSubDomains` (_boolean_):
    When enabled, applies HSTS to all subdomains.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.preload" >

- `preload` (_boolean_):
    When enabled, adds this domain to the browser's preload list. You
still need to declare the domain at
[hstspreload.org](https://hstspreload.org/).

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.redirect" >

- `redirect` (_boolean_):
    When enabled, redirects all HTTP requests to HTTPS.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.redirectStatusCode" >

- `redirectStatusCode` (_numeric enum_):
    With `redirect` enabled, specifies a `301` or `302` response
code.

</div>

</div>

<div class="feature" data-feature="httpToHttpsUpgrade" markdown="1">

## httpToHttpsUpgrade

__Property Manager name__:
[HTTP to HTTPS Upgrade](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5005)

Upgrades an HTTP edge
request to HTTPS for the remainder of the request flow. Enable this
behavior only if your origin supports HTTPS, and if your
[`origin`](#origin) behavior is configured with `originCertsToHonor`
to verify SSL certificates.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="imageManager" markdown="1">

## imageManager

__Property Manager name__:
[Image and Video Manager](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0052)

Optimizes images' size or
file type for the requesting device.  You can also use this behavior
to generate API tokens to apply your own policies to matching images
using the
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html).
To apply this behavior, you need to match on a
[`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="imageManager.enabled" >

- `enabled` (_boolean_):
    Enable image management capabilities and generate a corresponding
API token.

</div>

<div class="option" markdown="1" id="imageManager.resize" >

- `resize` (_boolean_):
    Specify whether to scale down images to the maximum screen
resolution, as determined by the rendering device's user agent.  Note
that enabling this may affect screen layout in unexpected ways.

</div>

<div class="option" markdown="1" id="imageManager.applyBestFileType" >

- `applyBestFileType` (_boolean_):
    Specify whether to convert images to the best file type for the
requesting device, based on its user agent and the initial image file.
This produces the smallest file size possible that retains image
quality.

</div>

<div class="option" markdown="1" id="imageManager.superCacheRegion" >

- `superCacheRegion` (_enum string_):
    Specifies a location for your site's heaviest traffic, for use in
caching derivatives on edge servers.  Possible values are `US`,
`JAPAN`, `ASIA`, `AUSTRALIA`, or `EMEA` (Europe, Middle East, and
Africa).

</div>

<div class="option" markdown="1" id="imageManager.cpCodeOriginal" >

- `cpCodeOriginal` (_object_):
    Assigns a CP code to track traffic and billing for original images
that the Image and Video Manager has not modified. Form the value as an object
with a single `id` member paired with an integer value, for example:
`"cpCodeOriginal":{"id":12345}`.

</div>

<div class="option" markdown="1" id="imageManager.cpCodeTransformed" >

- `cpCodeTransformed` (_object_):
    Assigns a separate CP code to track traffic and billing for derived
images. Form the value as an object with a single `id` member paired
with an integer value, for example:
`"cpCodeTransformed":{"id":12345}`.

</div>

<div class="option" markdown="1" id="imageManager.advanced" >

- `advanced` (_boolean_):
    When
enabled, allows you to generate a custom
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html)
token to apply a corresponding policy to this set of images. The token
consists of a descriptive label (the `policyToken`) concatenated with
a property-specific identifier that's generated when you save the
property. The API registers the token when you activate the
property.

</div>

<div class="option" markdown="1" id="imageManager.policyToken" >

- `policyToken` (_string_):
    With
`advanced` enabled, assign a prefix label to help match the policy
token to this set of images, limited to 32 alphanumeric or underscore
characters. If you don't specify a label, _default_ becomes the
prefix.

</div>

<div class="option" markdown="1" id="imageManager.policyTokenDefault" >

- `policyTokenDefault` (_string_):
    Specify the default policy identifier, which is registered with the
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html)
once you activate this property.  The `advanced` option needs to be
inactive.

</div>

</div>

<div class="feature" data-feature="imageManagerVideo" markdown="1">

## imageManagerVideo

__Property Manager name__:
[Image and Video Manager](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0124)

Optimizes videos
managed by Image and Video Manager for the requesting device.  You can also use
this behavior to generate API tokens to apply your own policies to
matching videos using the
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html).
To apply this behavior, you need to match on a
[`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="imageManagerVideo.enabled" >

- `enabled` (_boolean_):
    Applies
Image and Video Manager's video optimization to the current content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.resize" >

- `resize` (_boolean_):
    When
enabled, scales down video for smaller mobile screens, based on the
device's `User-Agent` header.

</div>

<div class="option" markdown="1" id="imageManagerVideo.applyBestFileType" >

- `applyBestFileType` (_boolean_):
    When enabled, automatically converts videos to the best file type
for the requesting device. This produces the smallest file size that
retains image quality, based on the user agent and the initial image
file.

</div>

<div class="option" markdown="1" id="imageManagerVideo.superCacheRegion" >

- `superCacheRegion` (_enum string_):
    To optimize caching, assign a region close to your site's heaviest
traffic, either `ASIA`, `AUSTRALIA`, `EMEA` (Europe, Middle East and
Africa), `JAPAN`, or `US`. Assign `US` if your site's heaviest traffic
varies across regions.

</div>

<div class="option" markdown="1" id="imageManagerVideo.cpCodeOriginal" >

- `cpCodeOriginal` (_object_):
    Select the CP code for which to track Image and Video Manager video traffic.
Use this along with `cpCodeTransformed` to track traffic to derivative
video content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.cpCodeTransformed" >

- `cpCodeTransformed` (_object_):
    Select the CP code to identify derivative transformed video
content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.advanced" >

- `advanced` (_boolean_):
    When
disabled, applies a single standard policy based on your property
name.  When enabled, allows you to reference a rule-specific
`policyToken` for videos with different match criteria.

</div>

<div class="option" markdown="1" id="imageManagerVideo.policyToken" >

- `policyToken` (_string_):
    With `advanced` enabled, specifies a custom policy defined in the
Image and Video Manager Policy Manager or the
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html).
The policy name can include up to 64 alphanumeric, dash, or underscore
characters.

</div>

<div class="option" markdown="1" id="imageManagerVideo.policyTokenDefault" >

- `policyTokenDefault` (_string_):
    Specify the default policy identifier, which is registered with
the
[Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html)
once you activate this property.

</div>

</div>

<div class="feature" data-feature="imOverride" markdown="1">

## imOverride

__Property Manager name__:
[Image and Video Manager: Set Parameter](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0051)

This specifies common query
parameters that affect how [`imageManager`](#imagemanager) transforms
images, potentially overriding policy, width, format, or density
request parameters. This also allows you to assign the value of one of
the property's [rule tree variables](#vf) to one of Image and Video Manager's
own policy variables.

__Options__:

<div class="option" markdown="1" id="imOverride.override" >

- `override` (_enum string_):
    Selects the
type of query parameter you want to set, either the `DPR` for pixel
density, `FORMAT` for browser types, `POLICY` for the name of the
Image and Video Manager policy you want to apply, or the predefined `WIDTH` to
constrain the image to.  Alternately specify that you want to set an
Image and Video Manager `POLICY_VARIABLE` from a [rule tree variable](#vf)
defined in the property.

</div>

<div class="option" markdown="1" id="imOverride.typesel" >

- `typesel` (_enum string_):
    When setting
any query parameter, specifies whether to set it to a specific
`VALUE`, or whether to assign a Property Manager rule tree
`VARIABLE`.

</div>

<div class="option" markdown="1" id="imOverride.formatvar" >

- `formatvar` (_string_):
    With the
`override` parameter set to `FORMAT` and the `typesel` set to
`VARIABLE`, this selects the variable with the name of the browser you
want to optimize images for. The variable specifies the same type of
data as the `format` option below.

</div>

<div class="option" markdown="1" id="imOverride.format" >

- `format` (_enum string_):
    With the
`override` parameter set to `FORMAT` and the `typesel` set to `VALUE`,
this specifies the name of the browser you want to optimize images
for, either `CHROME`, `SAFARI`, `IE`, or `GENERIC`.

</div>

<div class="option" markdown="1" id="imOverride.dprvar" >

- `dprvar` (_string_):
    With the
`override` parameter set to `DPR` and the `typesel` set to `VARIABLE`,
this selects the variable with the desired pixel density. The variable
specifies the same type of data as the `dpr` option below.

</div>

<div class="option" markdown="1" id="imOverride.dpr" >

- `dpr` (_number_):
    With the
`override` parameter set to `DPR` and the `typesel` set to `VALUE`,
this directly specifies the pixel density. The numeric value is a
scaling factor of 1, representing normal density.

</div>

<div class="option" markdown="1" id="imOverride.widthvar" >

- `widthvar` (_string_):
    With the
`override` parameter set to `WIDTH` and the `typesel` set to
`VARIABLE`, this selects the variable with the desired width.  If the
Image and Video Manager policy doesn't define that width, it serves the next
largest width.

</div>

<div class="option" markdown="1" id="imOverride.width" >

- `width` (_number_):
    With the
`override` parameter set to `WIDTH` and the `typesel` set to `VALUE`,
this sets the image's desired pixel width directly. If the Image
Manager policy doesn't define that width, it serves the next largest
width.

</div>

<div class="option" markdown="1" id="imOverride.policyvar" >

- `policyvar` (_string_):
    With the
`override` parameter set to `POLICY` and the `typesel` set to
`VARIABLE`, this selects the variable with the desired Image and Video Manager
policy name to apply to image requests. If there is no policy by that
name, Image and Video Manager serves the image unmodified.

</div>

<div class="option" markdown="1" id="imOverride.policy" >

- `policy` (_string_):
    With the
`override` parameter set to `POLICY` and the `typesel` set to `VALUE`,
this selects the desired Image and Video Manager policy name directly. If there
is no policy by that name, Image and Video Manager serves the image
unmodified.

</div>

<div class="option" markdown="1" id="imOverride.policyvarName" >

- `policyvarName` (_string_):
    With
`override` set to `POLICY_VARIABLE`, this selects the name of one of
the variables defined in an Image and Video Manager policy that you want to
replace with the property's rule tree variable.

</div>

<div class="option" markdown="1" id="imOverride.policyvarIMvar" >

- `policyvarIMvar` (_string_):
    With
`override` set to `POLICY_VARIABLE`, this selects one of the
property's rule tree variables to assign to the `policyvarName`
variable within Image and Video Manager.

</div>

</div>

<div class="feature" data-feature="injectReferenceId" markdown="1">

## injectReferenceId

__Property Manager name__:
[Inject Reference ID](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9042)

Allows you to inject an
Akamai reference ID, useful for troubleshooting, anywhere within the
response body. With this feature enabled, any `AKAM_REF` string you
specify is replaced with a unique identifier for each response.

__Options__:

<div class="option" markdown="1" id="injectReferenceId.referenceId" >

- `referenceId` (_boolean_):
    Enables injection of reference ID values.

</div>

</div>

<div class="feature" data-feature="inputValidation" markdown="1">

## inputValidation

__Property Manager name__:
[Input Validation Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0053)

The Input Validation
Cloudlet detects anomalous edge requests and helps mitigate repeated
invalid requests.  You can configure it using either the Cloudlets
Policy Manager application, available within
[Control Center](https://control.akamai.com)
under
__Your services__ &rArr; __Edge logic Cloudlets__,
or the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html).

Use this behavior to specify criteria that identifies each unique end
user, and optionally supplement the Input Validation policy with
additional criteria your origin uses to identify invalid requests.
Specify the threshold number of invalid requests that triggers a
penalty, and the subsequent response.  Also specify an ordinary
failure response for those who have not yet met the threshold, which
should not conflict with any other behavior that defines a failure
response.

__Options__:

<div class="option" markdown="1" id="inputValidation.enabled" >

- `enabled` (_boolean_):
    Applies
the Input Validation Cloudlet behavior.

</div>

<div class="option" markdown="1" id="inputValidation.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="inputValidation.label" >

- `label` (_string_):
    Distinguishes this Input Validation policy from any others within
the same property.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByCookie" >

- `userIdentificationByCookie` (_boolean_):
    When enabled, identifies users by the value of a cookie.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyCookie" >

- `userIdentificationKeyCookie` (_string_):
    With `userIdentificationByCookie` enabled, this specifies the
cookie name whose value must remain constant across requests to
identify a user.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByIp" >

- `userIdentificationByIp` (_boolean_):
    When enabled, identifies users by specific IP address. Do not
enable this if you are concerned about DDoS attacks from many
different IP addresses.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByHeaders" >

- `userIdentificationByHeaders` (_boolean_):
    When enabled, identifies users by specific HTTP headers on GET or
POST requests.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyHeaders" >

- `userIdentificationKeyHeaders` (_array of string values_):
    With `userIdentificationByHeaders` enabled, this specifies the
HTTP headers whose combined set of values identify each end user.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationByParams" >

- `userIdentificationByParams` (_boolean_):
    When enabled, identifies users by specific query parameters on GET
or POST requests.

</div>

<div class="option" markdown="1" id="inputValidation.userIdentificationKeyParams" >

- `userIdentificationKeyParams` (_array of string values_):
    With `userIdentificationByParams` enabled, this specifies the
query parameters whose combined set of values identify each end
user.

</div>

<div class="option" markdown="1" id="inputValidation.allowLargePostBody" >

- `allowLargePostBody` (_boolean_):
    Fails POST request bodies that exceed 16 KB when enabled, otherwise
allows them to pass with no validation for policy compliance.

</div>

<div class="option" markdown="1" id="inputValidation.resetOnValid" >

- `resetOnValid` (_boolean_):
    Upon
receiving a valid request, enabling this resets the `penaltyThreshold`
counter to zero.  Otherwise, even those series of invalid requests
that are interrupted by valid requests may trigger the
`penaltyAction`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginWith" >

- `validateOnOriginWith` (_enum string_):
    For any validation that edge servers can't perform alone,
this specifies additional validation steps based on how the origin
identifies an invalid request.  If a request is invalid, the origin
can indicate this to the edge server either with a `RESPONSE_CODE` or
`RESPONSE_CODE_AND_HEADER`.  If no additional validation is necessary,
specify `DISABLED`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginHeaderName" >

- `validateOnOriginHeaderName` (_string_):
    If `validateOnOriginWith` is set to `RESPONSE_CODE_AND_HEADER`,
this specifies the header name for a request that the origin
identifies as invalid.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginHeaderValue" >

- `validateOnOriginHeaderValue` (_string_):
    If `validateOnOriginWith` is set to `RESPONSE_CODE_AND_HEADER`,
this specifies an invalid request's header value that corresponds to
the `validateOnOriginHeaderName`.

</div>

<div class="option" markdown="1" id="inputValidation.validateOnOriginResponseCode" >

- `validateOnOriginResponseCode` (_number_):
    Unless `validateOnOriginWith` is `DISABLED`, this identifies the
integer response code for requests the origin identifies as invalid.

</div>

<div class="option" markdown="1" id="inputValidation.failure302Uri" >

- `failure302Uri` (_string_):
    Specifies the redirect link for invalid requests that have not yet
triggered a penalty.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyThreshold" >

- `penaltyThreshold` (_number_):
    Specifies the number of invalid requests permitted before executing
the `penaltyAction`.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyAction" >

- `penaltyAction` (_enum string_):
    Once the `penaltyThreshold` of invalid requests is met, this
specifies the response, either `BRANDED_403`, `BLANK_403` or
`REDIRECT_302`.

</div>

<div class="option" markdown="1" id="inputValidation.penalty302Uri" >

- `penalty302Uri` (_string_):
    With `penaltyAction` set to `REDIRECT_302`, this specifies the
redirect link for end users who trigger the penalty.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyNetStorage" >

- `penaltyNetStorage` (_object_):
    With `penaltyAction` set to `BRANDED_403`, this specifies the
NetStorage account that serves out the penalty's static 403 response
content. Details appear in an object featuring a
`downloadDomainName` string member that identifies the NetStorage
hostname, and an integer `cpCode` to track the traffic.

</div>

<div class="option" markdown="1" id="inputValidation.penalty403NetStoragePath" >

- `penalty403NetStoragePath` (_string_):
    With `penaltyAction` set to `BRANDED_403`, this specifies the full
path to the static 403 response content relative to the
`downloadDomainName` in the `penaltyNetStorage` object.

</div>

<div class="option" markdown="1" id="inputValidation.penaltyBrandedDenyCacheTtl" >

- `penaltyBrandedDenyCacheTtl` (_number within 5-30 range_):
    With `penaltyAction` set to `BRANDED_403`, this specifies the
penalty response's time to live in the cache, `5` minutes by
default.

</div>

</div>

<div class="feature" data-feature="instant" markdown="1">

## instant

__Property Manager name__:
[Akamai Instant](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0110)

The Instant feature allows you to
prefetch content to the edge cache by adding link relation attributes
to markup. For example:

```xml
<a href="page2.html" rel="Akamai-prefetch">Page 2</a>
```

Default link relation values are `prefetch` and `Akamai-prefetch`.
Applies only to HTML elements that may specify an external file:
`<a>`, `<base>`, `<img>`, `<script>`, `<input>`, `<link>`, `<table>`,
`<td>`, or `<th>`. (For the latter three, some legacy browsers support
a nonstandard `background` image attribute.)

This behavior provides an alternative to the
[`prefetch`](#prefetch) and
[`prefetchable`](#prefetchable) behaviors, which allow
you to configure more general prefetching behavior outside of
markup.

__Options__:

<div class="option" markdown="1" id="instant.prefetchCacheable" >

- `prefetchCacheable` (_boolean_):
    When
enabled, applies prefetching only to objects already set to be
cacheable, for example using the [`caching`](#caching) behavior. Only
applies to content with the
[`tieredDistribution`](#tiereddistribution) behavior enabled.

</div>

<div class="option" markdown="1" id="instant.prefetchNoStore" >

- `prefetchNoStore` (_boolean_):
    Allows
otherwise non-cacheable `no-store` content to prefetch if the URL path
ends with `/` to indicate a request for a default file, or if the
extension matches the value of the `prefetchNoStoreExtensions`
option. Only applies to content with the [`sureRoute`](#sureroute)
behavior enabled.

</div>

<div class="option" markdown="1" id="instant.prefetchNoStoreExtensions" >

- `prefetchNoStoreExtensions` (_array of string values_):
    Specifies a set of file extensions for which the `prefetchNoStore`
option is allowed.

</div>

<div class="option" markdown="1" id="instant.prefetchHtml" >

- `prefetchHtml` (_boolean_):
    When
enabled, allows edge servers to prefetch additional HTML pages while
pages that link to them are being delivered. This only applies to
links from `<a>` or `<link>` tags with the appropriate link relation
attribute.

</div>

<div class="option" markdown="1" id="instant.customLinkRelations" >

- `customLinkRelations` (_array of string values_):
    Specify link relation values that activate the prefetching
behavior. For example, specifying `fetch` allows you to use shorter
`rel="fetch"` markup.

</div>

</div>

<div class="feature" data-feature="instantConfig" markdown="1">

## instantConfig

__Property Manager name__:
[InstantConfig](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5001)

Multi-Domain Configuration, also
known as _InstantConfig_, allows you to apply property settings to all
incoming hostnames based on a DNS lookup, without explicitly listing
them among the property's hostnames.

__Options__:

<div class="option" markdown="1" id="instantConfig.enabled" >

- `enabled` (_boolean_):
    Enables the InstantConfig
behavior.

</div>

</div>

<div class="feature" data-feature="largeFileOptimization" markdown="1">

## largeFileOptimization

__Property Manager name__:
[Large File Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0054)

The
[Large File Optimization](http://www.akamai.com/dl/feature_sheets/fs_lfdo.pdf)
feature improves performance and reliability when delivering large
files. This behavior is required for objects larger than 1.8GB, and
recommended for anything over 100MB. You should apply it only to the
specific content to be optimized, such as a download directory's `.gz`
files, and enable the `useVersioning` option while enforcing your own
filename versioning policy.  Note that it is best to use
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
for objects larger than 1.8GB.

See also the
[`largeFileOptimizationAdvanced`](#largefileoptimizationadvanced)
behavior, which provides additional options for to configure partial
object caching and HTTP/2 prefetching.

__Options__:

<div class="option" markdown="1" id="largeFileOptimization.enabled" >

- `enabled` (_boolean_):
    Enables the file optimization behavior.

</div>

<div class="option" markdown="1" id="largeFileOptimization.enablePartialObjectCaching" >

- `enablePartialObjectCaching` (_enum string_):
    Caches entire objects if set to
`NON_PARTIAL_OBJECT_CACHING`. Otherwise when set to
`PARTIAL_OBJECT_CACHING`, allows _partial-object caching_, which
always applies to large objects served from
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html).
To enable this, the origin must support byte range requests.

</div>

<div class="option" markdown="1" id="largeFileOptimization.minimumSize" >

- `minimumSize` (_string_):
    Optimization only applies to files larger than this, expressed as a
number suffixed with a unit string such as `MB` or `GB`.

</div>

<div class="option" markdown="1" id="largeFileOptimization.maximumSize" >

- `maximumSize` (_string_):
    Optimization does not apply to files larger than this, expressed as
a number suffixed with a unit string such as `MB` or `GB`.

</div>

<div class="option" markdown="1" id="largeFileOptimization.useVersioning" >

- `useVersioning` (_boolean_):
    When `enablePartialObjectCaching` is set to
`PARTIAL_OBJECT_CACHING`, enabling this option signals your intention
to vary filenames by version, strongly recommended to avoid serving
corrupt content when chunks come from different versions of the same
file.

</div>

</div>

<div class="feature" data-feature="largeFileOptimizationAdvanced" markdown="1">

## largeFileOptimizationAdvanced

__Property Manager name__:
[Large File Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0054)

The
[Large File Optimization](http://www.akamai.com/dl/feature_sheets/fs_lfdo.pdf)
feature improves performance and reliability when delivering large
files. This behavior is required for objects larger than 1.8GB, and
recommended for anything over 100MB. You should apply it only to the
specific content to be optimized, such as a download directory's `.gz`
files.  Note that it is best to use
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
for objects larger than 1.8GB.

This advanced behavior provides additional HTTP/2 options not present
in the [`largeFileOptimization`](#largefileoptimization) behavior.

__Options__:

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.enabled" >

- `enabled` (_boolean_):
    Enables the file optimization behavior.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.objectSize" >

- `objectSize` (_string_):
    Specifies the size of the file at which point to apply partial
object (POC) caching. Append a numeric value with a `MB` or `GB`
suffix.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.fragmentSize" >

- `fragmentSize` (_enum string_):
    Specifies the size of each fragment used for partial object
caching, either `HALF_MB`, `ONE_MB`, `TWO_MB`, or `FOUR_MB`.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.prefetchDuringRequest" >

- `prefetchDuringRequest` (_number_):
    The number of POC fragments to prefetch during the request.

</div>

<div class="option" markdown="1" id="largeFileOptimizationAdvanced.prefetchAfterRequest" >

- `prefetchAfterRequest` (_number_):
    The number of POC fragments to prefetch after the request.

</div>

</div>

<div class="feature" data-feature="limitBitRate" markdown="1">

## limitBitRate

__Property Manager name__:
[Bit Rate Limiting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9006)

Control the rate at which
content serves out to end users, optionally varying the speed
depending on the file size or elapsed download time. Each bit rate
specified in the `bitrateTable` array corresponds to a
`thresholdTable` entry that activates it.  You can use this behavior
to prevent media downloads from progressing faster than they are
viewed, for example, or to differentiate various tiers of end-user
experience. To apply this behavior, you should match on a
[`contentType`](#contenttype), [`path`](#path), or
[`filename`](#filename).

__Options__:

<div class="option" markdown="1" id="limitBitRate.enabled" >

- `enabled` (_boolean_):
    When
enabled, activates the bit rate limiting behavior.

</div>

<div class="option" markdown="1" id="limitBitRate.bitrateTable" >

- `bitrateTable` (_array_):
    Specifies a download rate that corresponds to a `thresholdTable`
entry. The bit rate appears as a two-member object consisting of
a numeric `bitrateValue` and a `bitrateUnit` string, with allowed
values of `Kbps`, `Mbps`, and `Gbps`. For example:

        "bitrateTable": [
            {
                "bitrateValue": 1,
                "bitrateUnit": "Kbps"
            }
        ]

</div>

<div class="option" markdown="1" id="limitBitRate.thresholdTable" >

- `thresholdTable` (_array_):
    Specifies the minimum size of the file or the amount of elapsed
download time before applying the bit rate limit from the
corresponding `bitrateTable` entry. The threshold appears as a
two-member object consisting of a numeric `thresholdValue` and
`thresholdUnit` string, with allowed values of `s` or `B`. This
example throttles a download that lasts more than 5 seconds:

        "thresholdTable": [
            {
                "thresholdValue": 5,
                "thresholdUnit": "s"
            }
        ]

</div>

</div>

<div class="feature" data-feature="manifestPersonalization" markdown="1">

## manifestPersonalization

__Property Manager name__:
[Manifest Personalization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5002)

Allows customers
who use the Adaptive Media Delivery product to enhance content based
on the capabilities of each end user's device.  This behavior
configures a _manifest_ for both HLS Live and on-demand streaming.
For more information, see the
[Adaptive Media Delivery Implementation Guide](https://learn.akamai.com/en-us/webhelp/adaptive-media-delivery/adaptive-media-delivery-implementation-guide/).

__Options__:

<div class="option" markdown="1" id="manifestPersonalization.enabled" >

- `enabled` (_boolean_):
    Enables the Manifest Personalization feature.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsEnabled" >

- `hlsEnabled` (_boolean_):
    When enabled, allows you to customize the HLS master manifest that's
sent to the requesting client.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsMode" >

- `hlsMode` (_enum string_):
    With `hlsEnabled` on, specify either the default `BEST_PRACTICE`
mode, or a `CUSTOM` manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsPreferredBitrate" >

- `hlsPreferredBitrate` (_string_):
    With `hlsMode` set to `CUSTOM`, sets the preferred bit rate in
Kbps. This causes the media playlist specified in the
`#EXT-X-STREAM-INF` tag that most closely matches the value to list
first. All other playlists maintain their current position in the
manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsFilterInBitrates" >

- `hlsFilterInBitrates` (_string_):
    With `hlsMode` set to `CUSTOM`, specifies a comma-delimited set of
preferred bit rates, such as `100,200,400`. Playlists specified in the
`#EXT-X-STREAM-INF` tag with bit rates outside of any of those values
by up to 100 Kbps are excluded from the manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsFilterInBitrateRanges" >

- `hlsFilterInBitrateRanges` (_string_):
    With `hlsMode` set to `CUSTOM`, specifies a comma-delimited set of
bit rate ranges, such as `100-400,1000-4000`. Playlists specified in
the `#EXT-X-STREAM-INF` tag with bit rates outside of any of those
ranges are excluded from the manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamEnabled" >

- `hlsQueryParamEnabled` (_boolean_):
    With `hlsEnabled` on, allows you to specify query parameters for
the HLS master manifest to customize the manifest's content.  Any
settings specified in the query string override those already
configured in Property Manager.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamSecretKey" >

- `hlsQueryParamSecretKey` (_string_):
    With `hlsQueryParamEnabled` on, specifies a primary key as a token
to accompany the request.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamTransitionKey" >

- `hlsQueryParamTransitionKey` (_string_):
    With `hlsQueryParamEnabled` on, specifies a transition key as a
token to accompany the request.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsShowAdvanced" >

- `hlsShowAdvanced` (_boolean_):
    With `hlsEnabled` on, allows you to configure advanced settings.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsEnableDebugHeaders" >

- `hlsEnableDebugHeaders` (_boolean_):
    With `hlsShowAdvanced` enabled, includes additional
`Akamai-Manifest-Personalization` and
`Akamai-Manifest-Personalization-Config-Source` debugging headers.

</div>

</div>

<div class="feature" data-feature="manualServerPush" markdown="1">

## manualServerPush

__Property Manager name__:
[Manual Server Push](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9065)

With the
[`http2`](#http2) behavior enabled, this loads a specified set of
objects into the client browser's cache. To apply this behavior, you
should match on a [`path`](#path) or [`filename`](#filename).

__Options__:

<div class="option" markdown="1" id="manualServerPush.serverpushlist" >

- `serverpushlist` (_array of string values_):
    Specifies the set of objects to load into the client browser's cache
over HTTP2. Each value in the array represents a hostname and full
path to the object, such as `www.example.com/js/site.js`

</div>

</div>

<div class="feature" data-feature="mediaAcceleration" markdown="1">

## mediaAcceleration

__Property Manager name__:
[Media Acceleration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9015)

Enables
[Accelerated Media Delivery](https://www.akamai.com/us/en/products/media-delivery/media-acceleration.jsp)
for this set of requests.

__Options__:

<div class="option" markdown="1" id="mediaAcceleration.enabled" >

- `enabled` (_boolean_):
    Enables
Media Acceleration.

</div>

</div>

<div class="feature" data-feature="mediaAccelerationQuicOptout" markdown="1">

## mediaAccelerationQuicOptout

__Property Manager name__:
[Media Acceleration Opt-Out](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9035)

When enabled,
disables use of QUIC protocol for this set of accelerated media
content.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="mediaClient" markdown="1">

## mediaClient

__Property Manager name__:
[Media Client](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9008)

Enables client-side reporting
through analytics beacon requests.

__Options__:

<div class="option" markdown="1" id="mediaClient.enabled" >

- `enabled` (_boolean_):
    Enables
client-side download analytics.

</div>

<div class="option" markdown="1" id="mediaClient.beaconId" >

- `beaconId` (_string_):
    Specifies
the ID of data source's beacon.

</div>

<div class="option" markdown="1" id="mediaClient.useHybridHttpUdp" >

- `useHybridHttpUdp` (_boolean_):
    Enables the hybrid HTTP/UDP protocol.

</div>

</div>

<div class="feature" data-feature="mediaFileRetrievalOptimization" markdown="1">

## mediaFileRetrievalOptimization

__Property Manager name__:
[Media File Retrieval Optimization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9043)

Media File
Retrieval Optimization (MFRO) speeds the delivery of large media files
by relying on caches of partial objects. You should use it for files
larger than 100 MB. It's required for files larger than 1.8 GB, and
works best with
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html).
To apply this behavior, you should match on a
[`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="mediaFileRetrievalOptimization.enabled" >

- `enabled` (_boolean_):
    Enables the partial-object caching behavior.

</div>

</div>

<div class="feature" data-feature="mediaOriginFailover" markdown="1">

## mediaOriginFailover

__Property Manager name__:
[Media Origin Failover](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9039)

Specifies how edge
servers respond when the origin is unresponsive, or suffers from
server or content errors. You can specify how many times to retry,
switch to a backup origin hostname, or configure a redirect.

__Options__:

<div class="option" markdown="1" id="mediaOriginFailover.detectOriginUnresponsive" >

- `detectOriginUnresponsive` (_boolean_):
    When enabled, allows you to configure what happens when the origin
is unresponsive.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveDetectionLevel" >

- `originUnresponsiveDetectionLevel` (_enum string_):
    With `detectOriginUnresponsive` enabled, specify whether your
response to slow origin connections should be `AGGRESSIVE`,
`MODERATE`, or `CONSERVATIVE`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBlacklistOriginIp" >

- `originUnresponsiveBlacklistOriginIp` (_boolean_):
    With `detectOriginUnresponsive` enabled, enabling this blacklists
the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBlacklistWindow" >

- `originUnresponsiveBlacklistWindow` (_enum string_):
    With `originUnresponsiveBlacklistOriginIp` enabled, this sets the
delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or
`THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRecovery" >

- `originUnresponsiveRecovery` (_enum string_):
    With `detectOriginUnresponsive` enabled, this sets the recovery
option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRetryLimit" >

- `originUnresponsiveRetryLimit` (_enum string_):
    With `originUnresponsiveRecovery` set to `RETRY_X_TIMES`, sets
whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBackupHost" >

- `originUnresponsiveBackupHost` (_string_):
    With `originUnresponsiveRecovery` set to
`SWITCH_TO_BACKUP_ORIGIN`, this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveAlternateHost" >

- `originUnresponsiveAlternateHost` (_string_):
    With `originUnresponsiveRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's
destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveModifyRequestPath" >

- `originUnresponsiveModifyRequestPath` (_boolean_):
    With `originUnresponsiveRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`
or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you
to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveModifiedPath" >

- `originUnresponsiveModifiedPath` (_string_):
    With `originUnresponsiveModifyRequestPath` enabled, this specifies
the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveIncludeQueryString" >

- `originUnresponsiveIncludeQueryString` (_boolean_):
     With `originUnresponsiveModifyRequestPath` enabled, enabling this
includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRedirectMethod" >

- `originUnresponsiveRedirectMethod` (_numeric enum_):
    With `originUnresponsiveRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or
`302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveChangeProtocol" >

- `originUnresponsiveChangeProtocol` (_boolean_):
    With `originUnresponsiveRecovery` set to
`SWITCH_TO_BACKUP_ORIGIN`, or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`,
enabling this allows you to change the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveProtocol" >

- `originUnresponsiveProtocol` (_enum string_):
    With `originUnresponsiveChangeProtocol` enabled, specifies either
the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.detectOriginUnavailable" >

- `detectOriginUnavailable` (_boolean_):
    When enabled, allows you to configure failover settings when the
origin server responds with errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableDetectionLevel" >

- `originUnavailableDetectionLevel` (_enum string_):
    With `detectOriginUnavailable` enabled, specify `RESPONSE_CODES`,
the only available option.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableResponseCodes" >

- `originUnavailableResponseCodes` (_array of string values_):
    With `detectOriginUnavailable` enabled, specifies the set of
response codes identifying when the origin responds with errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBlacklistOriginIp" >

- `originUnavailableBlacklistOriginIp` (_boolean_):
    With `detectOriginUnavailable` enabled, enabling this blacklists
the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBlacklistWindow" >

- `originUnavailableBlacklistWindow` (_enum string_):
    With `originUnavailableBlacklistOriginIp` enabled, this sets the
delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or
`THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRecovery" >

- `originUnavailableRecovery` (_enum string_):
    With `detectOriginUnavailable` enabled, this sets the recovery
option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRetryLimit" >

- `originUnavailableRetryLimit` (_enum string_):
    With `originUnavailableRecovery` set to `RETRY_X_TIMES`, sets
whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBackupHost" >

- `originUnavailableBackupHost` (_string_):
    With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`,
this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableAlternateHost" >

- `originUnavailableAlternateHost` (_string_):
    With `originUnavailableRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's
destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableModifyRequestPath" >

- `originUnavailableModifyRequestPath` (_boolean_):
    With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`
or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you
to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableModifiedPath" >

- `originUnavailableModifiedPath` (_string_):
    With `originUnavailableModifyRequestPath` enabled, this specifies
the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableIncludeQueryString" >

- `originUnavailableIncludeQueryString` (_boolean_):
    With `originUnavailableModifyRequestPath` enabled, enabling this
includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRedirectMethod" >

- `originUnavailableRedirectMethod` (_numeric enum_):
    With `originUnavailableRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or
`302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableChangeProtocol" >

- `originUnavailableChangeProtocol` (_boolean_):
    With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`
or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you
to modify the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableProtocol" >

- `originUnavailableProtocol` (_enum string_):
    With `originUnavailableChangeProtocol` enabled, specifies either
the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.detectObjectUnavailable" >

- `detectObjectUnavailable` (_boolean_):
    When enabled, allows you to configure failover settings when the
origin has content errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableDetectionLevel" >

- `objectUnavailableDetectionLevel` (_enum string_):
    With `detectObjectUnavailable` enabled, specify `RESPONSE_CODES`,
the only available option.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableResponseCodes" >

- `objectUnavailableResponseCodes` (_array of string values_):
    With `detectObjectUnavailable` enabled, specifies the set of
response codes identifying when there are content errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBlacklistOriginIp" >

- `objectUnavailableBlacklistOriginIp` (_boolean_):
    With `detectObjectUnavailable` enabled, enabling this blacklists
the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBlacklistWindow" >

- `objectUnavailableBlacklistWindow` (_enum string_):
    With `objectUnavailableBlacklistOriginIp` enabled, this sets the
delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or
`THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRecovery" >

- `objectUnavailableRecovery` (_enum string_):
    With `detectObjectUnavailable` enabled, this sets the recovery
option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRetryLimit" >

- `objectUnavailableRetryLimit` (_enum string_):
    With `objectUnavailableRecovery` set to `RETRY_X_TIMES`, sets
whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBackupHost" >

- `objectUnavailableBackupHost` (_string_):
    With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`,
this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableAlternateHost" >

- `objectUnavailableAlternateHost` (_string_):
    With `objectUnavailableRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's
destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableModifyRequestPath" >

- `objectUnavailableModifyRequestPath` (_boolean_):
    With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`
or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you
to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableModifiedPath" >

- `objectUnavailableModifiedPath` (_string_):
    With `objectUnavailableModifyRequestPath` enabled, this specifies
the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableIncludeQueryString" >

- `objectUnavailableIncludeQueryString` (_boolean_):
    With `objectUnavailableModifyRequestPath` enabled, enabling this
includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRedirectMethod" >

- `objectUnavailableRedirectMethod` (_numeric enum_):
    With `objectUnavailableRecovery` set to
`REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or
`302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableChangeProtocol" >

- `objectUnavailableChangeProtocol` (_boolean_):
    With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`
or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you
to change the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableProtocol" >

- `objectUnavailableProtocol` (_enum string_):
    With `objectUnavailableChangeProtocol` enabled, specifies either
the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.clientResponseCode" >

- `clientResponseCode` (_string_):
    Specifies the response code served to the client.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.cacheErrorResponse" >

- `cacheErrorResponse` (_boolean_):
    When enabled, caches the error response.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.cacheWindow" >

- `cacheWindow` (_enum string_):
    With `cacheErrorResponse` enabled, this sets error response's TTL,
either `ONE_S`, `TEN_S`, or `THIRTY_S`.

</div>

</div>

<div class="feature" data-feature="metadataCaching" markdown="1">

## metadataCaching

__Property Manager name__:
[Metadata Caching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5029)

2DO

__Options__:

<div class="option" markdown="1" id="metadataCaching.enabled" >

- `enabled` (_boolean_):
    2DO

</div>

</div>

<div class="feature" data-feature="mobileSdkPerformance" markdown="1">

## mobileSdkPerformance

__Property Manager name__:
[Mobile App Performance SDK](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0057)

The
[Mobile Application Performance software development kit](https://developer.akamai.com/tools/sdk/mobile-application-performance)
allows you to optimize native iOS and Android apps, effectively
extending Akamai's intelligent edge platform's advantages to mobile
devices operation in poor network conditions. This behavior enables
the SDK's features for this set of requests.

__Options__:

<div class="option" markdown="1" id="mobileSdkPerformance.enabled" >

- `enabled` (_boolean_):
    Enables the Mobile App Performance SDK.

</div>

<div class="option" markdown="1" id="mobileSdkPerformance.secondaryMultipathToOrigin" >

- `secondaryMultipathToOrigin` (_boolean_):
    When enabled, sends secondary multi-path requests to the origin
server.

</div>

</div>

<div class="feature" data-feature="modifyIncomingRequestHeader" markdown="1">

## modifyIncomingRequestHeader

__Property Manager name__:
[Modify Incoming Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9062)

Modify, add,
remove, or pass along specific request headers coming upstream from
the client.

Depending on the type of `action` you want to perform, specify the
corresponding _standard_ header name, or a `customHeaderName` if the
standard name is set to `OTHER`.  The `headerValue` serves as a match
condition when the action is `DELETE` or `MODIFY`, and the
`newHeaderValue` applies when the action is `ADD` or `MODIFY`.

See also [`modifyIncomingResponseHeader`](#modifyincomingresponseheader),
[`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader), and
[`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyIncomingRequestHeader.action" >

- `action` (_enum string_):
    Either `ADD`, `DELETE`, `MODIFY`, or `PASS` incoming HTTP request
headers.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_):
    If the value of `action` is `ADD`, this specifies the name of the
field to add, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or
`OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_):
    If the value of `action` is `DELETE`, this specifies the name of
the field to remove, either `IF_MODIFIED_SINCE`, `VIA`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_):
    If the value of `action` is `MODIFY`, this specifies the name of
the field to modify, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or
`OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.standardPassHeaderName" >

- `standardPassHeaderName` (_enum string_):
    If the value of `action` is `PASS`, this specifies the name of the
field to pass through, either `ACCEPT_ENCODING`, `ACCEPT_LANGUAGE`, or
`OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_):
    Specifies a custom field name that applies when the relevant
_standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_):
    With the `action` set to `ADD`, specifies the new header value.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_):
    With the `action` set to `MODIFY`, supplies an HTTP header
replacement value.

</div>

<div class="option" markdown="1" id="modifyIncomingRequestHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_):
    When enabled with the `action` set to `MODIFY`, prevents creation
of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyIncomingResponseHeader" markdown="1">

## modifyIncomingResponseHeader

__Property Manager name__:
[Modify Incoming Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9031)

Modify, add,
remove, or pass along specific response headers coming downstream from
the origin.

Depending on the type of `action` you want to perform, specify the
corresponding _standard_ header name, or a `customHeaderName` if the
standard name is set to `OTHER`.  The `headerValue` serves as a match
condition when the action is `DELETE` or `MODIFY`, and the
`newHeaderValue` applies when the action is `ADD` or `MODIFY`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader),
[`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader), and
[`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyIncomingResponseHeader.action" >

- `action` (_enum string_):
    Either `ADD`, `DELETE`, `MODIFY`, or `PASS` incoming HTTP response
headers.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_):
    If the value of `action` is `ADD`, this specifies the name of the
field to add, any of the following values:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
CACHE_CONTROL
CONTENT_TYPE
EDGE_CONTROL
EXPIRES
LAST_MODIFIED
OTHER
</pre>

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_):
    If the value of `action` is `DELETE`, this specifies the name of
the field to remove, either `CACHE_CONTROL`, `CONTENT_TYPE`, `VARY`,
or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_):
    If the value of `action` is `MODIFY`, this specifies the name of
the field to modify, either `CACHE_CONTROL`, `CONTENT_TYPE`,
`EDGE_CONTROL`, or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.standardPassHeaderName" >

- `standardPassHeaderName` (_enum string_):
    If the value of `action` is `PASS`, this specifies the name of the
field to pass through, either `CACHE_CONTROL`, `EXPIRES`, `PRAGMA`, or
`OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_):
    Specifies a custom field name that applies when the relevant
_standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_):
    With the `action` set to `ADD`, specifies the header's new
value.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_):
    With the `action` set to `MODIFY`, specifies an HTTP header
replacement value.

</div>

<div class="option" markdown="1" id="modifyIncomingResponseHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_):
    When enabled with the `action` set to `MODIFY`, prevents creation
of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyOutgoingRequestHeader" markdown="1">

## modifyOutgoingRequestHeader

__Property Manager name__:
[Modify Outgoing Request Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9073)

Modify, add,
remove, or pass along specific request headers going upstream towards
the origin.

Depending on the type of `action` you want to perform, specify the
corresponding _standard_ header name, or a `customHeaderName` if the
standard name is set to `OTHER`.  The `headerValue` serves as a match
condition when the action is `DELETE` or `MODIFY`, and the
`newHeaderValue` applies when the action is `ADD` or `MODIFY`.
Whole-text replacements apply when the action is `MODIFY`, and
substitutions apply when set to `REGEX`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader),
[`modifyIncomingResponseHeader`](#modifyincomingresponseheader), and
[`modifyOutgoingResponseHeader`](#modifyoutgoingresponseheader).

__Options__:

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.action" >

- `action` (_enum string_):
    Either `ADD` or `DELETE` outgoing HTTP request headers, `MODIFY`
their fixed values, or specify a `REGEX` pattern to transform them.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_):
    If the value of `action` is `ADD`, this specifies the name of the
field to add, either `USER_AGENT` or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_):
    If the value of `action` is `DELETE`, this specifies the name of
the field to remove, either `PRAGMA`, `USER_AGENT`, `VIA`, or
`OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_):
    If the value of `action` is `MODIFY` or `REGEX`, this specifies
the name of the field to modify, either `USER_AGENT` or `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_):
    Specifies a custom field name that applies when the relevant
_standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_):
    With the `action` set to `ADD`, specifies the new header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_):
    With the `action` set to `MODIFY`, specifies an HTTP header
replacement value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.regexHeaderMatch" >

- `regexHeaderMatch` (_string; allows [variables](#vf)_):
    When the `action` is `REGEX`, specifies a Perl-compatible regular
expression to match within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.regexHeaderReplace" >

- `regexHeaderReplace` (_string; allows [variables](#vf)_):
    When the `action` is `REGEX`, specifies text that replaces the
`regexHeaderMatch` pattern within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.matchMultiple" >

- `matchMultiple` (_boolean_):
    When enabled with the `action` set to `REGEX`, replaces all
occurrences of the matched regular expression, otherwise only the
first match if disabled.

</div>

<div class="option" markdown="1" id="modifyOutgoingRequestHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_):
    When enabled with the `action` set to `MODIFY`, prevents creation
of more than one instance of a header.

</div>

</div>

<div class="feature" data-feature="modifyOutgoingResponseHeader" markdown="1">

## modifyOutgoingResponseHeader

__Property Manager name__:
[Modify Outgoing Response Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9052)

Modify, add,
remove, or pass along specific response headers going downstream
towards the client.

Depending on the type of `action` you want to perform, specify the
corresponding _standard_ header name, or a `customHeaderName` if the
standard name is set to `OTHER`. The `headerValue` serves as a match
condition when the action is `DELETE` or `MODIFY`, and the
`newHeaderValue` applies when the action is `ADD` or `MODIFY`.
Whole-text replacements apply when the action is `MODIFY`, and
substitutions apply when set to `REGEX`.

See also [`modifyIncomingRequestHeader`](#modifyincomingrequestheader),
[`modifyIncomingResponseHeader`](#modifyincomingresponseheader), and
[`modifyOutgoingRequestHeader`](#modifyoutgoingrequestheader)

__Options__:

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.action" >

- `action` (_enum string_):
    Either `ADD` or `DELETE` outgoing HTTP response headers, `MODIFY`
their fixed values, or specify a `REGEX` pattern to transform them.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardAddHeaderName" >

- `standardAddHeaderName` (_enum string_):
    If the value of `action` is `ADD`, this specifies the name of the
field to add, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ACCESS_CONTROL_ALLOW_CREDENTIALS
ACCESS_CONTROL_ALLOW_HEADERS
ACCESS_CONTROL_ALLOW_METHODS
ACCESS_CONTROL_ALLOW_ORIGIN
ACCESS_CONTROL_EXPOSE_HEADERS
ACCESS_CONTROL_MAX_AGE
CACHE_CONTROL
CONTENT_DISPOSITION
CONTENT_TYPE
EDGE_CONTROL
OTHER
P3P
PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardDeleteHeaderName" >

- `standardDeleteHeaderName` (_enum string_):
    If the value of `action` is `DELETE`, this specifies the name of
the field to remove, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ACCESS_CONTROL_ALLOW_CREDENTIALS
ACCESS_CONTROL_ALLOW_HEADERS
ACCESS_CONTROL_ALLOW_METHODS
ACCESS_CONTROL_ALLOW_ORIGIN
ACCESS_CONTROL_EXPOSE_HEADERS
ACCESS_CONTROL_MAX_AGE
CACHE_CONTROL
CONTENT_DISPOSITION
CONTENT_TYPE
EXPIRES
OTHER
P3P
PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.standardModifyHeaderName" >

- `standardModifyHeaderName` (_enum string_):
    If the value of `action` is `MODIFY` or `REGEX`, this specifies
the name of the field to modify, any of the following values:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ACCESS_CONTROL_ALLOW_CREDENTIALS
ACCESS_CONTROL_ALLOW_HEADERS
ACCESS_CONTROL_ALLOW_METHODS
ACCESS_CONTROL_ALLOW_ORIGIN
ACCESS_CONTROL_EXPOSE_HEADERS
ACCESS_CONTROL_MAX_AGE
CACHE_CONTROL
CONTENT_DISPOSITION
CONTENT_TYPE
OTHER
P3P
PRAGMA
</pre>

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.customHeaderName" >

- `customHeaderName` (_string; allows [variables](#vf)_):
    Specifies a custom field name that applies when the relevant
_standard_ header name is set to `OTHER`.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.headerValue" >

- `headerValue` (_string; allows [variables](#vf)_):
    Specifies the existing value of the header to match.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.newHeaderValue" >

- `newHeaderValue` (_string; allows [variables](#vf)_):
    With the `action` set to `MODIFY`, specifies the new HTTP header
replacement value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.regexHeaderMatch" >

- `regexHeaderMatch` (_string_):
    When the `action` is `REGEX`, specifies a Perl-compatible regular
expression to match within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.regexHeaderReplace" >

- `regexHeaderReplace` (_string; allows [variables](#vf)_):
    When the `action` is `REGEX`, specifies text that replaces the
`regexHeaderMatch` pattern within the header value.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.matchMultiple" >

- `matchMultiple` (_boolean_):
    When enabled with the `action` set to `REGEX`, replaces all
occurrences of the matched regular expression, otherwise only the
first match if disabled.

</div>

<div class="option" markdown="1" id="modifyOutgoingResponseHeader.avoidDuplicateHeaders" >

- `avoidDuplicateHeaders` (_boolean_):
    When enabled with the `action` set to `MODIFY`, prevents creation
of more than one instance of a header. The last header clobbers others
with the same name. This option affects the entire set of outgoing
headers, and is not confined to the subset of regular expression
matches.

</div>

</div>

<div class="feature" data-feature="modifyViaHeader" markdown="1">

## modifyViaHeader

__Property Manager name__:
[Modify Via Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5027)

2DO

__Options__:

<div class="option" markdown="1" id="modifyViaHeader.enabled" >

- `enabled` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="modifyViaHeader.modificationOption" >

- `modificationOption` (_enum string_):
    2DO: `REMOVE_HEADER`, `RENAME_HEADER`

</div>

<div class="option" markdown="1" id="modifyViaHeader.renameHeaderTo" >

- `renameHeaderTo` (_string_):
    2DO

</div>

</div>

<div class="feature" data-feature="mPulse" markdown="1">

## mPulse

__Property Manager name__:
[mPulse](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0055)

[mPulse](https://learn.akamai.com/en-us/products/web_performance/mpulse.html)
provides high-level performance analytics and predictive
recommendations based on real end user data. See the
[mPulse Quick Start](https://learn.akamai.com/en-us/webhelp/mpulse/mpulse-help/)
to set up mPulse on your website.

__Options__:

<div class="option" markdown="1" id="mPulse.enabled" >

- `enabled` (_boolean_):
    Applies performance
monitoring to this behavior's set of content.

</div>

<div class="option" markdown="1" id="mPulse.requirePci" >

- `requirePci` (_boolean_):
    Suppresses
gathering metrics for potentially sensitive end-user interactions.
Enabling this omits data from some older browsers.

</div>

<div class="option" markdown="1" id="mPulse.apiKey" >

- `apiKey` (_string_):
    This generated
value uniquely identifies sections of your website for you to analyze
independently. To access this value, see
[Enable mPulse in Property Manager](https://learn-qa.akamai.com/en-us/webhelp/mpulse/mpulse-help/GUID-8F356E35-C374-4598-90D7-5BE8CE770369.html).

</div>

<div class="option" markdown="1" id="mPulse.bufferSize" >

- `bufferSize` (_string_):
    Allows you
to override the browser's default (150) maximum number of reported
performance timeline entries.

</div>

<div class="option" markdown="1" id="mPulse.configOverride" >

- `configOverride` (_string_):
    A JSON
string representing a configuration object passed to the JavaScript
library under which mPulse runs. It corresponds at run-time to the
`window.BOOMR_config` object. For example, this turns on monitoring
of Single Page App frameworks: `"{\"history\": {\"enabled\":
true, \"auto\": true}}"`.  See
[Configuration Overrides](https://developer.akamai.com/tools/boomerang/#configuration-overrides)
for more information.

</div>

</div>

<div class="feature" data-feature="netSession" markdown="1">

## netSession

__Property Manager name__:
[NetSession](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9058)

This behavior enables various
features of
[NetSession](https://learn.akamai.com/en-us/products/media_delivery/netsession_download_manager.html),
a client-side download manager application that's especially
appropriate for large file downloads.  For the feature to work, the
end user needs to download the DLM client.

__Options__:

<div class="option" markdown="1" id="netSession.enabled" >

- `enabled` (_boolean_):
    Enables
NetSession DLM capabilities for this content.

</div>

<div class="option" markdown="1" id="netSession.enableDomain" >

- `enableDomain` (_boolean_):
    Enables
Download Manager domains.

</div>

<div class="option" markdown="1" id="netSession.enableDownloadManager" >

- `enableDownloadManager` (_boolean_):
    When
enabled, launches files once they are fully downloaded. For example,
specify this option to run an executable application.

</div>

<div class="option" markdown="1" id="netSession.enableDownloadClients" >

- `enableDownloadClients` (_boolean_):
    When enabled, allows download clients to form a peer-to-peer network
to reduce transmission time.

</div>

<div class="option" markdown="1" id="netSession.disableReporting" >

- `disableReporting` (_boolean_):
    Disable download state reporting via HTTP beacon messages. Otherwise
when enabled, you can view the state of each download by choosing
__Monitor__ &rArr; __Download Analytics__ on the DLM client.

</div>

<div class="option" markdown="1" id="netSession.resumeUrl" >

- `resumeUrl` (_array of string values_):
    Specify an
alternate domain from which to resume a paused download. This
generates a corresponding shortcut link on the end user's desktop that
disappears after the download is complete.

</div>

<div class="option" markdown="1" id="netSession.organizationName" >

- `organizationName` (_string_):
    The
name of the organization that displays in the NetSession client DLM
interface.

</div>

<div class="option" markdown="1" id="netSession.supportUrl" >

- `supportUrl` (_string_):
    A
supporting link to the `organizationName` that displays in the NetSession
client DLM interface.

</div>

</div>

<div class="feature" data-feature="networkConditionsHeader" markdown="1">

## networkConditionsHeader

__Property Manager name__:
[Network Conditions Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9051)

Instructs edge
servers to send an `X-Akamai-Network-Condition` header to the origin
assessing the quality of the network.

__Options__:

<div class="option" markdown="1" id="networkConditionsHeader.behavior" >

- `behavior` (_enum string_):
    If set to `TWO_TIER`, assessment is either `Excellent` or `Poor`. If
set to `THREE_TIER`, the assessment can also be `Fair`.

</div>

</div>

<div class="feature" data-feature="origin" markdown="1">

## origin

__Property Manager name__:
[Origin Server](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0058)

Specify the hostname and settings
used to contact the origin once service begins. You can use your own
origin,
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html),
an
[Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf)
origin, or a
[SaaS](https://control.akamai.com/dl/customers/SaaS/SaaS-User-Guide.pdf)
dynamic origin.

__Options__:

<div class="option" markdown="1" id="origin.originType" >

- `originType` (_enum string_):
    Choose whether
your content is retrieved from your own server (`CUSTOMER`), your
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
account (`NET_STORAGE`), any available
[Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf)
origin (`EDGE_LOAD_BALANCING_ORIGIN_GROUP`), a set of
[Application Load Balancer](#applicationloadbalancer) origins
(`APPLICATION_LOAD_BALANCER`), a SaaS dynamic origin
(`SAAS_DYNAMIC_ORIGIN`) if SaaS acceleration is available on your
contract, or `MEDIA_SERVICE_LIVE`. NetStorage is most appropriate for
static content.

</div>

<div class="option" markdown="1" id="origin.netStorage" >

- `netStorage` (_object_):
    If the `originType`
is `NET_STORAGE`, this option specifies the details of the netstorage
server. For example:

        "netStorage": {
            "id"                 : "netstorage_id",
            "name"               : "Example Downloads",
            "downloadDomainName" : "download.example.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="origin.originId" >

- `originId` (_string_):
    With the
`originType` set to `EDGE_LOAD_BALANCING_ORIGIN_GROUP`, identifies the
Edge Load Balancing origin. This must correspond to an
[`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior's
`id` attribute within the same property.

</div>

<div class="option" markdown="1" id="origin.hostname" >

- `hostname` (_string; allows [variables](#vf)_):
    With the
`originType` set to `CUSTOMER`, this specifies the hostname or IPv4
address of your origin server, from which edge servers can retrieve
your content.

</div>

<div class="option" markdown="1" id="origin.mslorigin" >

- `mslorigin` (_string_):
    With
`originType` set to `MEDIA_SERVICE_LIVE`, this specifies the media's
origin server.

</div>

<div class="option" markdown="1" id="origin.saasType" >

- `saasType` (_enum string_):
    With `originType` set
to `SAAS_DYNAMIC_ORIGIN`, specifies the part of the request that
identifies this SaaS dynamic origin, either `PATH`, `COOKIE`,
`QUERY_STRING`, or `HOSTNAME`.

</div>

<div class="option" markdown="1" id="origin.saasCnameEnabled" >

- `saasCnameEnabled` (_boolean_):
    With
`saasType` set to `HOSTNAME`, enabling this allows you to use a
_CNAME chain_ to determine the hostname for this SaaS dynamic
origin.

</div>

<div class="option" markdown="1" id="origin.saasCnameLevel" >

- `saasCnameLevel` (_number_):
    With
`saasType` set to `HOSTNAME` and `saasCnameEnabled` on, specifies
the desired number of hostnames to use in the _CNAME chain_, starting
backwards from the edge server.

</div>

<div class="option" markdown="1" id="origin.saasCookie" >

- `saasCookie` (_string_):
    With the
`originType` set to `SAAS_DYNAMIC_ORIGIN` and the `saasType` set to
`COOKIE`, this specifies the name of the cookie that identifies this
SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasQueryString" >

- `saasQueryString` (_string_):
    With the
`originType` set to `SAAS_DYNAMIC_ORIGIN` and the `saasType` set to
`QUERY_STRING`, this specifies the name of the query parameter that
identifies this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasRegex" >

- `saasRegex` (_string_):
    With the `originType`
set to `SAAS_DYNAMIC_ORIGIN`, this specifies the Perl-compatible
regular expression match that identifies this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasReplace" >

- `saasReplace` (_string_):
    Specifies
replacement text for what `saasRegex` matches.

</div>

<div class="option" markdown="1" id="origin.saasSuffix" >

- `saasSuffix` (_string_):
    With the
`originType` set to `SAAS_DYNAMIC_ORIGIN`, specifies the static part of the
SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.forwardHostHeader" >

- `forwardHostHeader` (_enum string_):
    When the
`originType` is set to either `CUSTOMER` or `SAAS_DYNAMIC_ORIGIN`, this
specifies which `Host` header to pass to the origin:

    - `REQUEST_HOST_HEADER` passes the original request's header.
    - `ORIGIN_HOSTNAME` passes the current origin's `HOSTNAME`.
    - `CUSTOM` passes the value of `customForwardHostHeader`. Use this     option if you want requests handled by different properties to     converge on the same cached object.

</div>

<div class="option" markdown="1" id="origin.customForwardHostHeader" >

- `customForwardHostHeader` (_string; allows [variables](#vf)_):
    With `forwardHostHeader` set to `CUSTOM`, this specifies the name of
the custom host header the edge server should pass to the origin.

</div>

<div class="option" markdown="1" id="origin.cacheKeyHostname" >

- `cacheKeyHostname` (_enum string_):
    With the
`originType` set to `CUSTOM`, this specifies the hostname to use when
forming a cache key. Specify `ORIGIN_HOSTNAME` if your origin server's
responses do not depend on the hostname, otherwise specify
`REQUEST_HOST_HEADER` when using a virtual server.

</div>

<div class="option" markdown="1" id="origin.useUniqueCacheKey" >

- `useUniqueCacheKey` (_boolean_):
    With
`cacheKeyHostname` set to `ORIGIN_HOSTNAME` and a shared `hostname`
such as provided by Amazon AWS, sets a unique cache key for your
content.

</div>

<div class="option" markdown="1" id="origin.compress" >

- `compress` (_boolean_):
    Enables _gzip_
compression for non-NetStorage origins.

</div>

<div class="option" markdown="1" id="origin.enableTrueClientIp" >

- `enableTrueClientIp` (_boolean_):
    When enabled
on non-NetStorage origins, allows you to send a custom header (the
`trueClientIpHeader`) identifying the IP address of the immediate client
connecting to the edge server. This may provide more useful
information than the standard `X-Forward-For` header, which proxies
may modify.

</div>

<div class="option" markdown="1" id="origin.trueClientIpHeader" >

- `trueClientIpHeader` (_string_):
    With
`enableTrueClientIp` enabled, this specifies the name of the field
that identifies the end client's IP address, for example
`True-Client-IP`.

</div>

<div class="option" markdown="1" id="origin.trueClientIpClientSetting" >

- `trueClientIpClientSetting` (_boolean_):
    With `enableTrueClientIp` on along with this option, if a client sets the
`True-Client-IP` header, the edge server allows it and passes the
value to the origin. Otherwise the edge server removes it and sets the
value itself.

</div>

<div class="option" markdown="1" id="origin.verificationMode" >

- `verificationMode` (_enum string_):
    For
non-NetStorage origins, maximize security by controlling which
certificates edge servers should trust, either `PLATFORM_SETTINGS`,
`THIRD_PARTY` when your origin server references certain types of
third-party hostname, or `CUSTOM`. The `CUSTOM` option only applies if
the property is marked as secure. See
[Secure property requirements](#sf) for guidance. Under some products,
you may also need to enable the _Secure Delivery - Customer Cert_
module. Contact your Akamai representative for details.

</div>

<div class="option" markdown="1" id="origin.originSni" >

- `originSni` (_boolean_):
    For
non-NetStorage origins, enabling this adds a Server Name Indication
(SNI) header in the SSL request sent to the origin, with the origin
hostname as the value.  Contact your Akamai representative for more
information.

</div>

<div class="option" markdown="1" id="origin.customValidCnValues" >

- `customValidCnValues` (_array of string values_):
    With
`verificationMode` set to `CUSTOM`, specifies values to look for in
the origin certificate's `Subject Alternate Name` or `Common Name`
fields. Specify `{{ "{{" }}Origin Hostname}}` and `{{ "{{" }}Forward Host Header}}`
within the text in the order you want them to be evaluated.
(Note that these two template items are not the same as in-line
[variables](#vf), which use the same curly-brace syntax.)

</div>

<div class="option" markdown="1" id="origin.originCertsToHonor" >

- `originCertsToHonor` (_enum string_):
    With
`verificationMode` set to `CUSTOM`, specifies whether to trust
pinned origin server certificates (`CUSTOM_CERTIFICATES`), any certificate
signed by an Akamai-managed authority set (`STANDARD_CERTIFICATE_AUTHORITIES`), or any
certificate signed by a custom authority set you manage
(`CUSTOM_CERTIFICATE_AUTHORITIES`). If set to `COMBO`, may rely on all three inputs.

</div>

<div class="option" markdown="1" id="origin.standardCertificateAuthorities" >

- `standardCertificateAuthorities` (_object_):
    With `originCertsToHonor` set to either `STANDARD_CERTIFICATE_AUTHORITIES` or
`COMBO`, specifies an array of Akamai-managed certificate
names. Currently, the only allowed value is `akamai-permissive`.

</div>

<div class="option" markdown="1" id="origin.customCertificateAuthorities" >

- `customCertificateAuthorities` (_object_):
    With `originCertsToHonor` set to either `CUSTOM_CERTIFICATE_AUTHORITIES` or `COMBO`,
specifies an array of certification objects. Contact your Akamai
representative for details on this object's requirements.

</div>

<div class="option" markdown="1" id="origin.customCertificates" >

- `customCertificates` (_object_):
    With `originCertsToHonor` set to either `CUSTOM_CERTIFICATES` or
`COMBO`, specifies an array of certification objects. Contact your
Akamai representative for details on this object's requirements.

</div>

<div class="option" markdown="1" id="origin.httpPort" >

- `httpPort` (_number_):
    Specifies the
port on your origin server to which edge servers should connect for
HTTP requests, customarily `80`.

</div>

<div class="option" markdown="1" id="origin.httpsPort" >

- `httpsPort` (_number_):
    Specifies the
port on your origin server to which edge servers should connect for
secure HTTPS requests, customarily `443`. This option only applies if
the property is marked as secure. See
[Secure property requirements](#sf) for guidance.

</div>

</div>

<div class="feature" data-feature="originCharacteristics" markdown="1">

## originCharacteristics

__Property Manager name__:
[Origin Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0059)

Specifies
characteristics of the origin. Akamai uses this information to
optimize your metadata configuration, which may result in better
origin offload and end-user performance.

See also [`clientCharacteristics`](#clientcharacteristics) and
various product-specific behaviors whose names are prefixed
_contentCharacteristics_.

__Options__:

<div class="option" markdown="1" id="originCharacteristics.country" >

- `country` (_enum string_):
    Specifies the origin's geographic region, or `UNKNOWN` to defer any
optimizations based on geography. Regions include `GLOBAL_MULTI_GEO`,
`EUROPE`, `NORDICS`, `GERMANY`, `UNITED_KINGDOM`, `ITALY`, `INDIA`,
`JAPAN`, `TAIWAN`, `ASIA_PACIFIC`, `AUSTRALIA`, `LATIN_AMERICA`,
`MEXICO`, `SOUTH_AMERICA`, `US_CENTRAL`, `US_EAST`, `US_WEST`,
`NORTH_AMERICA`, `OTHER_AMERICAS`, `OTHER_APJ` (Asia, Pacific, Japan),
`OTHER_EMEA` (Europe, Middle East, Africa), or `ADC` for Akamai Direct
Connection, available to Adaptive Media Delivery customers.

</div>

<div class="option" markdown="1" id="originCharacteristics.directConnectGeo" >

- `directConnectGeo` (_string_):
    With `country` set to `ADC`, provides a region used by Akamai
Direct Connection.

</div>

<div class="option" markdown="1" id="originCharacteristics.authenticationMethod" >

- `authenticationMethod` (_enum string_):
    Specifies the authentication method, either `AWSV4` (Amazon Web
Services), `GCP` (Google Cloud Platform), or `AUTOMATIC`.  With the
Adaptive Media Delivery product, choose additional
`SIGNATURE_HEADER_AUTHENTICATION` or `MSL_AUTHENTICATION` options.

</div>

<div class="option" markdown="1" id="originCharacteristics.encodingVersion" >

- `encodingVersion` (_numeric enum_):
    With `authenticationMethod` set to
`SIGNATURE_HEADER_AUTHENTICATION`, specifies the version of the
encryption algorithm, an integer from `1` to `5`.
<!-- `2`, `3`, `4` -->

</div>

<div class="option" markdown="1" id="originCharacteristics.useCustomSignString" >

- `useCustomSignString` (_boolean_):
    With `authenticationMethod` set to
`SIGNATURE_HEADER_AUTHENTICATION`, specifies whether to customize your
signed string.

</div>

<div class="option" markdown="1" id="originCharacteristics.customSignString" >

- `customSignString` (_array of string values_):
    With `useCustomSignString` enabled, specifies the data to be
encrypted as a sequence of concatenated strings. The array may include
any of the following enumerated values: `AK_CLIENT_REAL_IP`,
`AK_DOMAIN`, `AK_EXTENSION`, `AK_FILENAME`, `AK_HOSTHEADER`,
`AK_METHOD`, `AK_PATH`, `AK_QUERY`, `AK_SCHEME`, and `AK_URL`.
See [Support for variables](#vf) for guidance.

</div>

<div class="option" markdown="1" id="originCharacteristics.secretKey" >

- `secretKey` (_string_):
    Specifies the shared secret key.

</div>

<div class="option" markdown="1" id="originCharacteristics.nonce" >

- `nonce` (_string_):
    Specifies the nonce.

</div>

<div class="option" markdown="1" id="originCharacteristics.mslkey" >

- `mslkey` (_string_):
    With
`authenticationMethod` set to `MSL_AUTHENTICATION`, specifies the
access key provided by the hosting service.

</div>

<div class="option" markdown="1" id="originCharacteristics.mslname" >

- `mslname` (_string_):
    With `authenticationMethod` set to `MSL_AUTHENTICATION`, specifies
the origin name provided by the hosting service.

</div>

<div class="option" markdown="1" id="originCharacteristics.accessKeyEncryptedStorage" >

- `accessKeyEncryptedStorage` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsAccessKeyVersionGuid" >

- `gcsAccessKeyVersionGuid` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsHmacKeyAccessId" >

- `gcsHmacKeyAccessId` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.gcsHmacKeySecret" >

- `gcsHmacKeySecret` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsAccessKeyVersionGuid" >

- `awsAccessKeyVersionGuid` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsAccessKeyId" >

- `awsAccessKeyId` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsSecretAccessKey" >

- `awsSecretAccessKey` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsRegion" >

- `awsRegion` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="originCharacteristics.awsService" >

- `awsService` (_string_):
    2DO

</div>

</div>

<div class="feature" data-feature="originCharacteristicsWsd" markdown="1">

## originCharacteristicsWsd

__Property Manager name__:
[Origin Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0059)

Specifies
characteristics of the origin, for use in Akamai's Wholesale Delivery
product.

__Options__:

<div class="option" markdown="1" id="originCharacteristicsWsd.origintype" >

- `origintype` (_enum string_):
    Specifies `AZURE` or an `UNKNOWN` origin type.

</div>

</div>

<div class="feature" data-feature="persistentClientConnection" markdown="1">

## persistentClientConnection

__Property Manager name__:
[Persistent Connections: Client to Edge](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0060)

This
[read-only behavior](#ro) activates _persistent connections_ between
edge servers and clients, which allow for better performance and more
efficient use of resources. Compare with the
[`persistentConnection`](#persistentconnection) behavior, which
configures persistent connections for the entire journey from origin
to edge to client.  Contact Akamai Professional Services for help
configuring either.

> __WARNING__: Disabling or removing this behavior may negatively
affect performance.

__Options__:

<div class="option" markdown="1" id="persistentClientConnection.enabled" >

- `enabled` (_boolean_):
    Enables the persistent connections behavior.

</div>

<div class="option" markdown="1" id="persistentClientConnection.timeout" >

- `timeout` (_duration string_):
    Specifies the timeout period after which edge server closes the
persistent connection with the client, 500 seconds by default.

</div>

</div>

<div class="feature" data-feature="persistentConnection" markdown="1">

## persistentConnection

__Property Manager name__:
[Persistent Connections: Edge to Origin](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0060)

A [read-only
behavior](#ro) that enables more efficient _persistent connections_
from origin to edge server to client. Compare with the
[`persistentClientConnection`](#persistentclientconnection) behavior,
which customizes persistent connections from edge to client. Contact
Akamai Professional Services for help configuring either.

> __WARNING__: Disabling this behavior wastes valuable browser
resources. Leaving connections open too long makes them vulnerable to
attack. Avoid both of these scenarios.

__Options__:

<div class="option" markdown="1" id="persistentConnection.enabled" >

- `enabled` (_boolean_):
    Enables persistent connections.

</div>

<div class="option" markdown="1" id="persistentConnection.timeout" >

- `timeout` (_duration string_):
    Specifies the timeout period after which edge server closes a
persistent connection.

</div>

</div>

<div class="feature" data-feature="personallyIdentifiableInformation" markdown="1">

## personallyIdentifiableInformation

__Property Manager name__:
[Personally Identifiable Information](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0061)

Marks
content covered by the current rule as sensitive _personally
identifiable information_ that needs to be treated as secure and
private. That includes anything involving personal information: name,
social security number, date and place of birth, mother's maiden name,
biometric data, or any other data linked to an individual. If you
attempt to save a property with such a rule that also caches or logs
sensitive content, the added behavior results in a validation error.

> __WARNING__: This feature only identifies some vulnerabilities. For
example, it does not prevent you from including secure information in
a query string or writing it to an origin folder. It also can't tell
whether the SSL protocol is in effect.

__Options__:

<div class="option" markdown="1" id="personallyIdentifiableInformation.enabled" >

- `enabled` (_boolean_):
    When enabled, marks content as personally identifiable information
(PII).

</div>

</div>

<div class="feature" data-feature="phasedRelease" markdown="1">

## phasedRelease

__Property Manager name__:
[Phased Release Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0062)

The Phased Release
Cloudlet provides gradual and granular traffic management to an
alternate origin in near real time.  Use the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html)
or the Cloudlets Policy Manager application within
[Control Center](https://control.akamai.com)
to set up your Cloudlets policies.

__Options__:

<div class="option" markdown="1" id="phasedRelease.enabled" >

- `enabled` (_boolean_):
    Enables the Phased Release Cloudlet.

</div>

<div class="option" markdown="1" id="phasedRelease.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Specifies the Cloudlet policy as an object containing two members: a
descriptive `name` string and an integer `id` set by the Cloudlet
application.

</div>

<div class="option" markdown="1" id="phasedRelease.label" >

- `label` (_string_):
    A
label to distinguish this Phased Release policy from any others
within the same property.

</div>

<div class="option" markdown="1" id="phasedRelease.populationCookieType" >

- `populationCookieType` (_enum string_):
    For the population of users the Cloudlet defines, select whether
to assign a cookie to them, or else `NONE`.  Other option values
specify when the cookie expires: after a specific `DURATION`, at a
`FIXED_DATE`, once the browser session ends (`ON_BROWSER_CLOSE`), or
`NEVER`. If you select the Cloudlet's _random_ membership option, it
overrides the option value so that it is effectively `NONE`.

</div>

<div class="option" markdown="1" id="phasedRelease.populationExpirationDate" >

- `populationExpirationDate` (_ISO 8601 format date/time string_):
    With the `populationCookieType` set to `FIXED_DATE`, this
specifies the date and time when membership expires, and the browser
no longer sends the cookie. Subsequent requests re-evaluate based on
current membership settings.

</div>

<div class="option" markdown="1" id="phasedRelease.populationDuration" >

- `populationDuration` (_duration string_):
    With the `populationCookieType` set to `DURATION`, this sets the
lifetime of the cookie from the initial request. Subsequent requests
re-evaluate based on current membership settings.

</div>

<div class="option" markdown="1" id="phasedRelease.populationRefresh" >

- `populationRefresh` (_boolean_):
    With the `populationCookieType` set to `DURATION`, enabling this
option resets the original duration of the cookie if the browser
refreshes before the cookie expires.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverEnabled" >

- `failoverEnabled` (_boolean_):
    Allows failure responses at the origin defined by the Cloudlet to
fail over to the prevailing origin defined by the property.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverResponseCode" >

- `failoverResponseCode` (_array of string values_):
    With `failoverEnabled` on, this defines the set of failure codes
that initiate the failover response.

</div>

<div class="option" markdown="1" id="phasedRelease.failoverDuration" >

- `failoverDuration` (_number within 0-300 range_):
    Specifies the number of seconds to wait until the client tries to
access the failover origin after the initial failure is detected. Set
the value to `0` to immediately request the alternate origin upon
failure.

</div>

</div>

<div class="feature" data-feature="preconnect" markdown="1">

## preconnect

__Property Manager name__:
[Manual Preconnect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9029)

With the [`http2`](#http2)
behavior enabled, this requests a specified set of domains that relate
to your property hostname, and keeps the connection open for faster
loading of content from those domains.

__Options__:

<div class="option" markdown="1" id="preconnect.preconnectlist" >

- `preconnectlist` (_array of string values_):
    Specifies the set of hostnames to which to preconnect over HTTP2.

</div>

</div>

<div class="feature" data-feature="predictivePrefetching" markdown="1">

## predictivePrefetching

__Property Manager name__:
[Predictive Prefetching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0063)

This behavior
potentially reduces the client's page load time by pre-caching objects
based on historical data for the page, not just its current set of
referenced objects. It also detects second-level dependencies, such as
objects retrieved by JavaScript.

__Options__:

<div class="option" markdown="1" id="predictivePrefetching.enabled" >

- `enabled` (_boolean_):
    Enables
the predictive prefetching behavior.

</div>

<div class="option" markdown="1" id="predictivePrefetching.accuracyTarget" >

- `accuracyTarget` (_enum string_):
    The
level of prefetching, either `LOW`, `MEDIUM`, or `HIGH`. A higher level
results in better client performance, but potentially greater load on
the origin.

</div>

</div>

<div class="feature" data-feature="prefetch" markdown="1">

## prefetch

__Property Manager name__:
[Prefetch Objects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0064)

Instructs edge servers to retrieve
content linked from requested pages as they load, rather than waiting
for separate requests for the linked content. This behavior applies
depending on the rule's set of matching conditions. Use in
conjunction with the [`prefetchable`](#prefetchable)
behavior, which specifies the set of objects to prefetch.

__Options__:

<div class="option" markdown="1" id="prefetch.enabled" >

- `enabled` (_boolean_):
    Applies prefetching
behavior when enabled.

</div>

</div>

<div class="feature" data-feature="prefetchable" markdown="1">

## prefetchable

__Property Manager name__:
[Prefetchable Objects](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0064)

Allow matching objects to
prefetch into the edge cache as the parent page that links to them
loads, rather than waiting for a direct request. This behavior applies
depending on the rule's set of matching conditions. Use
[`prefetch`](#prefetch) to enable the overall behavior for parent
pages that contain links to the object. To apply this behavior, you
need to match on a [`filename`](#filename) or
[`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="prefetchable.enabled" >

- `enabled` (_boolean_):
    When enabled,
allows matching content to prefetch when referenced on a requested
parent page.

</div>

</div>

<div class="feature" data-feature="prefreshCache" markdown="1">

## prefreshCache

__Property Manager name__:
[Cache Prefreshing](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0065)

Refresh cached content
before its time-to-live (TTL) expires, to keep end users from having
to wait for the origin to provide fresh content.

Prefreshing starts asynchronously based on a percentage of remaining
TTL. The edge serves the prefreshed content only after the TTL
expires. If the percentage is set too high, and there is not enough
time to retrieve the object, the end user waits for it to refresh from
the origin, as is true by default without this prefresh behavior
enabled. The edge does not serve stale content.

__Options__:

<div class="option" markdown="1" id="prefreshCache.enabled" >

- `enabled` (_boolean_):
    Enables the
cache prefreshing behavior.

</div>

<div class="option" markdown="1" id="prefreshCache.prefreshval" >

- `prefreshval` (_number within 0-99 range_):
    Specifies when the prefresh occurs as a percentage of the TTL. For
example, for an object whose cache has 10 minutes left to live, and an
origin response that is routinely less than 30 seconds, a percentage
of `95` prefreshes the content without unnecessarily increasing load
on the origin.

</div>

</div>

<div class="feature" data-feature="quicBeta" markdown="1">

## quicBeta

__Property Manager name__:
[Quic Support](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9027)

For a share of responses,
includes an `Alt-Svc` header for compatible clients to initiate
subsequent sessions using the QUIC protocol.

__Options__:

<div class="option" markdown="1" id="quicBeta.enabled" >

- `enabled` (_boolean_):
    Enables QUIC
support.

</div>

<div class="option" markdown="1" id="quicBeta.quicOfferPercentage" >

- `quicOfferPercentage` (_number within 1-50 range_):
    The
percentage of responses for which to allow QUIC sessions.

</div>

</div>

<div class="feature" data-feature="randomSeek" markdown="1">

## randomSeek

__Property Manager name__:
[Random Seek](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0067)

Optimizes `.flv` and `.mp4`
files to allow random jump-point navigation.

__Options__:

<div class="option" markdown="1" id="randomSeek.flv" >

- `flv` (_boolean_):
    Enables random seek
optimization in FLV files.

</div>

<div class="option" markdown="1" id="randomSeek.mp4" >

- `mp4` (_boolean_):
    Enables random seek
optimization in MP4 files.

</div>

<div class="option" markdown="1" id="randomSeek.maximumSize" >

- `maximumSize` (_string_):
    With the
`mp4` option enabled, sets the maximum size of the
MP4 file to optimize, expressed as a number suffixed with a unit
string such as `MB` or `GB`.

</div>

</div>

<div class="feature" data-feature="rapid" markdown="1">

## rapid

__Property Manager name__:
[Akamai API Gateway](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9004)

The [Akamai API
Gateway](https://learn.akamai.com/en-us/products/web_performance/api_gateway.html)
allows you to configure API traffic delivered over the Akamai
network. Apply this behavior to a set of API assets, then use Akamai's
[API Endpoints
API](https://learn.akamai.com/en-us/api/web_performance/api_endpoints/v2.html)
to configure how the traffic responds.  Use the [API Keys and Traffic
Management
API](https://developer.akamai.com/api/web_performance/key_and_quota/v1.html)
to control access to your APIs.

__Options__:

<div class="option" markdown="1" id="rapid.enabled" >

- `enabled` (_boolean_):
    Enables API
Gateway for the current set of content.

</div>

</div>

<div class="feature" data-feature="readTimeout" markdown="1">

## readTimeout

__Property Manager name__:
[Read Timeout](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9002)

A [read-only behavior](#ro)
that specifies how long the edge server should wait for a response
from the requesting forward server after a connection has already been
established. Any failure to read aborts the request and sends a `504`
Gateway Timeout error to the client. Contact Akamai Professional
Services for help configuring this behavior.

__Options__:

<div class="option" markdown="1" id="readTimeout.value" >

- `value` (_duration string_):
    Specifies the read
timeout necessary before failing with a `504` error. This value should
never be zero.

</div>

</div>

<div class="feature" data-feature="realUserMonitoring" markdown="1">

## realUserMonitoring

__Property Manager name__:
[Real User Monitoring](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0068)

Real User Monitoring
(RUM) injects JavaScript into HTML pages served to end-user clients
that monitors page-load performance and reports on various data, such
as browser type and geographic location. The [`report`](#report)
behavior allows you to configure logs.

For more information on this behavior, see the
[Real User Monitoring Guide](https://learn.akamai.com/en-us/webhelp/ion/real-user-monitoring-guide/).

__Options__:

<div class="option" markdown="1" id="realUserMonitoring.enabled" >

- `enabled` (_boolean_):
    When
enabled, activates real-use monitoring.

</div>

</div>

<div class="feature" data-feature="redirect" markdown="1">

## redirect

__Property Manager name__:
[Redirect](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0069)

Respond to the client request
with a redirect without contacting the origin. Specify the redirect as
a path expression starting with a `/` character relative to the
current root, or as a fully qualified URL. This behavior relies
primarily on `destinationHostname` and `destinationPath` to manipulate
the hostname and path independently.

See also the [`redirectplus`](#redirectplus) behavior, which allows
you to use [variables](#vf) more flexibly to express the redirect's
destination.

__Options__:

<div class="option" markdown="1" id="redirect.mobileDefaultChoice" >

- `mobileDefaultChoice` (_enum string_):
    When set to `MOBILE`, allows only a `302` response code. When set to
`DEFAULT`, allows all other `responseCode` values.

</div>

<div class="option" markdown="1" id="redirect.destinationProtocol" >

- `destinationProtocol` (_enum string_):
    Choose the protocol for the redirect URL, either `HTTP`, `HTTPS`, or
`SAME_AS_REQUEST` to pass through the original protocol.

</div>

<div class="option" markdown="1" id="redirect.destinationHostname" >

- `destinationHostname` (_enum string_):
    Specify
how to change the requested hostname, independently from the pathname:

    - `SUBDOMAIN` prepends a subdomain from the     `destinationHostSubdomain` field.
    - `SIBLING` replaces the leftmost subdomain with the     `destinationHostSibling` field.
    - `OTHER` specifies a static domain in the     `destinationHostnameOther` field.
    - `SAME_AS_REQUEST` preserves the hostname unchanged.

</div>

<div class="option" markdown="1" id="redirect.destinationHostSubdomain" >

- `destinationHostSubdomain` (_string; allows [variables](#vf)_):
    If `destinationHostname` is set to `SUBDOMAIN`, this specifies a
subdomain to prepend to the current hostname. For example, a value of
`m` changes `www.example.com` to `m.www.example.com`.

</div>

<div class="option" markdown="1" id="redirect.destinationHostSibling" >

- `destinationHostSibling` (_string; allows [variables](#vf)_):
    If `destinationHostname` is set to `SIBLING`, this specifies the
subdomain with which to replace to the current hostname's leftmost
subdomain. For example, a value of `m` changes `www.example.com` to
`m.example.com`.

</div>

<div class="option" markdown="1" id="redirect.destinationHostnameOther" >

- `destinationHostnameOther` (_string; allows [variables](#vf)_):
    If `destinationHostname` is set to `OTHER`, this specifies the full
hostname with which to replace the current hostname.

</div>

<div class="option" markdown="1" id="redirect.destinationPath" >

- `destinationPath` (_enum string_):
    Specify
how to change the requested pathname, independently from the hostname:

    - `PREFIX_REQUEST` prepends a path with the     `destinationPathPrefix` field. You also have the option to     specify a suffix using `destinationPathSuffix` and     `destinationPathSuffixStatus`.
    - `OTHER` replaces the current path with the     `destinationPathOther` field.
    - `SAME_AS_REQUEST` preserves the current path unchanged.

</div>

<div class="option" markdown="1" id="redirect.destinationPathPrefix" >

- `destinationPathPrefix` (_string; allows [variables](#vf)_):
    When `destinationPath` is set to `PREFIX_REQUEST`, this prepends
the current path. For example, a value of `/prefix/path` changes
`/example/index.html` to `/prefix/path/example/index.html`.

</div>

<div class="option" markdown="1" id="redirect.destinationPathSuffixStatus" >

- `destinationPathSuffixStatus` (_enum string_):
    When `destinationPath` is set to `PREFIX_REQUEST`, this gives you
the option of adding a suffix. Specify `NO_SUFFIX` if you want to
preserve the end of the path unchanged. If you specify `SUFFIX`, the
`destinationPathSuffix` provides the value.

</div>

<div class="option" markdown="1" id="redirect.destinationPathSuffix" >

- `destinationPathSuffix` (_string; allows [variables](#vf)_):
    When `destinationPath` is set to `PREFIX_REQUEST` and
`destinationPathSuffixStatus` is set to `SUFFIX`, this specifies
the suffix to append to the path.

</div>

<div class="option" markdown="1" id="redirect.destinationPathOther" >

- `destinationPathOther` (_string; allows [variables](#vf)_):
    When `destinationPath` is set to `PREFIX_REQUEST`, this replaces
the current path.

</div>

<div class="option" markdown="1" id="redirect.queryString" >

- `queryString` (_enum string_):
    When set to
`APPEND`, passes incoming query string parameters as part of the
redirect URL. Otherwise set this to `IGNORE`.

</div>

<div class="option" markdown="1" id="redirect.responseCode" >

- `responseCode` (_numeric enum_):
    Specify the
redirect's response code: `301` (Moved Permanently), `302` (Found),
`303` (See Other), or `307` (Temporary Redirect).

</div>

</div>

<div class="feature" data-feature="redirectplus" markdown="1">

## redirectplus

__Property Manager name__:
[Redirect Plus](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0069)

Respond to the client
request with a redirect without contacting the origin. This behavior
fills the same need as [`redirect`](#redirect), but allows you to use
[variables](#vf) to express the redirect `destination`'s component
values more concisely.

__Options__:

<div class="option" markdown="1" id="redirectplus.enabled" >

- `enabled` (_boolean_):
    Enables the
redirect feature.

</div>

<div class="option" markdown="1" id="redirectplus.destination" >

- `destination` (_string; allows [variables](#vf)_):
    Specifies the redirect as a path expression starting with a `/`
character relative to the current root, or as a fully qualified URL.
Optionally inject variables, as in this example that refers to the
original request's filename: `/path/to/{{ "{{" }}builtin.AK_FILENAME}}`.

</div>

<div class="option" markdown="1" id="redirectplus.responseCode" >

- `responseCode` (_numeric enum_):
    Assigns
the status code for the redirect response, either `301`, `302`, `303`,
or `307`.

</div>

</div>

<div class="feature" data-feature="refererChecking" markdown="1">

## refererChecking

__Property Manager name__:
[Legacy Referrer Checking](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0070)

Limits allowed requests
to a set of domains you specify.

__Options__:

<div class="option" markdown="1" id="refererChecking.enabled" >

- `enabled` (_boolean_):
    Enables the
referer-checking behavior.

</div>

<div class="option" markdown="1" id="refererChecking.strict" >

- `strict` (_boolean_):
    When
enabled, excludes requests whose `Referer` header include a relative
path, or that are missing a `Referer`. When disabled, only excludes
requests whose `Referer` hostname is not part of the `domains` set.

</div>

<div class="option" markdown="1" id="refererChecking.domains" >

- `domains` (_array of string values_):
    Specifies
the set of allowed domains. With `allowChildren` disabled, prefixing
values with `*.` specifies domains for which subdomains are allowed.

</div>

<div class="option" markdown="1" id="refererChecking.allowChildren" >

- `allowChildren` (_boolean_):
    When enabled, allows all subdomains for the `domains` set, just like
adding a `*.` prefix to each.

</div>

</div>

<div class="feature" data-feature="removeQueryParameter" markdown="1">

## removeQueryParameter

__Property Manager name__:
[Remove Outgoing Request Parameters](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9013)

Remove named query
parameters before forwarding the request to the origin.

__Options__:

<div class="option" markdown="1" id="removeQueryParameter.parameters" >

- `parameters` (_array of string values_):
    Specifies parameters to remove from the request.

</div>

</div>

<div class="feature" data-feature="removeVary" markdown="1">

## removeVary

__Property Manager name__:
[Remove Vary Header](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0071)

By default, responses that feature a
`Vary` header value of anything other than `Accept-Encoding` and a
corresponding `Content-Encoding: gzip` header aren't cached on edge
servers. `Vary` headers indicate when a URL's content varies depending
on some variable, such as which `User-Agent` requests it. This
behavior simply removes the `Vary` header to make responses cacheable.

> __WARNING__: If your site relies on `Vary: User-Agent` to customize
content, removing the header may lead the edge to serve content
inappropriate for specific devices.

__Options__:

<div class="option" markdown="1" id="removeVary.enabled" >

- `enabled` (_boolean_):
    When enabled,
removes the `Vary` header to ensure objects can be cached.

</div>

</div>

<div class="feature" data-feature="report" markdown="1">

## report

__Property Manager name__:
[Log Request Details](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0072)

Specify the HTTP request headers
or cookie names to log in your Log Delivery Service reports.

__Options__:

<div class="option" markdown="1" id="report.logHost" >

- `logHost` (_boolean_):
    Log the `Host` header.

</div>

<div class="option" markdown="1" id="report.logReferer" >

- `logReferer` (_boolean_):
    Log the `Referer`
header.

</div>

<div class="option" markdown="1" id="report.logUserAgent" >

- `logUserAgent` (_boolean_):
    Log the
`User-Agent` header.

</div>

<div class="option" markdown="1" id="report.logAcceptLanguage" >

- `logAcceptLanguage` (_boolean_):
    Log the
`Accept-Language` header.

</div>

<div class="option" markdown="1" id="report.logCookies" >

- `logCookies` (_enum string_):
    With a set of
defined `cookie` names, specifies whether you want to log `ALL` or
`SOME` cookies, or to turn `OFF` the feature to stop logging
cookies.

</div>

<div class="option" markdown="1" id="report.cookies" >

- `cookies` (_array of string values_):
    With
`logCookies` set to `SOME`, this specifies
the set of cookies names whose values you want to log.

</div>

<div class="option" markdown="1" id="report.logCustomLogField" >

- `logCustomLogField` (_boolean_):
    Whether
to append additional custom data to each log line.

</div>

<div class="option" markdown="1" id="report.customLogField" >

- `customLogField` (_string; allows [variables](#vf)_):
    With
`logCustomLogField` enabled, specifies an additional data field to
append to each log line, maximum 40 bytes, typically based on a
dynamically generated built-in system variable. For example,
`round-trip: {{ "{{" }}builtin.AK_CLIENT_TURNAROUND_TIME}}ms` would log the
total time to complete the response. See [Support for variables](#vf)
for more information.

</div>

</div>

<div class="feature" data-feature="requestControl" markdown="1">

## requestControl

__Property Manager name__:
[Request Control Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0073)

The Request Control
Cloudlet allows you to control access to your web content based on the
incoming request's IP or geographic location.  With cloudlets
available on your contract, choose
__Your services__ &rArr; __Edge logic Cloudlets__
to control how the feature works within
[Control Center](https://control.akamai.com),
or use the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html)
to configure it programmatically.

__Options__:

<div class="option" markdown="1" id="requestControl.enabled" >

- `enabled` (_boolean_):
    Enables the
Request Control Cloudlet.

</div>

<div class="option" markdown="1" id="requestControl.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="requestControl.enableBranded403" >

- `enableBranded403` (_boolean_):
    If enabled, serves a branded 403 page for this Cloudlet instance.

</div>

<div class="option" markdown="1" id="requestControl.branded403StatusCode" >

- `branded403StatusCode` (_numeric enum_):
    Specifies the response status code for the branded deny action,
either `200`, `302`, `403`, or `503`.

</div>

<div class="option" markdown="1" id="requestControl.netStorage" >

- `netStorage` (_object_):
    Specifies the NetStorage domain that contains the branded 403
page.

</div>

<div class="option" markdown="1" id="requestControl.branded403File" >

- `branded403File` (_string_):
    Specifies the full path of the branded 403 page, including the
filename, but excluding the NetStorage CP code path component.

</div>

<div class="option" markdown="1" id="requestControl.branded403Url" >

- `branded403Url` (_string_):
    Specifies the redirect URL for the branded deny action.

</div>

<div class="option" markdown="1" id="requestControl.brandedDenyCacheTtl" >

- `brandedDenyCacheTtl` (_number within 5-30 range_):
    Specifies the branded response page's time to live in the cache, `5`
minutes by default.

</div>

</div>

<div class="feature" data-feature="requestTypeMarker" markdown="1">

## requestTypeMarker

__Property Manager name__:
[Request Type Marker](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0074)

The
[Internet of Things: OTA Updates](https://learn.akamai.com/en-us/webhelp/iot/internet-of-things-over-the-air-user-guide/)
product allows customers to securely distribute firmware to devices
over cellular networks. When using the
[`downloadCompleteMarker`](#downloadcompletemarker) behavior to log
successful downloads, this related behavior identifies download or
campaign server types in aggregated and individual reports.

__Options__:

<div class="option" markdown="1" id="requestTypeMarker.requestType" >

- `requestType` (_enum string_):
    Specifies the type of request as either `DOWNLOAD` or
`CAMPAIGN_SERVER`.

</div>

</div>

<div class="feature" data-feature="resourceOptimizer" markdown="1">

## resourceOptimizer

__Property Manager name__:
[Resource Optimizer](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9046)

The Resource Optimizer
helps compress and cache web resources such as JavaScript, CSS, and
font files.

__Options__:

<div class="option" markdown="1" id="resourceOptimizer.enabled" >

- `enabled` (_boolean_):
    Enables
the Resource Optimizer feature.

</div>

</div>

<div class="feature" data-feature="resourceOptimizerExtendedCompatibility" markdown="1">

## resourceOptimizerExtendedCompatibility

__Property Manager name__:
[Resource Optimizer Extended Compatibility](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_3004)

The Resource Optimizer helps compress and cache web resources such
as JavaScript, CSS, and font files.

__Options__:

<div class="option" markdown="1" id="resourceOptimizerExtendedCompatibility.enabled" >

- `enabled` (_boolean_):
    Enables the Resource Optimizer feature.

</div>

<div class="option" markdown="1" id="resourceOptimizerExtendedCompatibility.enableAllFeatures" >

- `enableAllFeatures` (_boolean_):
    Enables the full set of Resource Optimizer feature.

</div>

</div>

<div class="feature" data-feature="responseCode" markdown="1">

## responseCode

__Property Manager name__:
[Set Response Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0075)

Change the existing
response code. For example, if your origin sends a `301` permanent
redirect, this behavior can change it on the edge to a temporary `302`
redirect.

__Options__:

<div class="option" markdown="1" id="responseCode.statusCode" >

- `statusCode` (_numeric enum_):
    The HTTP status
code to replace the existing one, any of the following:

<pre style="-webkit-column-width:1in;-moz-column-width:1in;column-width:1in;margin-left:3pc">
100
101
102
103
122
200
201
202
203
204
205
206
207
226
300
301
302
303
304
305
306
307
308
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
422
423
424
425
426
428
429
431
444
449
450
499
500
501
502
503
504
505
506
507
509
510
511
598
599
</pre>

</div>

<div class="option" markdown="1" id="responseCode.override206" >

- `override206` (_boolean_):
    When
enabled, allows any specified `200` success code to override a `206`
partial-content code, in which case the response's content length
matches the requested range length.

</div>

</div>

<div class="feature" data-feature="responseCookie" markdown="1">

## responseCookie

__Property Manager name__:
[Set Response Cookie](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0076)

Set a cookie to send
downstream to the client, either with a fixed value or a unique
stamp.

__Options__:

<div class="option" markdown="1" id="responseCookie.enabled" >

- `enabled` (_boolean_):
    When
enabled, allows you to set a response cookie.

</div>

<div class="option" markdown="1" id="responseCookie.cookieName" >

- `cookieName` (_string; allows [variables](#vf)_):
    Specifies
the name of the cookie, which serves as a key to determine if the
cookie is set.

</div>

<div class="option" markdown="1" id="responseCookie.type" >

- `type` (_enum string_):
    Assign
either a `UNIQUE` value, or a `FIXED` one based on the
`value` field.

</div>

<div class="option" markdown="1" id="responseCookie.value" >

- `value` (_string; allows [variables](#vf)_):
    If the
cookie `type` is `FIXED`, this specifies
the cookie value.

</div>

<div class="option" markdown="1" id="responseCookie.format" >

- `format` (_enum string_):
    When the
`type` of cookie is set to `UNIQUE`, set this to either `APACHE` or
`AKAMAI` format. The latter format adds milliseconds to the date
stamp.

</div>

<div class="option" markdown="1" id="responseCookie.defaultDomain" >

- `defaultDomain` (_boolean_):
    When
enabled, uses the default domain value, otherwise the set specified in
the `domain` field.

</div>

<div class="option" markdown="1" id="responseCookie.defaultPath" >

- `defaultPath` (_boolean_):
    When
enabled, uses the default path value, otherwise the set specified in
the `path` field.

</div>

<div class="option" markdown="1" id="responseCookie.domain" >

- `domain` (_string; allows [variables](#vf)_):
    If the
`defaultDomain` is disabled, this sets the domain for which the cookie
is valid. For example, `example.com` makes the cookie valid for that
hostname and all subdomains.

</div>

<div class="option" markdown="1" id="responseCookie.path" >

- `path` (_string; allows [variables](#vf)_):
    If the
`defaultPath` is disabled, sets the path component for which the
cookie is valid.

</div>

<div class="option" markdown="1" id="responseCookie.expires" >

- `expires` (_enum string_):
    Sets
various ways to specify when the cookie expires:

    - A value of `NEVER` lets the cookie persist indefinitely.
    - A value of `ON_BROWSER_CLOSE` limits the cookie to the duration     of the session.
    - A value of `DURATION` requires a corresponding `DURATION` field     value.
    - A value of `FIXED_DATE` requires a corresponding     `expirationDate` field value.

</div>

<div class="option" markdown="1" id="responseCookie.expirationDate" >

- `expirationDate` (_ISO 8601 format date/time string_):
    If
`expires` is set to `FIXED_DATE`, this sets when the cookie expires as
a UTC date and time.

</div>

<div class="option" markdown="1" id="responseCookie.duration" >

- `duration` (_duration string_):
    If
`expires` is set to `DURATION`, this sets the cookie's lifetime.

</div>

<div class="option" markdown="1" id="responseCookie.secure" >

- `secure` (_boolean_):
    When
enabled, sets the cookie's `Secure` flag to transmit it with
`HTTPS`.

</div>

</div>

<div class="feature" data-feature="restrictObjectCaching" markdown="1">

## restrictObjectCaching

__Property Manager name__:
[Object Caching](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0121)

A [read-only
behavior](#ro) necessary to deploy the Object Caching product. It
disables serving HTML content and limits the maximum object size to
100MB. Contact Akamai Professional Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="restrictObjectCaching.maximumSize" >

- `maximumSize` (_read-only string_):
    Specifies a fixed maximum size of non-HTML content to cache.

</div>

</div>

<div class="feature" data-feature="returnCacheStatus" markdown="1">

## returnCacheStatus

__Property Manager name__:
[Return Cache Status](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9028)

Generates a response
header with information about cache status. Among other things, this
can tell you whether the response came from the Akamai cache, or from
the origin. Status values report with either of these forms of syntax,
depending for example on whether you're deploying traffic using
[`sureRoute`](#sureroute) or
[`tieredDistribution`](#tiereddistribution):

    {status} from child
    {status} from child, {status} from parent

The `status` value can be any of the following:

- `Hit`: The object was retrieved from Akamai's cache.

- `Miss`: The object was not found in the Akamai cache.

- `RefreshHit`: The object was found in Akamai's cache, but was stale,
so an `If-Modified-Since` request was made to the customer origin,
with 304 as the response code, indicating unmodified content.

- `HitStale`: The object was found in Akamai's cache and was stale,
but a more recent object was not available from the customer origin,
so the cache served the stale object to the client.

- `Constructed`: The [`constructResponse`](#constructresponse) behavior
directly specified the response to the client.

- `Redirect`: The Akamai edge configuration specified a redirect,
typically by executing the [`redirect`](#redirect),
[`redirectPlus`](#redirectplus), or
[`edgeRedirector`](#edgeredirector) behaviors.

- `Error`: An error occurred, typically when authorization is denied
or the request is rejected by WAF.

__Options__:

<div class="option" markdown="1" id="returnCacheStatus.responseHeaderName" >

- `responseHeaderName` (_string_):
    Specifies the name of the HTTP header in which to report the cache
status value.

</div>

</div>

<div class="feature" data-feature="rewriteUrl" markdown="1">

## rewriteUrl

__Property Manager name__:
[Modify Outgoing Request Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0077)

Modifies the path of incoming
requests to forward to the origin. This helps you offload
URL-rewriting tasks to the edge to increase the origin server's
performance, allows you to redirect links to different targets without
changing markup, and hides your original directory structure.

Except for regular expression replacements, this behavior manipulates
_path expressions_, which start and end with a `/` character.

__Options__:

<div class="option" markdown="1" id="rewriteUrl.behavior" >

- `behavior` (_enum string_):
    The action to
perform on the path:

    - If set to `PREPEND`, specify the `targetPathPrepend`. For     example, if set to `/prefix/`, `/path1/page.html` changes to     `/prefix/path1/page.html`.

    - If set to `REPLACE`, specify the `match` and `targetPath`. For     example, a `match` of `/path1/` and a `targetPath` of     `/path1/path2/` changes `/path1/page.html` to     `/path1/path2/page.html`.

    - If set to `REGEX_REPLACE`, specify the `matchRegex` and     `targetRegex`. For example, specifying `logo\\.(png|gif|jpe?g)`     and `brand\$1` changes `logo.png` to `brand.png`.

    - If set to `REWRITE`, specify the `targetUrl`. For example, you     can direct traffic to `/error/restricted.html`.

    - If set to `REMOVE`, specify the `match`. For example, a     `match` of `/path2/` changes `/path1/path2/page.html` to     `/path1/page.html`.

</div>

<div class="option" markdown="1" id="rewriteUrl.match" >

- `match` (_string_):
    When
`behavior` is `REMOVE` or `REPLACE`, specifies the part of the
incoming path you'd like to remove or modify.

</div>

<div class="option" markdown="1" id="rewriteUrl.matchRegex" >

- `matchRegex` (_string_):
    When
`behavior` is set to `REGEX_REPLACE`, specifies the Perl-compatible
regular expression to replace with `targetRegex`.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetRegex" >

- `targetRegex` (_string; allows [variables](#vf)_):
    When
`behavior` is set to `REGEX_REPLACE`, this replaces whatever the
`matchRegex` field matches, along with any captured sequences from
`\$1` through `\$9`.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetPath" >

- `targetPath` (_string; allows [variables](#vf)_):
    When
`behavior` is set to `REPLACE`, this path replaces whatever the
`match` field matches in the incoming request's path.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetPathPrepend" >

- `targetPathPrepend` (_string; allows [variables](#vf)_):
    When
`behavior` is set to `PREPEND`, specifies a path to prepend to the
incoming request's URL.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetUrl" >

- `targetUrl` (_string; allows [variables](#vf)_):
    When
`behavior` is set to `REWRITE`, specifies the full path to request
from the origin.

</div>

<div class="option" markdown="1" id="rewriteUrl.matchMultiple" >

- `matchMultiple` (_boolean_):
    When
enabled, replaces all potential matches rather than only the first.

</div>

<div class="option" markdown="1" id="rewriteUrl.keepQueryString" >

- `keepQueryString` (_boolean_):
    When enabled,
retains the original path's query parameters.

</div>

</div>

<div class="feature" data-feature="rmaOptimization" markdown="1">

## rmaOptimization

__Property Manager name__:
[RMA Optimizations](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9007)

This behavior is
deprecated. Do not add it to any properties.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="rumCustom" markdown="1">

## rumCustom

__Property Manager name__:
[RUM SampleRate](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0068)

With
[`realUserMonitoring`](#realusermonitoring) enabled, this configures
the sample of data to include in your RUM report.

__Options__:

<div class="option" markdown="1" id="rumCustom.rumSampleRate" >

- `rumSampleRate` (_number within 0-100 range_):
    Specifies
the percentage of web traffic to include in your RUM report.

</div>

<div class="option" markdown="1" id="rumCustom.rumGroupName" >

- `rumGroupName` (_string_):
    A
deprecated option to specify an alternate name under which to batch
this set of web traffic in your report. Do not use it.

</div>

</div>

<div class="feature" data-feature="saasDefinitions" markdown="1">

## saasDefinitions

__Property Manager name__:
[SaaS Definitions](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0078)

Configures how the
Software as a Service feature identifies _customers_, _applications_,
and _users_. A different set of options is available for each type of
targeted request, each enabled with the `action`-suffixed option. In
each case, you can use `PATH`, `COOKIE`, `QUERY_STRING`, or `HOSTNAME`
components as identifiers, or `disable` the
[SaaS](https://control.akamai.com/dl/customers/SaaS/SaaS-User-Guide.pdf)
behavior for certain targets. If you rely on a `HOSTNAME`, you also
have the option of specifying a _CNAME chain_ rather than an
individual hostname. The various options suffixed `regex` and
`replace` subsequently remove the identifier from the request.
This behavior requires a sibling [`origin`](#origin)
behavior whose `originType` option is set to `SAAS_DYNAMIC_ORIGIN`.

__Options__:

<div class="option" markdown="1" id="saasDefinitions.applicationAction" >

- `applicationAction` (_enum string_):
    Specifies the request component that identifies a SaaS application,
either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to
`DISABLED` effectively ignores applications.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCookie" >

- `applicationCookie` (_string_):
    With `applicationAction` set to `COOKIE`, this specifies the name
of the cookie that identifies the application.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationQueryString" >

- `applicationQueryString` (_string_):
    With `applicationAction` set to `QUERY_STRING`, this names the
query parameter that identifies the application.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCnameEnabled" >

- `applicationCnameEnabled` (_boolean_):
    With `applicationAction` set to `HOSTNAME`, enabling this allows
you to identify applications using a _CNAME chain_ rather than a
single hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationCnameLevel" >

- `applicationCnameLevel` (_number_):
    With `applicationCnameEnabled` on, this specifies the number of
CNAMEs to use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationRegex" >

- `applicationRegex` (_string_):
    Specifies a Perl-compatible regular expression with which to
substitute the request's application ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.applicationReplace" >

- `applicationReplace` (_string_):
    Specifies a string to replace the request's application ID matched
by `applicationRegex`.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerAction" >

- `customerAction` (_enum string_):
    Specifies the request component that identifies a SaaS customer,
either `COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to
`DISABLED` effectively ignores customers.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCookie" >

- `customerCookie` (_string_):
    With `customerAction` set to `COOKIE`, this specifies the name of
the cookie that identifies the customer.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerQueryString" >

- `customerQueryString` (_string_):
    With `customerAction` set to `QUERY_STRING`, this names the query
parameter that identifies the customer.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCnameEnabled" >

- `customerCnameEnabled` (_boolean_):
    With `customerAction` set to `HOSTNAME`, enabling this allows you
to identify customers using a _CNAME chain_ rather than a single
hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerCnameLevel" >

- `customerCnameLevel` (_number_):
    With `customerCnameEnabled` on, this specifies the number of
CNAMEs to use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerRegex" >

- `customerRegex` (_string_):
    Specifies a Perl-compatible regular expression with which to
substitute the request's customer ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.customerReplace" >

- `customerReplace` (_string_):
    Specifies a string to replace the request's customer ID matched by
`customerRegex`.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersAction" >

- `usersAction` (_enum string_):
    Specifies the request component that identifies a SaaS user, either
`COOKIE`, `HOSTNAME`, `PATH`, or `QUERY_STRING`. Setting it to
`DISABLED` effectively ignores users.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCookie" >

- `usersCookie` (_string_):
    With
`usersAction` set to `COOKIE`, this specifies the name of the cookie
that identifies the user.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersQueryString" >

- `usersQueryString` (_string_):
    With `usersAction` set to `QUERY_STRING`, this names the query
parameter that identifies the user.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCnameEnabled" >

- `usersCnameEnabled` (_boolean_):
    With `usersAction` set to `HOSTNAME`, enabling this allows you to
identify users using a _CNAME chain_ rather than a single hostname.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersCnameLevel" >

- `usersCnameLevel` (_number_):
    With `userCnameEnabled` on, this specifies the number of CNAMEs to
use in the chain.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersRegex" >

- `usersRegex` (_string_):
    Specifies a Perl-compatible regular expression with which to
substitute the request's user ID.

</div>

<div class="option" markdown="1" id="saasDefinitions.usersReplace" >

- `usersReplace` (_string_):
    Specifies a string to replace the request's user ID matched by
`usersRegex`.

</div>

</div>

<div class="feature" data-feature="salesForceCommerceCloudClient" markdown="1">

## salesForceCommerceCloudClient

__Property Manager name__:
[Akamai Connector for Salesforce Commerce Cloud](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_3001)

If you use
the Salesforce Commerce Cloud platform for your origin content, this
behavior allows your edge content managed by Akamai to contact
directly to origin.

__Options__:

<div class="option" markdown="1" id="salesForceCommerceCloudClient.enabled" >

- `enabled` (_boolean_):
    Enables the Akamai Connector for Salesforce Commerce Cloud.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.connectorId" >

- `connectorId` (_string; allows [variables](#vf)_):
    An ID value that helps distinguish different types of traffic sent
from Akamai to the Salesforce Commerce Cloud. Form the value as
_instance-realm-customer_, where _instance_ is either `production` or
`development`, _realm_ is your Salesforce Commerce Cloud service
`$REALM` value, and _customer_ is the name for your organization in
Salesforce Commerce Cloud.  You can use alphanumeric characters,
underscores, or dot characters within dash-delimited segment values.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.originType" >

- `originType` (_enum string_):
    Specifies whether to use a `DEFAULT` Salesforce origin, or a
`CUSTOMER` defined origin.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.sf3cOriginHost" >

- `sf3cOriginHost` (_string; allows [variables](#vf)_):
    With `originType` set to `CUSTOMER`, this specifies the hostname
or IP address of the custom Salesforce origin.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.originHostHeader" >

- `originHostHeader` (_enum string_):
    Specifies whether to use a `DEFAULT` or `CUSTOMER` defined
Salesforce host header.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.sf3cOriginHostHeader" >

- `sf3cOriginHostHeader` (_string; allows [variables](#vf)_):
    With `originHostHeader` set to `CUSTOMER`, this specifies the
hostname or IP address of the custom Salesforce host header.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.allowOverrideOriginCacheKey" >

- `allowOverrideOriginCacheKey` (_boolean_):
    When enabled, overrides the forwarding origin's cache key.

</div>

</div>

<div class="feature" data-feature="salesForceCommerceCloudProvider" markdown="1">

## salesForceCommerceCloudProvider

__Property Manager name__:
[Akamai Provider for Salesforce Commerce Cloud](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9055)

This
manages traffic between mutual customers and the Salesforce Commerce
Cloud platform.

__Options__:

<div class="option" markdown="1" id="salesForceCommerceCloudProvider.enabled" >

- `enabled` (_boolean_):
    Enables Akamai Provider for Salesforce Commerce Cloud.

</div>

</div>

<div class="feature" data-feature="salesForceCommerceCloudProviderHostHeader" markdown="1">

## salesForceCommerceCloudProviderHostHeader

__Property Manager name__:
[Akamai Provider for Salesforce Commerce Cloud Host Header Control](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9049)

Manages host header values sent to the Salesforce Commerce Cloud
platform.

__Options__:

<div class="option" markdown="1" id="salesForceCommerceCloudProviderHostHeader.hostHeaderSource" >

- `hostHeaderSource` (_enum string_):
    Whether the host header derives from this `PROPERTY` or from the
`CUSTOMER` property.

</div>

</div>

<div class="feature" data-feature="savePostDcaProcessing" markdown="1">

## savePostDcaProcessing

__Property Manager name__:
[Save POST DCA processing result](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9069)

A [read-only
behavior](#ro), used in conjunction with the [`cachePost`](#cachepost)
behavior, that allows the body of POST requests to be processed
through Dynamic Content Assembly.  Contact Akamai Professional
Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="savePostDcaProcessing.enabled" >

- `enabled` (_boolean_):
    Enables
processing of POST requests.

</div>

</div>

<div class="feature" data-feature="scheduleInvalidation" markdown="1">

## scheduleInvalidation

__Property Manager name__:
[Scheduled Invalidation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9022)

Specifies when
cached content that satisfies a rule's criteria expires, optionally at
repeating intervals. In addition to periodic cache flushes, you can
use this behavior to minimize potential conflicts when related objects
expire at different times.

> __WARNING__: scheduled invalidations can significantly increase
origin servers' load when matching content expires simultaneously
across all edge servers. As best practice, schedule expirations during
periods of lowest traffic.

__Options__:

<div class="option" markdown="1" id="scheduleInvalidation.start" >

- `start` (_ISO 8601 format date/time string_):
    The
UTC date and time when matching cached content is to expire.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.repeat" >

- `repeat` (_boolean_):
    When enabled, invalidation recurs periodically from the `start`
time based on the `repeatInterval` time.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.repeatInterval" >

- `repeatInterval` (_duration string_):
    With `repeat` enabled, specifies how often to invalidate content
from the `start` time, expressed in seconds. For example, an
expiration set to midnight and an interval of `86400` seconds
invalidates content once a day.  Repeating intervals of less than 5
minutes are not allowed for
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
origins.

</div>

<div class="option" markdown="1" id="scheduleInvalidation.refreshMethod" >

- `refreshMethod` (_enum string_):
    Specifies how to invalidate the content. Setting it to `INVALIDATE`
sends an `If-Modified-Since` request to the origin, re-caching the
content only if it is fresher. Setting it to `PURGE` re-caches content
regardless of its freshness, potentially creating more traffic at the
origin.

</div>

</div>

<div class="feature" data-feature="scriptManagement" markdown="1">

## scriptManagement

__Property Manager name__:
[Script Management](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_3000)

Ensures unresponsive
linked JavaScript files do not prevent HTML pages from loading.

__Options__:

<div class="option" markdown="1" id="scriptManagement.enabled" >

- `enabled` (_boolean_):
    Enables
the Script Management feature.

</div>

<div class="option" markdown="1" id="scriptManagement.serviceworker" >

- `serviceworker` (_enum string_):
    Choose `NO_SERVICE_WORKER` to simply view script insights within the
Akamai Control Panel.  Choose `YES_SERVICE_WORKER` to configure
additional script actions, and to activate policies.

</div>

<div class="option" markdown="1" id="scriptManagement.timestamp" >

- `timestamp` (_number_):
    A
read-only epoch timestamp value used for synchronization.

</div>

</div>

<div class="feature" data-feature="segmentedContentProtection" markdown="1">

## segmentedContentProtection

__Property Manager name__:
[Segmented Media Protection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0079)

Validates
authorization tokens at the edge server to prevent unauthorized link
sharing.

__Options__:

<div class="option" markdown="1" id="segmentedContentProtection.enabled" >

- `enabled` (_boolean_):
    Enables the segmented content protection behavior.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.key" >

- `key` (_string_):
    Specifies the encryption key to use as a shared secret to validate
tokens.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.useAdvanced" >

- `useAdvanced` (_boolean_):
    When enabled, allows you to specify advanced `transitionKey` and
`salt` options.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.transitionKey" >

- `transitionKey` (_string_):
    An alternate encryption key to match along with the `key` field,
allowing you to rotate keys with no down time.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.salt" >

- `salt` (_string_):
    Specifies a salt as input into the token for added security. This
value must match the salt used in the token generation code.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.headerForSalt" >

- `headerForSalt` (_array of string values_):
    With `useAdvanced` enabled, this allows you to include additional
salt properties specific to each end user to strengthen the
relationship between the session token and playback session. This
specifies the set of request headers whose values generate the salt
value, typically `User-Agent`, `X-Playback-Session-Id`, and
`Origin`. Any specified header must appear in the player's
request.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.sessionId" >

- `sessionId` (_boolean_):
    With `useAdvanced` enabled, enabling this option carries the
`session_id` value from the access token over to the session token,
for use in tracking and counting unique playback sessions.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.dataPayload" >

- `dataPayload` (_boolean_):
    With `useAdvanced` enabled, enabling this option carries the
`data/payload` field from the access token over to the session token,
allowing access to opaque data for log analysis for a URL protected by
a session token.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.ip" >

- `ip` (_boolean_):
    With `useAdvanced` enabled, enabling this restricts content access
to a specific IP address, only appropriate if it does not change
during the playback session.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.acl" >

- `acl` (_boolean_):
    With `useAdvanced` enabled, enabling this option carries the `ACL`
field from the access token over to the session token, to limit the
requesting client's access to the specific URL or path set in the
`ACL` field. Playback may fail if the base path of the master playlist
(and variant playlist, plus segments) varies from that of the `ACL`
field.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.enableTokenInURI" >

- `enableTokenInURI` (_boolean_):
    When enabled, passes tokens in HLS variant manifest URLs and HLS
segment URLs, as an alternative to cookies.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.hlsMasterManifestFiles" >

- `hlsMasterManifestFiles` (_array of string values_):
    With `enableTokenInURI` enabled, specifies the set of filenames
that form HLS master manifest URLs. You can use `*` wildcard
characters, but make sure to specify master manifest filenames
uniquely, to distinguish them from variant manifest files.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.tokenRevocationEnabled" >

- `tokenRevocationEnabled` (_boolean_):
    Enable this to deny requests from playback URLs that contain a
`TokenAuth` token that uses specific token identifiers.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.blackListName" >

- `blackListName` (_string_):
    With `tokenRevocationEnabled` on, this selects the blacklist that
contains the `TokenAuth` token identifiers to block from accessing your
content.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.hlsMediaEncryption" >

- `hlsMediaEncryption` (_boolean_):
    Enables HLS Segment Encryption.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.encryptionMode" >

- `encryptionMode` (_enum string_):
    With `hlsMediaEncryption` enabled, specifies the encryption
algorithm, the only valid value for which is `AES128`.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.useAdvancedOption" >

- `useAdvancedOption` (_boolean_):
    With `hlsMediaEncryption` enabled, allows you to use advanced
encryption options.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.iv" >

- `iv` (_string_):
    With `hlsMediaEncryption` and `useAdvancedOption` both enabled, this
specifies the initialization vector used to generate the encryption
key.

</div>

</div>

<div class="feature" data-feature="segmentedMediaOptimization" markdown="1">

## segmentedMediaOptimization

__Property Manager name__:
[Segmented Media Delivery Mode](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0080)

Optimizes segmented
media for live or streaming delivery contexts.

__Options__:

<div class="option" markdown="1" id="segmentedMediaOptimization.behavior" >

- `behavior` (_enum string_):
    Set to either cached `ON_DEMAND`, or streaming `LIVE`. Only
`ON_DEMAND` is allowed for
[NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html)
origins.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.enableUllStreaming" >

- `enableUllStreaming` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.showAdvanced" >

- `showAdvanced` (_boolean_):
    When enabled, allows you to configure advanced media options.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.liveType" >

- `liveType` (_enum string_):
    The type of live media, either `CONTINUOUS` or an `EVENT` for a
range of time.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.startTime" >

- `startTime` (_ISO 8601 format date/time string_):
    With `liveType` set to `EVENT`, this specifies when the live media
event begins.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.endTime" >

- `endTime` (_ISO 8601 format date/time string_):
    With `liveType` set to `EVENT`, this specifies when the live media
event ends.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.dvrType" >

- `dvrType` (_enum string_):
    The type of DVR, either `CONFIGURABLE` or `UNKNOWN`.

</div>

<div class="option" markdown="1" id="segmentedMediaOptimization.dvrWindow" >

- `dvrWindow` (_duration string_):
    Set the duration for your media, or `0m` if a DVR is not
required.

</div>

</div>

<div class="feature" data-feature="segmentedMediaStreamingPrefetch" markdown="1">

## segmentedMediaStreamingPrefetch

__Property Manager name__:
[Segmented Media Streaming - Prefetch](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5007)

Prefetches HLS and DASH media stream manifest and segment files,
accelerating delivery to end users. For prefetching to work, your
origin media's response needs to specify
`CDN-Origin-Assist-Prefetch-Path` headers with each URL to prefetch,
expressed as either a relative or absolute path.

__Options__:

<div class="option" markdown="1" id="segmentedMediaStreamingPrefetch.enabled" >

- `enabled` (_boolean_):
    Enables media stream prefetching.

</div>

</div>

<div class="feature" data-feature="setVariable" markdown="1">

## setVariable

__Property Manager name__:
[Set Variable](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0008)

Modify a variable to insert
into subsequent fields within the rule tree.  Use this behavior to
specify the predeclared `variableName` and determine from where to
derive its new value. Based on this `valueSource`, you can either
generate the value, extract it from some part of the incoming request,
assign it from another variable (including a set of built-in system
variables), or directly specify its text.  Optionally choose a
`transform` function to modify the value once.
See [Support for variables](#vf) for more information.

__Options__:

<div class="option" markdown="1" id="setVariable.variableName" >

- `variableName` (_string_):
    Specifies the predeclared root name of the variable to modify.  When
you declare a variable name such as `VAR`, its name is preprended with
`PMUSER_` and accessible in a `user` namespace, so that you invoke it
in subsequent text fields within the rule tree as
`{{ "{{" }}user.PMUSER_VAR}}`. In deployed
[XML metadata](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#getaversion),
it appears as `%(PMUSER_VAR)`.

</div>

<div class="option" markdown="1" id="setVariable.valueSource" >

- `valueSource` (_enum string_):
    Determines how you want to set the value: either `GENERATE` it,
`EXTRACT` it from another value, or specify your own string
`EXPRESSION`.

</div>

<div class="option" markdown="1" id="setVariable.variableValue" >

- `variableValue` (_string; allows [variables](#vf)_):
    With
`valueSource` set to `EXPRESSION`, this directly specifies the value
to assign to the variable. The expression may include a mix of static
text and other variables, such as
`new_filename.{{ "{{" }}builtin.AK_EXTENSION}}` to embed a system variable.

</div>

<div class="option" markdown="1" id="setVariable.extractLocation" >

- `extractLocation` (_enum string_):
    With
`valueSource` set to `EXTRACT`, this specifies from where to get the
value, either the `CLIENT_CERTIFICATE`, `CLIENT_REQUEST_HEADER`,
`RESPONSE_HEADER`, `COOKIE`, `SET_COOKIE`, `EDGESCAPE` (for location
or network data), `PATH_COMPONENT_NAME`, `PATH_COMPONENT_OFFSET`,
`PATH_PARAMETER`, `DEVICE_PROFILE` (for client device attributes) or
`QUERY_STRING`.

</div>

<div class="option" markdown="1" id="setVariable.certificateFieldName" >

- `certificateFieldName` (_enum string_):
    With `extractLocation` set to `CLIENT_CERTIFICATE`, specifies the
certificate's content, either:

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

- `headerName` (_string_):
    With
`extractLocation` set to `CLIENT_REQUEST_HEADER`, specifies the
case-insensitive name of the HTTP header to extract.

</div>

<div class="option" markdown="1" id="setVariable.responseHeaderName" >

- `responseHeaderName` (_string_):
    With `extractLocation` set to `RESPONSE_HEADER`, specifies the
case-insensitive name of the HTTP header to extract.

</div>

<div class="option" markdown="1" id="setVariable.setCookieName" >

- `setCookieName` (_string_):
    With
`extractLocation` set to `SET_COOKIE`, specifies the name of the
origin's `Set-Cookie` response header.

</div>

<div class="option" markdown="1" id="setVariable.cookieName" >

- `cookieName` (_string_):
    With
`extractLocation` set to `COOKIE`, specifies the name of the cookie to
extract.

</div>

<div class="option" markdown="1" id="setVariable.locationId" >

- `locationId` (_enum string_):
    With
`extractLocation` set to `EDGESCAPE`, specifies the
`X-Akamai-Edgescape` header's field name. Possible values specify
basic geolocation, various geographic standards, and information about
the client's network:

    - Two-letter `CONTINENT`, ISO-3166 `COUNTRY_CODE` or       `REGION_CODE`, `COUNTY`, `CITY`, `TIMEZONE`, `AREACODE`, `ZIP`,       `LAT`, and `LONG`.
    - `ASNUM` (Autonomous System Number), `DMA` (Designated Market       Area), `FIPS` (Federal Information Processing System code),       `MSA` (Metropolitan Statistical Area), and `PMSA` (Primary       Metropolitan Statistical Area).
    - `NETWORK` (name), `NETWORK_TYPE`, or tiered level of       `THROUGHPUT` or `BW` (bandwidth).

    For details on EdgeScape header fields, see the
    [EdgeScape User Guide](https://control.akamai.com/dl/customers/ESCAPE/EdgeScape_users_guide.pdf).

</div>

<div class="option" markdown="1" id="setVariable.pathComponentOffset" >

- `pathComponentOffset` (_string_):
    With `extractLocation` set to `PATH_COMPONENT_OFFSET`, this
specifies a portion of the path.  The indexing starts from `1`, so a
value of `/path/to/nested/filename.html` and an offset of `1` yields
`path`, and `3` yields `nested`. Negative indexes offset from the
right, so `-2` also yields `nested`.

</div>

<div class="option" markdown="1" id="setVariable.queryParameterName" >

- `queryParameterName` (_string_):
    With `extractLocation` set to `QUERY_STRING`, specifies the name of
the query parameter from which to extract the value.

</div>

<div class="option" markdown="1" id="setVariable.generator" >

- `generator` (_enum string_):
    With
`valueSource` set to `GENERATE`, this specifies the type of value to
generate: either `RAND` for a random number, or `HEXRAND` for a random
hex sequence.

</div>

<div class="option" markdown="1" id="setVariable.numberOfBytes" >

- `numberOfBytes` (_number within 1-16 range_):
    With
`valueSource` set to `GENERATE` and the `generator` set to `HEXRAND`,
this specifies the number of random hex bytes to generate.

</div>

<div class="option" markdown="1" id="setVariable.minRandomNumber" >

- `minRandomNumber` (_string; allows [variables](#vf)_):
    With
`valueSource` set to `GENERATE` and the `generator` set to `RAND`,
this specifies the lower bound of the random number.

</div>

<div class="option" markdown="1" id="setVariable.maxRandomNumber" >

- `maxRandomNumber` (_string; allows [variables](#vf)_):
    With
`valueSource` set to `GENERATE` and the `generator` set to `RAND`,
this specifies the upper bound of the random number.

</div>

<div class="option" markdown="1" id="setVariable.transform" >

- `transform` (_enum string_):
    Specifies a
function to transform the value, either `NONE` for no transformation,
or any from the following categories:

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

- `operandOne` (_string; allows [variables](#vf)_):
    Specifies
an additional operand when the `transform` function is set to various
arithmetic functions (`ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, or
`MODULO`) or bitwise functions (`BITWISE_AND`, `BITWISE_OR`, or
`BITWISE_XOR`).

</div>

<div class="option" markdown="1" id="setVariable.algorithm" >

- `algorithm` (_enum string_):
    With the
`transform` function set to either `ENCRYPT` or `DECRYPT`, this
specifies the algorithm to apply, either `ALG_AES128` or `ALG_AES256`
(Advanced Encryption Standard, 128 or 256 bits), or `ALG_3DES` (Triple
DES).

</div>

<div class="option" markdown="1" id="setVariable.encryptionKey" >

- `encryptionKey` (_string; allows [variables](#vf)_):
    With
the `transform` function set to either `ENCRYPT` or `DECRYPT`, this
specifies the encryption hex key. For `ALG_3DES` it must be 48
characters long, 32 characters for `ALG_AES128`, and 64 characters for
`ALG_AES256`.

</div>

<div class="option" markdown="1" id="setVariable.initializationVector" >

- `initializationVector` (_string_):
    With the `transform` function set to either `ENCRYPT` or `DECRYPT`,
specifies a one-time number as an initialization vector.  It must be
15 characters long for `ALG_3DES`, and 32 characters for both
`ALG_AES128` and `ALG_AES256`.

</div>

<div class="option" markdown="1" id="setVariable.encryptionMode" >

- `encryptionMode` (_enum string_):
    With
the `transform` function set to either `ENCRYPT` or `DECRYPT`,
specifies either `CBC` (Cipher Block Chaining) or `ECB` (Electronic
Codebook) encryption modes.

</div>

<div class="option" markdown="1" id="setVariable.nonce" >

- `nonce` (_string; allows [variables](#vf)_):
    With the
`transform` function set to either `ENCRYPT` or `DECRYPT`, specifies
the one-time number used for encryption.

</div>

<div class="option" markdown="1" id="setVariable.prependBytes" >

- `prependBytes` (_boolean_):
    With the
`transform` function set to either `ENCRYPT` or `DECRYPT`, specifies a
number of random bytes to prepend to the key.

</div>

<div class="option" markdown="1" id="setVariable.formatString" >

- `formatString` (_string_):
    With the
`transform` function set to either `EPOCH_TO_STRING` or
`STRING_TO_EPOCH`, this specifies an optional format string for the
conversion, using format codes such as `%m/%d/%y` as specified by
[`strftime`](http://man7.org/linux/man-pages/man3/strftime.3.html).
A blank value defaults to RFC-2616 format.

</div>

<div class="option" markdown="1" id="setVariable.paramName" >

- `paramName` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `EXTRACT_PARAM`, this extracts the value
for the specified parameter name from a string that contains key/value
pairs. (Use `separator` below to parse them.)

</div>

<div class="option" markdown="1" id="setVariable.separator" >

- `separator` (_string_):
    With the
`transform` function set to `EXTRACT_PARAM`, this specifies the
character that separates pairs of values within the string.

</div>

<div class="option" markdown="1" id="setVariable.min" >

- `min` (_number_):
    With the
`transform` function set to `HASH`, specifies a minimum value for the
generated integer.

</div>

<div class="option" markdown="1" id="setVariable.max" >

- `max` (_number_):
    With the
`transform` function set to `HASH`, specifies a maximum value for the
generated integer

</div>

<div class="option" markdown="1" id="setVariable.hmacKey" >

- `hmacKey` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `HMAC`, specifies the secret to use in
generating the base64-encoded digest.

</div>

<div class="option" markdown="1" id="setVariable.hmacAlgorithm" >

- `hmacAlgorithm` (_enum string_):
    With
the `transform` function set to `HMAC`, specifies the algorithm to use
to generate the base64-encoded digest, either `MD5`, `SHA1`, or
`SHA256`.

</div>

<div class="option" markdown="1" id="setVariable.ipVersion" >

- `ipVersion` (_enum string_):
    With the
`transform` function set to `NETMASK`, this specifies the IP version
under which a subnet mask generates, either `IPV4` or `IPV6`.

</div>

<div class="option" markdown="1" id="setVariable.ipv6Prefix" >

- `ipv6Prefix` (_number within 0-128 range_):
    With the
`transform` function set to `NETMASK` and the `ipVersion` set to
`IPV6`, specifies the prefix of the IPV6 address, a value between 0
and 128.

</div>

<div class="option" markdown="1" id="setVariable.ipv4Prefix" >

- `ipv4Prefix` (_number within 0-32 range_):
    With the
`transform` function set to `NETMASK` and the `ipVersion` set to
`IPV4`, specifies the prefix of the IPV4 address, a value between 0
and 32.

</div>

<div class="option" markdown="1" id="setVariable.subString" >

- `subString` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `STRING_INDEX`, specifies a substring for
which the returned value represents a zero-based offset of where it
appears in the original string, or `-1` if there's no match.

</div>

<div class="option" markdown="1" id="setVariable.regex" >

- `regex` (_string_):
    With the
`transform` function set to `SUBSTITUTE`, this specifies the regular
expression pattern (PCRE) to match the value.

</div>

<div class="option" markdown="1" id="setVariable.replacement" >

- `replacement` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `SUBSTITUTE`, this specifies the
replacement string. Reinsert grouped items from the match into the
replacement using `$1`, `$2` ... `$n`.

</div>

<div class="option" markdown="1" id="setVariable.caseSensitive" >

- `caseSensitive` (_boolean_):
    With
the `transform` function set to `SUBSTITUTE`, enabling this makes all
matches case sensitive.

</div>

<div class="option" markdown="1" id="setVariable.globalSubstitution" >

- `globalSubstitution` (_boolean_):
    With the `transform` function set to `SUBSTITUTE`, enabling this
replaces all matches in the string, not just the first.

</div>

<div class="option" markdown="1" id="setVariable.startIndex" >

- `startIndex` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `SUBSTRING`, specifies the zero-based
character offset at the start of the substring. Negative indexes
specify the offset from the end of the string.

</div>

<div class="option" markdown="1" id="setVariable.endIndex" >

- `endIndex` (_string; allows [variables](#vf)_):
    With the
`transform` function set to `SUBSTRING`, specifies the zero-based
character offset at the end of the substring, without including the
character at that index position. Negative indexes specify the offset
from the end of the string.

</div>

<div class="option" markdown="1" id="setVariable.exceptChars" >

- `exceptChars` (_string_):
    With the
`transform` function set to `URL_ENCODE`, specifies characters _not_
to encode, possibly overriding the default set.

</div>

<div class="option" markdown="1" id="setVariable.forceChars" >

- `forceChars` (_string_):
    With the
`transform` function set to `URL_ENCODE`, specifies characters to
encode, possibly overriding the default set.

</div>

<div class="option" markdown="1" id="setVariable.deviceProfile" >

- `deviceProfile` (_enum string_):
    With
`extractLocation` set to `DEVICE_PROFILE`, specifies the client
device attribute. Possible values specify information about the
client device, including device type, size and browser:

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

## shutr

__Property Manager name__:
[SHUTR](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9026)

The
[SHUTR](http://www.akamai.com/dl/brochures/aqua_ion_mobile_pb.pdf)
protocol extends HTTP to reduce the amount of header data necessary
for web transactions with mobile devices.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="simulateErrorCode" markdown="1">

## simulateErrorCode

__Property Manager name__:
[Simulate Error Response Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9048)

A [read-only
behavior](#ro) that simulates various error response codes. Contact
Akamai Professional Services for help configuring it.

__Options__:

<div class="option" markdown="1" id="simulateErrorCode.errorType" >

- `errorType` (_enum string_):
    Specifies the type of error, any of the following:

<pre style="-webkit-column-width:3in;-moz-column-width:3in;column-width:3in;margin-left:3pc">
ERR_CONNECT_FAIL
ERR_CONNECT_TIMEOUT
ERR_DNS_FAIL
ERR_DNS_IN_REGION
ERR_DNS_TIMEOUT
ERR_NO_GOOD_FWD_IP
ERR_READ_ERROR
ERR_READ_TIMEOUT
ERR_SUREROUTE_DNS_FAIL
ERR_WRITE_ERROR
</pre>

</div>

<div class="option" markdown="1" id="simulateErrorCode.timeout" >

- `timeout` (_duration string_):
    When
the `errorType` is `ERR_CONNECT_TIMEOUT`, `ERR_DNS_TIMEOUT`,
`ERR_SUREROUTE_DNS_FAIL`, or `ERR_READ_TIMEOUT`, generates an error
after the specified amount of time from the initial request.

</div>

</div>

<div class="feature" data-feature="siteShield" markdown="1">

## siteShield

__Property Manager name__:
[SiteShield](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9063)

A [read-only behavior](#ro)
implementing the
[Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html)
feature, which helps prevent non-Akamai machines from contacting your
origin. Your service representative periodically sends you a list of
Akamai servers allowed to contact your origin, with which you
establish an Access Control List on your firewall to prevent any other
requests.

__Options__:

<div class="option" markdown="1" id="siteShield.ssmap" >

- `ssmap` (_object_):
    Identifies the
hostname for the Site Shield map, available from your Akamai
representative. Form an object with a `value` key that references the
hostname, for example: `"ssmap":{"value":"ss.akamai.net"}`.

</div>

</div>

<div class="feature" data-feature="spdy" markdown="1">

## spdy

__Property Manager name__:
[SPDY](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9045)

Applies the SPDY protocol, which
enhances HTTPS traffic by using many concurrent connections to
download objects within one TCP connection. You can only apply this
behavior within a [`hostname`](#hostname) match, and if the property
is marked as secure.  See [Secure property requirements](#sf) for
guidance.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="standardTLSMigration" markdown="1">

## standardTLSMigration

__Property Manager name__:
[Standard TLS Migration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0200)

Migrates traffic to
Standard TLS. Apply this behavior within the default rule or any
[`hostname`](#hostname) match.  In some cases you may need to apply
this along with the
[`standardTLSMigrationOverride`](#standardtlsmigrationoverride)
behavior.

__Options__:

<div class="option" markdown="1" id="standardTLSMigration.enabled" >

- `enabled` (_boolean_):
    Allows migration to Standard TLS.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationFrom" >

- `migrationFrom` (_enum string_):
    Whether you are migrating traffic from `ENHANCED_SECURE` TLS, from a
`SHARED_CERT`, or `NON_SECURE` traffic.

</div>

<div class="option" markdown="1" id="standardTLSMigration.allowHTTPSUpgrade" >

- `allowHTTPSUpgrade` (_boolean_):
    With `migrationFrom` set to `NON_SECURE`, allows temporary upgrade
of HTTP traffic to HTTPS.

</div>

<div class="option" markdown="1" id="standardTLSMigration.allowHTTPSDowngrade" >

- `allowHTTPSDowngrade` (_boolean_):
    With `migrationFrom` set to `NON_SECURE`, allow temporary
downgrade of HTTPS traffic to HTTP. This removes various `Origin`,
`Referer`, `Cookie`, `Cookie2`, `sec-*` and `proxy-*` headers from the
request to origin.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationStartTime" >

- `migrationStartTime` (_ISO 8601 format date/time string_):
    With either `allowHTTPSUpgrade` or `allowHTTPSDowngrade` enabled,
specifies when to start migrating the cache.

</div>

<div class="option" markdown="1" id="standardTLSMigration.migrationDuration" >

- `migrationDuration` (_number_):
    With either `allowHTTPSUpgrade` or `allowHTTPSDowngrade` enabled,
specifies the number of days to migrate the cache.

</div>

<div class="option" markdown="1" id="standardTLSMigration.cacheSharingStartTime" >

- `cacheSharingStartTime` (_ISO 8601 format date/time string_):
    With `migrationFrom` set to `ENHANCED_SECURE`, specifies when to
start cache sharing.

</div>

<div class="option" markdown="1" id="standardTLSMigration.cacheSharingDuration" >

- `cacheSharingDuration` (_number_):
    With `migrationFrom` set to `ENHANCED_SECURE`, specifies the
number cache sharing days.

</div>

<div class="option" markdown="1" id="standardTLSMigration.isCertificateSNIOnly" >

- `isCertificateSNIOnly` (_boolean_):
    With `migrationFrom` set to `ENHANCED_SECURE`, sets whether your
new certificate is SNI-only.

</div>

<div class="option" markdown="1" id="standardTLSMigration.isTieredDistributionUsed" >

- `isTieredDistributionUsed` (_boolean_):
    With `migrationFrom` set to `NON_SECURE`, allows you to align
traffic to various [`tieredDistribution`](#tiereddistribution)
areas.

</div>

<div class="option" markdown="1" id="standardTLSMigration.tdLocation" >

- `tdLocation` (_enum string_):
    With `isTieredDistributionUsed` enabled, specifies the
[`tieredDistribution`](#tiereddistribution) location, either `EUROPE`,
`APAC` (Asia and Pacific), `AUSTRALIA`, `US_WEST`, `US_CENTRAL`,
`US_EAST`, `GLOBAL`, or `GLOBAL_LEGACY`.

</div>

</div>

<div class="feature" data-feature="standardTLSMigrationOverride" markdown="1">

## standardTLSMigrationOverride

__Property Manager name__:
[Standard TLS Migration Override](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9077)

When
applying [`standardTLSMigration`](#standardtlsmigration), add this
behavior if your new certificate is SNI-only, if your property
includes any [advanced features](#ro), any Edge IP Binding enabled
hosts, or if any foreground downloads are configured.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="subCustomer" markdown="1">

## subCustomer

__Property Manager name__:
[Subcustomer Enablement](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5000)

When positioned in a
property's top-level default rule, enables various
[Cloud Embed](https://learn.akamai.com/en-us/products/media_delivery/cloud_embed.html)
features that allow you to leverage Akamai's CDN architecture for your
own subcustomers.  This behavior's options allow you to use Cloud
Embed to configure your subcustomers' content.  Once enabled, you can
use the
[Akamai Cloud Embed API](https://developer.akamai.com/api/media_delivery/cloud_embed/v2.html)
(ACE) to assign subcustomers to this base configuration, and to
customize policies for them.  See also the
[`dynamicWebContent`](#dynamicwebcontent) behavior to configure
subcustomers' dynamic web content.

__Options__:

<div class="option" markdown="1" id="subCustomer.enabled" >

- `enabled` (_boolean_):
    Allows Cloud
Embed to dynamically modify your subcustomers' content.

</div>

<div class="option" markdown="1" id="subCustomer.origin" >

- `origin` (_boolean_):
    Allows you to
assign origin hostnames for customers.

</div>

<div class="option" markdown="1" id="subCustomer.partnerDomainSuffix" >

- `partnerDomainSuffix` (_string_):
    With `origin` enabled, this specifies the appropriate domain suffix,
which you should typically match with your property hostname. It
identifies the domain as trustworthy on the Akamai network, despite
being defined within Cloud Embed, outside of your base property
configuration. Include this domain suffix if you want to purge
subcustomer URLs. For example, if you provide a value of
`suffix.example.com`, then to purge `subcustomer.com/some/path`,
specify `subcustomer.com.suffix.example.com/some/path` as the purge
request's URL.

</div>

<div class="option" markdown="1" id="subCustomer.caching" >

- `caching` (_boolean_):
    Modifies
content caching rules.

</div>

<div class="option" markdown="1" id="subCustomer.referrer" >

- `referrer` (_boolean_):
    Sets
subcustomers' referrer whitelists or blacklist.

</div>

<div class="option" markdown="1" id="subCustomer.ip" >

- `ip` (_boolean_):
    Sets subcustomers'
IP whitelists or blacklists.

</div>

<div class="option" markdown="1" id="subCustomer.geoLocation" >

- `geoLocation` (_boolean_):
    Sets
subcustomers' location-based whitelists or blacklists.

</div>

<div class="option" markdown="1" id="subCustomer.refreshContent" >

- `refreshContent` (_boolean_):
    Allows
you to reschedule when content validates for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.modifyPath" >

- `modifyPath` (_boolean_):
    Modifies a
subcustomer's request path.

</div>

<div class="option" markdown="1" id="subCustomer.cacheKey" >

- `cacheKey` (_boolean_):
    Allows you
to set which query parameters are included in the cache key.

</div>

<div class="option" markdown="1" id="subCustomer.tokenAuthorization" >

- `tokenAuthorization` (_boolean_):
    When enabled, this allows you to configure edge servers to use
tokens to control access to subcustomer content.  Use Cloud Embed to
configure the token to appear in a cookie, header, or query
parameter.

</div>

<div class="option" markdown="1" id="subCustomer.siteFailover" >

- `siteFailover` (_boolean_):
    When
enabled, allows you to configure unique failover sites for each
subcustomer's policy.

</div>

<div class="option" markdown="1" id="subCustomer.contentCompressor" >

- `contentCompressor` (_boolean_):
    Allows compression of subcustomer content.

</div>

<div class="option" markdown="1" id="subCustomer.accessControl" >

- `accessControl` (_boolean_):
    When
enabled, this allows you to deny requests to a subcustomer's content
based on specific match conditions, which you use Cloud Embed to
configure in each subcustomer's policy.

</div>

<div class="option" markdown="1" id="subCustomer.dynamicWebContent" >

- `dynamicWebContent` (_boolean_):
    When enabled, allows you to apply the
[`dynamicWebContent`](#dynamicwebcontent) behavior to further modify
how dynamic content behaves for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.onDemandVideoDelivery" >

- `onDemandVideoDelivery` (_boolean_):
    Enables delivery of media assets to subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.largeFileDelivery" >

- `largeFileDelivery` (_boolean_):
    Enables large file delivery for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.liveVideoDelivery" >

- `liveVideoDelivery` (_boolean_):
    Enables live media streaming for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.webApplicationFirewall" >

- `webApplicationFirewall` (_boolean_):
    2DO

</div>

</div>

<div class="feature" data-feature="sureRoute" markdown="1">

## sureRoute

__Property Manager name__:
[SureRoute](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0081)

The [SureRoute](http://www.akamai.com/dl/feature_sheets/fs_edgesuite_sureroute.pdf) feature continually tests different routes between origin and edge servers to identify the optimal path. By default, it conducts _races_ to identify alternative paths to use in case of a transmission failure. These races increase origin traffic slightly.

This behavior allows you to configure SureRoute along with a test
object to improve delivery of non-cacheable `no-store` or
`bypass-cache` content. Since edge servers are already positioned as
close as possible to requesting clients, the behavior does not apply
to cacheable content.

__Options__:

<div class="option" markdown="1" id="sureRoute.enabled" >

- `enabled` (_boolean_):
    Enables the
SureRoute behavior, to optimize delivery of non-cached content.

</div>

<div class="option" markdown="1" id="sureRoute.type" >

- `type` (_enum string_):
    Specifies the
set of edge servers used to test routes, either the default
`PERFORMANCE` or a `CUSTOM_MAP` that must be provided to you by
Akamai Professional Services.

</div>

<div class="option" markdown="1" id="sureRoute.customMap" >

- `customMap` (_string_):
    If `type` is
`CUSTOM_MAP`, this specifies the map string provided to you by Akamai
Professional Services, or included as part of the
[Site Shield](https://learn.akamai.com/en-us/products/cloud_security/site_shield.html)
product.

</div>

<div class="option" markdown="1" id="sureRoute.testObjectUrl" >

- `testObjectUrl` (_string_):
    Specifies the path and filename for your origin's test object to use
in races to test routes.

    Akamai provides sample test objects for the
    [Dynamic Site Accelerator](https://dl.akamai.com/DSA/DSA_SLA_test_page.zip)
    and
    [Web Application Accelerator](https://dl.akamai.com/WAA/Waa_sla_sr_v1.zip)
    products. If you want to use your own test object, it needs to be on
    the same origin server as the traffic being served through
    SureRoute. Make sure it returns a `200` HTTP response and does not
    require authentication. The file should be an average-sized static
    HTML file (`Content-Type: text/html`) that is no smaller than 8KB,
    with no back-end processing.

    If you have more than one origin server deployed behind a load
    balancer, you can configure it to serve the test object directly on
    behalf of the origin, or route requests to the same origin server to
    avoid deploying the test object on each origin server.

</div>

<div class="option" markdown="1" id="sureRoute.toHostStatus" >

- `toHostStatus` (_enum string_):
    If
set to `INCOMING_HH`, uses the incoming `Host` header when requesting
the SureRoute test object. If set to `OTHER`, use `toHost` to
specify a custom `Host` header.

</div>

<div class="option" markdown="1" id="sureRoute.toHost" >

- `toHost` (_string_):
    If
`toHostStatus` is `OTHER`, this specifies the custom `Host`
header to use when requesting the SureRoute test object.

</div>

<div class="option" markdown="1" id="sureRoute.raceStatTtl" >

- `raceStatTtl` (_duration string_):
    Specifies the time-to-live to preserve SureRoute race results,
typically `30m`. If traffic exceeds a certain threshold after TTL
expires, the overflow is routed directly to the origin, not
necessarily optimally. If traffic remains under the threshold, the
route is determined by the winner of the most recent race.

</div>

<div class="option" markdown="1" id="sureRoute.forceSslForward" >

- `forceSslForward` (_boolean_):
    Forces
SureRoute to use SSL when requesting the origin's test object,
appropriate if your origin does not respond to HTTP requests, or
responds with a redirect to HTTPS.

</div>

<div class="option" markdown="1" id="sureRoute.enableCustomKey" >

- `enableCustomKey` (_boolean_):
    When
disabled, caches race results under the race destination's
hostname. If enabled, use `customStatKey` to specify a custom
hostname.

</div>

<div class="option" markdown="1" id="sureRoute.customStatKey" >

- `customStatKey` (_string_):
    With
`enableCustomKey` enabled, this specifies a hostname under which to
cache race results. This may be useful when a property corresponds to
many origin hostnames. By default, SureRoute would launch races for
each origin, but consolidating under a single hostname runs only one
race.

</div>

</div>

<div class="feature" data-feature="tcpOptimization" markdown="1">

## tcpOptimization

__Property Manager name__:
[TCP Optimizations](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9041)

Enables a suite of
optimizations targeting buffers, time-outs, and packet loss that
improve transmission performance. This behavior is deprecated, but you
should not disable or remove it if present.

This behavior does not include any options. Specifying the
behavior itself enables it.

</div>

<div class="feature" data-feature="teaLeaf" markdown="1">

## teaLeaf

__Property Manager name__:
[IBM Tealeaf Connector](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0082)

Allows IBM Tealeaf Customer
Experience on Cloud to record HTTPS requests and responses for
Akamai-enabled properties. Recorded data becomes available in your
IBM Tealeaf account.

__Options__:

<div class="option" markdown="1" id="teaLeaf.enabled" >

- `enabled` (_boolean_):
    When enabled,
capture HTTPS requests and responses, and send the data to your IBM
Tealeaf account.

</div>

<div class="option" markdown="1" id="teaLeaf.limitToDynamic" >

- `limitToDynamic` (_boolean_):
    Limit
traffic to dynamic, uncached (`No-Store`) content.

</div>

<div class="option" markdown="1" id="teaLeaf.ibmCustomerId" >

- `ibmCustomerId` (_number_):
    The
integer identifier for the IBM Tealeaf Connector account.

</div>

</div>

<div class="feature" data-feature="tieredDistribution" markdown="1">

## tieredDistribution

__Property Manager name__:
[Tiered Distribution](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0083)

This behavior allows
Akamai edge servers to retrieve cached content from other Akamai
servers, rather than directly from the origin. These interim _parent_
servers in the _cache hierarchy_ (`CH`) are positioned close to the
origin, and fall along the path from the origin to the edge
server. Tiered Distribution typically reduces the origin server's
load, and reduces the time it takes for edge servers to refresh
content.

See also the
[`tieredDistributionAdvanced`](#tiereddistributionadvanced)
behavior.

__Options__:

<div class="option" markdown="1" id="tieredDistribution.enabled" >

- `enabled` (_boolean_):
    When
enabled, activates tiered distribution.

</div>

<div class="option" markdown="1" id="tieredDistribution.tieredDistributionMap" >

- `tieredDistributionMap` (_enum string_):
    Optionally map the tiered parent server's location close to your
origin: `CHEU2` for Europe; `CHAUS` for Australia; `CHAPAC` for China
and the Asian Pacific area; `CHWUS2`, `CHCUS2`, and `CHEUS2` for
different parts of the United States. Choose `CH` or `CH2` for a more
global map. A narrower local map minimizes the origin server's load,
and increases the likelihood the requested object is cached. A wider
global map reduces end-user latency, but decreases the likelihood the
requested object is in any given parent server's cache.  This option
cannot apply if the property is marked as secure. See
[Secure property requirements](#sf) for guidance.

</div>

</div>

<div class="feature" data-feature="tieredDistributionCustomization" markdown="1">

## tieredDistributionCustomization

__Property Manager name__:
[Tiered Distribution Customization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5026)

2DO

__Options__:

<div class="option" markdown="1" id="tieredDistributionCustomization.customMapEnabled" >

- `customMapEnabled` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.customMapName" >

- `customMapName` (_string; allows [variables](#vf)_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.serialStart" >

- `serialStart` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.serialEnd" >

- `serialEnd` (_string_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.hashAlgorithm" >

- `hashAlgorithm` (_enum string_):
    2DO: `GCC`, `JENKINS`.

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.mapMigrationEnabled" >

- `mapMigrationEnabled` (_boolean_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.migrationStartDate" >

- `migrationStartDate` (_ISO 8601 format date/time string_):
    2DO

</div>

<div class="option" markdown="1" id="tieredDistributionCustomization.migrationEndDate" >

- `migrationEndDate` (_ISO 8601 format date/time string_):
    2DO

</div>

</div>

<div class="feature" data-feature="timeout" markdown="1">

## timeout

__Property Manager name__:
[Connect Timeout](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9033)

Sets the HTTP connect
timeout.

__Options__:

<div class="option" markdown="1" id="timeout.value" >

- `value` (_duration string_):
    Specifies the
timeout, for example `10s`.

</div>

</div>

<div class="feature" data-feature="uidConfiguration" markdown="1">

## uidConfiguration

__Property Manager name__:
[UID Configuration](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0084)

This behavior allows you
to extract unique identifier (UID) values from live traffic, for use
in OTA applications. Note that you are responsible for maintaining the
security of any data that may identify individual users.

__Options__:

<div class="option" markdown="1" id="uidConfiguration.enabled" >

- `enabled` (_boolean_):
    Allows
you to extract UIDs from client requests.

</div>

<div class="option" markdown="1" id="uidConfiguration.extractLocation" >

- `extractLocation` (_enum string_):
    Whether to extract the UID value from a `CLIENT_REQUEST_HEADER`, a
`QUERY_STRING`, or from a rule tree `VARIABLE`.
(You should mark these variables as
[sensitive](https://developer.akamai.com/api/core_features/property_manager/v1.html#82234a11).
See also [Support for variables](#vf) above.)

</div>

<div class="option" markdown="1" id="uidConfiguration.headerName" >

- `headerName` (_string_):
    With
`extractLocation` set to `CLIENT_REQUEST_HEADER`, this specifies the
name of the HTTP header from which to extract the UID value.

</div>

<div class="option" markdown="1" id="uidConfiguration.queryParameterName" >

- `queryParameterName` (_string_):
    With `extractLocation` set to `QUERY_STRING`, this specifies the
name of the query parameter from which to extract the UID value.

</div>

<div class="option" markdown="1" id="uidConfiguration.variableName" >

- `variableName` (_string_):
    With `extractLocation` set to `VARIABLE`, this specifies the name of
the rule tree variable from which to extract the UID value.

</div>

</div>

<div class="feature" data-feature="validateEntityTag" markdown="1">

## validateEntityTag

__Property Manager name__:
[Validate Entity Tag](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9034)

Instructs edge servers
to compare the request's ETag header with that of the cached
object. If they differ, the edge server sends a new copy of the
object. This validation occurs in addition to the default validation
of `Last-Modified` and `If-Modified-Since` headers.

__Options__:

<div class="option" markdown="1" id="validateEntityTag.enabled" >

- `enabled` (_boolean_):
    Enables
the ETag validation behavior.

</div>

</div>

<div class="feature" data-feature="verifyJsonWebToken" markdown="1">

## verifyJsonWebToken

__Property Manager name__:
[JWT verification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9053)

This behavior allows
you to use JSON Web Tokens (JWT) to verify requests.

__Options__:

<div class="option" markdown="1" id="verifyJsonWebToken.extractLocation" >

- `extractLocation` (_enum string_):
    Specify from where to extract the JWT value, either from the
`CLIENT_REQUEST_HEADER` or from the request's `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.headerName" >

- `headerName` (_string_):
    With `extractLocation` set to `CLIENT_REQUEST_HEADER`, this
specifies the name of the header from which to extract the JWT
value.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.queryParameterName" >

- `queryParameterName` (_string_):
    With `extractLocation` set to `QUERY_STRING`, this specifies the
name of the query parameter from which to extract the JWT value.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.jwt" >

- `jwt` (_string_):
    An
identifier for the JWT keys collection.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.enableRS256" >

- `enableRS256` (_boolean_):
    2DO.

</div>

<div class="option" markdown="1" id="verifyJsonWebToken.enableES256" >

- `enableES256` (_boolean_):
    2DO.

</div>

</div>

<div class="feature" data-feature="verifyJsonWebTokenForDcp" markdown="1">

## verifyJsonWebTokenForDcp

__Property Manager name__:
[JWT](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9044)

This behavior
allows you to use JSON web tokens (JWT) to verify requests for use in
implementing
[IoT Edge Connect](https://learn.akamai.com/en-us/products/web_performance/iot_edge_connect.html),
which you use the [`dcp`](#dcp) behavior to configure. You can specify
the location in a request to pass a JSON web token (JWT), collections
of public keys to verify the integrity of this token, and specific
claims to extract from it. Use the
[`verifyJsonWebToken`](#verifyjsonwebtoken) behavior for other JWT
validation.

When authenticating to edge servers with both JWT and mutual
authentication (using the
[`dcpAuthVariableExtractor`](#dcpauthvariableextractor) behavior), the
JWT method is ignored, and you need to authenticate with a client
authentication certificate.

__Options__:

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractLocation" >

- `extractLocation` (_enum string_):
    Specifies whether to get the JWT value from the
`CLIENT_REQUEST_HEADER`, or from a `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.primaryLocation" >

- `primaryLocation` (_enum string_):
    2DO: `CLIENT_REQUEST_HEADER`, `QUERY_STRING`.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.customHeader" >

- `customHeader` (_boolean_):
    With `extractLocation` set to `CLIENT_REQUEST_HEADER`, The JWT
value comes from the `X-Akamai-DCP-Token` header by default.  Enabling
this option allows you to extract it from another header name that you
specify.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.headerName" >

- `headerName` (_string_):
    With `customHeader` enabled, this specifies the name of the header
to extract the JWT value from.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.queryParameterName" >

- `queryParameterName` (_string_):
    With `extractLocation` set to `QUERY_STRING`, this specifies the
name of the query parameter from which to extract the JWT value.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.jwt" >

- `jwt` (_string_):
    An
identifier for the JWT keys collection.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractClientId" >

- `extractClientId` (_boolean_):
    When enabled, allows you to extract the client ID claim name
stored in JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.clientId" >

- `clientId` (_string_):
    With `extractClientId` enabled, this specifies the claim name.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractAuthorizations" >

- `extractAuthorizations` (_boolean_):
    When enabled, allows you to extract the authorization groups
stored in the JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.authorizations" >

- `authorizations` (_string_):
    With `extractAuthorizations` enabled, this specifies the
authorization group name.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.extractUserName" >

- `extractUserName` (_boolean_):
    When enabled, allows you to extract the user name stored in the
JWT.

</div>

<div class="option" markdown="1" id="verifyJsonWebTokenForDcp.userName" >

- `userName` (_string_):
    With `extractUserName` enabled, this specifies the user name.

</div>

</div>

<div class="feature" data-feature="verifyTokenAuthorization" markdown="1">

## verifyTokenAuthorization

__Property Manager name__:
[Auth Token 2.0 Verification](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9068)

Verifies Auth
2.0 tokens.

__Options__:

<div class="option" markdown="1" id="verifyTokenAuthorization.useAdvanced" >

- `useAdvanced` (_boolean_):
    If enabled, allows you to specify advanced options such as
`algorithm`, `escapeHmacInputs`, `ignoreQueryString`, `transitionKey`,
and `salt`.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.location" >

- `location` (_enum string_):
    Specifies where to find the token in the incoming request, either
`CLIENT_REQUEST_HEADER`, `QUERY_STRING`, or `COOKIE`.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.locationId" >

- `locationId` (_string_):
    When `location` is `CLIENT_REQUEST_HEADER`, specifies the name of
the incoming request's header where to find the token.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.algorithm" >

- `algorithm` (_enum string_):
    With `useAdvanced` enabled, specifies the algorithm that generates
the token, either `SHA256`, `SHA1`, or `MD5`, in order of descending
security. It must match the method chosen in the token generation
code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.escapeHmacInputs" >

- `escapeHmacInputs` (_boolean_):
    With `useAdvanced` enabled, URL-escapes HMAC inputs passed in as
query parameters.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.ignoreQueryString" >

- `ignoreQueryString` (_boolean_):
    With `useAdvanced` enabled, enabling this removes the query
string from the URL used to form an encryption key.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.key" >

- `key` (_string_):
    The
shared secret used to validate tokens, which must match the key used
in the token generation code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.transitionKey" >

- `transitionKey` (_string_):
    With `useAdvanced` enabled, specifies a transition key as a hex
value.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.salt" >

- `salt` (_string_):
    With `useAdvanced` enabled, specifies a salt string for input when
generating the token, which must match the salt value used in the
token generation code.

</div>

<div class="option" markdown="1" id="verifyTokenAuthorization.failureResponse" >

- `failureResponse` (_boolean_):
    When enabled, sends an HTTP error when an authentication test
fails.

</div>

</div>

<div class="feature" data-feature="visitorPrioritization" markdown="1">

## visitorPrioritization

__Property Manager name__:
[Visitor Prioritization Cloudlet](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0085)

The
[Visitor Prioritization Cloudlet](http://www.akamai.com/html/technology/visitor-prioritization.html)
is designed to decrease abandonment by providing a user-friendly
waiting room experience.  With cloudlets available on your contract,
choose
__Your services__ &rArr; __Edge logic Cloudlets__
to control Visitor Prioritization within
[Control Center](https://control.akamai.com).
Otherwise use the
[Cloudlets API](https://learn.akamai.com/en-us/api/web_performance/cloudlets/v2.html)
to configure it programmatically.  To serve non-HTML API content such
as JSON blocks, see the [`apiPrioritization`](#apiprioritization)
behavior.

__Options__:

<div class="option" markdown="1" id="visitorPrioritization.enabled" >

- `enabled` (_boolean_):
    Enables the Visitor Prioritization behavior.

</div>

<div class="option" markdown="1" id="visitorPrioritization.cloudletPolicy" >

- `cloudletPolicy` (_object_):
    Identifies the Cloudlet policy in an object featuring unique numeric
`id` and descriptive string `name` members.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByCookie" >

- `userIdentificationByCookie` (_boolean_):
    When enabled, identifies users by the value of a cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyCookie" >

- `userIdentificationKeyCookie` (_string_):
    With `userIdentificationByCookie` enabled, specifies the name of
the cookie whose value identifies users. To match a user, the value of
the cookie needs to remain constant across all requests.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByHeaders" >

- `userIdentificationByHeaders` (_boolean_):
    When enabled, identifies users by the values of GET or POST
request headers.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyHeaders" >

- `userIdentificationKeyHeaders` (_array of string values_):
    With `userIdentificationByHeaders` enabled, specifies names of
request headers whose values identify users. To match a user, values
for all the specified headers need to remain constant across all
requests.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByIp" >

- `userIdentificationByIp` (_boolean_):
    When enabled, allows IP addresses to identify users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationByParams" >

- `userIdentificationByParams` (_boolean_):
    When enabled, identifies users by the values of GET or POST
request parameters.

</div>

<div class="option" markdown="1" id="visitorPrioritization.userIdentificationKeyParams" >

- `userIdentificationKeyParams` (_array of string values_):
    With `userIdentificationByParams` enabled, specifies names of
request parameters whose values identify users. To match a user,
values for all the specified parameters need to remain constant across
all requests. Parameters that are absent or blank may also identify
users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieEnabled" >

- `allowedUserCookieEnabled` (_boolean_):
    When enabled, sets a cookie for users who have been allowed
through to the site.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieLabel" >

- `allowedUserCookieLabel` (_string_):
    With `allowedUserCookieEnabled` on, specifies a label to
distinguish this cookie for an allowed user from others. The value
appends to the cookie's name, and helps you to maintain the same user
assignment across behaviors within a property, and across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDuration" >

- `allowedUserCookieDuration` (_number within 0-600 range_):
    With `allowedUserCookieEnabled` on, sets the number of seconds for
the allowed user's session once allowed through to the site.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieRefresh" >

- `allowedUserCookieRefresh` (_boolean_):
    With `allowedUserCookieEnabled` on, enabling this resets the
duration of an allowed cookie with each request, so that it only
expires if the user doesn't make any requests for the specified
duration. Do not enable this option if you want to set a fixed time
for all users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieAdvanced" >

- `allowedUserCookieAdvanced` (_boolean_):
    With `allowedUserCookieEnabled` on, sets advanced configuration
options for the allowed user's cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieAutomaticSalt" >

- `allowedUserCookieAutomaticSalt` (_boolean_):
    With `allowedUserCookieAdvanced` enabled, sets an automatic _salt_
value to verify the integrity of the cookie for an allowed user.
Disable this if you want to share the cookie across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieSalt" >

- `allowedUserCookieSalt` (_string_):
    With `allowedUserCookieAdvanced` enabled and
`allowedUserCookieAutomaticSalt` disabled, specifies a fixed _salt_
value, which is incorporated into the cookie's value to prevent users
from manipulating it. You can use the same salt string across
different behaviors or properties to apply a single cookie to all
allowed users.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDomainType" >

- `allowedUserCookieDomainType` (_enum string_):
    With `allowedUserCookieAdvanced` enabled, selects whether to use
the `DYNAMIC` incoming host header, or a `CUSTOMER`-defined cookie
domain.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieDomain" >

- `allowedUserCookieDomain` (_string_):
    With `allowedUserCookieAdvanced` enabled, specifies a domain for
an allowed user cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieHttpOnly" >

- `allowedUserCookieHttpOnly` (_boolean_):
    With `allowedUserCookieAdvanced` enabled, applies the `HttpOnly`
flag to the allowed user's cookie to ensure it's accessed over HTTP
and not manipulated by the client.

</div>

<div class="option" markdown="1" id="visitorPrioritization.allowedUserCookieSecure" >

- `allowedUserCookieSecure` (_boolean_):
    With `allowedUserCookieAdvanced` enabled, applies the `Secure`
flag to the allowed user's cookie to transmit it over a secure
connection.  You can apply this option only if the property itself is
secure.  See [Secure property requirements](#sf) for guidance.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieEnabled" >

- `waitingRoomCookieEnabled` (_boolean_):
    Enables a cookie to track a waiting room assignment.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieShareLabel" >

- `waitingRoomCookieShareLabel` (_boolean_):
    With `allowedUserCookieEnabled` and `waitingRoomCookieEnabled`
both `true`, enabling this option shares the same
`allowedUserCookieLabel` string. If disabled, specify a different
`waitingRoomCookieLabel`.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieLabel" >

- `waitingRoomCookieLabel` (_string_):
    With `waitingRoomCookieEnabled` on and either
`allowedUserCookieEnabled` or `waitingRoomCookieShareLabel` off,
specifies a label to distinguish this waiting room cookie from
others. The value appends to the cookie's name, and helps you to
maintain the same waiting room assignment across behaviors within a
property, and across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDuration" >

- `waitingRoomCookieDuration` (_number within 0-120 range_):
    With `waitingRoomCookieEnabled` on, sets the number of seconds for
which users remain in the waiting room. During this time, users who
refresh the waiting room page remain there.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieAdvanced" >

- `waitingRoomCookieAdvanced` (_boolean_):
    When enabled along with `waitingRoomCookieEnabled`, sets advanced
configuration options for the waiting room cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieAutomaticSalt" >

- `waitingRoomCookieAutomaticSalt` (_boolean_):
    With `waitingRoomCookieAdvanced` enabled, sets an automatic _salt_
value to verify the integrity of the waiting room cookie.  Disable
this if you want to share the cookie across properties.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieSalt" >

- `waitingRoomCookieSalt` (_string_):
    With `waitingRoomCookieAdvanced` enabled and
`waitingRoomCookieAutomaticSalt` disabled, specifies a fixed _salt_
value, which is incorporated into the cookie's value to prevent users
from manipulating it. You can use the same salt string across
different behaviors or properties to apply a single cookie for the
waiting room session.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDomainType" >

- `waitingRoomCookieDomainType` (_enum string_):
    With `waitingRoomCookieAdvanced` enabled, selects whether to use
the `DYNAMIC` incoming host header, or a `CUSTOMER`-defined cookie
domain.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieDomain" >

- `waitingRoomCookieDomain` (_string_):
    With `waitingRoomCookieAdvanced` enabled, specifies a domain for
the waiting room cookie.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieHttpOnly" >

- `waitingRoomCookieHttpOnly` (_boolean_):
    With `waitingRoomCookieAdvanced` enabled, applies the `HttpOnly`
flag to the waiting room cookie to ensure it's accessed over HTTP and
not manipulated by the client.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCookieSecure" >

- `waitingRoomCookieSecure` (_boolean_):
    With `waitingRoomCookieAdvanced` enabled, applies the `Secure`
flag to the waiting room cookie to transmit it over a secure
connection.  You can apply this option only if the property itself is
secure. See [Secure property requirements](#sf) for guidance.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomStatusCode" >

- `waitingRoomStatusCode` (_number_):
     Specifies the response code for requests sent to the waiting
room.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomUseCpCode" >

- `waitingRoomUseCpCode` (_boolean_):
    When enabled, allows you to assign a different CP code that tracks
any requests that are sent to the waiting room.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCpCode" >

- `waitingRoomCpCode` (_object_):
    With `waitingRoomUseCpCode` enabled, specifies a `cpcode` object
for requests sent to the waiting room, including a numeric `id` key
and a descriptive `name`:

        "waitingRoomCpCode": {
            "id": 12345,
            "name": "sent to waiting room"
        }

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomNetStorage" >

- `waitingRoomNetStorage` (_object_):
    Specifies the NetStorage domain for the waiting room page. For
example:

        "waitingRoomNetStorage": {
            "id": "netstorage_id",
            "name": "Example Downloads",
            "downloadDomainName": "download.example.com",
            "cpCode": 12345
        }

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomDirectory" >

- `waitingRoomDirectory` (_string; allows [variables](#vf)_):
    Specifies the NetStorage directory that contains the static waiting
room page, with no trailing slash character.

</div>

<div class="option" markdown="1" id="visitorPrioritization.waitingRoomCacheTtl" >

- `waitingRoomCacheTtl` (_number within 5-30 range_):
    Specifies the waiting room page's time to live in the cache, `5`
minutes by default.

</div>

</div>

<div class="feature" data-feature="watermarkUrl" markdown="1">

## watermarkUrl

__Property Manager name__:
[Watermark Token](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9014)

Aliases a token to a
watermark image URL.

__Options__:

<div class="option" markdown="1" id="watermarkUrl.token" >

- `token` (_string_):
    Specifies the
string token.

</div>

<div class="option" markdown="1" id="watermarkUrl.imageUrl" >

- `imageUrl` (_string_):
    Specifies
the URL for the watermark image.

</div>

</div>

<div class="feature" data-feature="webApplicationFirewall" markdown="1">

## webApplicationFirewall

__Property Manager name__:
[Web Application Firewall](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9059)

The
[Web Application Firewall](http://www.akamai.com/html/solutions/web-application-firewall.html)
behavior implements a suite of security features that blocks
threatening HTTP and HTTPS requests. Use it as your primary firewall,
or in addition to existing security measures.  Only one referenced
configuration is allowed per property, so this behavior typically
belongs as part of its default rule.

__Options__:

<div class="option" markdown="1" id="webApplicationFirewall.firewallConfiguration" >

- `firewallConfiguration` (_object_):
    An object featuring details about your firewall configuration, for
example:

        "firewallConfiguration": {
            "configId"          : 1,
            "productionStatus"  : "Active",
            "productionVersion" : 1,
            "stagingStatus"     : "Active",
            "stagingVersion"    : 1
        }

</div>

</div>

<div class="feature" data-feature="webdav" markdown="1">

## webdav

__Property Manager name__:
[WebDAV](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9057)

Web-based Distributed Authoring
and Versioning (WebDAV) is a set of extensions to the HTTP protocol
that allows users to collaboratively edit and manage files on remote
web servers. This behavior enables WebDAV, and provides support for
the following additional request methods: PROPFIND, PROPPATCH, MKCOL,
COPY, MOVE, LOCK, and UNLOCK. To apply this behavior, you need to
match on a [`requestMethod`](#requestmethod).

__Options__:

<div class="option" markdown="1" id="webdav.enabled" >

- `enabled` (_boolean_):
    Enables the WebDAV
behavior.

</div>

</div>

<div class="feature" data-feature="webSockets" markdown="1">

## webSockets

__Property Manager name__:
[WebSockets](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0086)

The WebSocket protocol allows
web applications real-time bidirectional communication between
clients and servers.

__Options__:

<div class="option" markdown="1" id="webSockets.enabled" >

- `enabled` (_boolean_):
    Enables
WebSocket traffic.

</div>

</div>
