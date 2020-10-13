---
title: "Learn about bulk search and update"
slug: "learn-about-bulk"
hidden: false
createdAt: "2020-06-05T17:39:42.474Z"
updatedAt: "2020-06-11T13:00:52.009Z"
---
This section describes PAPI's new bulk search and update feature. With bulk search and update, you're no longer limited to modifying your property configurations one at a time. Maintaining a large set of properties, you can keep important behaviors synchronized with a few API calls.

This section shows you how to search across all your properties, then create a new set of editable property versions based on the results. It shows you how to _patch_ a set of configurations to modify them, then activate the entire set of modified properties on Akamai's staging and production networks.  The section initially focuses on how to substitute simple values such as hostnames, but eventually you learn more complex techniques to add new behaviors and rules, and how to modify other data structures.

This table lists each API operation discussed in this section, along with schema specifications for the JSON data the API exchanges.  In each phase of the bulk update procedure, you run a pair of operations, the first to launch a request, and the second to poll the asynchronous results:

| POST request...  | ...followed by GET response | Object type |
| :--- | :--- | :--- |
| [Bulk search a set of properties](https://papi-akamai.readme.io/reference/bulkrules-search-requests#post_bulk-rules-search-requests) | [List bulk search results](https://papi-akamai.readme.io/reference/bulkrules-search-requestsbulksearchid#get_bulk-rules-search-requests-bulksearchid) | [BulkSearch](#bulksearch) |
| [Bulk version a set of properties](https://papi-akamai.readme.io/reference/bulkproperty-version-creations#post_bulk-property-version-creations) | [List bulk-versioned properties](https://papi-akamai.readme.io/reference/bulkproperty-version-creationsbulkcreateid#get_bulk-property-version-creations-bulkcreateid) | [BulkVersion](#bulkversion) |
| [Bulk patch a set of properties](https://papi-akamai.readme.io/reference/bulkrules-patch-requests#post_bulk-rules-patch-requests)  | [List bulk-patched properties](https://papi-akamai.readme.io/reference/bulkrules-patch-requestsbulkpatchid#get_bulk-rules-patch-requests-bulkpatchid) | [BulkPatch](#bulkpatch) |
| [Bulk activate a set of properties](https://papi-akamai.readme.io/reference/bulkactivations#post_bulk-activations) | [List bulk-activated properties](https://papi-akamai.readme.io/reference/bulkactivationsbulkactivationid#get_bulk-activations-bulkactivationid) | [BulkActivation](#bulkactivation) |

As an alternative to get the initial set of bulk search results directly, but with likely delays, use this additional operation:

- [Synchronously bulk search a set of properties](#postbulksearchessynchronus)