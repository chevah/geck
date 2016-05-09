Release process
###############

:menu_order: 101

..  contents::


General
=======

This page describes the release process and steps to be followed during
development to simplify the release or a final product or library.


Releasing a product usually consists of publishing the following:

* Binary or source archives.
* Documentation, which includes Release Notes, Known Issues and Upgrade Steps.
* Public announcement. Notification email or website news/blog article.


Release Review Process
======================

As a means to allow all team members that are involved in
coding, testing and supporting the product to keep up with the changes,
they must be part of the reviewers of the release branch/PR.

Being part of the release review will help to ackwnoledge the changes and to
confirm that you've okayed the changes.

The release review request should also include the text used to announce the
new release on the website.


Release Notes
=============

Release notes explain what changed with this version. **Period**.
Release notes are **not** installation, upgrade or configuration.

Each time a branch fixes a bug, adds a new feature or makes any changes
which are visible to end users a new entry is added inside the release notes
file. A release note entry is a summary for one change.

We keep release notes for all versions in a single file so that users can
easily read all changes starting from their version up to latest or a
specific version.

Release notes are grouped in one of the following categories. The category
may be omitted if no changes were added for it. Here are some categories::

* Major changes (only for major releases)
* New features
* Bug fixes (this will be the only section for bugfix releases)
* Deprecation and Removals
* Other changes. Documentation changes.

A marker/tag is added at the end of the sentence to point the ticket ID
associated with this change. Ticket ID marker is not mandatory for new features.

It can be followed by a list of tags to help users understand / filter the
scope of the change. Here are some examples::

* ``[https]`` - for changes affecting only a sub-system.
* ``[aix]`` - for changes affecting only AIX systems.
* ``[windows]`` - for changes affection only Windows system.

Remember your audience/user/clients and write for that audience.

Don't explain all details of the change. When more details are required
use a link to documentation.

All entries should be complete sentences or phrases, ending with a
punctuation mark.

Use present tense as opposed to past tense. The text should state what the
change **does** and not what it **did**.
"Product no longer falls over X." as opposed to "Product fell over X.".

Write text in **resolution** form, describe what impact the change will have
on users. What will the users notice?

If a single sentence isn't clear enough to understand, explaining the
background of the change can be helpful, by adding in
`Previously, X used to do Y.` or `Previously, X used to do Y. Now Z.`.

Don't add low-level, internal details about product logic. Focus on how
the change affects / is perceived by the user.

Here are some examples:

* Support was added for doing / integrating with X.
* Users now can do X.
* It is no longer possible to do Y.
* The text on the ABC form is now Z.
* Reworded text from X to be gender neutral.
* Doing X on a session in state Y no longer gives the XYZ error.
* Fix the XZY error generated when client was doing X on a session in Y state.
* Previously, users were unable to upload files to a folder if they
  had write permissions.


Sample release notes
--------------------

::

    Release Notes
    =============

    This is the list of all changes for PRODUCT NAME releases.


    Version 2.1.0, released 24/02/2014
    ----------------------------------


    New features
    ^^^^^^^^^^^^

    * Support was added to transfer files using SCP over SSH.
      Read more... [scp]
    * SFTP protocol now support reading and creating symbolic links on
      Windows. [sftp][windows]


    Defect fixes
    ^^^^^^^^^^^^

    * Fix an internal server error when SSH client requests
      to execute a command, a shell or a pseudo-terminal. [#176][sftp][scp]


    Deprecations and removals
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    * It is no longer possible to do X. [#1359][unix]
    * Windows XP is no longer supported. [#2345]
    * Configuration option X, deprecated since Product version 12.1.2, is now
      removed. [#1366]


    Other changes
    ^^^^^^^^^^^^^

    * The howto document page of X now has documentation about doing Y. [#2452]



    Version 2.0.0, released 20/02/2014
    ----------------------------------


    Major changes
    ^^^^^^^^^^^^^

    * All log handlers were converted to event handlers.
      This allows an unified method for interacting the the audit events
      produced by SFTPPlus.
    * All authentication methods are now explicitly defined and ordered.
      You can now choose the order in which different authentication methods
      are used.


    New features
    ^^^^^^^^^^^^

    * Support was added to transfer files using SCP over SSH.
      Read more... [scp]


    Defect fixes
    ^^^^^^^^^^^^

    * Fix an internal server error when SSH client requests
      to execute a command, a shell or a pseudo-terminal. [#176][sftp][scp]


    Deprecations and removals
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    * It is no longer possible to do X. [#1359][unix]
    * Windows XP is no longer supported. [#2345]
    * Configuration option X, deprecated since Product version 12.1.2, is now
      removed. [#1366]


    Version 1.1.1, released 14/02/2013
    ----------------------------------


    Defect fixes
    ^^^^^^^^^^^^

    * Fix an internal server error when FTP client requests
      an unknown command. [#160][ftp][ftps]

