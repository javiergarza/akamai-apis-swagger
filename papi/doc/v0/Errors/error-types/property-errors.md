---
title: "Property errors"
slug: "property-errors"
hidden: false
createdAt: "2020-06-05T21:17:39.345Z"
updatedAt: "2020-06-05T21:17:39.345Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `property/invalid-name` | Property names may only use alphanumeric characters, underscores, dashes, and dots. |
| [400](https://httpstatuses.com/400) | `property/name-in-use` | Each property name must be unique. |
| [403](https://httpstatuses.com/403) | `property-version/lock-error` | Only Akamai representatives can change read-only behaviors, criteria, and child rules. [Learn more](#advancedfeatures). |
| [403](https://httpstatuses.com/403) | `property-version/lock-error/behaviors-changed` | Read-only behaviors have been added, removed, changed, or moved. [Learn more](#advancedfeatures). |
| [403](https://httpstatuses.com/403) | `property-version/lock-error/criteria-changed` | Read-only criteria have been added, removed, changed, or moved. [Learn more](#advancedfeatures). |
| [403](https://httpstatuses.com/403) | `property-version/lock-error/rule-structure-changed` | Read-only rules have been added, removed, changed, or moved. [Learn more](#advancedfeatures). |
| [404](https://httpstatuses.com/404) | `property-deletion/not-found` | The property you're trying to delete is unknown.|
| [404](https://httpstatuses.com/404) | `property-version/not-found` | The requested Property version isn't available. |
| [429](https://httpstatuses.com/429) | `limit-exceeded.properties_per_contract` | You exceeded the limit on the number of properties for your contract, and must deactivate one before proceeding. Contact your Akamai representative for information on how to increase this limit. [Learn more](#ratelimiting). |
| [500](https://httpstatuses.com/500) | `property-version/error` | The platform couldn't process your request on the specified property version. |