Generic Programing Advice
#########################

General
=======


* Optimization should come second and only if really needed.
  Don't use clever tricks and other optimization to early.

* Do the simplest thing that could possibly work and do it well.
  Always work on the story you have, not something you think we're going to
  need some time in the future.
  Don't try implement all use cases you can think of and end with poorly
  designed code and poorly tested code.

* Try to keep methods as flat as possible and return as early as possible.

* Don't mix multiple languages in a single file.

* When reporting a code related problem, use
  `Short, Self Contained, Correct (Compilable), Example`_

.. _Short, Self Contained, Correct (Compilable), Example: http://sscce.org

* Each repository / project will have a README file describing why it exists
  and what it should do.
  The README should also include notes about contributing to the project.

* Each repository will have a LICENSE and AUTHORS files.

* Use a graphical commit tool (``git gui`` or ``gitg``) for doing the commit.
  In this way you can split the changes in multiple commits and you can also
  do a first review just before the commit.

* When you don't understand something related to security, don't just walk
  by and ignore it.
  Try to understand what is happening there, or ask
  someone else to take a look or to explain it to you.

* Don't abuse inheritance and favour composition and delegation.

* All branches will need to use the following convention:
  ``TICKETNO-SHORT_DESCRIPTION``.
  By having a reference to a ticket, it will be much easier to track and keep a record of the branch purpose and its
  development.

Example::

    447-add_sqlite_log


Exceptions handling
===================

Here are some simple generic rules for working with exceptions.

In Chevah project we use 2 major "kinds" of exceptions:

* `Errors` are top level exceptions that are not going to be handled
  internally by the package / library.

* `Exceptions` are normal exceptions, passed inside the package/library to signal
  various conditions.
  The public API for the package/library should not raise this kind of exceptions.

Exceptions can take any format, and most of the time they can contain only a 
piece of text with some details about the error.
These exceptions are low level and should be raised in simple conditions.

Errors should have a unique ID and a data attribute.
Each ID should be raised from a single place.
The data attribute is a dictionary with key / value pairs that makes sense of the
error.

Don't use the `assert` statement in code but rather raise an explicit error.
`assert` statement optimization is useless as it was scientifically proven
that some bugs only show up when a customer uses the machine and we want
those exceptions to be raised in production, not to be accidentally
disabled.

Don't raise `AssertionError` outside of the test code.
Use `RuntimeError` or a more specific exception.

The `AssertionError` should never be handled; neither in production nor in
testing code.
Using `self.assertRaises(AssertionError)` is a form of handling an
exception.

Don't raise `RuntimeError` outside of the production code.
Use `AssertionError` when implementing doubles, stub or mock implementations
to support the testing.

All raised assertions should have a descriptive message.
Raising an error without a message is a way of saying:
"I cared enough to give you an error, but not enough to tell you what is
going on".


Logging
=======

* Each log message should be documented listing format, introduction version,
  version since it was obsolete, log type, conditions in which it is raised;
  and other information which could be useful for users.

* A logging message should only be called from a single place in the code.
  This will greatly help with support and debugging.

* A logging message should have a unique ID.
  This will help the support team by pointing a specific event.
  It will also help when using localized logs.

* If a logging message should be issued from multiple places, move the
  logging call into a dedicated helper method. This will help with
  automatically detecting accidental usage of the same message ID for different
  logs.

* Components should not issue logging messages that are outside of
  theirs scope, but rather use exceptions to pass the log information.

* If there are no other options, rather than directly issuing a logging
  message, the component should call a function located inside the component
  that 'owns' the log ID that would issue the log.


Configuration
=============

* Each user configuration options should be documented
  listing valid values, place where the configuration is located,
  introduction version and version since it was obsolete,
  together with a description of the purpose and effect.

* Configuration options must be documented using the following format.
  Please note the order in which fields are defined, the name of the files, and the
  format for declaring possible values.
  All fields should be present, and if no value is defined, use 'None' or leave it blank.

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

      It can also span multiple paragraphs.

      This should be the place to describe in detail each available value
      that can be set.
