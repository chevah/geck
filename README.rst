Chevah Project Coding Style Guide
=================================

This is the source for http://styleguide.chevah.com hosted via GitHub Pages.

Pelican is used for generating static pages. Blog article generation from

Pelican blog article template is hijacked to generate simple pages.
This is done since we don't care about blog part but don't want to create
'content/pages' folder in order to automatically generate all pages...
and also have 'pages/*' URLs.

See the changes using `paver run`.

Continuously update content with `paver dev`.

Publish changes from current branch with `paver publish`.
