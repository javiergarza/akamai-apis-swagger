---
title: "requestMethod"
slug: "requestmethod"
hidden: false
createdAt: "2020-06-15T22:26:18.418Z"
updatedAt: "2020-06-15T22:26:18.418Z"
---
__Property Manager name__: [Request Method](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Specify the request's HTTP verb. Also supports WebDAV methods and common Akamai operations.

__Options__:

- `matchOperator` (_enum string_): Matches the `value` when set to `IS`, otherwise `IS_NOT` reverses the match.

- `value` (_enum string_): Any of the following HTTP methods:

    - `CONNECT`
    - `COPY`
    - `GET`
    - `HEAD`
    - `HTTP_DELETE` (note the additional prefix)
    - `OPTIONS`
    - `POST`
    - `PUT`
    - `TRACE`

    May also specify the following WebDAV methods:

    - `DAV_ACL`
    - `DAV_CHECKOUT`
    - `DAV_COPY`
    - `DAV_DMCREATE`
    - `DAV_DMINDEX`
    - `DAV_DMMKPATHS`
    - `DAV_DMMKPATH`
    - `DAV_DMOVERLAY`
    - `DAV_DMPATCHPATHS`
    - `DAV_LOCK`
    - `DAV_MERGE`
    - `DAV_MKACTIVITY`
    - `DAV_MKCALENDAR`
    - `DAV_MKCOL`
    - `DAV_MOVE`
    - `DAV_PROPFIND`
    - `DAV_PROPPATCH`
    - `DAV_REPORT`
    - `DAV_SETPROCESS`
    - `DAV_SETREDIRECT`
    - `DAV_TRUTHGET`
    - `DAV_UNLOCK`

    May also specify the following Akamai operations:

    - `AKAMAI_PURGE`
    - `AKAMAI_TRANSLATE`
