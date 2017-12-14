Development Notes
==================

The pages are published using the Read The Docs online service.

Any changed pushed to master is automatically published online.

There is a Makefile to help running a few local tasks.

To initiate the dev environment::

    make env

To generate the page on your local system::

    make generate


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
