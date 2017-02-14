Documentation
#############

:menu_order: 101

.. contents::


General
=======

**What is documented?**

* Packages, modules, classes and functions using docstrings.

* User interfaces that need further explanation and / or guidance.

* Guides aimed at general audiences that require more in-depth detail than
marketing / promotion materials.

* Questions and issues that have risen to Support and Sales that can instead be
linked to in public.

* Release notes that explains the changes tied to a specific version.

* Further notes that will help administrators in securing their file transfer
process while using SFTPPlus.


Narrative documentation
=======================

There are two main types of documentation - technical documentation and the
User's Guides section.

Documentation changes are linked to a certain version of SFTPPlus. 

When documentation changes are made, these are anchored to a specific release
version.

For narrative documentation use 
`semantic newlines <http://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_.

Make lines short, and break lines at natural places, such as after commas and
semicolons, rather than after the Nth column.

..  code-block:: text
    :linenos:

    When editing a narrative documentation file, I wrap the lines semantically.
    Instead of inserting a newline at 70 columns (or whatever),
    or making paragraphs one long line,
    I put in newlines at a point that seems logical to me.
    Modern code-oriented text editors are very good at wrapping and arranging
    long lines.


Technical Documentation
-----------------------

The primary audience are the administrators actively using the software either
as an existing customer or on the software trial.

The secondary audience are those involved in the decision-making and
implementation of the software.  

Both types of audiences will have some form of technical background.

The documentation is constantly being developed as updates to the product are
made, or when an issue is found which needs further guidance.


User's Guides
-------------

Pages in the User's Guides are used to describe how a task can be performed by
applying various configuration options.

It is also used for other frequent questions sent to Support / Sales. 

User guides are targeted to the more general audience - pre- and post-sales.

If the page has a very specific audience in mind, it is stated in the page's intro.


Markup
======

The documentation is delivered in the .rst format.  


Adnotation classes
------------------

The following adnotation classes are available:

- seealso - green
- tip - green
- note - blue
- danger - strong red
- warning - red
- attention - yellow

Example:

.. sourcecode:: rst

.. attention::
This option is in the `experimental` stage.


Header formats
--------------

- heading 1 -> #
- heading 2 -> =
- heading 3 -> -
- heading 4 -> ^


Embedding Images
----------------

Ensure screenshots are legible, take up the screen width and any commands are
correct.

If screenshots are outdated, update them.

.. sourcecode:: rst

.. image:: /_static/guides/image.png


Internal linking
----------------

Use  `` :doc:`link to Local Manager</operation/local-manager>` `` when linking
to internal documentation pages.

Use `` :ref:`section in this page <internal-page-link>` `` when linking to
internal sections within a documentation page.  The internal section should
have the link name above it in the form of `` ._internal-page-link: ``


Breaking up long logs
---------------------

Add | to break up a long log line such as below:

.. sourcecode:: rst

    | 20182 2017-01-30 11:56:41 Process user 127.0.0.1:50568 Account "jan"
      logged in.


Describing a configuration option
---------------------------------

Example:

.. sourcecode:: rst

:Default value: 'DEFAULT-EXAMPLE'
:Optional: No/Yes
:From version: VERSION_HERE
:Values: * The values section should only list the type of values supported
         * Examples include Path, Disabled, Inherit, Path+${USER}
:Description:
    The description should further describe the configuration options for the
    user and what is expected.


Adding configuration and log examples
-------------------------------------

Examples of configuration or logs in the documentation should be edited to be
more of a real world example. 

For example, instead of 'user', add a real name such as 'alice' or 'bob'.

Example:

.. sourcecode:: rst

    [accounts/mark-uuid]
    name = mark
    enabled = Yes
    type = application
    group = Staff
    description = Staff SFTPPlus application account for Mark
    home_folder_path = /PATH/TO/MARK/HOME
    password = PASSWORD

Tables
------

Table 1 with alignment:

.. sourcecode:: rst

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

.. sourcecode:: rst

Table 2 with typography elements:

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3


Updating the documentation
--------------------------

The release process will be similar to the rest of the software.

An empty ``.ignore`` with the internal ID can be added in the release notes.

Further details about generating and building documentation is found in the
chevah server repository.

When creating a new page, ensure to add the page name in the index.rst.


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

Release notes are grouped in one of the following categories. The category
may be omitted if no changes were added for it. 
Here are some categories::

* Major changes (only for major releases)
* New features
* Bug fixes with internal bug ID (this is the only section for bugfix releases)
* Deprecation and Removals
* Documentation changes
* Other changes
* Security related issues (to be highlighted or tagged for easy filtering)

A marker/tag is added at the end of the sentence to point to the ticket ID
associated with this change. Having a ticket ID marker is not mandatory for
new features.

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

Use present tense as opposed to past tense. The text should state what the
change **does** and not what it **did**.
eg. "Product no longer falls over X." as opposed to "Product fell over X.".

Write text in **resolution** form and describe what impact the change will have
on users. What will the users notice?

If a single sentence isn't clear enough to understand, explaining the
background of the change can be helpful, by adding in
`Previously, X used to do Y` or `Previously, X used to do Y. Now it does Z`.

Don't add low-level internal details about product logic. Focus on how
the change affects / is perceived by the user.

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



Known Issues
============

This section lists known issues for the current release of SFTPPlus along with
a reference to the internal ID.

A workaround can be added in this section along with the known issue statement
and ID.

If there is further information of a fix, include info as to when.

The style is similar to what is expected of the release notes.


Docstrings
==========

* Well documented code is extremely important.
  Take time to describe components, how they work, their limitations, and the
  way they are constructed.
  Don't leave others in the team guessing what is the purpose of uncommon or
  non-obvious code.

* Document code as part of docstrings and not as comments.

.. sourcecode:: python

    def iamanExample(doc):
        """
        A simple docstring is placed here.
        """
          config = self.createSomethingHere('')

There are two types of docstrings for production and test code.


Test code docstrings
--------------------

Test code docstrings can contain information during the review process of new
tests that can be written.

Test code docstring example:

.. sourcecode:: python

    class TestHelpers(IAmATestCase):
        """
        The docstring here may add tests for helpers for a certain module
        """
        def test_of_a_module_1(self):

         """
         What is expected to happen in the first module of this test case
         """
        ... 
        ...
        def test_of_a_module_2(self):
         """
         What is expected to happen in the first module of this second case
         """
        ...
        ...


Production code docstrings
-------------------------

If a docstring is not added in production code, readers and reviewers are
unable to tell what is it.  For example:

.. sourcecode:: python

    def getSomethingNewHere(self):
    ...
    ...

Whereas a docstring should be added to add further information:

.. sourcecode:: python

    def getSomethingNewHere(self):
        """
        A docstring describing what SomethingNewHere is about
        """
    ...
    ...


Marketing / Promotional Materials
=================================

Promotions and marketing materials are located in the main website.

It should be as generic and non-technical as possible with links to the
Documentation for more in-depth / technical information.

Please go to the internal wiki under General > Marketing for internal marketing
details and links to image files.


Announcing a new release to the email list
------------------------------------------

After the website is updated and News item published, we send a newsletter:

1. Go to Campaigns in Mailchimp.

2. Select 'Replicate' in the drop down besides 'NEW: SFTPPlus Release Announcement'.
If it is a security bugfix, use the SFTPPlus Security Advisories email list.

3. Select the News Announcements email list.

4. Update the email subject and email with the News text used to announce the
new release. You can use the copy that is in the News article for the email.

5. Select Send. Before sending the final email, you can preview first by going
to 'Preview and Send' on the top menu and select 'Send a test email'.

