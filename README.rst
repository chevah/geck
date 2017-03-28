Chevah Project Style Guide
==========================

This repository is the source for the Chevah Styleguide at
http://styleguide.chevah.com hosted via GitHub Pages.

Pelican is used for generating static pages. 

The markup used is reStructuredText.


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
the Styleguide is a good starting point.

Below are is a guide that you can follow to make changes to the Styleguide:

Make sure that SSH is set up and clone the repository:
``git clone git@github.com:chevah/styleguide.git``
The link can be found from the Github repo.

Navigate to the styleguide repo: ``cd styleguide``

Create a new branch and check out to that branch so that you are working on
your own branch and not the master branch:
``git checkout -b styleguide-improvements`` with
``styleguide-improvements`` as an example branch name.
If there is a Trac ticket involved, add the Trac ID like
``1234-styleguide-improvements``

If you are not sure what branch you are on: ``git status``

On that branch you can make changes to the files - either on Terminal
(using Vim or your preferred editor) or software (like Sublime Text).
Save those changes.

To show what files are not yet staged for the commit: ``git status``

Add the changed files: ``git add <filename>``

Then commit the files to the branch: ``git commit -m "Your description about
the commit here"``

You may need to do more than one commit.  
Follow the Development Notes above to run the Styleguide locally.

Once all changes are made, git push your changes out to your git branch
(not the Master branch) and create the first Pull Request. To create the pull
request, you can go to the branch’s page on github.com and click on the green
"Compare and Pull Request" button.
