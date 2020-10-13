---
title: "Bulk version a set of properties"
slug: "post_bulk-property-version-creations"
excerpt: "POST a [BulkVersion](#bulkversion) object to create new\nversions of a set of properties based on any previous version.\nThis operation launches an asynchronous process to increment\nversions. To check its progress,\nrun the [List bulk-versioned properties](#getbulkpropertyversion)\noperation, whose link is available in the `Location` header or\n`bulkCreateVersionLink` member of this operation's response.\nRun this operation only after\n[bulk searching](#postbulksearches) a set of properties you want\nto change, to prepare new versions to bulk patch. See\n[Bulk Search and Update](#bulksearchandupdate)\nfor guidance on this feature."
hidden: false
createdAt: "2020-06-05T15:07:48.783Z"
updatedAt: "2020-06-05T15:07:48.783Z"
---
