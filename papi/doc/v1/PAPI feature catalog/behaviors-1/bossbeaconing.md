---
title: "bossBeaconing"
slug: "bossbeaconing"
hidden: false
createdAt: "2020-06-15T20:44:56.063Z"
updatedAt: "2020-06-15T20:44:56.063Z"
---
__Property Manager name__: [Diagnostic data beacons](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9066)

Triggers diagnostic data beacons for use with BOSS, Akamai's monitoring and diagnostics system.

__Options__:

<div class="option" markdown="1" id="bossBeaconing.enabled" >

- `enabled` (_boolean_): Enable diagnostic data beacons.

</div>

<div class="option" markdown="1" id="bossBeaconing.cpcodes" >

- `cpcodes` (_string_): The space-separated list of CP codes that trigger the beacons. You need to specify the same set of CP codes within BOSS.

</div>

<div class="option" markdown="1" id="bossBeaconing.requestType" >

- `requestType` (_enum string_): Specify whether to trigger a beacon for `EDGE` requests only, or `EDGE_MIDGRESS` to include midgress requests.

</div>

<div class="option" markdown="1" id="bossBeaconing.forwardType" >

- `forwardType` (_enum string_): Specify whether to trigger a beacon for internal `MIDGRESS` forwards only, `ORIGIN` forwards only, or `MIDGRESS_ORIGIN` for both.

</div>

<div class="option" markdown="1" id="bossBeaconing.samplingFrequency" >

- `samplingFrequency` (_enum string_): Specifies `SAMPLING_FREQ_0_1` as a sampling frequency, or `SAMPLING_FREQ_0_0` to disable beacons altogether.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalSamplingFrequency" >

- `conditionalSamplingFrequency` (_enum string_): Specifies either `CONDITIONAL_SAMPLING_FREQ_0_1`, `CONDITIONAL_SAMPLING_FREQ_0_2`, `CONDITIONAL_SAMPLING_FREQ_0_3`, or `CONDITIONAL_SAMPLING_FREQ_0_0` to disable beacons altogether.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalHTTPStatus" >

- `conditionalHTTPStatus` (_array of string values_): Specifies the set of response status codes or ranges that trigger the beacon. You can combine any of these values: `0xx`, `302`, `304`, `3xx`, `401`, `403`, `404`, `408`, `4xx`, `500`, `503`, `5xx`, `6xx`.

</div>

<div class="option" markdown="1" id="bossBeaconing.conditionalErrorPattern" >

- `conditionalErrorPattern` (_string_): A space-separated set of error patterns that trigger beacons to conditional feeds. Each pattern can include wildcards, such as `*CONNECT* *DENIED*`.

</div>

</div>

<div class="feature" data-feature="breadcrumbs" markdown="1">
