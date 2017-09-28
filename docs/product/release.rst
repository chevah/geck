Release process
###############

..  contents::


General
=======

This page describes the release process and steps to be followed during
development to simplify the release of a final product or a library.

Releasing a product usually consists of publishing the following:

* Binary or source archives.
* Documentation, which includes Release Notes, Known Issues and Upgrade Steps.
* Public announcement.
  Website news/blog article and newsletter.

Each version sent to a customer should have a unique version number
and must be mentioned in the release notes.

Sometimes, special features are required by clients with custom needs
and the functionalities are not to be included in the main release
series.
The versions with dedicated features should be released from
their own branches, which are not to be removed.
Each release from these branches should have an associated tag.
All the related custom bits in the release notes are to be imported into the release notes
from the main branch though.

TODO: see what to do with customers using releases from staging... maybe
make a production release without a full QA review.
Such a release can have a normal version... and if changes are made
during the QA review a new patch version is released.


Release Planning
================

Tickets marked for the 'next-release' milestone are technically to be
covered for the next release but in most situations these will fall beyond
the next release.
Tickets that must be in the 'next-release' are set with priority 'High'.

The general timeframe between each release is 30 to 45 days.
However, defects are worked on and released as soon as it is feasible by the
development team.


Release Review Process
======================

As a means to allow all team members that are involved in
coding, testing and supporting the product to keep up with the changes,
they must be part of the reviewers of the release branch/PR.

Being part of the release review will help you to acknowledge the changes and to
confirm that you have accepted the changes.

The release review request should also include the text used to announce the
new release on the website.


Release Manager
===============

During the time of an 'in-work' release, a single person is in charge of
driving the release, and that person will be the **release manager**.

Some functions of the **release manager** are:

* Defining the milestone description and due date
* About 1 week before the release, creating a release milestone and moving all
  closed tickets from the 'next-release' milestone to the new release milestone.
* Creating a dedicated ticket for the release itself, and associating it
  to the new release milestone.
* Making sure the ticket dedicated to the release has an owner, and that the
  owner will do the required steps.
* Organizing: Some tickets from the `next-release` milestone which are not yet 
  closed but are soon to be (like needs_merge) can also be moved to the new
  release milestone.
* Checking post-commit BuildBot results for the master branch (about once per week) 
  to make sure no regressions were introduced on the tests executed post-merge.
* Creating high priority tickets in case the tests are failing on master.
* Coordinating story tickets for the milestone.
* After sending the release branch to RQM, check that the Downloads page is updated.
* Check that a tag is created for the release, and that the tag points to the release branch and   not the release merge.
* Check that RQM has closed the release PR and associated Trac.
* After the Downloads page is updated, ensure that the release branch is merged
  with the master branch.
* Sends the newsletter to the relevant list/s.

Release Manager should look into obtaining access to the following:

* Write access to production website (from infrastructure team) to
  the news release to the website.
* Ability to stage a release branch to staging server then to production
  server.
* Access to Mailchimp to send the release newsletter.
* Access to the Support helpdesk or emails to know which customers should be
  contacted directly if the release is awaiting upon them.

When the release is out, the Release Manager organizes the team release
meeting (times and dates), initiates the call and holds the meeting including
a distributed agenda.
Release meeting notes are `located here <https://drive.google.com/drive/u/3/folders/0BwQo7116Iy2tZ2M2bDhadFV4R0E>`_


The Release Branch
==================

A release branch starts like any other branch by creating a ticket in Trac.

The release branch should be created from master (for latest release) or
from a tag (for a maintenance release).

To integrate with our automated process, the release branch should be named:
`TICKET_ID-release-MAJOR.MINOR.BUGFIX`.

For the latest release, the release branch should only update the release notes
and increment the version.

For a maintenance release, besides incrementing the release and creating the
release notes, the branch should also cherry pick the fixes or apply dedicated
fixes.

The review request for a release branch should include the text used by news
articles for our website.

Before requesting the review for this branch, the release should be done on
the staging server using the normal RQM command.

These are the extra review steps for a release branch:

* Release the product on the staging/testing server.
* Check that story tickets are solved/closed.
* Check that release notes are valid and with the correct date.
* Check that version constants were updated
* Check that known issues are up to date and issues fixed in this release are
  removed.
* Check the list of supported operating system (DISTRIBUTABLES in pavement.py)
  is valid.
* Check the download page to see that we have files for all the supported OSs.
* [Linux] From the distributable archives, check that the service can be initialized
  and started using a Unix init script.
* [Windows] From the distributable archives, check that the service can be installed
  and started.

The release itself is done using the automated RQM (Release Queue Manager)
process which for now is implemented on top of BuildBot.

Check the repo's README file for info on how to do the actual release
in staging and in production.

These are the extra steps for checking a release in production:

* Check that the tag was automatically created for the latest release.
* For maintenance releases, manually create a tag based on the release branch
  and push the tag.
* Close the milestone for the current release and re-target all tickets which are
  not closed yet to `next-release`.
* When releasing a **<maintenance>** release, a new ticket should be created on
  "next-release" to update release notes.

Future improvements for the automated release process:

* Add a news article to our website
* Trigger a website crawler to check broken links for download pages and
  documentation.


Release Notes
=============

Release notes explain what changed with this version. **Period**.
Release notes are **not** installation, upgrade or configuration.

Each time a branch fixes a bug, adds a new feature or makes any changes
which are visible to end users, a new entry is added inside the release notes
file. A release note entry is a summary for one change.

We keep release notes for all versions in a single file so that users can
easily read all changes starting from their version up to latest, or up to
a specific version.

Release notes are grouped in one of the following categories.
The category may be omitted if no changes were added for it. 
Here are some categories::

* Major changes (only for major releases)
* New features
* Bug fixes with internal bug ID (this is the only section for defect releases)
* Deprecation and Removals
* Documentation changes
* Other changes
* Security related issues (to be highlighted or tagged for easy filtering)

A marker/tag is added at the end of the sentence to point to the ticket ID
associated with this change.
Having a ticket ID marker is not mandatory for new features.

It can be followed by a list of tags to help users understand / filter the
scope of the change. 
Here are some examples::

* ``[https]`` - for changes affecting only a sub-system.
* ``[aix]`` - for changes affecting only AIX systems.
* ``[windows]`` - for changes affecting only Windows systems.

Remember your audience/user/clients and write for that audience.

Don't explain every detail of the change. When more details are required
use a link to the documentation.

All entries should be complete sentences or phrases, ending with a
punctuation mark.

Use present tense as opposed to past tense.
The text should state what the change **does** and not what it **did**.
eg. "Product no longer falls over X." as opposed to "Product fell over X.".

Write text in **resolution** form and describe what impact the change will have
on users.
What will the users notice?

If a single sentence isn't clear enough to understand, explaining the
background of the change can be helpful, by adding in
`Previously, X used to do Y` or `Previously, X used to do Y.
Now it does Z`.

Don't add low-level internal details about product logic.
Focus on how the change affects / is perceived by the user.

Here are some examples:

* Support was added for doing / integrating with X.
* Users can now do X.
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
    * SFTP protocol now supports reading and creating symbolic links on
      Windows. [sftp][windows]


    Defect fixes
    ^^^^^^^^^^^^

    * Fixed an internal server error when SSH client requests
      to execute a command, a shell or a pseudo-terminal. [#176][sftp][scp]


    Deprecations and removals
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    * It is no longer possible to do X. [#1359][unix]
    * Windows XP is no longer supported. [#2345]
    * Configuration option X, deprecated since Product version 12.1.2, is now
      removed. [#1366]


    Other changes
    ^^^^^^^^^^^^^

    * The HowTo document page of X now has documentation about doing Y. [#2452]



    Version 2.0.0, released 20/02/2014
    ----------------------------------


    Major changes
    ^^^^^^^^^^^^^

    * All log handlers were converted to event handlers.
      This allows a unified method for interacting the the audit events
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

    * Fixed an internal server error when SSH client requests
      were used to execute a command, a shell, or a pseudo-terminal. [#176][sftp][scp]


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

    * Fixed an internal server error which occurred when an FTP client requested
      an unknown command. [#160][ftp][ftps]


Version Management
==================

Chevah release versions are based on the MAJOR.MINOR.PATCH[.SpecialNN] scheme
documented at `Semantic Versioning <http://semver.org/>`_.

A **MAJOR** version is released to introduce new major features, remove
functionalities which have become obsolete, or add features not
compatible with previous versions.

**MINOR** versions are released based on a rolling update development model at
intervals varying between 30 to 60 days.
The goal is to have functionalities and defect fixes available to customers as
soon as possible.
Each release has a certain overhead, and the overhead should be minimized by
automating the release process.

**PATCH** versions are released as soon as a defect is fixed,
usually one week after it has been initially discovered and reported.
Security issues have top priority and a fix is released as soon as possible.
**PATCH** version doesn't include any new functionality and changes are focused
only on fixing the targeted bugs.

**SpecialNNN** is our non-standard version marker.
These versions are not targeted for general availability or for every customer.
The special version should be a word or keyword followed by an integer acting as a counter.

In an ideal world a release should be done by preparing a release
branch.
Then, by issuing a single command, the documentation, download and news pages would be updated.
Users would be automatically notified about the new release.


Compatibility Policy
====================

Any release from a **MAJOR** version release series should be backward and
forward compatible with any other release from the same **MAJOR** series.

That is, users should be able to upgrade or downgrade to any minor release
without having to change any external system interaction, API interaction or
configuration option.

A **MINOR** version release might introduce various functionalities which are
not available in previous versions.
Downgrading to a previous **MINOR** version will not make the newest functionalities available, but
configuration options or other setup specific to newer functionalities
should just be ignored in previous **MINOR** versions, without requiring
any other changes.

**MAJOR** releases are designed to allow major cleanups or redesigns which 
would break backward compatibility with previous versions.

**MAJOR** releases should be made at intervals greater than 2 years.

**MAJOR** releases should support being able to run them in parallel on the same system.
This is done to simplify testing, moving the new version in production, or reverting 
the old version in production in case of problems.

Two **MAJOR** versions can sometimes not be using the same resource at the same time,
e.g. same TCP port, but they should allow fast configuration changes to
release a shared resource and to allow use a shared resource.

The upgrading to a new **MAJOR** version should be designed to require the
minimum effort and the process should be automated as much as possible.
For example, the straightforward configuration can be automatically migrated.

Some changes might not be automatically migrated and may require user interaction.
To simplify the migration process, these changes should be made in **MINOR**
versions as preparation for removals, which will be done in the next **MAJOR**
release.
These changes are done by keeping the functionality from the current **MAJOR**
release, but a warning is emitted to inform users about the future changes.
User should be pointed to a documentation page describing the changes and
providing information on how to prepare the migration.

If the latest **MINOR** release from a **MAJOR** release series is operating in
production without any removal warnings, then users can upgrade to the next
**MAJOR** release without any other manual migration process.

All removal warnings should have a similar format to simplify filtering and
reporting them.
The removal message should describe how the value was changed and what steps
are required to update/upgrade the configuration to the new functionality.


Here are some steps you can use for testing the compatibility between
**MAJOR** releases.
While some functionalities might not be available, the product should still start.

* Install the new release and use the configuration from the previous major release
  to start the product.
  Check that no errors were reported and all services are properly configured
  and started.
* Install the previous major release, and use the configuration from the new
  release to start the product.
  Make sure that all services are properly configured and no errors are
  reported.


Releasing a forked library
==========================

Sometimes we might need to do small or major changes to an upstream
package/library.
For example, changes were rejected upstream, or not yet released upstream,
or just consist of minor re-packaging changes.

The forked versions should be published only on our private PyPy server and
all versions should use the `.chevahN` suffix.

When forking an upstream project, keep the master/trunk branch as upstream.
You can create separate branches dedicated to the Chevah project like
`master-chevah` or `release-1.2.3-chevah`.


Releasing a library
===================

A library is a collection of software which provides code shared by multiple products.
Libraries should always be released using the standard package management
system.

Releasing a library consists of the following:

* creating a distributable in a format used by the package manager.
* publishing the distributable to the package manager website.
  In our case most of the time it will be a Python package pushed to our
  internal PyPi server.

For libraries we aim at releasing a new version with each merge to master.
Once you get your branch approved, make sure it has a unique version in
setup.py, and then land the branch on master using PQM and release it using::

    python setup.py publish

Sometimes, you might want/need to release it before the branch is approved
and merged, as you might want to experience how it can be used. This is fine,
just make sure that each release has a unique version and it follows the
general versioning semantics.


Releasing a product
===================

A product is a stand-alone fully functional application that provides direct
functionality to end users.

For now, we will target doing a minor release every 60 days.

Bug fix releases are made on request.

A major release is supported for minimum of 2 years, but our customers are
expecting to have support for up to 10 years.

We are now aiming to extending the support / product life cycle to 5 years.

While working on a product, we have the following types of branches::

* master - one master branch with the latest stable development version
* release-branch - ephemeral branches where the version number is updated and release notes finalized.
* task-branch - multiple ephemeral branches where a new feature or fix has a task-branch

Each released version has a dedicated tag.
When you need to create a defect release or a maintenance release for a previous version, you will
create the release branch based on the desired tag.

The **master** branch should be kept in good shape so that we can release it at
any time.
Especially if a security defect is found, we will make a new release
as soon as the defect is fixed.

Releases may include fixes for defects observed by customers or new product
features requested by customers.
In this case it is customary to let a customer know directly that the release
is now available.
It should be noted to customers that they will still need to take the
necessary steps to test the new release in their own environments.
