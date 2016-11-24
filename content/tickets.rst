Tickets
#######

:menu_order: 100

.. contents::


General
=======

This page talks about how we manage the tickets/issues/tasks/defects.

For now we are using Trac for managing tickets.

We would like to use GitHub issues, but for now it is too simple for our needs.

**When working at something, that something should have an associated ticket in Trac.**

A Trac ticket is opened when some work needs to be done, a problem is found or someone has an idea about a new feature or how to improve something.

The ticket workflow is described in computer friendly manner here: https://gist.github.com/adiroiban/c1991d524cc5e14d27b4

Try not to upload attachments to the ticket.
When we migrate away from Trac we find it difficult to migrate the attachments.

* For text file, try to use the descriptions... or create a dedicate wiki page.
* For logs, errors... etc use gist.github.com .
* For pictures and other non/text data... I don't know, just attach it.

Is ok to attach screenshots as a last resort but alway try to describe the issue so that the screenshot is not required and that you can report a text log or text error.

When you start working at a task, you can optionally accept that task and the task will be considered 'in work'.
At any given time, a team member should not have more than 3 in work tickets.


Work priority
=============

Below is the list of priority order for work items. Top of the list is top priority:

 * Critical tickets should be solved first.
 * Support tickets. It is known that nobody likes them, but keeping customers happy is one of our main goals, and apart from that, support contracts are covering a bit part of our income.
 * Your ticket that pass the review and require to be merged.
 * 'Need review' tickets that requires your review.
 * Your ticket that did not pass the review.
 * Bugs for active milestone
 * Tasks from active milestone with 'High' priority.
 * Task from active milestone with 'Normal' priority.
 * Any other ticket from 'Important' report.
 * If you ran out of tickets, you discuss with the team to assign a new ticket or to add a new ticket to the current milestones.


Support tickets
===============

THIS SECTIONS NEED EXPANSION.

Tickets related to support issues should contain the following information in description::

 * The customer name
 * Affected products
 * Version of each affected product
 * Operating system version and architecture


Bug / Defect reporting
======================

We have multiple bug levels:

1. Those found after a need-review request, but before the code
   reaches the master. Developer to get full blame.

2. Those found in master, but not in a release. Developer and
   Reviewers get internal team blame.

3. Those found in a release version.  Developer and Reviewers get the
   blame, product get public blame.

Level 1 are reported as review comments and needs-changes and they don't need separate bug reports.

Level 2 are reported as bug tickets with high priority and assigned to the in work milestone,
as they should be fixed ASAP. They are also release blocker.

Level 3 can be reported by QA or support team.
QA team will report them just like Level 2 bugs. The developer who analyze the bug and find that it is a Level 3 bug, will mark it as bug
set priority to **critical**.

Support team ca also report level 3 bugs, after receiving a report from the customer and reproducing it.

When closed, Level 3 bugs will also have an associated release note.


Ticket details
==============

Ticket triage
-------------

Read Launchpad Bug Triage page for some general things: https://dev.launchpad.net/BugTriage

In Trac, we do not allow external parties to add tickets, so we do an initial triage process in the same time when we add a bug (we choose component, priority... and sometimes milestone)


Ticket types
------------

 * Task - are the usual/normal internal tickets.
 * Story - User stories - are high level task describing features that we want for our product
 * Bug - are defects detected by us or by users.


Assigning priorities
--------------------

In Chevah tickets usually have a priority value of '''High''' or '''Low '''. All tickets that are '''undecide''' should get a Low priority. Critical are for very special cases when someone is dying and we can help with an action in the next days... otherwise the priority for such cases can be '''High'''.

When we ran out of '''High''' priorities we can re-evaluate tickets with '''Low''' and change some of them to '''High'''.


Ticket keywords
---------------

We don't use free form keywords or tags for tickets. Only set keywords is really required.
Below is a list of in used tags:

 * **tech-debt**

  - Any task that should have been done in the past, but was postponed
  - Technical dept should be 'payed' as soon as possible since the longer it takes to 'pay' them to bigger is the cost.
  - For more information about the subject start by looking here: http://en.wikipedia.org/wiki/Technical_debt


 * **easy**

  - These are task that require no advance knowledge of the product or advance operating system know-how.


Milestone planning
==================

At the start of each cycle, we create a milestone or a sprint that represent our focus for the next month or week. We add new tickets to the new milestone or move tickets from 'Horse's Easter' milestone.

Until the all tickets from the milestones/sprint are not done, we should not work on any other task/ticket. If we start working on something, that something should be added to the current milestone.

If new tasks/tickets are required, they are discussed with the team and if they are important they are added to the current milestone. If the milestone is already full, adding a new ticket might imply removing an already planed ticket.


How to not be turned down by the big amount of opened bugs ?
------------------------------------------------------------

In the Chevah project, we add a bug for each action we consider should be done to improve the project state.

Adding a ticket is easy and quick, while closing a ticket is hard and slow :) This will cause the accumulation over time of a big number of opened tickets.

To help focus and get things done Adi Libotean created a nice "My Tickets" report: https://trac.chevah.com:10443/report/7

That report is your friend. Please suggest any improvements.


Horse's Easter and Near Future
------------------------------

'Horse easter' milestone is used for all long distance tickets. Many if the ticket will be added to 'horse easter' milestone at creation time.

You don't need to bother about these tickets and most of the time they can be ignored.

Same for 'Near future' milestones.
