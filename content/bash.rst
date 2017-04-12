Bash
####

:menu_order: 016

..  contents::


General
-------

* Shell scripts should be kept at a minimum and **only** for internal scripts.
  For every other script we should use Python.

* Public shell scripts should use ``/bin/sh``. Bash is not available on all
  Unix systems and ksh or other shells are not compatible with Bash syntax.

* Use ``printf`` instead of ``echo`` when using  ``/bin/sh`` as a shell,
  because ``echo`` behaviour is incompatible in Bash and Korn shells.
  Eg. use ``printf`` instead of ``echo -n`` and ``printf "blabla\n"`` instead
  of ``echo "blabla"``.

* For internal scripts we should use ``/bin/bash``, as the default ``/bin/sh``
  sometimes points to a lesser shell such as Dash.

* A function called main is required for scripts long enough to contain at
  least one other function.

* Put all functions together in the file just below constants. Don't hide
  executable code between functions.

* Use uppercase for all GLOBAL variables.

* In tests, enclose all uncontrolled string variables in double quotes to
  handle empty strings or spaces in variables.

* Always double quote the ``$@`` variable to keep all arguments with spaces.

* Pipelines should be split one per line if they don't all fit in one line.

* Use $(command) instead of backticks. Nested backticks require escaping the
  inner ones with \. The $(command) format doesn't change when nested and is
  easier to read. See the example below

.. sourcecode:: bash

    # This is preferred:
    var="$(command "$(command1)")"

    # This is not:
    var="`command \`command1\``"

* Always guard your Bash scripts from unexpected errors by using

.. sourcecode:: bash

    set -o nounset

Path constants
--------------

When defining a directory path as a constant, you should include the trailing
slash to make sure it is a directory and not a file. Two consecutive /'s are
harmless in POSIX shells as long as they are not at the beginning of the path
in some exotic environment such as Cygwin that actually uses this notation for
SMB shares.

Always double quote path constants to handle files with spaces:

.. sourcecode:: bash

    SOME_PATH=/some/path/
    # and use it like this:
    command "${SOME_PATH}/some.file"

    # Another example
    REMOTE_URI=chevah@chevah.com:/home/chevah/styleguide.chevah.com/vm/
    scp "$LOCAL_FILE" "${REMOTE_URL}/file"

Instead of:

.. sourcecode:: bash

    SOME_PATH=/some/path/
    # and then:
    command "${SOME_PATH}some.file"

Function Definition
-------------------

Leave 2 blank lines between function definitions and always use ``local`` for
local variable declaration.

Define local variables at the start of the function, in a distinct block.
It is recommended to define a local variable named `result` to hold the value
produced by calling the function.

Put the final returned result in a separate block.

Procedures are functions which have no result.

Since Bash only support returning numeric values, which are interpreted
as exit codes, we will pass values between functions by using ``echo``.


.. sourcecode:: bash

    #
    # Description of function 1.
    #
    # * $1 - description of first argument
    # * $2 - description of second argument
    # * return - description of return value.

    function1() {
        local variable_which_is_local
        local result

        do_some_action_here
        do_more_action

        echo $result
    }


    #
    # Description of procedure 1.
    #
    # It does this and this.
    #
    procedure1() {
        local something=$(function1 ARG1)

        do_something_else something
    }

Case Syntax
-----------

.. sourcecode:: bash

    case "$VARIABLE_NAME" in
        "option1")
            do specific
            ;;
        option2*)
            do generic
            ;;
        *)
            do default
            ;;
    esac


IF/THEN/ELSE
------------

.. sourcecode:: bash

    if TEST; then
        call something
    elif [ "$string" = OTHER_TEST ]; then
        call something_else
    else
        call something_else_completely
    fi

FOR
---

.. sourcecode:: bash

    for CONDITION; do
        call something
    done

WHILE/UNTIL
-----------

.. sourcecode:: bash

    while TEST; do
        call something
    done

References
----------

Here are the pages I used to create this page.

 * http://www.davidpashley.com/articles/writing-robust-shell-scripts/
 * http://www.linuxjournal.com/content/return-values-bash-functions
