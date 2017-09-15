Generic Style Guide
###################


General
=======

The content of this website is intended to help new team members understand
the direction of our team.

It also helps novice and advance beginners by providing a set of simple rules.
Anyone should read this as best practice and provide feedback in case
something is wrong.

* All code in any code-base should look like a single person typed it, no
  matter how many people contributed.

* No single person is responsible for a part of the code.
  We write code together, we take the blame together, we take the glory together.
  Once a code was approved for review, reviewers are also responsible for
  that code.

* Write all code as if it will be written once and read a thousand times.
  Write code for maximum readability.

* When you need a trade-off between readability and code duplication, choose
  to have a code less readable but without duplication.

* Write code as it will be used by humans, not by a machine.
  You are not a compiler / interpreter.

* Don't use abbreviation.
  Use full, meaningful names.

* Don't use tabs for indentation, and in general don't use tabs for anything
  else.
  The only exceptions are Makefiles.

* Favour indentation using 4 spaces.
  For deep nested languages (HTML, JS) it is OK to use 2 spaces.

* Maximum line length for code is 80 characters, but for Python we use 79 to be in
  sync with PEP8 Style Guide for Python Code.

* No need for the ultimate purism, when using / calling code from external
  libraries it is OK if those calls don't comply with coding convention.

* When extending external libraries, use the coding convention used by that
  library.
  It might be harder to define the border of those changes but this
  should help with sending patches upstream.

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

* Write code so that it can be read / used by developers having a work
  style different than yours. Don't add IDE / text editor specific things
  Don't assume that other developer will use the same IDE / text editor,
  fancy keyboard (or foot pedals), array of huge monitors...

* When you have a non-trivial conditional expression (logical condition from
  an if statement), break it into smaller sub-conditionals.

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

    if source_not_full && destination_available:
      do_something()

    # Or even better.
    class Source(object):
      MAX_SIZE = 10
      @property
      def not_full(self):
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

    if source.not_full and destination.ready:
      do_something()


Comments
========

* All comments should be valid sentences and should end with a full stop (.).

* Try to write code so that it speaks for itself, and so that a comment is not
  required.

* Try to name variables, methods, functions so that they communicate their
  intent.
  A comment is only written in the place where the name is defined,
  and not present in all other multiple places where it is used.
  IDE can help, but we should not rely on that.

* When writing a comment is like saying: "I have no idea for a better name
  for this thing, so here is my poor comment”, good luck with figuring out the
  intent of this name when you see it in the rest of the file."

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
