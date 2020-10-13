---
title: "adaptiveImageCompression"
slug: "adaptiveimagecompression"
hidden: false
createdAt: "2020-06-15T20:24:57.518Z"
updatedAt: "2020-06-15T20:27:45.639Z"
---
good, and 3 for poor. It assigns separate
performance criteria for mobile (cellular) and non-mobile networks,
which the `compressMobile` and `compressStandard` options enable
independently.

There are six `method` options, one for each tier and type of network. If the `method` is `COMPRESS`, choose from among the six corresponding `slider` options to specify a percentage. As an alternative to compression, setting the `method` to `STRIP` removes unnecessary application-generated metadata from the image. Setting the `method` to `BYPASS` serves clients the original image.

The behavior serves `ETags` headers as a data signature for each adapted variation. In case of error or if the file size increases, the behavior serves the original image file. Flushing the original image from the edge cache also flushes adapted variants. The behavior applies to the following image file extensions: `jpg`, `jpeg`, `jpe`, `jif`, `jfif`, and `jfi`.

__Options__:

<div class="option" markdown="1" id="adaptiveImageCompression.compressMobile" >

- `compressMobile` (_boolean_): When enabled, adapts images served over cellular mobile networks.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.compressStandard" >

- `compressStandard` (_boolean_): When enabled, adapts images served over non-cellular networks.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1StandardCompressionMethod" >

- `tier1StandardCompressionMethod` (_enum string_): Specifies tier-1 non-cellular network behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1StandardCompressionValue" >

- `tier1StandardCompressionValue` (_number within 0-100 range_): With `tier1StandardCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2StandardCompressionMethod" >

- `tier2StandardCompressionMethod` (_enum string_): Specifies tier-2 non-cellular network behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2StandardCompressionValue" >

- `tier2StandardCompressionValue` (_number within 0-100 range_): With `tier2StandardCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3StandardCompressionMethod" >

- `tier3StandardCompressionMethod` (_enum string_): Specifies tier-5 non-cellular network behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3StandardCompressionValue" >

- `tier3StandardCompressionValue` (_number within 0-100 range_): With `tier3StandardCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1MobileCompressionMethod" >

- `tier1MobileCompressionMethod` (_enum string_): Specifies tier-1 behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier1MobileCompressionValue" >

- `tier1MobileCompressionValue` (_number within 0-100 range_): With `tier1MobileCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2MobileCompressionMethod" >

- `tier2MobileCompressionMethod` (_enum string_): Specifies tier-2 cellular-network behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier2MobileCompressionValue" >

- `tier2MobileCompressionValue` (_number within 0-100 range_): With `tier2MobileCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3MobileCompressionMethod" >

- `tier3MobileCompressionMethod` (_enum string_): Specifies tier-5 cellular-network behavior, either `COMPRESS`, `STRIP`, or `BYPASS`.

</div>

<div class="option" markdown="1" id="adaptiveImageCompression.tier3MobileCompressionValue" >

- `tier3MobileCompressionValue` (_number within 0-100 range_): With `tier3MobileCompressionMethod` set to `COMPRESS`, this specifies the compression percentage.

</div>

</div>

<div class="feature" data-feature="advanced" markdown="1">
