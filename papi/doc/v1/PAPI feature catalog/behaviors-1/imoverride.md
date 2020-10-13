---
title: "imOverride"
slug: "imoverride"
hidden: false
createdAt: "2020-06-15T21:30:45.603Z"
updatedAt: "2020-06-15T21:30:45.603Z"
---
__Property Manager name__: [Image and Video Manager: Set Parameter](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0051)

This specifies common query parameters that affect how [`imageManager`](#imagemanager) transforms images, potentially overriding policy, width, format, or density request parameters. This also allows you to assign the value of one of the property's [rule tree variables](#vf) to one of Image and Video Manager's own policy variables.

__Options__:

<div class="option" markdown="1" id="imOverride.override" >

- `override` (_enum string_): Selects the type of query parameter you want to set, either the `DPR` for pixel density, `FORMAT` for browser types, `POLICY` for the name of the Image and Video Manager policy you want to apply, or the predefined `WIDTH` to constrain the image to.  Alternately specify that you want to set an Image and Video Manager `POLICY_VARIABLE` from a [rule tree variable](#vf) defined in the property.

</div>

<div class="option" markdown="1" id="imOverride.typesel" >

- `typesel` (_enum string_): When setting any query parameter, specifies whether to set it to a specific `VALUE`, or whether to assign a Property Manager rule tree `VARIABLE`.

</div>

<div class="option" markdown="1" id="imOverride.formatvar" >

- `formatvar` (_string_): With the `override` parameter set to `FORMAT` and the `typesel` set to `VARIABLE`, this selects the variable with the name of the browser you want to optimize images for. The variable specifies the same type of data as the `format` option below.

</div>

<div class="option" markdown="1" id="imOverride.format" >

- `format` (_enum string_): With the `override` parameter set to `FORMAT` and the `typesel` set to `VALUE`, this specifies the name of the browser you want to optimize images for, either `CHROME`, `SAFARI`, `IE`, or `GENERIC`.

</div>

<div class="option" markdown="1" id="imOverride.dprvar" >

- `dprvar` (_string_): With the `override` parameter set to `DPR` and the `typesel` set to `VARIABLE`, this selects the variable with the desired pixel density. The variable specifies the same type of data as the `dpr` option below.

</div>

<div class="option" markdown="1" id="imOverride.dpr" >

- `dpr` (_number_): With the `override` parameter set to `DPR` and the `typesel` set to `VALUE`, this directly specifies the pixel density. The numeric value is a scaling factor of 1, representing normal density.

</div>

<div class="option" markdown="1" id="imOverride.widthvar" >

- `widthvar` (_string_): With the `override` parameter set to `WIDTH` and the `typesel` set to `VARIABLE`, this selects the variable with the desired width.  If the Image and Video Manager policy doesn't define that width, it serves the next largest width.

</div>

<div class="option" markdown="1" id="imOverride.width" >

- `width` (_number_): With the `override` parameter set to `WIDTH` and the `typesel` set to `VALUE`, this sets the image's desired pixel width directly. If the Image Manager policy doesn't define that width, it serves the next largest width.

</div>

<div class="option" markdown="1" id="imOverride.policyvar" >

- `policyvar` (_string_): With the `override` parameter set to `POLICY` and the `typesel` set to `VARIABLE`, this selects the variable with the desired Image and Video Manager policy name to apply to image requests. If there is no policy by that name, Image and Video Manager serves the image unmodified.

</div>

<div class="option" markdown="1" id="imOverride.policy" >

- `policy` (_string_): With the `override` parameter set to `POLICY` and the `typesel` set to `VALUE`, this selects the desired Image and Video Manager policy name directly. If there is no policy by that name, Image and Video Manager serves the image unmodified.

</div>

<div class="option" markdown="1" id="imOverride.policyvarName" >

- `policyvarName` (_string_): With `override` set to `POLICY_VARIABLE`, this selects the name of one of the variables defined in an Image and Video Manager policy that you want to replace with the property's rule tree variable.

</div>

<div class="option" markdown="1" id="imOverride.policyvarIMvar" >

- `policyvarIMvar` (_string_): With `override` set to `POLICY_VARIABLE`, this selects one of the property's rule tree variables to assign to the `policyvarName` variable within Image and Video Manager.

</div>

</div>

<div class="feature" data-feature="injectReferenceId" markdown="1">
