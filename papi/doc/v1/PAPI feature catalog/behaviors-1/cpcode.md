---
title: "cpCode"
slug: "cpcode"
hidden: false
createdAt: "2020-06-15T21:03:58.187Z"
updatedAt: "2020-06-15T21:03:58.187Z"
---
__Property Manager name__: [Content Provider Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0030)

Content Provider Codes (CP codes) allow you to distinguish various reporting and billing segments. You receive a CP code when purchasing Akamai service, and you need it to access properties. This behavior allows you to apply any valid CP code, including additional ones you may request from Akamai Professional Services. For a CP code to be valid, it must belong to the same contract and be associated with the same product as the property, and the group must have access to it.

__Options__:

<div class="option" markdown="1" id="cpCode.value" >

- `value` (_object_): Specifies a `value` object, which includes an `id` key and a descriptive `name`:

        "value": {
            "id"   : 12345,
            "name" : "my cpcode"
        }

</div>

</div>

<div class="feature" data-feature="customBehavior" markdown="1">
