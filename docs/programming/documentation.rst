Documenting the code
####################

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
====================

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
==========================

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
