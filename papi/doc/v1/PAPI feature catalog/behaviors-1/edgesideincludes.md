---
title: "edgeSideIncludes"
slug: "edgesideincludes"
hidden: false
createdAt: "2020-06-15T21:21:56.695Z"
updatedAt: "2020-06-15T21:21:56.695Z"
---
__Property Manager name__: [ESI](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0094)

Allows edge servers to process [edge side include (ESI)](http://www.akamai.com/html/support/esi.html) code to generate dynamic content. To apply this behavior, you need to match on a [`contentType`](#contenttype), [`path`](#path), or [`filename`](#filename). Since this behavior requires more parsing time, you should not apply it to pages that lack ESI code, or to any non-HTML content.

__Options__:

<div class="option" markdown="1" id="edgeSideIncludes.enabled" >

- `enabled` (_boolean_): Enables ESI processing.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.enableViaHttp" >

- `enableViaHttp` (_boolean_): Enable ESI only for content featuring the following HTTP response header: `Edge-control: dca=esi`

</div>

<div class="option" markdown="1" id="edgeSideIncludes.passSetCookie" >

- `passSetCookie` (_boolean_): When enabled, allows edge servers to pass your origin server's cookies to the ESI processor.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.passClientIp" >

- `passClientIp` (_boolean_): When enabled, allows edge servers to pass the client IP header to the ESI processor.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.i18nStatus" >

- `i18nStatus` (_boolean_): When enabled, provides internationalization support for ESI.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.i18nCharset" >

- `i18nCharset` (_array of string values_): With `i18nStatus` enabled, specifies the character sets to use when transcoding the ESI language, `UTF-8` and `ISO-8859-1` for example.

</div>

<div class="option" markdown="1" id="edgeSideIncludes.detectInjection" >

- `detectInjection` (_boolean_): When enabled, denies attempts to inject ESI code.

</div>

</div>

<div class="feature" data-feature="enhancedAkamaiProtocol" markdown="1">
