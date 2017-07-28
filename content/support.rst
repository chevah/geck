Support
#######

:menu_order: 009

.. contents::


Introduction
============

This page describes the guidelines for the support activities together with
best practices that were extracted based on our past experience with support
related activities.

For access to any of the Support platforms, please contact the Support team.

For the full details on the Support offering, please go to the website's
`Support options <https://www.sftpplus.com/support/options.html>`_ page.


Helpdesk
========

Each message to the Support email automatically crease a helpdesk ticket.

The helpdesk software is currently under evaluation.
Currently the main point of contact for Support and liaising with customers
is via the Google Group email.


Template: Obtaining the installation detail
-------------------------------------------

The following is a template to obtain the installation detail from a client.
Please modify the template below to suit the communications.

.. sourcecode:: rst

	Can you please provide us with the following details about the system
	used for running the product:

	* Product version?

	* Operating system name and version?

	* File transfer protocol(s) used?

	* Please send through a time-stamped version of the server-side log, and
	   if relevant, the corresponding client-side log.

	* Other information (if known).

	* Please advise brief details of any: integration, software, resilience / redundancy /
	high availability architecture, security or other technologies that interact with the
	product.
	e.g. Firewalls, Proxy, LDAP, Active Directory, Single Sign On, Management software etc.

	Before releasing a new version, we run an automated test suite to validate new features
	and check for regressions.
	
	By knowing details about your installations we can configure the test suite to run
	against a setup similar to your installation.

	This information will not be shared with any other third party and will be used
	solely for improving further support for you and development of the product.


Using the installation details
------------------------------

Once the installation details are provided, recreate the issue in a similar
environment.

This should be created via a dedicated VM for testing/support activities.


Chat
====

`Olark <https://www.olark.com>`_ is currently used for chat with our customers
or possible customers.

Each chat transcript is automatically forwarded to the Support email list.


Licenses and support contract
=============================

See the `Support options page <https://www.sftpplus.com/support/options.html>`_
which describes what options are available.
If a support case goes beyond the standard option (such as a new
product feature), the Sales team will determine the quote.

See the `Life cycle page <https://www.sftpplus.com/product/life-cycle.html>`_ 
for details about the product life cycle.

If a feature request is obtained, check that it is included in the
`Product roadmap <https://www.sftpplus.com/product/roadmap.html>`_ 


Support Case Management
=======================


Working on a support case
-------------------------

Support cases can be received either through the online contact form,
direct email or phone call.

Email and support forms are the preferred methods.
When we have a phone call, we request the customer at the beginning to do a
follow up over email and confirm in writing.

Support cases can be logged by partners, customers or the Support team.

When a support case is started, obtain and collating as much information as
possible, as this will help in potential follow-up with the rest of the Support
team.


Troubleshooting a Support Case
------------------------------

The `troubleshooting theory from CompTIA <http://certmag.com/guide-troubleshooting-theory-comptia-perspective/>`_ is a good overview when
troubleshooting a support case:

1. Identify the problem
2. Establish a theory of probable cause (question the obvious)
3. Test the theory to determine cause
4. Establish a plan
5. Determine system status
6. Make a record


Initial Assessment
------------------

When a support case is opened it should receive a response that it has
been received and a case open within the same or next business day.

The case will be allocated to an Owner, who should do the initial assessment:

* Verify all details logged against the call, checking what additional
  information is required;

* Make initial contact with the originator, acknowledge that we have receive
  the initial case;

* Verify understanding of initial information provided;

* Ask for additional information if required and/or provided initial diagnosis;

* If more time is needed before providing an answer, inform about the
  approximate time.

If a customer asks for multiple support questions in a single email, it is
better to respond in multiple emails.


Managing a Support Case
-----------------------

The helpdesk allows you to keep track of which support cases still need a
response.
Once a response is made, close the helpdesk ticket as to not accumulate
on the helpdesk dashboard.
When there is a response back to the customer, the helpdesk ticket will re-open.

If the support case is waiting on a developer (in the case of a defect
example), a Trac ticket should be created.


Escalating a Support Case due to defects
----------------------------------------

If the support case leads to finding a defect, a new Trac ticket should be
created with details of the customer and link to the helpdesk conversation.

For the defect, create a Trac ticket with priority High and notify the
customer of the Trac ticket ID so that they can follow up with Support on the
issue.


Holding a screenshare session
-----------------------------

GoToMeeting can be used to conduct a screenshare or meeting session with the
customer if the issue is best resolved via screenshare.
