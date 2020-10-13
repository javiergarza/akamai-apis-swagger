---
title: "Data errors"
slug: "data-errors"
hidden: false
createdAt: "2020-06-05T21:14:46.818Z"
updatedAt: "2020-06-05T21:14:46.818Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `json-mapping-error` | Your input couldn't be validated against the schema, most likely because it isn't the expected data type. |
| [400](https://httpstatuses.com/400) | `json-parse-error` | Your input couldn't be parsed as JSON. The problem response provides details on the location of the parsing error. |
| [400](https://httpstatuses.com/400) | `json-schema-invalid` | Your input doesn't validate against the data's schema. |
| [400](https://httpstatuses.com/400) | `missing-request-body-field` | Your request is missing a `Body` field. |
| [400](https://httpstatuses.com/400) | `missing-required-parameter` | The request URL is missing a required parameter, which is detailed in the problem response. |
| [400](https://httpstatuses.com/400) | `search/extra-request-body-fields` | Only a single key/value pair is allowed in the search request. [Learn more](#postfindbyvalue). |
| [400](https://httpstatuses.com/400) | `search/missing-request-body-field` | A required key/value pair is missing from the request. [Learn more](#postfindbyvalue). |
| [400](https://httpstatuses.com/400) | `search/missing-request-body` | A request body object is required for the search. [Learn more](#postfindbyvalue). |
| [400](https://httpstatuses.com/400) | `search/unrecognized-request-body-field` | The JSON member in the request is unrecognized. [Learn more](#postfindbyvalue). |