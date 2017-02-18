Chevah Project Style Guide
==========================

This repository is the source for the Chevah Styleguide at
http://styleguide.chevah.com hosted via GitHub Pages.

Pelican is used for generating static pages. 

The markup used is reStructuredText.

The Pelican blog article template is used to generate simple pages.
This is done since we don't care about the blog part but don't want to create
'content/pages' folder in order to automatically generate all pages...
and also have 'pages/*' URLs.

Run `paver deps` then `paver run` to build the project locally.

Continuously update content with `paver dev`.

Publish changes from current branch with `paver publish`.
