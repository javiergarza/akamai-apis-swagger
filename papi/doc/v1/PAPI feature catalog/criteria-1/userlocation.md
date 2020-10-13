---
title: "userLocation"
slug: "userlocation"
hidden: false
createdAt: "2020-06-15T22:29:41.775Z"
updatedAt: "2020-06-15T22:29:41.775Z"
---
__Property Manager name__: [User Location Data](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

The client browser's approximate geographic location, determined by looking up the IP address in a database.

__Options__:

- `field` (_enum string_): Indicates the geographic scope: `CONTINENT`, `COUNTRY`, or `REGION` for states or provinces within a country.

- `matchOperator` (_enum string_): Matches the specified set of values when set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `countryValues` (_array of string values_): ISO 3166-1 country code, such as `US` or `CN`.

- `continentValues` (_array of string values_): Continent code, one of `AF` (Africa), `AS` (Asia), `EU` (Europe), `NA` (North America), `SA` (South America), `OC` (Oceania), or `OT` (Antarctica).

- `regionValues` (_array of string values_): ISO 3166 country and region codes, for example `US:MA` for Massachusetts or `JP:13` for Tokyo.

- `checkIps` (_enum string_): Specifies which IP addresses determine the user's location:

    - `CONNECTING` considers the connecting client's IP address.
    - `HEADERS` considers IP addresses specified in the `X-Forwarded-For`     header, succeeding if any of them match.
    - `BOTH` behaves like `HEADERS`, but also considers the connecting     client's IP address.

- `useOnlyFirstXForwardedForIp` (_boolean_): When connecting via a proxy server as determined by the `X-Forwarded-For` header, enabling this option matches the end client specified in the header. Disabling it matches the connecting client's IP address.
