Support
#######

:menu_order: 009

.. contents::


Introduction
============

This page briefly describes Support details.

For access to any of the Support platforms, please contact the Support team.

For the full details on the Support offering, please go to the website at 


Helpdesk
========

Each message to the Support email starts a helpdesk ticket in Freshdesk.

The helpdesk software is currently under evaluation.
Currently the main point of contact for Support and liaising with customers
is via the Google Group email.


Template: Obtaining the installation detail
-------------------------------------------

Can you please provide us with the following details about the system used for running the SFTPPlus Server or Client:

.. sourcecode:: rst

	 * SFTPPlus Server or Client?

	 * SFTPPlus product version?

	 * If Server – do you also use WebAdmin?

	 * Operating system name?

	 * Operating system version?

	 * CPU architecture?

	 * File transfer protocol(s) used?

	 * Is this installation part of a resilience/redundancy/high availability architecture?

	 * Other information (if known). Please advise brief details of any
	 integration, software, security or other technologies that interact
	 with SFTPPlus products. e.g. Firewalls, Proxy, LDAP, Active Directory,
	 Single Sign On, Management software etc

	Before releasing a new version of SFTPPlus products or any fix, we run
	an automated test suite to validate new features and check for
	regressions. By knowing a few details about your installations we can
	configure the test suite to run against a setup similar to your
	installation. This information will not be shared with any other third
	party and will be used solely for improving further support for you and
	development of the product.


Using the installation details
------------------------------

Once the installation details are provided, recreate the issue in a similar
environment.

Access the buildslave page of the OS to obtain the IP address and SSH into
the IP.

Download the initialize the SFTPPlus version that is the same as the customer's
and initialise.  Do not test with the buildslave version.


Knowledge Base
==============

Currently the main knowledge base is in documentation - both on the website
and in the internal documentation pages supplied with each package.

A separate knowledge base is currently under evaluation.


Chat
====

`Olark <https://www.olark.com>`_ is currently used for chat.

Each chat transcript is forwarded to the Support email list and subsequently
creates a new ticket in the helpdesk.


Licenses and support contract
=============================

See the `Support options page <https://www.sftpplus.com/support/options.html>`_
which describes what options are available.
If a support request goes beyond the standard option (such as a new
product feature), the Sales team will determine the quote.

See the `Life cycle page <https://www.sftpplus.com/product/life-cycle.html>`_ 
for details about the product life cycle.

If a feature request is obtained, check that it is included in the
`Product roadmap <https://www.sftpplus.com/product/roadmap.html>`_ 

License information is available from Sales team to check if a customer
has an existing Support license.


Support Request Management
==========================


Logging a support request
-------------------------

Support requests can be received either through the online support form,
direct email or phone call.

Email and support forms are the preferred methods.
This is due to the possibility of miscommunication that can happen in a
phone call.

Support requests can be logged by partners, customers or the Support team.

When a support request is logged by a customer or partner, an email is sent to
the support team.

When one of the members of the support team logs a support request, he/she
should consider obtaining and collating as much information as possible,
ensuring that any of the support team members can pick up the SR at any time
without recourse to the owner.

All files related to a support request should also be available in the SR
system.


Initial Assessment
------------------

When a new support request is logged it should receive a response within the
same or next business day.

The SR will be allocated to an Owner, who should do the initial assessment:

* Verify all details logged against the call, checking what additional
  information is required;

* Make initial contact with the originator, acknowledge that we have receive
  the request;

* Verify understanding of initial information provided;

* Ask for additional information if required and/or provided initial diagnosis;

* If more time is needed before providing an answer, inform about the
  approximate time.

If a customer asks for multiple support questions in a single email, it is
better to respond in multiple emails, creating a new ticket for each email.


Managing a Support Request 
--------------------------

Once a ticket has been responded, close the ticket (a notification will not be
sent to the customer).

The ticket will re-open when the customer responds.

Do not close the ticket if the response is a 'holding' type of response.


Escalating a Support Request
----------------------------

If the owner of a SR is not be able to answer the issue raised by the customer
and they have gone through the additional steps to obtain more information,
they can discuss the issue within the Support team.

This is especially the case if the issue is on legacy software, customized
software (ie a new module was created for the customer only), or it is a
potential defect in the software.

The ticket holder is still the owner.

When escalating an SR to the development team, a new Trac ticket should be
created with details of the customer and link to the helpdesk conversation.

Each support request should have an unique ID which will be the Trac ticket ID
associated with this support case.

Depending on the urgency of the SR, the development team should address the
issue, investigate and provide feedback/fix.

If a defect is found, create a ticket in Trac with priority High and notify the
customer.


Holding a screenshare session
-----------------------------

GoToMeeting can be used to conduct a screenshare or meeting session with the
customer if the issue cannot be solved via email.

Please contact the team to create a schedule or for access to GoToMeeting.

