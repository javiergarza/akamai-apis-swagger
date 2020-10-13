---
title: "imageManagerVideo"
slug: "imagemanagervideo"
hidden: false
createdAt: "2020-06-15T21:30:16.761Z"
updatedAt: "2020-06-15T21:30:16.761Z"
---
__Property Manager name__: [Image and Video Manager](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0124)

Optimizes videos managed by Image and Video Manager for the requesting device.  You can also use this behavior to generate API tokens to apply your own policies to matching videos using the [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html). To apply this behavior, you need to match on a [`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="imageManagerVideo.enabled" >

- `enabled` (_boolean_): Applies Image and Video Manager's video optimization to the current content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.resize" >

- `resize` (_boolean_): When enabled, scales down video for smaller mobile screens, based on the device's `User-Agent` header.

</div>

<div class="option" markdown="1" id="imageManagerVideo.applyBestFileType" >

- `applyBestFileType` (_boolean_): When enabled, automatically converts videos to the best file type for the requesting device. This produces the smallest file size that retains image quality, based on the user agent and the initial image file.

</div>

<div class="option" markdown="1" id="imageManagerVideo.superCacheRegion" >

- `superCacheRegion` (_enum string_): To optimize caching, assign a region close to your site's heaviest traffic, either `ASIA`, `AUSTRALIA`, `EMEA` (Europe, Middle East and Africa), `JAPAN`, or `US`. Assign `US` if your site's heaviest traffic varies across regions.

</div>

<div class="option" markdown="1" id="imageManagerVideo.cpCodeOriginal" >

- `cpCodeOriginal` (_object_): Select the CP code for which to track Image and Video Manager video traffic. Use this along with `cpCodeTransformed` to track traffic to derivative video content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.cpCodeTransformed" >

- `cpCodeTransformed` (_object_): Select the CP code to identify derivative transformed video content.

</div>

<div class="option" markdown="1" id="imageManagerVideo.advanced" >

- `advanced` (_boolean_): When disabled, applies a single standard policy based on your property name.  When enabled, allows you to reference a rule-specific `policyToken` for videos with different match criteria.

</div>

<div class="option" markdown="1" id="imageManagerVideo.policyToken" >

- `policyToken` (_string_): With `advanced` enabled, specifies a custom policy defined in the Image and Video Manager Policy Manager or the [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html). The policy name can include up to 64 alphanumeric, dash, or underscore characters.

</div>

<div class="option" markdown="1" id="imageManagerVideo.policyTokenDefault" >

- `policyTokenDefault` (_string_): Specify the default policy identifier, which is registered with the [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html) once you activate this property.

</div>

</div>

<div class="feature" data-feature="imOverride" markdown="1">
