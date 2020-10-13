---
title: "Various SIERRA tests"
slug: "random-tests"
hidden: false
createdAt: "2020-06-05T21:57:30.509Z"
updatedAt: "2020-06-05T22:20:05.673Z"
---
[block:api-header]
{
  "title": "Headers"
}
[/block]
Headings within each page appear in TOC in right panel
[block:api-header]
{
  "title": "Variables"
}
[/block]

- Invoke a variable named `api_name` and render as <<api_name>> . 

- Invoke  a variable named `portal_name` and render as <<portal_name>>. 

- Invoke a variable named `portal_name_initial` and render as <<portal_name_initial>>. 

- Invoke a nonexistent variable named `fubar` and render silently as <<fubar>>.

- Sample sentence, featuring two variables wrapped with in-line markdown formatting. (Can't embed any formatting.) To enable this API, choose the API service named __<<service_name>>__  and set the access level to __<<service_level>>__.
[block:api-header]
{
  "title": "Glossary"
}
[/block]

- Test of a glossary item named <<glossary:group>> whose description is visible on hover over the term. 

- Test of a glossary item named <<glossary:account>> whose description is visible on hover over the term. 

- Test of a nonexistent glossary item named `fubar` <<glossary:fubar>> that simply does not render. 

Note: no click-thru "learn more" links from within glossary description.

Type `<<` in markdown editor for pop-up to insert variables & glossary items.
[block:api-header]
{
  "title": "Links"
}
[/block]

- See [ID prefixes](doc:id-prefixes).

- See [Nonexistent link](doc-missing-link)

- This tests a link to a section called [Initial setup](doc:set-up-api-token)  whose URL stub later gets renamed. Does README resolve the pointers? No, it doesn't. So guys, don't rename page slugs after drawing links to them.

- See the sample sequence link at the bottom of this page. These links are hard-coded using a special widget built into the markdown editor.

[block:api-header]
{
  "title": "Video"
}
[/block]
Here's a YouTube video of the greatest blues guitar player ever:
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F8k54r_ANt8o%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D8k54r_ANt8o&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F8k54r_ANt8o%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"640\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=8k54r_ANt8o",
  "title": "Buddy Guy in 1969 with Jack Bruce and Buddy Miles",
  "favicon": "https://www.youtube.com/s/desktop/8ace1dc9/htdocs-ytimg-desktop-kevlar-production/img/favicon.ico",
  "image": "https://i.ytimg.com/vi/8k54r_ANt8o/hqdefault.jpg"
}
[/block]

[block:api-header]
{
  "title": "Non-markdown (widget) table"
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "All work",
    "0-1": "No play",
    "0-2": "Makes Jack",
    "0-3": "a dull boy",
    "1-0": "All work and no play makes Jack a dull boy.",
    "1-1": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.",
    "1-2": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.  All work and no play makes Jack a dull boy.",
    "1-3": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.",
    "2-0": "All work and no play makes Jack a dull boy.",
    "2-1": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.",
    "2-2": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.  All work and no play makes Jack a dull boy.",
    "2-3": "All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy."
  },
  "cols": 4,
  "rows": 3
}
[/block]