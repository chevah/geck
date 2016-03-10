GitHub and Trac integration
###########################

This page discuss the integration between GitHub and Trac tracking
system.

..  contents::


General
=======

The repository
`github-hooks-server <https://github.com/chevah/github-hooks-server>`_
contains the code responsible for handling GitHub hooks and
applying changes to Trac tickets.


Usernames
=========

If your usernames for GitHub and Trac differ, the handler needs to map it.
Please check `handler.py
<https://github.com/chevah/github-hooks-server/blob/master/chevah/github_hooks_server/handler.py#L18>`_
for details.


Triggers and hooks
==================

The integration is mainly between GitHub Pull Requests and Trac tickets,
following the workflow described in `review <{filename}/review.rst>`_.

The Pull Request title should start with **[#TRAC_TICKET_ID]** and
each message on this Pull Request triggers a hook looking for special keywords.

On Pull Request body
`````````````````````
- reviewers: @username1 @username2

Sets which users need to review and approve this Pull Request


On comments
```````````
- needs-review

Issues a review request modifying the state of the Trac Ticket to needs_review.

- needs-changes

Modifies the state of Trac Ticket to needs_changes, notifying the assigned user
that the Pull Request should be fixed and reviewed again.

- changes-approved

Approves the changes on this Pull Request. All reviewers must approve and
mark as changes-approved before the Pull Request can be merged.

When all reviewers use this keyword the ticket state changes to needs-merge.
