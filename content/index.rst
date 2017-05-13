Overview
########

:menu_order: 0
:url: /index.html
:save_as: index.html

These pages are a guide for working on the Chevah project. They include programming
style guides but also notes about working on the project as a whole. The content might
be nitpicking, but we hope that by following these guide lines
you will find it easier to collaborate and improve the quality of your code and work.
Please note that these guides are continuously updated according to the latest
best practices.

::

  Simple things should be simple and complex things should be possible (Alan Kay)

Overall rules of the project
============================
* Based on Kay's idea, the project should fit simple needs but also be able to scale for more complex usage.
* **Read the coding conventions** applied for this project under `Generic`_. This set of general coding conventions should be valid for all 'texts' (code, documentation... etc) written for this project. There are also specific rules that apply to languages used by the project. You should start by reading the general coding conventions and then read each language's specific convention as you need to write in that language.

* **We use Skype for phone calls and meetings**. Please create a dedicated Skype account in the form of "NAME.SURNAME.proatria" to collaborate with the team. Also, please note that Skype has no feature to discover team members at once, so you will have to manually add your contacts.

* **Make sure you are connected to IRC** on the #chevah channel while you are "at work". Set it to *autoaway* to let others know that you are not at the computer. Set it to *busy* if is are working at something and don't want to be disturbed.

* **Each task you are working on, should have a ticket in Trac**. If there is no ticket, create one and start the Ticket Work Flow (see `Tickets`_).

    * The tickets corresponding to you, that you are currently working on, should have the 'owner' value set to your Trac username.
    * If a task requires more than two days of work, split the task in multiple tickets each requiring no more than 2 days to complete. Occasionally, check the Trac timeline to stay up to date with latest changes in the project.
    * When starting a support ticket, always ask for the operating system version architecture used, as well as the version of the SFTPPlus products. Check the `template`_ used for initiating a support request.
    * Add your preferred email address in Trac ( Preferences -> General ) to enable email notifications.

* **A Pull Request can be closed** only after it has been **reviewed** by at least one other member of the team. See `Review`_ for details.
* **Leave days** can be requested at any time. Check the `Leave/Holiday`_ page. There is also a `spreadsheet`_ to mark your days and see who's off.

* **Update your GitHub account** to display your full name and avatar/picture. You don't need a photo of your face, just make sure you are not using the default image as this will help identify your activity.

* To compensate for the **usage of your own hardware for work** related tasks we will cover hardware expenses as needed. Also if you need any hardware component or peripheral that will help your work related tasks, just ask and we will be happy to cover those expenses. Ask the tech lead for details.


We consider that debates over these guides are not pointless. At the same
time, it is hard to agree on a universal style guide, and we don't
expect that everyone will agree with the rules stated here.
If you have any comments or suggestions, please get in touch with us over email,
or by adding an issue or pull request on
`Github`_.

We try to automatically check software development rules using `pocket-lint`_.

This is a collection of programming craftsmanship recommendations and ideas, so
please let us know if we fail to properly cite the source.

.. _Generic: http://styleguide.chevah.com/generic.html
.. _Tickets: http://styleguide.chevah.com/tickets.html
.. _template: http://styleguide.chevah.com/tickets.html#support-tickets
.. _Review: http://styleguide.chevah.com/review.html
.. _Leave/Holiday: http://styleguide.chevah.com/leave-holiday.html
.. _spreadsheet: https://docs.google.com/spreadsheets/d/11N3Zakrz0xQZ4Z_vPQxcdeOGK122136cx2PD4YPfels/edit#gid=1
.. _pocket-lint: https://launchpad.net/pocket-lint/
.. _Github: https://github.com/chevah/styleguide
