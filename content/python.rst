Python
######

:menu_order: 011

.. contents::


General
=======

* Start by reading
  `The Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_

.. sourcecode:: python

    import this

* For python, we have pocket-lint that checks for PEP8 and some other things.

* `Python PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_
  Style guide for Python code.

* Favour single inheritance.

* As the second best option, use Mixins to reuse code and avoid multiple inheritance.

* Docstring always uses multiline strings with double quotes and empty first
  and last lines. There's no blank line either before or after the docstring.

.. sourcecode:: python

    def some_function(argument):
        """
        Single line docstring.
        """
        code_starts_here()


    class SomeClass(ParentClass):
        """
        Quick explanation of the role of this class which is a bit long so we
        wrap it.

        More details to follow in long paragraphs.
        """

        def method_starts_here(self):
          """
          Some description.
          """

* Class members or instance members can be documented inline using the
  following syntax:

.. sourcecode:: python

    class SomeClass(ParentClass):
        """
        Docstring for class.
        """

        #: Docstring for class member.
        #: Can be on multiple lines.
        class_member = True

* All test functions, test methods and test suites will have docstrings.

* Tests methods will be prefixed with ``test_``.

* Tests suites (test class) will be prefixed with ``Test``.

* Test's docstring should state what is the expected behavior based on
  test's input.

.. sourcecode:: python

    def test_methodName(self):
        """
        When doing this `methodName` will raise an AssertionError.
        """

* When adding linter exception, always add a comment explaining the reason
  why the exception was added.

* Use named parameters for calling methods. This will reduce future
  refactoring efforts.

* If a method or class initialization / constructor method has more than 1
  argument, always use named parameters for calling that method.

* Try to use single quotes for strings. This will make it easier to generate
  quoted text for UI or HTML.

YES

.. sourcecode:: python

    other_var = 'string'
    some_var = 'string "b" yes'

NO

.. sourcecode:: python

    other_bad = "string"
    some_bad = "string 'b' yes"

* As PEP8 recommends, don't use '\' to split long lines. Wrap long lines by
  using Python's implied line continuation inside parentheses, brackets and
  braces. More details here:
  http://www.python.org/dev/peps/pep-0008/#maximum-line-length

* Multi-line splits using parentheses, brackets, etc, will follow the normal
  indentation rules. The code might look ugly and then exceptions are allowed.

* Define all class members at the beginning of class definition.
  Don't interleave methods and class members definitions. This should make it
  easy to identify all class members used by the class.

* Define all instance members inside the __init__() method. This should make
  it easy to identity all instance members used by the class and reduce the
  risk of using the same member for more than one purpose.

* Decode all input to Unicode and encode all output from Unicode. Do **all**
  internal text handling in **Unicode**.

.. sourcecode:: python

    input_raw_string = read_from_wire()
    input_string = input_raw_string.decode('utf-8')

    # Only work with Unicode data.
    output_string = process_something(input_string)

    output_raw_string = output_string.encode('utf-8')
    send_to_wire(output_raw_string)

* UTF-8 is not Unicode.
  Unicode is a character set and UTF-8 is a particular way of
  encoding Unicode.

* When a method does not use the *self* attribute, this is a code smell
  that this method should be placed somewhere else.


Abstract
========

Abstract classes are classes that contain one or more abstract methods.

An abstract method is a method that is declared,
but contains no implementation.
Calling an abstract method will raise `NotImplementedError`.

Abstract classes may not be instantiated.
They require subclasses to provide implementations for the abstract methods.

Abstract classes are somehow similar to interfaces, but they also come with
partial implementations.

Abstract methods can be public or private.

When raising the `NotImplementedError`, make sure you add some text to uniquely
identify this abstract methods.
During development, we might report errors without a traceback, and having a
custom message associated with the error makes it easier to identify what is
wrong.

When defining an abstract class, suffix it with `Abstract` name.
This should let others know that this class should not be directly instantiated.

All abstract methods should be defined at the beginning of the class, even
before the `__init__` method or class variables.
They should be documented with docstring, describing their usage and how they
should be implemented.


.. sourcecode:: python

    class LocationAbstract(LocationBase):
        """
        Shared code by some type of locations.

        More information about the functionality provided by this class.
        """

        def getProtocol(self):
            """
            Return the client protocol used to connect to the FTP server.
            """
            raise NotImplementedError('_getProtocol not implemented.')

        def _beforeConnection(self, client):
            """
            Called before the FTP command channel connection is initiated.

            Should return a deferred.
            """
            raise NotImplementedError('_beforeConnection not implemented.')

        # Class members defined by the abstract.
        # They can be public or private.
        _reactor = reactor
        REQUIRE_RESTART = ('address', 'port')

        def __init__(self, parent, configuration):
            """
            Abstract classes can implement the init method.
            """
            super(LocationAbstract, self).__init__(parent, configuration)
            # Low level FTP transport protocol.
            self._protocol = None
            self._features = ()

        def onConnect(self):
            """
            They can also fully implement some public methods.
            """
            return self._doMoreWorkHereInPrivateCode()


Mixin
=====

As stated by `Wikipedia <http://en.wikipedia.org/wiki/Mixin>`_:
Mixins encourage code reuse and avoid well-known pathologies associated
with multiple inheritance.

Mixin is a limited usage of multiple inheritance, but they should **not be
mixed with overriding**.

We use mixins to reuse code, and they provide great help for writing tests.

Methods from a mixin should not be overwritten by classes using the mixin.

Mixins should not overwrite methods or call **super()**.

When defining a class using mixins, put the parent class first, and then
add the mixin classes in alphabetical order.

.. sourcecode:: python

    class SomeMixedClass(ParentClass, AnotherMixin, SomeMixin, ZoroMixin):
        """
        A class with `single` inheritance and multiple mixins.
        """

When defining a mixin, document the external class or instance members used
by the mixin.

.. sourcecode:: python

    from some_package import complicated_code_using, complicated_other_using


    class LoginMixin(object):
        """
        Does some kind of work.

        username - account used for authentication.
        password - password for the account
        ssh_key - SSH key for authentication
        """

        def loginWithUsernameAndPassword(self):
            """
            Does something.
            """
            if self.username:
                raise SomeException()

            complicated_code_using(self.username, self.password)

        def loginWithUsernameAndSSHKey(self):
            """
            Does something else.
            """
            complicated_other_using(self.username, self.ssh_key)


Project specific
================

* When default arguments have mutable values, they are defined as `None` and
  then assigned the default value.

  Otherwise this can hit us very hard. `More details here
  <http://stackoverflow.com/q/1132941/539264>`_.

.. sourcecode:: python

    def methodName(self, a, b='imutable', c=None, d=None):
        """
        Describe method.
        """
        if c is None:
           c = []

        if d is None:
           d = SomeObject()


Multi line indentation
----------------------

* For now, just see some examples:

.. sourcecode:: python

    self.logger.log(
        message_id=factory.number(),
        name=factory.getUniqueString(),
        callback=do_something_else,
        )

Same indentation applies for brackets:

.. sourcecode:: python

    some_list = [
        bla,
        blabla,
        alabala,
        ]

* Two-line coding exception: If the parentheses expression does not fit on one line:

.. sourcecode:: python

    self.logger.log(
        factory.number(), factory.getUniqueString())

* Conditional exceptions. When indenting parentheses for conditional
  expressions add one extra indent to separate the conditional expression
  from the conditional block.

.. sourcecode:: python

    if (somethin_else is None or
            say_something_else is None):
        do_else = nothing
        do_something()

    if (somethin_else is None or
            say_something_else is None or
            we_should_not_have_long_conditionals
            ):
        do_else = nothing
        do_something()

* Class, method and function indentation.

.. sourcecode:: python

    class MyClassName(
            VeryLongParentClass, VeryLongOtherMixin):
        """
        Docstring here.
        """

    def myMethodWithLongArguments(self,
            name=None, other_long_thing=None):
        """
        Docstring here.
        """

    def my_function_with_long_arguments(
            name=None,
            other_long_thing=None,
            other_very_long_argument=None,
            ):
        """
        Docstring here.
        """


Imports
-------

* Imports should be called at the start of each module, the only exception
  allowed is when used for avoiding circular imports.

* There is one empty line between the import block and the module comment.

* The import blocks are separated by one empty line.

* They will be arranged in 3 major blocks:

  * 1 - Importing from Python standard modules.
  * 2 - Importing from modules outside of the project (3rd party).
  * 3 - Importing from modules belonging to the project.

* In each block, the modules are sorted in alphabetical order,
  case-insensitive.

* When importing multiple members of a module, if they don't exceed the 79
  characters limit, they will be listed on the same line

* When importing multiple members of a module, and they exceed the 79
  characters limit, they will be listed as a list, with each member on a
  line ending with comma.

A good example:

.. sourcecode:: python

    # Copyright (c) YEAR Your Name.
    # See LICENSE for details.
    """Sample module for demonstrating imports coding conventions."""
    from __future__ import with_statement

    from optparse import OptionParser
    import logging
    import os
    import sys
    import time
    import types

    from OpenSSL import crypto
    from twisted.web import server
    import simplejson as json

    from chevah.commons.utils.constants import (
        DEFAULT_KEY_SIZE,
        DEFAULT_KEY_TYPE,
        DEFAULT_PUBLIC_KEY_EXTENSION,
        )
    from chevah.commons.utils.exceptions import OperationalException
    from chevah.commons.utils.crypto import Key
    from chevah.commons.utils.helpers import (
        _,
        log_add_default_handlers,
        open_local_admin_webpage,
        )
    from chevah.server.commons.configuration import (
        ApplicationConfiguration,
        )
    from chevah.server.commons.constants import (
        CONFIGURATION_SERVER_FILE,
        CONFIGURATION_PID_FILE,
        PRODUCT_NAME,
        )
    from chevah.server.commons.process import ChevahTwistedProcess
