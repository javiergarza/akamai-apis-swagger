---
title: "deviceCharacteristicCacheId"
slug: "devicecharacteristiccacheid"
hidden: false
createdAt: "2020-06-15T21:12:23.837Z"
updatedAt: "2020-06-15T21:12:23.837Z"
---
__Property Manager name__: [Device Characterization - Define Cached Content](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0033)

By default, source URLs serve as cache IDs on edge servers. Electronic Data Capture allows you to specify an additional set of device characteristics to generate separate cache keys. Use this in conjunction with the [`deviceCharacteristicHeader`](#devicecharacteristicheader) behavior.

__Options__:

<div class="option" markdown="1" id="deviceCharacteristicCacheId.elements" >

- `elements` (_array of string values_): Specifies a set of information about the device with which to generate a separate cache key, any of the following values:

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
