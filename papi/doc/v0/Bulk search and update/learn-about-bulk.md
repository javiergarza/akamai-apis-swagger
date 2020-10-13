---
title: "Learn about bulk search and update"
slug: "learn-about-bulk"
hidden: false
createdAt: "2020-06-05T17:39:42.474Z"
updatedAt: "2020-06-05T17:40:54.470Z"
---
This section describes PAPI's new bulk search and update feature. With
bulk search and update, you're no longer limited to modifying your
property configurations one at a time. Maintaining a large set of
properties, you can keep important behaviors synchronized with a few
API calls.

This section shows you how to search across all your properties, then
create a new set of editable property versions based on the results.
It shows you how to _patch_ a set of configurations to modify them,
then activate the entire set of modified properties on Akamai's
staging and production networks.  The section initially focuses on how
to substitute simple values such as hostnames, but eventually you
learn more complex techniques to add new behaviors and rules, and how
to modify other data structures.

This table lists each API operation discussed in this section, along
with schema specifications for the JSON data the API exchanges.  In
each phase of the bulk update procedure, you run a pair of operations,
the first to launch a request, and the second to poll the asynchronous
results:

| POST request...  | ...followed by GET response | Object type |
| :--- | :--- | :--- |
| [Bulk search a set of properties](#postbulksearches) | [List bulk search results](#getbulksearch) | [BulkSearch](#bulksearch) |
| [Bulk version a set of properties](#postbulkpropertyversions) | [List bulk-versioned properties](#getbulkpropertyversion) | [BulkVersion](#bulkversion) |
| [Bulk patch a set of properties](#postbulkpatch)  | [List bulk-patched properties](#getbulkpatches) | [BulkPatch](#bulkpatch) |
| [Bulk activate a set of properties](#postbulkpropertyactivations) | [List bulk-activated properties](#getbulkpropertyactivation) | [BulkActivation](#bulkactivation) |

As an alternative to get the initial set of bulk search results
directly, but with likely delays, use this additional operation:

- [Synchronously bulk search a set of properties](#postbulksearchessynchronus)