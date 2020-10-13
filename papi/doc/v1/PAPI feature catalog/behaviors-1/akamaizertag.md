---
title: "akamaizerTag"
slug: "akamaizertag"
hidden: false
createdAt: "2020-06-15T20:25:56.507Z"
updatedAt: "2020-06-15T20:31:40.094Z"
---
__Property Manager name__: [Akamaize Tag](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9075)

This [read-only behavior](#ro) specifies HTML tags and replacement rules for hostnames used in conjunction with the [`akamaizer`](#akamaizer) behavior. Contact Akamai Professional Services for help configuring the Akamaizer.

__Options__:

<div class="option" markdown="1" id="akamaizerTag.matchHostname" >

- `matchHostname` (_string_): Specifies the hostname to match on as a Perl-compatible regular expression.

</div>

<div class="option" markdown="1" id="akamaizerTag.replacementHostname" >

- `replacementHostname` (_string_): Specifies the replacement hostname for the tag to use.

</div>

<div class="option" markdown="1" id="akamaizerTag.scope" >

- `scope` (_enum string_): Specifies the part of HTML content the `tagsAttribute` refers to:

    - `ATTRIBUTE` for when `tagsAttribute` refers to a     tag/attribute pair, the match only applies to the attribute.
    - `URL_ATTRIBUTE` is the same as `ATTRIBUTE`, but applies when the attribute     value is a URL. In that case, it converts to an absolute URL     prior to substitution.
    - `BLOCK` substitutes within the tag's contents, but not within     any nested tags.
    - `PAGE` ignores the `tagsAttribute` field     and performs the substitution on the entire page.

</div>

<div class="option" markdown="1" id="akamaizerTag.tagsAttribute" >

- `tagsAttribute` (_enum string_): Specifies the tag or tag/attribute combination to operate on, any of the following:

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

- `replaceAll` (_boolean_): Replaces all matches when enabled, otherwise replaces only the first match.

</div>

<div class="option" markdown="1" id="akamaizerTag.includeTagsAttribute" >

- `includeTagsAttribute` (_boolean_): Whether to include the `tagsAttribute` value.

</div>
