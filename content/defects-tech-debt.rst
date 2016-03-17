Bugs and Tech-Debt
##################

:menu_order: 100

.. contents::


General
=======

As with any other product, our ideal is to release a product without any
known defects and with optimal implementation.

While this is a noble goal, achieving it might not be economically feasible.
That is creating a zero bugs product will result a product which costs more
than the customers are willing to pay for.


Defects and Release Blockers
============================

Defects are defined as behavior of our product which does not follow our
specification or the way we want it to work.

Mis-behaviors in our build system, testing system or infrastructure are also
defects.

We split the defect into 3 categories:

* `bugs with priority high or critical` - are defects which affect
  (or we thing that it might affect) the workflow of at least one customer
* `bugs with priority low` -
  are defects for which we are not aware of any affected customer
  but which we would like the product to not behave in this way.
  They are acknowledged in the **Known Issues** section of our documentation.
* `tasks with priority high or critical` - are defects affecting our build
  system or testing infrastructure, but are not defects in the actual
  product.

For some defects, fixing them is a lot of work and its impact is minor
as maybe our customers will never use the product in a way to trigger the bug.
In this case, we create a ticket with type `bug` and add it in the backlog.

All defects which affect the work-flow of at least one customer are
considered top priority and will **block the release**.

All defects which are present in a release **should** be acknowledge in the
documentation.

If we gather a considerable number of minor bugs / defect we will schedule
a release dedicated / focused on reducing their numbers.

We should focus on fixing all bugs as soon as possible. Even if a defect does
not currently affect a customer, the changes are high that a customer
will be affected by it in the near future.

In the same small/minor bugs might release big flaws in the structure of our
code. We should focus on fixing them as soon as possible so that we can work
on them in a normal pace and not wait to fix them in a hurry under the
pressure of a release blocker or customer complaining about bad behavior.


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

If you go for *the former* method you will generate a *tech-debt*.

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
with `tech-debt` when we talk about our code. I was not able to find a better
metaphor so for now we are stuck with this term.

We are not paying tech-debt in dedicated sprints or releases.

Please read the `Refactoring - Not on the backlog!
<http://ronjeffries.com/xprog/articles/refactoring-not-on-the-backlog/>`_
article by Ron Jeffries.

We use the `FIXME:1234:` marker to signal and acknowledge a section of code
which was created as a tech-debt.
We will leave the tech-debt unpaid and will try to pay it next time we hit
an issue with that section of code.

Sometimes your experience tells you that a section of code is not right and
that it can be implemented as re-usable section.
When you only had one use case for that code is very hard to create a
generalized / re-usable version and something trying to do that is wrong as
you most probably ain't gonna need that.
Then it comes the second use cases which provides a hint that the section
should be re-factored for reusal.
If you know how to refactor it then just go ahead.
If you have doubts about how to refactor it, try to do your best and mark
the section as tech-debt.
As more use cases are gathered you should have a better understanding of
the requirements and refactor it in a better way.
The tech-debt marker will inform the person which tries to re-use that code
for a 3rd or 4th use case not to try to hard to create it's code to work
with the existing re-usable component, but to consider refactoring the
re-usable component itself so that it provide a clean re-usable API.

We are not blocking a release due to a tech-debt.


References
==========

* http://c2.com/cgi/wiki?TechnicalDebt
* https://en.wikipedia.org/wiki/Technical_debt
* http://martinfowler.com/tags/technical%20debt.html
* http://ronjeffries.com/categories/technical-debt/
* https://sites.google.com/site/unclebobconsultingllc/a-mess-is-not-a-technical-debt
