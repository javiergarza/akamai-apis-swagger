---
title: "HTTP success codes"
slug: "http-success-codes"
hidden: false
createdAt: "2020-06-05T21:13:18.354Z"
updatedAt: "2020-06-10T03:12:18.039Z"
---
The API produces these HTTP success codes:

| Code | Description |
| :--- | :--- |
| [200](https://httpstatuses.com/200) | The request is successful. |
| [201](https://httpstatuses.com/201) | The new item was successfully created. |
| [204](https://httpstatuses.com/204) | The item was successfully removed. |
| [302](https://httpstatuses.com/302) | The requested item is available at the link provided. |

The tables below provide details for many of the errors you may encounter, along with the HTTP status codes they share. Note that this is _not_ an exhaustive listing, and excludes problems relating to rule trees. Each problem object's `type` member corresponds to items listed in the tables below. Problem types reported in HTTP error responses follow this URL pattern, where the `type` identifier may include an additional slash character:

```
https://problems.luna.akamaiapis.net/papi/{version}/{type}
```

URLs for many problem types included within rule tree and property hostname response objects are formed with an additional `validation` component:

```
https://problems.luna.akamaiapis.net/papi/{version}/validation/{type}
```