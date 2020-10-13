---
title: "Data conventions"
slug: "data-conventions"
hidden: false
createdAt: "2020-06-05T16:09:20.427Z"
updatedAt: "2020-06-10T03:02:22.992Z"
---
PAPI's JSON data follows these overall conventions:

- When any response data can be singular or plural, it's always [represented as an array](http://jsonapi.org/format), named `items`, to simplify client processing. This also applies to resources that only yield a single item.

- Response data is wrapped within a common [Envelope](#envelope) object that provides necessary context about the data.

- Parameter names always match member names in JSON requests and responses.

- Member names explicitly reference the type of object, for example `propertyVersion` rather than `version`.

PAPI applies these JSON member naming conventions:

- `*Id` members are machine-readable identifiers used for inputs to URL operations.  Their values may appear with three-letter prefixes, or you can configure them not to appear. See [ID prefixes](#prefixes).

- `*Name` members are descriptive and human-readable, and never serve as URL parameter values or in any other context to key data.

- `*Date` members represent timestamps in ISO 8601 format using the UTC timezone.

- `*Link` members are URLs that respond to HTTP GET requests, described by a linked JSON schema document. As a convenience, any response that provides a `*Link` JSON member also provides the same information in the `Location` HTTP header. Since API hostnames are client-specific, URLs appear as [absolute-path relative reference URLs](http://tools.ietf.org/html/rfc3986#section-4.2), for example `/papi/v1/properties` rather than `https://myclient.luna.akamaiapis.net/papi/v1/properties`. Clients need to establish the base URL of links from the [retrieval URL](http://tools.ietf.org/html/rfc3986#section-5.1.3). The `*` portion of the name serves as the [link relation](http://tools.ietf.org/html/rfc5988#section-4.2).