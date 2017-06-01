Bugs and Tech-Debt
##################

:menu_order: 004

.. contents::


General
=======

As with any other product, our ideal is to release a product without any
known defects and with optimal implementation and documentation, all this
backed by a perfect support process.

In the same time, we aim to have the perfect development process, with the
perfect QA process and the perfect release process.

While this is a noble goal, achieving it might not be economically feasible.
This is because creating a zero bugs product will result in a product which costs more
than what customers are willing to pay for.


Defects and Release Blockers
============================

Defects are defined as unintended behavior of our product which does not follow our
specification or the way we want it to work.

Misbehaviors in our build system, testing system or infrastructure are also
defects.

Defects can fall into 3 categories:

* `bugs with high or critical priority` - are defects which affect
  (or we think that might affect) the workflow of at least one customer
* `bugs with low priority` - are defects which do not seem to be affecting our
   customers, but which make the product behave in an unintended way.
   They are acknowledged in the **Known Issues** section of our documentation.
* `tasks with high or critical priority` - are defects affecting our build
   system or testing infrastructure, but are not defects in the actual
   product.

For some defects, fixing them is a lot of work and their impact is minor
as maybe our customers will never use the product in a way to trigger the bug.
In this case, we create a ticket with type `bug` and add it in the backlog.

All defects which affect the work-flow of at least one customer are
considered top priority and will **block the release**.

All defects which are present in a release **should** be acknowledged in the
documentation.

If we gather a considerable number of minor bugs / defect we will schedule
a release dedicated / focused on reducing that number.

We should focus on fixing all bugs as soon as possible.
If it is not currently affecting customers, there is high probability that a customer
will be affected by it in the near future.

Also small/minor bugs might trigger big flaws in the structure of our
code.
We should focus on fixing them as soon as possible so that we can work
on them at a normal pace and not take the chance of having to fix them in a hurry
under the pressure of a release blocker, or when having a customer complaining 
about bad behaviour.


Technical Debt
==============

Technical debts are areas in which we trade code quality for having a feature
delivered faster or a defect fixed sooner.

For every tech-debt the quality of our code is reduced.

As expressed by Martin Fowler::

    You have a piece of functionality that you need to add to your system.
    You see two ways to do it.
    One is quick to do but is messy -
    you are sure that it will make further changes harder in the future.
    The other results in a cleaner design, but will take longer to put in
    place.

If you go for *the former* method you will generate *tech-debt*.

Further comments by Uncle Bob::

    Messy code, produced by people who are ignorant of good design practices,
    shouldn't be a debt.
    Technical Debt should be reserved for cases when people have made a
    considered decision to adopt a design strategy that isn't sustainable
    in the longer term, but yields a short term benefit,
    such as making a release.

    There’s nothing inherently unwise about tech-debt.
    If the early release of 1.0 drives the business that pays for
    the development of 2.0 then the business has won.
    So this kind of reasoned technical debt may indeed be appropriate.

Another comment by Ron Jeffries::

    Technical debt is never a good thing.
    It is sometimes inevitable.
    We should never take on technical debt on purpose,
    and we should pay it back as soon as we know how.

The analogy with the financial term is weak so please read
`Technical Debt – Bad metaphor or worst metaphor?
<http://ronjeffries.com/articles/015-11/tech-debt/>`_ and all the other
articles in the reference section to find out more.

While tech-debt is a bad metaphor, we should all know what we want to say
with `tech-debt` when we talk about our code.
I was not able to find a better metaphor so for now we are stuck with this term.

We are not paying tech-debt in dedicated sprints or releases.

Please read the `Refactoring - Not on the backlog!
<http://ronjeffries.com/xprog/articles/refactoring-not-on-the-backlog/>`_
article by Ron Jeffries.

Sometimes your experience tells you that a section of code is not right and
that it can be implemented as re-usable section.
When you only have one use case for that code, it becomes very hard to create a
generalized / re-usable version, and sometimes trying to do that is wrong as
you most probably ain't gonna need that.
Then it comes the second use cases which provides a hint that the section
should be re-factored for reuse.
If you know how to refactor it then just go ahead.
If you have doubts about how to refactor it, try to do your best and mark
the section as tech-debt.
As more use cases are gathered, you should have a better understanding of
the requirements and refactor it in a better way.
The tech-debt marker will inform the person which tries to re-use that code
for a 3rd or 4th use case not to try too hard to create his code to work
with the existing re-usable component, but to consider refactoring the
re-usable component itself so that it provide a clean re-usable API.

We are not blocking a release due to tech-debt.


Shared code and refactoring for code reusal
===========================================

While working on a task you might identify a piece of code which you think 
might be reused at a later time with a future feature.

Based on the principle of not coding for things that you don't need yet,
don't try to implement interfaces or decorators just yet.

Implement your current task using the simplest method you can think of.

If you have an idea about how the code might be refactored for reusal, just
create a ticket (an maybe a FIXME marker) and describe the design.

You will need at least 2 other places from which a code is reused to assert
the quality of an interface / shared code.
It is better to wait for more real use cases before designing a shared code.


FIXME Markers
=============

We use the `FIXME:1234:` marker to signal and acknowledge a section of code
which was created as tech-debt.
We will leave the tech-debt unpaid and will try to pay it next time we hit
an issue with that section of code.

Only use **FIXME** markers followed by ticket ID.
Don't use TODO or other markers.

Technical debt comments will always have an attached ticket ID and will use
the following format.
Comments will come on new lines.
Adapt this to the style of comments used in the specific language::

    # FIXME:1234:
    # Details about this tech-dept. Ex: Can only be fixed when full moon.

    /* FIXME:1234:
    Some other type of syntax.
    */


The comment should be descriptive enough so that when you are
reading the code while working on your task it will help you decide whether
to go look for the details of the ticket or just ignore it, as it is not related
to what you are doing now.


Happy Hacking Day
=================

One day each month is reserved for working on whatever task you want.

This is called the 'Happy Hacking Day' or 'I work on whatever I want day'.

This is the first Wednesday of each month.

The idea is that we always have top priority tasks on which we work on a regular basis.

This is why minor/small tasks will never get top priority.

If there is a minor/small task which has a big impact on our day to day work,
we can work on in in that day.

Tickets that can be done in this day can be tagged with the **happy-hacking**
keyword.

Tickets started during happy hacking day,
can be continued in the following days in order to be completed.

Things that can be done in this day:

* work at improving our tools
* improve the way we work to make it easier and more fun
* fixing small technical debts, code cleanup, renaming... etc
* push or send upstream your local changes to open source projects
* fix a bug in an upstream open source project.

After each hacking session, please send email feedback to the team to talk
about what you have done.

If you cannot participate on the day, you can use another day to work on the
Happy Hacking session.


References
==========

* http://c2.com/cgi/wiki?TechnicalDebt
* https://en.wikipedia.org/wiki/Technical_debt
* http://martinfowler.com/tags/technical%20debt.html
* http://ronjeffries.com/categories/technical-debt/
* https://sites.google.com/site/unclebobconsultingllc/a-mess-is-not-a-technical-debt
