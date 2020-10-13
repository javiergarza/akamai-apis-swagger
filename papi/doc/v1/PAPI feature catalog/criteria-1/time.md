---
title: "time"
slug: "time"
hidden: false
createdAt: "2020-06-15T22:28:01.387Z"
updatedAt: "2020-06-15T22:28:01.387Z"
---
__Property Manager name__: [Time Interval](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Specifies ranges of times during which the request occurred.

__Options__:

- `matchOperator` (_enum string_): Specifies how to define the range of time:

    - `BEGINNING` if the duration is indefinite, using the value of     `beginDate`.
    - `BETWEEN` sets a single range between two dates, using the     values of `beginDate` and `endDate`.
    - `LASTING` also sets a single range, but based on duration     relative to the starting time. It relies on the values of     `lastingDate` and `lastingDuration`.
    - `REPEATING` allows a `LASTING`-style range to repeat at regular     intervals. It relies on the values of `repeatBeginDate`,     `repeatDuration`, and `repeatInterval`.

- `repeatInterval` (_duration string_): Sets the time between each repeating time period's starting points when `behavior` set to `REPEATING`.

- `repeatDuration` (_duration string_): Sets the duration of each repeating time period with `behavior` set to `REPEATING`.

- `lastingDuration` (_duration string_): With `behavior` set to `LASTING`, specifies the end of a time period as a duration relative to the `lastingDate`.

- `lastingDate` (_ISO 8601 format date/time string_): Sets the start of a fixed time period with `behavior` set to `LASTING`.

- `repeatBeginDate` (_ISO 8601 format date/time string_): Sets the start of the initial time period with `behavior` set to `REPEATING`.

- `applyDaylightSavingsTime` (_boolean_): Adjusts the start time plus repeat interval to account for daylight saving time. Applies when the current time and the start time use different systems, daylight and standard, and the two values are in conflict.

- `beginDate` (_ISO 8601 format date/time string_): Sets the start of a time period with `behavior` set to `BEGINNING` or `BETWEEN`.

- `endDate` (_ISO 8601 format date/time string_): Sets the end of a fixed time period with `behavior` set to `BETWEEN`.
