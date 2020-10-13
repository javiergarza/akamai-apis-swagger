---
title: "Edge hostname errors"
slug: "edge-hostname-errors"
hidden: false
createdAt: "2020-06-05T21:15:27.374Z"
updatedAt: "2020-06-05T21:15:27.374Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `edgehostname/bad-suffix` | The edge hostname's specified `domainSuffix` isn't allowed. [Learn more](#postedgehostnames). |
| [400](https://httpstatuses.com/400) | `edgehostname/not-available` | The specified edge hostname isn't available. |
| [403](https://httpstatuses.com/403) | `edgehostname/create-forbidden` | The product you assigned to the edge hostname isn't included in your contract. [Learn more](#postedgehostnames). |
| [429](https://httpstatuses.com/429) | `limit-exceeded.edgehostnames_per_contract` | You exceeded the limit on the number of edge hostnames for your contract, and must deactivate one before proceeding. Contact your Akamai representative for information on how to increase this limit. [Learn more](#ratelimiting). |
| [500](https://httpstatuses.com/500) | `edgehostname/create-error` | The platform encountered an unknown error when trying to create the edge hostname. |