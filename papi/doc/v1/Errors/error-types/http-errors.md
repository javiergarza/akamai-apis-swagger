---
title: "HTTP errors"
slug: "http-errors"
hidden: false
createdAt: "2020-06-05T21:14:20.240Z"
updatedAt: "2020-06-05T21:14:20.240Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `http/bad-request` | The system cannot understand your request, perhaps due to malformed data. |
| [401](https://httpstatuses.com/401) | `http/unauthorized` | The request requires authentication. |
| [403](https://httpstatuses.com/403) | `http/forbidden` | The authorization token doesn't allow access to the resource. For example, the request may specify products not authorized on a contract. |
| [404](https://httpstatuses.com/404) | `http/not-found` | Unable to locate the requested resource. |
| [405](https://httpstatuses.com/405) | `http/method-not-allowed` | The specified HTTP method isn't supported for this resource. |
| [406](https://httpstatuses.com/406) | `http/not-acceptable` | The `content-type` restriction specified by your `Accept` header isn't supported. |
| [412](https://httpstatuses.com/412) | `etag-conflict` | The `Etag` you provided doesn't match the most recent edit. The data has changed since initially accessed. [Learn more](#concurrencycontrol). |
| [412](https://httpstatuses.com/412) | `http/precondition-failed` | Preconditions such as `If-Match` or `If-Not-Match` aren't satisfied. The data has changed since initially accessed. [Learn more](#concurrencycontrol). |
| [415](https://httpstatuses.com/415) | `http/unsupported-media-type` | The requested MIME format isn't allowed. |
| [500](https://httpstatuses.com/500) | `http/internal-server-error` | The platform experienced an unknown error. |
| [501](https://httpstatuses.com/501) | `http/not-implemented` | The platform doesn't support the requested functionality. |