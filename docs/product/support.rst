Support
#######

:menu_order: 009

.. contents::


Introduction
============

This page describes the guidelines for the support activities together with
best practices that were extracted based on our past experience with support
related activities.

The main point of contact for Support and liaising with customers
is via the Google Group email.


Template: Obtaining the installation detail
-------------------------------------------

The following is a template to obtain the installation detail.
Please modify the template below to suit.

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
	
	By knowing details about your installations, we can configure the test suite to run
	against a similar setup.

	This information will not be shared with any other third party and will be used
	solely for improving further support for you and development of the product.


Using the installation details
------------------------------

Once the installation details are provided, recreate the issue in a similar
environment.

This should be created via a dedicated VM for testing / support activities.


Chat
====

`Kayako <https://sftpplus.kayako.com/>`_ is used for chat with our customers
or possible customers.

A widget is added on the website.
A new conversation is created in Inbox when a visitor initiates the conversation.
A response is sent via the web platform.

Each conversation is assigned to an agent who handles that conversation.

Team notes can be created to share informatino but for faster response time
use IRC or to discuss with more than one person, send an email.

In a live conversation customers expect quicker response time than email.
If you need to spend more time, notify the customer or follow up via email.

Use the chat as an opportunity to gain quick feedback from the customer about
the scope of the issue.


Support Case Management
=======================


Working on a support case
-------------------------

Support cases can be received either through the online contact form,
messenger, direct email or phone call.

Email, messenger and support forms are the preferred methods.
For call, request the customer at the beginning to do a follow up over email
and confirm in writing as the first preference.
As second preference, follow up with a summary of the call and request the
customer to confirm the details.

When a support case is started, obtain and collate as much information as
possible.
This will help in potential follow-up with the rest of the Support team.


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


Escalating a Support Case due to defects
----------------------------------------

If the support case leads to finding a defect or it needs to be escalated,
a Trac ticket should be created with details of the customer.

For the defect, create a Trac ticket with priority High and notify the
customer of the Trac ticket ID so that they can follow up with Support on the
issue.


Holding a screenshare session
-----------------------------

GoToMeeting can be used to conduct a screenshare or meeting session with the
customer if the issue is best resolved via screenshare.

