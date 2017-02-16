Release process
###############

:menu_order: 101

..  contents::


General
=======

This page describes the release process and steps to be followed during
development to simplify the release of a final product or a library.

Releasing a product usually consists of publishing the following:

* Binary or source archives.
* Documentation, which includes Release Notes, Known Issues and Upgrade Steps.
* Public announcement. Website news/blog article and newsletter.

Each version sent to a customer should have a unique version number
and must be mentioned in the release notes.

Sometimes, special features are required by clients with custom needs
and the functionalities are not to be included in the main release
series. The versions with dedicated features should be released from
their own branches, which are not to be removed. Each release from
these branches should have an associated tag. All the related custom
bits in the release notes are to be imported into the release notes
from the main branch though.

TODO: see what to do with customers using releases from staging... maybe
make a production release without a full Q&A review.
Such a release can have a normal version... and if changes are made
during the Q&A review a new patch version is released.


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

* Create a release notification list and send an email to everyone who cares
  about new releases. The email should include a changelog for the latest version.
  Trac ticket #525.
* Add a news article to our website
* Trigger a website crawler to check broken links for download pages and
  documentation.


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

**SpecialNNN** is our non-standard version marker. These versions are not targeted
for general availability or for every customer. The special version should be a word
or keyword followed by an integer acting as a counter.

In an ideal world a release should be done by preparing a release
branch. Then, by issuing a single command, the documentation, download
and news pages would be updated. Users would be automatically notified
about the new release.


Compatibility Policy
====================

Any release from a **MAJOR** version release series should be backward and
forward compatible with any other release from the same **MAJOR** series.

That is, users should be able to upgrade or downgrade to any minor release
without having to change any external system interaction, API interaction or
configuration option.

A **MINOR** version release might introduce various functionalities which are
not available in previous versions. Downgrading to a previous **MINOR**
version will not make the newest functionalities available, but
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

Here are some steps you can use for testing the compatibility between
**MAJOR** releases. While some functionalities might not be available, the
product should still start.

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

Each released version has a dedicated tag. When you need to create a
bugfix release or a maintenance release for a previous version, you will
create the release branch based on the desired tag.

The **master** branch should be kept in good shape so that we can release it at
any time.
Especially if a security bugfix is found, we will make a new release as soon
as the bug is fixed.

