Documentation
#############

:menu_order: 007

.. contents::


Introduction
============

We have the following types of documentation:

1. Code documentation
2. Low level technical information
3. Narrative documentation including User's Guides
4. Marketing and promotional materials


Narrative documentation
=======================

Overview
--------

Readers are mainly:

* Administrators directly involved with SFTPlus. 
  They can be in three stages - pre-sales, on trial, or existing customers.

* Decision-makers involved in the implementation of the software. 
  They can include the business and technical arm of the organization.

* Chevah development team to check the specifications of a functionality.

* Chevah support team to direct support queries to parts of the documentation.

Readers will have varying form of technical backgrounds and familiarity with
the software and its features and functionalities.

If there is a customer needing help with the setup, like securing their setup,
ask what they are trying to do to see if the documentation can be improved.


Semantic Linefeeds
------------------

For narrative documentation use 
`semantic linefeeds <http://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_.

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


About the Documentation Sections
================================

**Introduction**

High level introduction to the software.


**Installation and Upgrade Instructions**

System requirements, installation, installation validation/procedures, upgrade
procedures, uninstallation instructions.


**Getting Started with SFTPPlus**

Prerequisite to this page is the installation section.

Contains information about the initial, basic configurations that come with the
installation package and first account configurations.


**Configuration Instructions**

Should contain information to the general configuration principle and
references for each configuration option.

This section focuses only on the **individual configuration options**.

Samples and guides in this section should be aimed at the Local Manager GUI
and the text file configuration.

For example, the HTTP/HTTPS configuration page is only restricted to the
configuration options available for this service.


**Operation (under 'Usage Instructions')**

Should only contain general principles of operation.

The section can go into further detail about a particular feature or service
beyond the configuration file and configuration file options.

For example, the HTTP/HTTPS operations page goes into detail about what actions
are available with this service, examples of usage and more.


**User's Guides**

Pages in the User's Guides are used to describe how a task can be performed by
applying various configuration options.

This section is also used for other frequent questions sent to Support / Sales.

Can be written to the more general audience. 
It is a good idea to list out who the audience is.

Before adding to the Users Guide, check to make sure that the information is
better suited elsewhere - such as the Operations or Configuration sections.


Miscellaneous Topics
--------------------

These are pages that do not otherwise fall under the other main sections.


Using reStructuredText (rst)
============================

We use `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ as a documentation
generator that uses reStructuredText as its markup language, extending and
using Docutils for parsing.

Both Sphinx and Docutils were created in Python to document Python, but
documenting C and C++ is also supported.

Sphinx supports several output formats directly, such as HTML, LaTeX, and ePub,
and supports PDF output via either LaTeX or the external rst2pdf tool.

Due to the ability to output to several formats, keep in mind how the output
will look like. For example, raw HTML is discouraged as this will affect the
look of a PDF output.

For us, narrative documentation is delivered in the reStructuredText (.rst)
format.  

Further details are available in this
`Docutils documentation page <http://docutils.sourceforge.net/rst.html>`_. 

The following are some useful tips on the rst format.


Adnotation classes
------------------

The following adnotation classes are available:

- Seealso - green
- Tip - green
- Note - blue
- Danger - strong red
- Warning - red
- Attention - yellow

Examples of existing adnotation classes used in the documentation:

.. sourcecode:: rst

  ..  tip::
      On OS X you can use the `dscacheutil -q user` and `dscacheutil -q group`
      tools to identify the used IDs and pick a unique ID for the system.

.. sourcecode:: rst

  .. note::
      The `password` is ignored for accounts of `type = os`.

.. sourcecode:: rst

  ..  danger::
      This default admin account is provided for testing and debugging purpose.
      For production usage it is highly recommended to change the account
      name and password or to disable the account.

.. sourcecode:: rst

  ..  warning::
      Account credentials and account configuration are transferred using
      unsecured HTTP connections. Use this method only over private networks.

.. sourcecode:: rst

    .. attention::
    On Linux and Unix, this authentication method can only be used when the
    SFTPPlus service is started as `root`.


Header formats
--------------

- Heading 1 - #
- Heading 2 - =
- Heading 3 - -
- Heading 4 - ^


Embedding Screenshots and Images
--------------------------------

Ensure screenshots are updated, legible, take up the screen width and any
commands or settings are correct.

.. sourcecode:: rst

    .. image:: /_static/guides/image.png
        :alt: Description of the image
        :align: center


Internal and external linking
-----------------------------

When linking to internal documentation pages, use the :doc: tag:

.. sourcecode:: rst

    :doc:`link to Local Manager</operation/local-manager>` `` 

When linking to internal sections within a page, use the :ref: tag:

.. sourcecode:: rst

    :ref:`section in this page <internal-page-link>`

For the :ref: link, create an anchor to the section:

.. sourcecode:: rst

    ._internal-page-link:

When linking to external web links:

.. sourcecode:: rst

    `Bug Writing Guidelines <http://developer.mozilla.org/en/docs/Bug_writing_guidelines>`_

When linking to other resources, aim to make documentation be as cursive as
possible - meaning that users should not have to break mid-guide and search for
other information.


Breaking up long lines of logs
------------------------------

Add a pipe (|) to break up a long log line such as below:

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
        The description further describes the configuration options for the
        user and what is expected.


Adding configuration and log examples
-------------------------------------

Examples of configuration or logs in the documentation should be edited to be
more of a real world example. 

For example, instead of 'user', add a real name such as 'alice' or 'bob':

.. sourcecode:: rst

    [accounts/mark-uuid]
    name = mark
    enabled = Yes
    type = application
    group = Staff
    description = Staff SFTPPlus application account for Mark
    home_folder_path = /PATH/TO/MARK/HOME
    password = PASSWORD

Since many customers are using the text file configuration, it is a good idea
to include this along with steps in the Local Manager GUI.


Updating the documentation
==========================

Narrative documentation may be added for a number of reasons such as:

- The process to set up the software needs further explanation.
- A Support request is made since the documentation is not clear.
- A new feature has been released or modified.
- A customer has requested how x can be done, and this can be added to the
  documentation as it is related to the software.  
- A commonly asked sales request about the software and the documentation is
  added as the publicly-available answer.

**Tips when updating documentation:**

When creating a new page, add the page name in a doctree (ie index.rst).

See the towncrier repo for news fragments and the extensions to use.
Documentation changes is usually ``.ignore`` with the internal ID. 

Release notes are tied to a specific version so that changes are linked to a
version of SFTPPlus. 

Further details about generating and building documentation is found in the
chevah server repository.


Communicating command-line syntax
----------------------------------

Use the following convention:

.. sourcecode:: shell

    $ client-shell webdavs://user@acme.onmicrosoft.com@acme.sharepoint.com -p 'password'
    > connect


.. sourcecode:: bash

    # useradd sftpplus
    # groupadd sftpplus


``$`` means a non-root user. 

``#`` is a root user.

``>`` means a client-shell command.


Documenting the code
====================

Code documentation can be in the form of docstrings, comments, examples or
tests.

Use docstrings to document packages, modules, classes and functions regardless
of what language it is - Python, shell, C etc.

* Well documented code is extremely important.
  Take time to describe components, how they work, their limitations, and the
  way they are constructed.
  Don't leave others in the team guessing what is the purpose of uncommon or
  non-obvious code.

**Python Examples:**

Document code as part of docstrings and not as comments.

.. sourcecode:: python

    def iamanExample(doc):
        """
        A simple docstring is placed here.
        """
          config = self.createSomethingHere('')

Other tips about Python docstrings are this
`wiki entry <https://en.wikipedia.org/wiki/Docstring>`_.

**Shell Examples:** 

Use comments to document what the shell script does and notes to keep in mind
to the developers using a script.

.. sourcecode:: shell

    #
    # This script is used to check all combination for cryto algorithms between
    # twisted.conch.ssh server and OpenSSH client.
    #
    KEXs='diffie-hellman-group14-sha1 diffie-hellman-group1-sha1
    diffie-hellman-group-exchange-sha1 diffie-hellman-group-exchange-sha256'
    MACs='hmac-sha2-512 hmac-sha2-256 hmac-sha1 hmac-md5'

Document how portions of the script works, where needed:

.. sourcecode:: shell

    # Put default values and create them as global variables.
    OS='not-detected-yet'
    ARCH='x86'

**C Examples:** 

Use comments to document notes to the developer utilizing the c script.

.. sourcecode:: c

    /* file1() replacement (from file2, if you must know) */

    #include "newfile.h"

Use comments to provide further notes of additional changes / additions,
where needed:

.. sourcecode:: c

    # This is the default-included GNU make and its counterpart: makeinfo.
    export MAKE=/usr/sfw/bin/gmake
    export MAKEINFO=/usr/sfw/bin/makeinfo


Test code docstrings
--------------------

Test code docstrings can contain information during the review process of new
tests that can be written.

.. sourcecode:: python

    class TestHelpers(IAmATestCase):
        """
        The docstring here may add tests for helpers for a certain module
        """
        def test_of_a_module_1(self):
         """
         What is expected to happen in the first module of this test case
         """
        def test_of_a_module_2(self):
         """
         What is expected to happen in the second module of this first case
         """

.. sourcecode:: python

    class MyClass(object):
        """The class's docstring"""

        def my_method(self):
            """The method's docstring"""

    def my_function():
        """The function's docstring"""


Production code docstrings
--------------------------

Docstring are added in the production code to provide further information for
readers and reviewers.  

For example:

.. sourcecode:: python

    def getSomethingNewHere(self):

In this case, a docstring should be added to add further information:

.. sourcecode:: python

    def getSomethingNewHere(self):
        """
        A docstring describing what SomethingNewHere is about
        """


Marketing / Promotional Materials
=================================

Promotions and marketing materials are mainly located in the main website.

It should be as generic and non-technical as possible with links to the
Documentation for more in-depth / technical information.


Announcing a new release to the email list
------------------------------------------

After the website is updated and News item published, we send a newsletter:

1. Go to Campaigns in Mailchimp.

2. Select 'Replicate' besides 'NEW: SFTPPlus Release Announcement'.
   If it is a security bugfix, use the Security Advisories email list.

3. Select the News Announcements email list.

4. Update the subject and email with the News text used to announce the
   new release. You can use the text in the News article.

5. Select Send. Before sending the final email, preview first by going
   to 'Preview and Send' on the top menu. Select 'Send a test email'.
   

Known Issues
============

Known issues are Z-Horse Easter type of bugs with workarounds.

There is a page on the documentation where Known Issues and the ID are listed
publicly
`here <https://www.sftpplus.com/documentation/sftpplus/latest/known-issues.html>`_.

The page is useful for handling Support queries. For example, if a
customer finds a problem with the software, check that the problem exists in
the Known Issues list first.

If there is an existing issues, then the customer can continue using the
product as long as there is also a workaround provided in the Known Issues
page.

Known Issues will include a reference to the internal Trac ID which provided
further details about that issues

Mock ups and designs for the website
====================================

If a change involves a design or content addition (such as an image carousel
in JS), it is a good idea to write/mock up the content first before coding.

In this way, you can check to see what type of code work should be done to best
communicate the content.

Please go to the 'design' repository for sample images and screenshots to use
and add your own samples.

If raw HTML needs to be used, see if custom directives can be used such as:

.. sourcecode:: bash

    :call_for_action: Ready to install SFTPPlus?
    :call_for_action_link: /pricing/?utm_source=client&utm_campaign=clientbtn&utm_medium=btn#id1
    :call_for_action_button: Ask for a trial

For documentation pages, please do not add raw HTML as the format is designed
to be converted into multiple other formats.
