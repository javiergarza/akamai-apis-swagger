---
title: "Caching"
slug: "caching"
type: "fixed"
createdAt: "2020-06-05T18:42:57.332Z"
hidden: false
---
This release contains a fix for a situation when a property specifies the Caching behavior in multiple rules. When one rule has the Caching behavior configured with Caching Option Honor Origin Cache-Control or Honor Origin Cache-Control and Expires, and Honor Private is set to Yes, and a second rule has the Caching behavior configured with the Caching Option Cache and a defined Max-age time configured for the same object, the following issues could occur:

- The content at the Tier Distribution parent is never revalidated with the origin, and so remains stale, also known as an infinite cache.

- Cacheable content at the Edge is treated as no-store.