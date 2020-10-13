---
title: "Concurrency control"
slug: "concurrency-control"
hidden: false
createdAt: "2020-06-05T16:15:44.961Z"
updatedAt: "2020-06-05T20:08:54.731Z"
---
PAPI provides support for
[optimistic concurrency control](http://en.wikipedia.org/wiki/Optimistic_concurrency_control)
on its [property version](#propertyversionsgroup),
[property hostname](#propertyversionhostnamesgroup), and
[rule](#propertyversionrulesgroup) resources. When
reading data from any of these resources, an opaque digest string
representing a snapshot of the property version is available from:

- An `etag` object member.
- The double-quoted contents of the `Etag` HTTP header.

When performing any subsequent PUT, PATCH, or DELETE write operation,
or when calling [POST to clone a property](#postproperties), provide
the same data as either of these:

- An `etag` object member.
- The double-quoted contents of the `If-Match` HTTP header.

The request succeeds if the digest matches the current state of the
resource's data, otherwise it produces a 412 error. This prevents
outdated representations from being used as the basis for updates when
more than one client accesses the same resource. It keeps you from
overwriting other users' data, regardless of whether they access it
with PAPI or the Property Manager interface.


[block:callout]
{
  "type": "warning",
  "body": "Within the `Etag` or `If-Match` HTTP headers, the data\ndigest _must_ be double-quoted, or the request fails even if the\ndigest otherwise appears to match. Also, you can only use the\n`If-Match` HTTP header when writing\n[property hostnames](#propertyversionhostnamesgroup),\nbecause that interface specifies an array, which can't accommodate a\ntop-level `etags` object member",
  "title": "Double-quoted etag values"
}
[/block]
PAPI offers other ways to use this mechanism:

- When
[creating a new property version](#postpropertyversions),
passing the request's `createFromVersionEtag` member back in as an
`etag` ensures the component hostnames or rules of the version on
which it was based haven't changed in the interim.

- When [cloning a property](#postproperties),
passing the request's `cloneFromVersionEtag` member back in as an
`etag` ensures the component hostnames or rules of the property
version on which it was based haven't changed in the interim.

PAPI tracks changes to data for the entire property version. Suppose
you read a property version's rule tree along with its `etag` digest.
Another client then modifies the property version's set of hostnames.
When you write the rule tree back along with the `etag`, the request
fails because one of the version's components has been modified.


[block:callout]
{
  "type": "info",
  "body": "The\n[Network Lists API]({{base.url}}/{{page.language}}/api/cloud_security/network_lists/v2.html)\nuses the term _Sync Point_ to refer to the same concurrency control\nfeature."
}
[/block]