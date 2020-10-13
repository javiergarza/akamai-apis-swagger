---
title: "limitBitRate"
slug: "limitbitrate"
hidden: false
createdAt: "2020-06-15T21:34:01.700Z"
updatedAt: "2020-06-15T21:34:01.700Z"
---
__Property Manager name__: [Bit Rate Limiting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9006)

Control the rate at which content serves out to end users, optionally varying the speed depending on the file size or elapsed download time. Each bit rate specified in the `bitrateTable` array corresponds to a `thresholdTable` entry that activates it.  You can use this behavior to prevent media downloads from progressing faster than they are viewed, for example, or to differentiate various tiers of end-user experience. To apply this behavior, you should match on a [`contentType`](#contenttype), [`path`](#path), or [`filename`](#filename).

__Options__:

<div class="option" markdown="1" id="limitBitRate.enabled" >

- `enabled` (_boolean_): When enabled, activates the bit rate limiting behavior.

</div>

<div class="option" markdown="1" id="limitBitRate.bitrateTable" >

- `bitrateTable` (_array_): Specifies a download rate that corresponds to a `thresholdTable` entry. The bit rate appears as a two-member object consisting of a numeric `bitrateValue` and a `bitrateUnit` string, with allowed values of `Kbps`, `Mbps`, and `Gbps`. For example:

        "bitrateTable": [
            {
                "bitrateValue": 1,
                "bitrateUnit": "Kbps"
            }
        ]

</div>

<div class="option" markdown="1" id="limitBitRate.thresholdTable" >

- `thresholdTable` (_array_): Specifies the minimum size of the file or the amount of elapsed download time before applying the bit rate limit from the corresponding `bitrateTable` entry. The threshold appears as a two-member object consisting of a numeric `thresholdValue` and `thresholdUnit` string, with allowed values of `s` or `B`. This example throttles a download that lasts more than 5 seconds:

        "thresholdTable": [
            {
                "thresholdValue": 5,
                "thresholdUnit": "s"
            }
        ]

</div>

</div>

<div class="feature" data-feature="manifestPersonalization" markdown="1">
