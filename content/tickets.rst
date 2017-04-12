Tickets
#######

:menu_order: 005

.. contents::


General
=======

This page talks about how we manage the tickets/issues/tasks/defects.

For now we are using Trac for managing tickets.

We would like to use GitHub issues, but for now it is too simple for our needs.

**When working on something, that something should have an associated ticket in Trac.**

A Trac ticket is opened when some work needs to be done, a problem is found or someone has an idea about a new feature or how to improve something.

The ticket workflow is described in a computer friendly manner here: https://gist.github.com/adiroiban/c1991d524cc5e14d27b4

Try not to upload attachments to tickets.
When we eventually migrate away from Trac, we may find it difficult to migrate the attachments.

* For text files, try to use the descriptions or create a dedicate wiki page.
* For logs, errors, long code samples from test reviews, use gist.github.com.  
* For pictures and other non/text data, you can attach these.

It is ok to attach screenshots as a last resort but always try to describe the issue in a way where the screenshot is not really required and where you can report a text log or text error.

When you start working at a task, you can optionally accept that task and the task will be considered 'in work'.
At any given time, a team member should not have more than 3 'in work' tickets.

When creating a ticket you can set yourself as the owner if you are implementing the task.


Work priority
=============

Below is the list of priority order for work items. Top of the list is top priority:

 * Critical tickets should be solved first.
 * Support tickets. It is known that nobody likes them, but keeping customers happy is one of our main goals, and apart from that, support contracts are covering a big part of our income.
 * Your ticket that passes the review and requires to be merged.
 * 'Need review' tickets which require your review.
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
QA team will report them just like Level 2 bugs. The developer who analyzes the bug and finds that it is a Level 3 bug, will mark it as a bug and set it's priority to **critical**.

Support team can also report level 3 bugs, after receiving a report from the customer and reproducing it.

When closed, Level 3 bugs will also have an associated release note.


Ticket details
==============

Ticket triage
-------------

Read Launchpad Bug Triage page for some general information: https://dev.launchpad.net/BugTriage

In Trac, we do not allow external parties to add tickets, so we do an initial triage process at the same time when we add a bug (we choose component, priority... and sometimes milestone)


Ticket types
------------

 * Task - are the usual/normal internal tickets.
 * Story - User stories - are high level tasks describing features which we want for our product
 * Bug - are defects detected by us or by end users.


Assigning priorities
--------------------

In Chevah tickets usually have a priority value of '''High''' or '''Low '''. All tickets that are '''undecided''' should get a Low priority. Critical are for very special cases when someone is dying and we can help with an action in the next days... otherwise the priority for such cases can be '''High'''.

When we ran out of '''High''' priorities we can re-evaluate tickets with '''Low''' and change some of them to '''High'''.


Ticket keywords
---------------

We don't use free form keywords or tags for tickets. Only set keywords are really required.
Below is a list of used tags:

 * **tech-debt**

  - Any task that should have been done in the past, but was postponed
  - Technical debt should be 'payed' as soon as possible since the longer it takes to 'pay' them, the bigger the cost is.
  - For more information about the subject start by looking here: http://en.wikipedia.org/wiki/Technical_debt


 * **easy**

  - These are tasks that don’t require knowledge of the product or operating system 'know-how' in advance.


Ticket components
-----------------

Components and their explanations:

 * client-commons
 * client-ftp
 * client-http
 * client-ssh
 * component not set
 * gateway
 * infrastructure
 * libs
 * manager
 * pr (I think this is website/marketing related?)
 * server-commons
 * server-ftp
 * server-http
 * server-ssh
 * support (also includes documentation, anything that involves information to the customer)
 * webadmin


Milestone planning
==================

At the start of each cycle, we create a milestone that represents our focus for the next month or week. We add new tickets to the new milestone or move tickets from 'Horse's Easter' milestone.

Until the all tickets from the milestones/sprint are done, we should not work on any other task/ticket. If we start working on something, that something should be added to the current milestone.

If new tasks/tickets are required, they are discussed with the team and if they are important they are added to the current milestone. If the milestone is already full, adding a new ticket might imply removing an already planed ticket.

Usually, milestones are set to next-release, followed by Y-Near-Future, Z-Long-Term.

Milestones associated with a release are also included.


How not to be turned down by the big amount of opened bugs ?
------------------------------------------------------------

In the Chevah project, we add a bug for each action we consider should be done to improve the project state.

Adding a ticket is easy and quick, while closing a ticket is hard and slow :) This will cause the accumulation over time of a big number of opened tickets.

To help focus and get things done, Adi Libotean created a nice "My Tickets" report: https://trac.chevah.com:10443/report/7

That report is your friend. Please suggest any improvements.


Horse's Easter and Near Future
------------------------------

The 'Horse easter' milestone is used for all long term tickets. Many of the tickets will be added to this milestone at the time of creation.

You don't need to bother about these tickets and most of the time they can be ignored.

Same for 'Near future' milestones.


Story Tickets
-------------

See https://trac.chevah.com/ticket/3391 for an example of a Story Ticket.

Use this to list out smaller tasks associated with a larger task, such as the "Add WebDAV client" ticket.

This may be a good ticket type to use if you are carrying out a high level task and need to keep track of notes on Trac...
