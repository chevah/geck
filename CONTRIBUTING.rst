Development Notes
==================

The Pelican blog article template is used to generate simple pages.
This is done since we don't care about the blog part but don't want to create
'content/pages' folder in order to automatically generate all pages...
and also have 'pages/*' URLs.

Run ``paver deps`` then ``paver run`` to build the project locally on
``http://localhost:8080``

Continuously update content with ``paver dev``.

Publish changes from current branch with ``paver publish``.


Onboarding Notes
================

If you are currently onboarding with the Chevah Project, making improvements to
the GECK is a good starting point.

Below is a guide that you can follow to make changes to this repo:

Create a new branch and check out to that branch so that you are working on
your own branch and not the master branch.

``git checkout -b styleguide-improvements`` with
``styleguide-improvements`` as an example branch name.

If there is a Trac ticket/ GitHub issue involved, add the ID at the
beginning of the branch name::

    1234-styleguide-improvements

Once all changes are made, git push your changes out to your git branch
(not the `master` branch) and create the first Pull Request.
