---
title: "imageManager"
slug: "imagemanager"
hidden: false
createdAt: "2020-06-15T21:29:51.024Z"
updatedAt: "2020-06-15T21:29:51.024Z"
---
__Property Manager name__: [Image and Video Manager](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0052)

Optimizes images' size or file type for the requesting device.  You can also use this behavior to generate API tokens to apply your own policies to matching images using the [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html). To apply this behavior, you need to match on a [`fileExtension`](#fileextension).

__Options__:

<div class="option" markdown="1" id="imageManager.enabled" >

- `enabled` (_boolean_): Enable image management capabilities and generate a corresponding API token.

</div>

<div class="option" markdown="1" id="imageManager.resize" >

- `resize` (_boolean_): Specify whether to scale down images to the maximum screen resolution, as determined by the rendering device's user agent.  Note that enabling this may affect screen layout in unexpected ways.

</div>

<div class="option" markdown="1" id="imageManager.applyBestFileType" >

- `applyBestFileType` (_boolean_): Specify whether to convert images to the best file type for the requesting device, based on its user agent and the initial image file. This produces the smallest file size possible that retains image quality.

</div>

<div class="option" markdown="1" id="imageManager.superCacheRegion" >

- `superCacheRegion` (_enum string_): Specifies a location for your site's heaviest traffic, for use in caching derivatives on edge servers.  Possible values are `US`, `JAPAN`, `ASIA`, `AUSTRALIA`, or `EMEA` (Europe, Middle East, and Africa).

</div>

<div class="option" markdown="1" id="imageManager.cpCodeOriginal" >

- `cpCodeOriginal` (_object_): Assigns a CP code to track traffic and billing for original images that the Image and Video Manager has not modified. Form the value as an object with a single `id` member paired with an integer value, for example: `"cpCodeOriginal":{"id":12345}`.

</div>

<div class="option" markdown="1" id="imageManager.cpCodeTransformed" >

- `cpCodeTransformed` (_object_): Assigns a separate CP code to track traffic and billing for derived images. Form the value as an object with a single `id` member paired with an integer value, for example: `"cpCodeTransformed":{"id":12345}`.

</div>

<div class="option" markdown="1" id="imageManager.advanced" >

- `advanced` (_boolean_): When enabled, allows you to generate a custom [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html) token to apply a corresponding policy to this set of images. The token consists of a descriptive label (the `policyToken`) concatenated with a property-specific identifier that's generated when you save the property. The API registers the token when you activate the property.

</div>

<div class="option" markdown="1" id="imageManager.policyToken" >

- `policyToken` (_string_): With `advanced` enabled, assign a prefix label to help match the policy token to this set of images, limited to 32 alphanumeric or underscore characters. If you don't specify a label, _default_ becomes the prefix.

</div>

<div class="option" markdown="1" id="imageManager.policyTokenDefault" >

- `policyTokenDefault` (_string_): Specify the default policy identifier, which is registered with the [Image and Video Manager API](https://learn.akamai.com/en-us/api/web_performance/image_manager/v2.html) once you activate this property.  The `advanced` option needs to be inactive.

</div>

</div>

<div class="feature" data-feature="imageManagerVideo" markdown="1">
