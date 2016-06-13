Generic
#######

:menu_order: 001

..  contents::

General
=======

The content of this website is intended to help new team members understand
the direction of our team.

It also helps novice and advance beginners by providing a set of simple rules.
Anyone should read this as best practice and provide feedback in case
something is wrong.

* Rule #1: Keep it DRY! Don't repeat yourself!

* Rule #2: KISS - Keep it simple, stupid simple!

* Rule #3: If it ain't broke, don't fix it!

* All code in any code-base should look like a single person typed it, no
  matter how many people contributed.

* No single person is responsible for a part of the code. We write code
  together, we take the blame together, we take the glory together.
  Once a code was approved for review, reviewers are also responsible for
  that code.

* Write all code as it will be written once and read thousand times.
  Write code for maximum readability.

* When you need a trade-off between readability and code duplication, choose
  to have a code less readable but without duplication.

* Write code as it will be used by humans, not a machine. You are not a
  a compiler / interpretor.

* Optimization should come second and only if really needed. Don't Use clever
  tricks and other optimization to early.

* Do the simplest thing that could possibly work and do it well.
  Always work on the story you have, not something you think we're going to
  need sometime in the future.
  Don't try implement all usecases you can think of and end with poorly
  designed code and poorly tested code.

* Try to keep methods as flat as possible and return as soon as possible.

* Don't use abbreviation. Use full, meaningful names.

* Don't use tabs for indentation, and in general don't use tabs for anything
  else. The only exceptions are the Makefiles.

* Favor indentation using 4 spaces. For deep nested languages (HTML, JS) it
  is OK to use 2 spaces.

* Maximum line length for code is 80 characters, but for Python we use 79 to be in
  sync with PEP8.

* For narrative documentation use `semantic newlines
  <http://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_.
  Make lines short, and break lines at natural places, such as after commas and semicolons, rather than after the Nth column.

..  code-block:: text
    :linenos:

    Sometimes when editing a narrative documentation file, I wrap the lines semantically.
    Instead of inserting a newline at 70 columns (or whatever),
    or making paragraphs one long line,
    I put in newlines at a point that seems logical to me.
    Modern code-oriented text editor are very good at wrapping and arranging long lines.

* Don't mix multiple languages in a single file.

* No need for the ultimate purism, when using / calling code from external
  libraries it is OK if those calls don't comply with coding convention.

* When extending external libraries use the coding convention used by that
  library. It might be harder to define the border of those changes but this
  should help with sending patches upstream.

* When reporting a code related problem, use
  `Short, Self Contained, Correct (Compilable), Example`_

.. _Short, Self Contained, Correct (Compilable), Example: http://sscce.org

* Each repository / project will have a README file describing why it exists
  and what it should do.
  The README should also include notes about contributing to the project.

* Each repository will have a LICENSE and AUTHORS files.

* Words are an important part of how software works.
  Even though there may be dozens of people creating a product, reading
  comments, documentation, notes etc, it should still sound like we speak
  in one consistent voice.

* When writing text for the documentation or text that appears in the
  program favour classy over cute or mechanical.
  Respect the reader, act more like a human and less like a computer,
  and use fewer words::

      Instead of:

      Successfully deleted the #{branch_name} branch.

      Try something like:

      The #{branch_name} branch has been deleted.

* Use a graphical commit tool (``git gui`` or ``gitg``) for doing the commit.
  In this way you can split the changes in multiple commits and you can also
  do a first review just before the commit.

* When you don't understand something related to security, don't just walk
  by and ignore it. Try to understand what is happening there, or ask
  someone else to take a look or to explain it to you.

* Don't abuse inheritance and favour composition and delegation.

* Write code so that it can be read / used by developers having a work
  style different than yours. Don't add IDE / text editor specific things
  Don't assume that other developer will use the same IDE / text editor,
  fancy keyboard (or foot pedals), array of huge monitors...

* When you have a non-trivial conditional expression (logical condition from
  an if statement), break it in smaller sub-conditionals.

.. sourcecode:: python

    # Long conditional which is not that bad.
    if ((source.length < source.MAX_SIZE) and
        (destination.state != ACTIVE) and
        (destination.state != PAUSED)):
      do_something()

    # But can be better.
    source_not_full = source.length < source.MAX_SIZE
    destination_available = (
        (destination.state != ACTIVE) and
        (destination.state != PAUSED)
        )

    if source_available && destination_available:
      do_something()

    # Or even better.
    class Source(object):
      MAX_SIZE = 10
      @property
      def full(self):
        return self.size < self.MAX_SIZE

    class Destination(object):
      ACTIVE = 1
      PAUSED = 2
      STOPPED = 3
      FAILDED = 4

      @property
      def ready(self):
        return (
          (destination.state != self.ACTIVE) and
          (destination.state != self.PAUSED)
          )

    if not source.full and destination.ready:
      do_something()


Comments
========

* All comments should be valid sentences and should end with a full stop (.).

* Try to write code so that it speak for itself and so that a comment is not
  required.

* Try to name variables, methods, function so that they communicate their
  intend. A comment is only attached to the place where the name is defined,
  and not present in all other multiple places where it is used. IDE can help,
  but we should not rely on that.

  When a comment is required is like saying: I have no idea for a better name
  for this thing, so here is my poor comment. Good luck with figuring the
  intend of this name when you see it in the rest of this file.

* Place comments on a new line above their subject and in the same block as the referred code.

.. sourcecode:: python

    if some_condition:
      # We got into into this branch to do x.
      do_something()

    for line in lines:
      if line.startswith('marker'):
        # Marker lines are ignored.
        continue
      do_something()

* Avoid end of line comments.

* Technical debt comments (ex FIXME, TODO) will always have an attached
  ticket ID and will use the following format. Only **FIXME** marker is used
  followed by ticket ID. Comments will come on a new lines.
  Adapt this to the style of comments used in the specific language, but
  is important to keep the **FIXME:123:** marker.::

    # FIXME:1234:
    # Details about this tech-dept. Ex: Can only be fixed when full moon.


Documentation
=============

* Well documented code is extremely important.
  Take time to describe components, how they work, their limitations, and the way they are constructed.
  Don't leave others in the team guessing as to the purpose of uncommon or non-obvious code.

* Document code as part of docstrings and not as comments.

* Document packages, modules, classes, functions.

* For narative documentation (non docstrings) use `semantic linefeeds <http://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_.

..  code-block:: text
    :linenos:

    Sometimes when editing a narrative documentation file, I wrap the lines semantically.
    Instead of inserting a newline at 70 columns (or whatever),
    or making paragraphs one long line,
    I put in newlines at a point that seems logical to me.
    Modern code-oriented text editor are very good at wrapping and arranging long lines.


Exceptions handling
===================

Here are some simple generic rules for working with exceptions.

In Chevah project we use 2 major "kinds" of exceptions:

* `Errors` are top level exceptions that are not going to be handled
  internally by the package / library.

* `Exceptions` normal exceptions, passed inside the package/library to signal
  various conditions. The public API for the package/library should not raise
  this kind of exceptions.

Exceptions can take any format, and most of the time they can contain only
a text with some details about the error. These exceptions are low level
and should be raised in simple conditions.

Errors should have an unique ID and a data attribute.
Each ID should be raised from a single place.
The data attribute is a dictionary with key / values that make sense for the
error.

Don't use the `assert` statement in code but rather raise an explicit error.
`assert` statement optimization is useless as it was scientifically proven
that some bugs only show up when a customer uses the machine and we want
those exceptions to be raised in production and not be accidentally
disabled.

Don't raise `AssertionError` outside of the test code.
Use `RuntimeError` or a more specific exception.

The `AssertionError` should never be handled; be in production nor in
testing code.
Using `self.assertRaises(AssertionError)` is a form of handling an
exception.

Don't raise `RuntimeError` outside of the production code.
Use `AssertionError` when implementing doubles, stub or mock implementation
to support the testing.

All raised assertions should have a descriptive message.
Raising an error without a message is a way of saying:
"I cared enough to give you an error, but not enough to tell you what is
going on".


Experimental Features Without Feature Branches
==============================================

Feature branches are one way to develop slow/long changes without affecting
the production / master branch.

We don't use feature branches because:

* They need to be permanently kept in sync with main branch. This will solve
  conflicts with the main branch, but there might still be hidden conflicts
  with **other feature** branches.
* You will need to keep in sync with other feature branches to make sure
  there are no integration problems. This just creates more work and in the
  end you will have something close to multiple **masters** as each feature
  branch will contain latest development from all other feature branches.
* They create multiple versions of a product which requires more release work.
  You will want to release an alpha/beta version of the feature as soon as
  possible to get feedback from end users.
* Along the focus feature, they might fix or refactor some code code which is
  of great help for the main branch.
* Once merged, a feature branch will introduce a big change in a short time.

Instead of feature branches we develop experimental features directly in the
main branch. Experimental features are triggered using dedicated
(configuration) flags.

In this way, a feature is gradually added to master, and during development
by spending more time in master it should have a greater exposure to testing
and checking that it integrates with other features.


Project specific
================

* Each log message should be documented, listing format, introduction version,
  version since it was obsolete, log type, conditions in which it is raised
  and other informations that can be useful for users.

* A logging messages should only be called from a single place in the code.
  This will greatly help with support and debugging.

* A logging message should have a unique ID. This will help the support team
  by pointing a specific event. It will also help when localized logs are
  used.

* If a logging message should be issued from multiple places, move the
  logging call into a dedicated helper method. This will help with
  automatic detection of accidentally using same message ID for different
  logs.

* Components should not issue logging messages that are outside of
  theirs scope, but rather use exceptions to pass the log informations.

* If there are no other options, rather than directly issuing a logging
  message, the component should call a function located in the component
  that 'owns' the log ID that will issue the log.

* All branches will need to use the following convention:
  ``TICKETNO-SHORT_DESCRIPTION``. By having a reference to a ticket, it will
  be much easier to track and keep a record of branch purpose and its
  development.

Example::

    447-add_sqlite_log

* Each user configuration options should be documented,
  listing valid values, place where the configuration is located,
  introduction version, version since it was obsolete,
  together with a description of the purpose and effect.

* Configuration options will be documented using the following format. Please
  note the order in which fields are defined, the name of the files and the
  format for declaring possible values. All fields should be present, and
  if no value is defined, use 'None' or leave it blank.

::

  log_file
  --------

  :Optional: Yes
  :Default value: `log/server.log`
  :Values: * `some value`
           * `other value` - short description or this value.
           * `yet another value`
  :Available from version: 1.6.0
  :Available up to version: 2.0.3
  :Description:
      This is the long description of the configuration option. It can
      span multiple lines.

      It can also span multiple paragraph.

      This should be the place to describe in details available values
      that can be set.
