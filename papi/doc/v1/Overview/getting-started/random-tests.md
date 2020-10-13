---
title: "Various tests"
slug: "random-tests"
hidden: false
createdAt: "2020-06-05T21:57:30.509Z"
updatedAt: "2020-06-15T22:43:27.871Z"
---
[block:api-header]
{
  "title": "Headings. Widgets interpreted as B-heads"
}
[/block]

- Headings within each page appear in a TOC in the right panel.

- Heading widgets are interpreted as B-heads.

- Invalid structure (initial B-heads prior to A-heads) does not render in right panel.

- Heading widgets are unnecessary, as standard markdown headings render fine.

- Only A- and B-heads render in the TOC. Any subsequent heading levels appear in text, with no navigation. That's fine with me. Shouldn't be going any deeper than that.

- No apparent way to define custom heading slugs. (Tried both `[...]` and `{:...}` markdown dialects below.)

- You can only use standard `#anchor` syntax to link headings within a page. No way to use `doc:` links. The IDs generate dynamically from heading content, with no mechanism to define a fixed slug. so the links are fragile. E.g., this next heading is linkable at `#section-a-head-customanchor-1`. The link will break when I change the heading's text.

# A-head [customanchor1]

This is a top-level heading.

## B-head {:customanchor2}

This is a secondary  heading.

### C-head

This is a tertiary heading.

#### D-head

How low can we go?
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
- [List custom behaviors](ref:get_custom-behaviors)

- See [ID prefixes](doc:id-prefixes).

- See [Nonexistent link](doc-missing-link)

- See the sample sequence link at the bottom of this page. These links are hard-coded using a special widget built into the markdown editor.

## Images

Portrait:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/20aac1e-1782368_10152760792037183_8025065937628498791_o.jpg",
        "1782368_10152760792037183_8025065937628498791_o.jpg",
        1152,
        2048,
        "#928d8c"
      ]
    }
  ]
}
[/block]
Landscape, large:


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1b298d8-_large.png",
        "_large.png",
        2739,
        1381,
        "#d0d6dc"
      ]
    }
  ]
}
[/block]
Smaller image:


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed88f6a-_small.png",
        "_small.png",
        550,
        359,
        "#c0dbee"
      ],
      "caption": "How to resize?"
    }
  ]
}
[/block]

![with caption](https://developer.akamai.com/api/core_features/test_center/img/workflow_diagram.png)

![](https://developer.akamai.com/api/core_features/test_center/img/workflow_diagram.png)

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
    "1-2": "Only inline markdown content interprets within table cells. These bullets are hand-coded:\n• All work \n• and no play \n• makes _Jack_ \n• a **dull** boy. \n• All work and no play makes Jack a dull boy..",
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
## Do in-page links work?

Here are attempts to link to:

- a [heading within a page](doc:section-a-head-customanchor-1) using `doc:` prefix syntax.

- a [heading within a page](#section-a-head-customanchor-1) using standard `#` anchor syntax.
