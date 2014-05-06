Testing
#######

.. contents::

Writing automated tests is an important part of development.

We write tests to:

* help improve quality
* help understand the product and its components
* reduce risk and fears when doing bold changes into product structure
* make work easier and fun

All tests should have the following characteristic:

* simple
* easy to write and maintain as product evolves
* easy to read and understand what they are doing
* easy to run, easy to re-run, fully automated run and reporting
* run very, very fast
* each test should be an independent test which can run by itself

Writing tests is not only done to check that code works as expected, it is
also done to make sure that code has a simple designed, decoupled and easy
to be reused.

Writing test is also about making sure that you fully understand what the
code should do and how it is used.

Writing tests is not a silver bullet for improving code quality and is easy to
write bad tests.

Once used to having tests that show how things work (and that they do work), you
will start using the key phrase: **Do you have a test for that?**.

You are going to test your code anyway, spend the time to do it right.

We write tests as a tool for regression checking, ie preventing bugs.
Tests should be easy to run and should be fast. Tests will also help us find
bugs and avoid long debugging session, but they primary goal is to keep the
bugs out of our product.

We should write code and do clean-up / refactoring without any fear and with
a confident and free mind. Don't take decision out of fear.

Imperfect tests, run frequently, are much better than perfect tests that are
never written at all.

Writing tests does not mean writing twice as much code or coding slower.

Most of the time the associated test code is tree times longer, or more
in lines of code. Test code should be trivial, easy to write and easy to
understand. Even if there are many lines of test, they should be easy
to write and should not add a big overhead to what you're doing.

On the long run, it's faster and more robust than coding without tests.

Another important part of writing test is to help us have a clean code base.
You can not refactor and do clean-up without an easy mechanism to check for
regression.
Clean-up tasks are just normal business and an integrated part of
coding process. We will do cleanup all the time, and there is no
dedicated development window for cleanup.

The goal is to write test first and code later.

If you are starting and learning how to write tests, you will write tests
after writing the code simply because you have so much to learn and find
that writing tests first is impossible. This is a normal start.
It's just a stepping stone on your way to test-first development.

Passing software to another developer without tests is like saying
'Good luck dude!', but instead we should say 'I've got you covered!'.


Types of tests
==============

Tests can be placed in many categories according to various criteria.

Below is an attempt to identify various types of tests based on their interaction
with other code / systems.


Unit testing
------------

This is the least controversial type of tests, and people usually know what
unit tests are.

Test for single method or functions. As the number of unit tests significantly grows
throughout the lifecycle of the project one key requirement is that they run as
fast as possible. Therefore the tests should use only data from memory for both input 
and output.


Integration testing
-------------------

These are the tests which take what was tested using unit tests (functions,
methods) and combine / integrate them in bigger tests for the whole module or even
module interactions.

The time / speed restrictions still apply. They should also use only data from memory.

Try to test all corner cases regarding the component's integration.

Don't write corner cases for a specific component since they *should* be handled at
unit testing level. If that is not the case please revise the unit tests accordingly.

The purpose of integration testing is to detect any inconsistencies between
the software units / modules that are integrated together or between any
modules and the hardware.

Since they should be fast, you can put them together with unit tests.


System testing
--------------

In contrast with unit or functional tests, we have system test which have no
restriction for
interacting with external systems.

A test is a system test if:

* It touches the file system.
* It talks to the database.
* It communicates across the network.
* It uses some type of shared resource and can't run at the same time as
  any other unit tests.
* You have to do special things to prepare your environment.
* Requires a special OS account / OS credentials to exists.

They interact with local filesystem, network and other services provided by
the operating system.

While interacting with external system, system tests require additional
steps in configuration and preparing the external system for running the
tests, so their execution depend on these external systems.
Example: configure an OS account, do special network configuration,
configure a printer, create certain files or folder structures on the
filesystem.

The external services are "black boxes", as we don't have access to their
internal structure.

They test the integration with external services, and at some
extend they are integration tests.

Due to interaction with external system, system tests are slower than unit or
integration tests.

While configuring external systems, take special care to avoid side effects or
leaving the system in an inconsistent tests that will not allow other tests
to execute. At the end of the test, leave the system in the same state as the
one from the start.

We put them in together with unit tests, since they should be fast,
but we tag them since they require special handling due to dependency on
external systems. Ex, when porting on a new platform, they are likely to
fail.


Story / Functional / Customer tests
-----------------------------------

These are the tests for the final product. All modules are put together just
like in the production (real) system.

In other places, they are also called *acceptance tests*.

This kind of tests help us detect **what** features of our product are
not working. In case we have good unit test, we look there to find **why**
a functional tests is failing.

Functional tests will not help with development and locating the source
of an error. Use unit tests for this. In case unit test pass, and we have
failing functional tests, then we have just discovered a hole in our unit
testing and we should fix it first.

The functional tests are just recording the same steps required in manual
testing. If a functional tests pass, you can look around by starting
the real server and manually perform the same steps as in the functional
test.

You can consider them black box testing as their role is to check that the
system, as a whole, works.

While for system tests only external systems are handled as black boxes,
for functional testing the system under test is also handled as a black box.

They will read actual input just like the real life application and will
produce actual, real life, results.

Don't do too much work here and don't bother with corner cases.
A simple success scenario and a failure scenario should be enough.

Sometimes reading and writing actual input can slow tests, so for performance
reasons, some system tests also read and write data in memory, but the format
used closely resembles the one used in real life, production environments.


Developing using tests
======================

As there is no guarantee for the order in which the tests will execute there is
one major requirement, regardless of the test type. The *test should not have any
side effect* as the order of execution is random.

When writing application code, only write enough code to make a test work.
It helps you to realise when to stop coding and move on to the next task.
If you know there should be more code to handle other cases, you should write the tests 
for those particular cases. This technique prevents writing code that is never executed 
and ensures that you always have a test for the code you write.

When you find a bug, start by writing a test reproducing the bug then
continue you work in fixing the bug. Ask the *5 whys* in order to find the
root cause of the bug and fix the problem there. The initial test written
to reproduce the bug, might be a high level tests which is not at the same
level to the code which was fixed. Removed the high level tests and write
a specific unit test, directly associated with the fixed code.

Running the test suite should be fast, but sometimes some tests are just slow.
Functional tests are always slow, and system tests tend to be slow. We mark
these slow tests so that we can skip them using the test runner.

Principle of developing using tests:

* **Write test first** - the test will save a lot of debugging time and
  setup time for each time you would have to run the manual test to check
  your code.

* **Design for testability** - Now, if you don't write your test first, you
  should at least let the test design your code and not design the test
  after your code. If you **write test first** you don't need to worry
  about this.

* Use **Front Door First**, this means that you should first try to write
  tests only using the public interface.

* **Verify one condition per test**. Don't test more than one thing in a test,
  as it will make the test hard to read. There is an exception for customer
  tests, which are story based and those tests will check a complete
  work-flow.

* **Comunicate Intent** write short tests, which are clean and easy to read
  and serve as documentation for the code.

* **Keep testing login out of production code**. Don't add hooks or
  conditional statements in the production code to help with testing.

* **Keep tests independent** each test should run on it's own and should also
  run together with the other tests.


Domain Specific Language
------------------------

Group multiple / related calls into dedicated, helper methods. Give the method
an easy to read name. Try to create a Domain Specific Language for your tests.


.. sourcecode:: python

    class TestSuperUser(TestCase):
        """
        Tests for super user.
        """

        def test_rename_ulgy(self):
            """
            Users can be renamed just by calling rename() on the user object.

            Ugly initialization code.
            """
            username = factory.makeUsername()
            new_username = factory.makeUsername()
            configuration = factory.makeSuperConfiguration()
            configuration.addUser(username)
            user = configuration.getUser(username)
            user.enabled = True

            user.rename(new_username)

            self.assertTrue(configuration.userExists(new_username))
            self.assertFalse(configuration.userExists(username))

        def makeUser(self, username, configuration=None):
            """
            Return a new username created for `configuration`.

            If `configuration` is `None` it will use a new configuration.
            """
            if configuration is None:
                configuration = factory.makeSuperConfiguration()
            configuration.addUser(username)
            user = configuration.getUser(username)
            user.enabled = True
            return user

        def test_rename_clean(self):
            """
            Users can be renamed just by calling rename() on the user object.

            Clean version.
            """
            username = factory.makeUsername()
            new_username = factory.makeUsername()
            user = self.makeUser(username)

            user.rename(new_username)

            self.assertTrue(configuration.userExists(new_username))
            self.assertFalse(configuration.userExists(username))


Dependency injection of system components
-----------------------------------------

For unit testing, we want to make them easy to write, run them fast and
without touching the system (filesystem / network / os services).

In order to be useful, methods need to interact with the system.

As a first practice, methods interacting with the system should be grouped
and isolated into component dedicated with input / output operations.

When writing tests for code which touches the system, the tests will also
use the system. This can slow the tests or create unwanted side effects, since
most of the time system resources are persistent.

In some cases, especially when testing code for failures, it is very hard
to setup the external system to raise a certain failure condition. For example
we have the code which handles a socket which can raise a timeout error.
Timeout errors are complicated since they requite a certain amount of time
to pass before they appear and this can slow down the whole tests.


.. sourcecode:: python

    import socket

    class ClientWithoutDependecy(object):
        """
        A network client.
        """

        def connect(self, address):
            """
            Try to connect to a server and return False if connection was
            not successful.
            """
            result = False
            try:
                socket.connect(address)
                result = True
            except socket.TimeoutError:
                do_something_on_timeout()
                result = False
            return result

    def test_connect_with_slow_timeout(self):
        """
        When a server does not exist at the address, the timeout is handled
        in some way.
        """
        client = ClientWithoutDependecy()

        result = client.connect_to_server('bad.address')
        # Wait a lot for method to return.

        self.assertFalse(result)


    class ClientWithDependecy(object):
        """
        A network client which has its dependencies as class members.
        """

        socket = socket

        def connect(self, address):
            """
            Try to connect to a server and return False if connection was
            not successful.
            """
            result = False
            try:
                self.socket.connect(address)
                result = True
            except socket.TimeoutError:
                do_something_on_timeout()
                result = False
            return result

    def test_connect_with_fast_timeout(self):
        """
        When a server does not exist at the address, the timeout is handled
        in some way.
        """
        class TimingOutSocket(object):
            """
            A socket which times out at connection.
            """
            def connect(self, address):
                raise socket.TimeoutError()

        client = ClientWithDependecy()
        client.socket = TimingOutSocket()

        result = connect_to_server('bad.address')
        # Returns very fast.

        self.assertFalse(result)


Mock object
-----------

Mock object can simplify a lot test writing and are a very powerful test
tool.

With great power, comes great responsibility! Don't abuse the mocks.

As much as possible, try to use a Mock object together with the specification
of the mocked class.

.. sourcecode:: python

    # Bad.
    mocked_object = Mock()
    # Good.
    mocked_object = Mock(specs=SomeClass)


You can use mock object in the following circumstances:

* Want to trigger an error from a function that requires a precondition
  that is hard to create in a test.

.. sourcecode:: python

    some_object = SomeClass()
    some_object.openFile = Mock(side_effect=SomeHardException())


* Want to check for delegation and you know that the delegated methods /
  objects have good test coverage.


Structure of a test
===================

Use the **Assert, Act, Arrange,** pattern: each part must have it's own paragraph.

 * **Arrange** is variable declaration and initialization code.
   Set up all conditions and environment for testing.
 * **Act** is invoking the code being tested.
   Call the method or trigger the necessary state.
 * **Assert** is using the assert methods or any other code to verify that
   expectations were met.

For integration tests, this can also be called **Assemble, Activate, Assert**.

The tests needs to be short and easy to read.

Some test might not require the *arrange* part, but this is usually a code
smell and most of the time you should have something in arrange part.

Make sure to test only a single thing at once.

When *asserting* that *acting* on a code raised an exception, these two steps
might get intertwined and look like the following code. This is OK.

.. sourcecode:: python

    def test_getAllProperties_no_accounts(self):
        """
        An error is raised if no accounts are defined.
        """

        with self.assertRaises(ConfigurationError):
            some.getAllProperties()

The *arrange* part can get very long. Try to move as much code in setUp()
method, or move related initialization code in a helper method.

When the code is used only in a few tests, put it in a dedicated, reusable, method.

.. sourcecode:: python

    def test_section_navigation_long_arrange(self):
        """
        This does not uses setUp or other
        """
        account = factory.makeTestAccount()
        browser = factory.makeTestBrowser()
        browser.open(self.BASE_URL + '/login')
        browser.setField('username', account.name)
        browser.setField('password', account.password)
        browser.clickButton('Submit')

        browser.open(self.BASE_URL + '/some_section')

        self.assertEqual('section_title', browser.title)

    def setUp(self):
        """
        Object used by almost all tests.
        """
        super(X, self).setUp()
        self.account = factory.makeTestAccount()
        self.browser = factory.makeTestBrowser()

    def login(self):
        """
        Go to login page and submit username and password.
        """
        self.browser.open(self.BASE_URL + '/login')
        self.browser.setField('username', self.account.name)
        self.browser.setField('password', self.account.password)
        self.browser.clickButton('Submit')

    def test_section_navigation(self):
        """
        After login, users can navigate to specific sections.
        """
        self.login()

        self.browser.open(self.BASE_URL + '/some_section')

        self.assertEqual('section_title', self.browser.title)


Especially on some integration test or system tests, you also have one last
part for a test: the cleanup. It is recommended to do it in tearDown() but
when not practical, do it as a new paragraph, at the end of the test.

Smells
======

* Don't abuse the debugger. The tests should have a good coverage so that
  any code can be debugged just by using the debugger on a failed tests.
  In case you need more than 1 breakpoint in the code, this is a sign that
  you are missing a test.

* Hard work in finding / debugging an error is often an indication of failure
  in writing good code or good tests.

* In case using the automatic breakpoint provided test runner is enough to
  detect the problem, that the code might be good :)

* If a functional test fails, but no unit test fails, than we have at least
  one missing unit test.


Naming conventions
==================

* All test cases should have names prefixed with `Test`.

* Include the tested class name in the name of the test case.

* When multiple test cases exist for the same class, suffix the test case with
  some hints about the special cases in each test case.

.. sourcecode:: python

    class TestSuperButtonInSpace(TestCase):
        """
        Test for super button behavior in space.
        """

        def setUp():
            super(TestSuperButtonInSpace, self).setUp()
            DO YOUR SPACE INITIALIZATION HERE.

    class TestSuperButtonOnEarth(TestCase):
        """
        Test for super button behavior on earth.
        """

        def setUp():
            super(TestSuperButtonOnEarth, self).setUp()
            DO YOUR EARTH INITIALIZATION HERE.

* All methods that perform tests should be prefixed with `test_`.

* If testing a specific method, include the exact name of the method, in the
  test name, at the beginning, just after the `test_` marker.

* When there are multiple tests for the same method, suffix the test with
  a short underline ("_") delimited summary. No need to add all details in the name.
  Just make sure it is unique in the test case. Avoid long descriptions, you
  can add everything in the docstring.

.. sourcecode:: python

    def test_getAllProperties_no_accounts(self):
        """
        An empty dictionary is returned if no accounts are defined.
        """


Test fixtures, setUp and tearDown
=================================

Reusing base test cases and grouping code in setUp and tearDown are great
ways of reducing code duplications.

Since this is a good thing, it does not need to be abused.
Don't forget that code and tests also need to be easy to read.

We write test cases based on the class under test.
For example, when we have an object called Account which can have two
important states: Application and OS, we will write two test case
*AccountOSTestCase* and *AccountApplicationTestCase*.
This is why all tests from a specific test case will need to instantiate the
same object, and this is why is OK to create **self.object_under_test**
instance in the *setUp*.

As a raw rule, in the setUp try to only create raw instances which are
used in all tests, without calling any other code that change the state
of an object.


.. sourcecode:: python

    class BadStorageTestCase(TestCase):
        """
        A test that is hard to read.
        """

        def setUp(self):
            stream = SomeStream()
            self.storage = StreamStorage(stream)
            self.object_1 = NewStoredObject(name='one')
            self.storage.add(self.object_1)
            self.object_2 = NewStoredObject(name='two')
            self.storage.add(self.object_2)
            super(BadHandlerTestCase, self).setUp()

        def test_get_all_objects(self):
            """
            Without arguments, returns all objects for the storage.
            """
            # This test smells, since it had no arrange part.
            result = self.storage.get()

            self.assertEqual(2, len(result))
            self.assertContains(self.object_1, result)
            self.assertContains(self.object_2, result)

        def test_get_filtered_objects(self):
            """
            A name can be specified to filter results.
            """
            # This test smells, since it had no arrange part.
            result = self.storage.get(name='one')

            self.assertEqual(1, len(result))
            self.assertContains(self.object_1, result)
            self.assertNotContains(self.object_2, result)


    class BetterStorageTestCase(TestCase):
        """
        A test that is easier to read.
        """

        def setUp(self):
            stream = SomeStream(self)
            self.storage = StreamStorage(stream)
            super(BadHandlerTestCase, self).setUp()

        def test_get_all_objects(self):
            """
            Without arguments, returns all objects for the storage.
            """
            object_1 = NewStoredObject()
            self.storage.add(object_1)
            object_2 = NewStoredObject()
            self.storage.add(object_2)

            result = self.storage.get()

            self.assertEqual(2, len(result))
            self.assertContains(object_1, result)
            self.assertContains(object_2, result)

        def test_get_all_objects(self):
            """
            A name can be specified to filter results.
            """
            object_1 = NewStoredObject(name='one')
            self.storage.add(object_1)
            object_2 = NewStoredObject(name='two')
            self.storage.add(object_2)

            result = self.storage.get(name='one')

            self.assertEqual(1, len(result))
            self.assertContains(object_1, result)
            self.assertNotContains(object_2, result)

Try to put as much cleanup code in the tearDown method and not after the
**assert** block. If a test fails, the rest of the assert block is not
executed, and putting everything in a try/finally increase indentation.
You can register object for cleanup by using dedicated creation method.

.. sourcecode:: python

    class BadTestCase(TestCase):

        def test_someMethod_with_test_bad_cleanup(self):
            """
            When an assertion fails, cleanup is not called.
            """
            file = open('some_file')
            operator = SomeFancy(file)

            operator.read()

            self.assertEqual('something', operator.getAllContent())
            # When assert fails, the remaining code is not executed.
            file.close()
            os.rm(file.path)


    class GoodTestCase, self(.tearDown()TestCase):

        def setUp(self):
            super(GoodTestCase, self).setUp()
            self.opened_files = []

        def tearDown(self):
            for file in self.opened_files:
                try:
                    file.close()
                    os.rm(file.path)
                except:
                    # Pass or record the files which were not closed
                    # and fail with more details.
                    pass
            super(GoodTestCase, self).tearDown()

        def openFile(self, path):
            """
            Creation method which also registers the object for cleanup.
            """
            file = open('some_file')
            self.opened_files.append(file)

        def test_someMethod_with_test_bad_cleanup(self):
            """
            When an assertion fails, cleanup is still called via tearDown.
            """
            file = self.openFile('some_file')
            operator = SomeFancy(file)

            operator.read()

            self.assertEqual('something', operator.getAllContent())


To reduce the need of tearDown and cleanup code, try to run each test on
new instances and avoid global or singleton objects.

You can still reuse object, in case creating a new instance takes a long time,
as we want test to be fast.


Tests description - docstrings
==============================

Good tests can help document and define what something is supposed to do,
so dedicate effort to write good docstrings.

Each test should have a description (docstring) with information about the
purpose of the test or any other additional info that could help another
person to understand the test.

Writing docstring for tests is not easy, but doing so will reduce the
WTF/minute.

* Describe in simple plain English what you are testing and what is the
  expected behaviour.

* Think of the test's docstring as an extension of documentation for the
  method under tests.

* For integration tests add notes about pre-conditions or other requirements.

* Add a brief description and don't describe how the test is done.
  Detailed information about the test should be available by reading
  the code implementing the tests.
  When code fails to speak for itself use inline comments.

* Avoid including the name of the method under tests. The test method name
  should already include it.

* When testing for raised exceptions avoid adding the exception name in
  the test description. Just inform that an exception is raised. By
  reading the test code, it should be easy to get more details about the
  exception.


Here are some tips from Jonathan Lange as a handy five-step guide:

1. Write the first docstring that comes to mind. It will almost certainly be::

    """Test that input is parsed correctly."""

2. Get rid of "Test that" or "Check that". We know it's a test.::

    """Input should be parsed correctly."""

3. Seriously?! Why'd you have to go and add "should"? It's a test,
   it's all about "should". ::

    """Input is parsed correctly."""

4. "Correctly", "properly", and "as we expect" are all redundant.
   Axe them too. ::

    """Input is parsed."""

5. Look at what's left. Is it saying anything at all?
   If so, great. If not, consider adding something specific about the test
   behaviour and perhaps even why it's desirable behaviour to have. ::

    """
    Input is parsed into an immutable dict according to the config
    schema, so we get config info without worrying about input
    validation all the time.
    """

6. Happy hacking!


Rerefences
==========

Here are the pages I used to create this page.

 * http://integralpath.blogs.com/thinkingoutloud/2005/09/principles_of_t.html
 * https://plus.google.com/115348217455779620753/posts/YA3ThKWhSAj
 * http://c2.com/cgi/wiki?ArrangeActAssert
 * http://stackoverflow.com/q/67299/539264
 * http://agileprogrammer.com/2005/08/14/i-really-did-mean-it-avoid-setup-and-teardown/
 * http://agilesoftwaredevelopment.com/blog/vaibhav/acceptance-testing-what-why-how
