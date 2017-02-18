JavaScript
##########

:menu_order: 151

.. contents::

General
=======

* Variable declarations must start with 'var'.

* Try your best to never to use a semicolon.
  This means avoiding them at line breaks and avoiding multi-statement lines.
  A semi-colon at the end of the line is only added when required.

* Use 4 space indentation.

* Use variables, functions, methods and constants names following PEP8.
  variable_name, function_name, methodName, ClassName, CONSTANT_NAME

* Callback methods should always end with 'Callback' as the
  method / function name. This is a reminder of the fact that
  the context is lost.

* Constructor functions (those that are called with **new**) should use
  class naming convention.

* use ``===`` instead of ``==`` for comparison. ``===`` doesn't do type
  coercion.

* Only use ``typeof`` for checking against undefined variables::

    typeof foo !== 'undefined'

* For all other type checking use the custom defined typeOf() function.

* Try to avoid the usage of ``instanceof`` and don't use it for native types.

* Create new arrays using the array literals ``[]`` notation. Don't use
  ``new Array()``.

* Iterate through arrays using the classic ``for`` loop::

    var list = [1, 2, 3, 4, 5, ...... 100000000];
    for (var i = 0, l = list.length; i == l; i++) {
        console.log(list[i]);
    }

* Always define the variable used to iterate into the ``for`` loop first statement. 

* Don't use ``eval`` and don't pass strings to ``setTimeout`` and
  ``setInterval``.

* Use ``undefined`` instead of the the traditional ``null``.

* Keep braces on the same line as their corresponding statements. Never omit
  them for single-line if / else statements.

.. sourcecode:: javascript

    if (something) {
        // code here
    } else {
        // code here
    }

    function duppy() {
        var something
        return {
            foo: function() {}
        }
    }

* Leave 2 empty lines between global function or class definitions.
  Leave 1 empty line between functions from the same class.
  Global variables can be grouped and the don't require empty lines in between them.

.. sourcecode:: javascript

    var GLOBAL_DAY = 1
    var GLOBAL_YEAR = 3


    /*
    Docstring for duppy.
    */
    function duppy() {
        // Do something here.
    }


    /*
    Docstring for duppy_doo.
    */
    function duppy_doo() {
        // Do something here.
    }


    /*
    A simple mock for Browser service.
    */
    function MockBrowser() {
        this._cookies = {}

        /*
        Docstring for MockBrower.setCookies()
        */
        this.setCookie = function(name, value) {
            // Implementation here.
        }

        /*
        Docstring here.
        */
        this.doSomethingElse = function(name) {
            // Implementation here.
        }

        this._methodWihoutDocstring = function(name) {
            // Implementation here.
        }

    }


* Avoid using leading parenthesis.

* Avoid using the ``delete`` operator and only use it to delete explicitly
  set properties on normal objects:

.. sourcecode:: javascript

    var obj = {x: 1};
    obj.y = 2;
    delete obj.x;  // true
    delete obj.y;  // true

* Use single quote for strings.

Example::

    In HTML, we use " as quotes around attribute values, like this:

.. sourcecode::

    <a href="foo">bar</a>
    In JavaScript, we use ' as much as possible.

    alert('qux');
    This way, we can use consistent quotes when writing HTML inside of JS:

    alert('<a href="foo">bar</a>')

* REST web services should always return a valid dictionary
  and not an Array or a primitive. JSON-RPC is forced to return a dictionary
  by the protocol.

* Callbacks called from the GUI / DOM should be prefixed with `on`.
  Ex: onAuthentication (when authenticate button is pressed),
  onLogout (when logout link is pressed),
  onLoginFormSubmit (when login form is submitted)

* Callbacks/Errback for XHR are be prefixed with `cb` and `eb`, similar
  with Python/Twisted convention.

* For one line comments, leave one empty space after the comment marker.

.. sourcecode:: javascript

    // Good comment line.
    //Bad comment line.

* For multi line comments use the following convention.

.. sourcecode:: javascript

    /*
    Short single line comment title.
    More details about what is here and
    here and here.

    Feel free to create paragraphs separation.
    */

* Global constants will follow the CONSTANT_NAME naming convention.

* Global services (objects with methods) are named similar to class names.
  Most of the time they will be singletons so there will be no associated
  class.

.. sourcecode:: javascript

    var Shell = new ActiveXObject("WScript.Shell");

    function do_something() {
        var bla = Shell.method_usage()
    }


TODO
http://javascript.crockford.com/code.html http://jibbering.com/faq/notes/code-guidelines/ http://neil.rashbrook.org/Js.htm

Prevent polluting the global scope
==================================

You can use immediately invoked function expression IIFE to avoid
injecting more variables into global scope.
When using IIFE don't forget to add the semicolon at the beginning.

.. sourcecode:: javascript

    // Path something from global scope.
    ;(function () {
      // tagsInput is kept only inside this scope.
      var tagsInput = angular.module('ngTagsInput')
      tagsInput.factory('tiTranscludeAppendDirective', function() {
          return function() {}
      })
    })()

Defining classes
================

In JS there is no strict way of defining a class and instances are created
using a function and new operator.

When defining a class we use an anonymous function to allow class
private instances and create a new class scope.

.. sourcecode:: javascript

    var BaseAccount = (function() {

        var class_private_member = 2

        /*
        Constructor is here.
        */
        var cls = function(name, age) {
            this.name = name
            this.age = age
        }

        cls.prototype.class_member = 3

        /*
        Base method.
        */
        cls.prototype.base_method = function() {
            return this.name + '-' + this.age
        }

        /*
        Some method.
        */
        cls.prototype.some_method = function(prefix) {
            return prefix + this.base_method()
        }

        /*
        Another method.
        */
        cls.prototype.tuned = function() {
            return false
        }

        return cls
    }())


    var SpecialAccount = (function() {

        var cls = function(name, age) {
            this.variant = 'light'
            /* Something similar to super()*/
            BaseAccount.call(this, name, age)
        }

        /* Something similar to inheritance. */
        cls.prototype = Object.create(BaseAccount.prototype)
        cls.prototype.constructor = cls

        /*
        Method extending parent.
        */
        cls.prototype.some_method = function(prefix) {
            var parent = BaseAccount.prototype.some_method.call(this, prefix)
            return prefix + '-child-' + parent
        }

        /*
        Method overwriting parent.
        */
        cls.prototype.tuned = function() {
            return true
        }

        return cls
    }())

CSS interaction
===============


JS related CSS class
--------------------

Try to append js- to all javascript-based selectors. This is taken from
`slightly obtrusive javascript`_. The idea is that you should be able to tell
a presentational class from a functional class.

There are good things and bad things about "Unobtrusive JavaScript."
One bad thing: it's hard to tell when JavaScript is touching an element.

Only use classes and ids prefix with js- when touching the DOM with
JavaScript.

For example::

.. sourcecode:: 

    <a href="#prices" class="button js-open-tab">Prices</a>

Now we know how to look for any JavaScript touching .js-open-tab, which should
only be a simple search away.

And hey, now JavaScript and CSS won't share selectors. Since we're separating
our content and presentation, we might as well separate our behaviour all the
way too.

.. _slightly obtrusive javascript: http://ozmm.org/posts/slightly_obtrusive_javascript.html


Changing CSS/HTML from JS
-------------------------

Don't modify the associated CSS properties, but rather modify the CSS class:

GOOD: 

.. sourcecode:: javascript

   $('#element_id').addClass('highlight');

BAD:

.. sourcecode:: javascript

   $('#element_id').css('font-weight': 'bold');

Same story as with CSS, don't modify HTML tag attributes,
but rather try to change the CSS class:

GOOD:

.. sourcecode:: javascript

    $('#element_id').addClass('sprite red_dot');

BAD: 

.. sourcecode:: javascript

    $('#element_id').attr('src': 'some/red_dot.png');

Test styleguide
===============

* We use ``expect`` style testing.
* Leave 2 emtpy lines before each ``suite`` and one empty line before each
  ``test``

.. sourcecode:: javascript

    /*
    Tests for login controller.
    */

    suite('LoginCtrl', function() {

        // Shared variables.
        var scope
        var ctrl

        setup(function() {
            // Initialize first.
        })

        teardown(function() {
            // Clean second.
        })

        test(
        'Initializes with no errors and blank values' +
        'long line are wrapped',
        function() {
            var something = Something()

            something.doSomething()

            assert.equal('', something.username)
        })


        suite('critical_error attribute', function(){

            test(
            'When set, hides the form and sets the error message.',
            function(){
                var message = manu.makeUniqueString()

                scope.critical_error = message
                scope.$digest()

                assert.isFalse(scope.show_form)
                assert.equal(message, scope.alert.error)
            })
        })
    })

Rerefences
----------

Here are the pages I used to create this page:

* http://toranbillups.com/blog/archive/2013/05/15/Basic-javascript-inheritance-and-polymorphism/