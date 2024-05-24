Onboarding
##########


Introduction
------------

This page is used to organize tasks and track the onboarding process for new members.
You can see past/active tasks in the `onboarding repo <hhttps://github.com/chevah/onboarding/>`_.

**Things to note and do:**

- You can use your personal accounts.

- Initially your GitHub account is only part of the onboarding team with limited access to resources.

- Ask one of the system administrators to add your email to our groups / mailing lists.

- During onboarding, please ask for weekly meetings with your onboarding supervisor and send corresponding calendar invites.

- Be connected to IRC on #chevah while you are "in the office".


1. First stage
--------------

**Create the Github milestone**

To practice your GitHub issue management skills, create your milestone as 'YOUR-NAME Onboarding' in the chevah/onboarding repository and create the initial tickets associated with your onboarding project.

Below is a list of initial issues/tasks to be added in the milestone:

**Review and provide feedback for chevah/geck**

- geck is at http://geck.chevah.com/

- Comments/suggestions can be added in the ticket.

When submitting repo changes based on your feedback:

- Clone the repository, create a new branch and modify the file/s with your changes.

- Create pull requests (PRs) with these changes. 

- Use the `Github PR template <https://github.com/chevah/geck/blob/463556d4e9219e28fd030759ba7af9c0a3ec89e6/.github/PULL_REQUEST_TEMPLATE>`_ and @ mention the oboarding supervisor for review.

**Review and provide feedback for the software**

- Obtain the trial version of the server and client.

- You can choose whichever OS to trial the product in.

- Follow the installation in the documentation.

- Any issues or comments can be mentioned in the Milestone tickets.


**Review and provide feedback for the website.**

- Review the website excluding the documentation.

- Comment in the Milestone your feedback.

When submitting repo changes based on your feedback:

- Clone the repository and create PRs to the right repo.

- Follow the README requirements and development to run the site locally.

- Use the PR template and @ mention the onboarding supervisor for review.

- Please take note of the README in the repo for additional requirements.


For any of the tasks above, feel free to check existing or previous milestones for ideas on scope and approach.


2. Know the basic rules
-----------------------

We have basic requirements and practices when working for the Chevah project.
Ask the tech lead for any questions.

* Take note of the `coding conventions <http://geck.chevah.com/>`_ applied for this project. These general coding conventions are for all 'texts' (code, documentation, etc).

* There are specific rules that apply to programming languages.
  Begin by reading the general `styleguide <http://geck.chevah.com/en/latest/styleguide/index.html>`_.
  Then review each language specific convention as you will be writing in that language.

* While you are in IRC on #chevah "in the office", set to auto-away to let others know that you are not at the computer.
  Set the away status to "busy" (/away busy) if you are working at something and don't want to be disturbed.

* You will use your own hardware for work tasks.
  To compensate for this usage of your hardware we will cover hardware expenses for your home computer.
  If you need a hardware component or peripheral that will help your work related tasks, ask and we can cover those expenses.
  Ask tech lead for details.

* Each task that you are working on should have an associated Issue in a Github repo from Chevah org.
  If there is no ticket (issue), create one and start the `Ticket Work Flow <http://geck.chevah.com/en/latest/product/tickets.html>`_.

* Tickets corresponding to you that you are currently working should have the 'Assignees ' value set to your Github username.

* If a task requires more than two days of work, split the task in multiple tickets each requiring no more than 2 days to complete.

* When starting a support ticket, request the OS version architecture used and version of the products.

* Before a Pull Request is closed, it must be approved by at least one other team member.
  Further info of the `Review process <http://geck.chevah.com/en/latest/programming/review.html>`_.

* Leave days can be requested at any time.
  :doc:`Check the dedicated page.</office/leave>`

* Update your GitHub account to display your full name, and an avatar/picture that is not the default image to help differentiate activity.


3. Get all your accounts after the initial stage
------------------------------------------------

Once the initial onboarding state is over, you will get full access to the project's resources.

The initial stage is over when all the Onboarding tickets from the milestone dedicated to your onboarding process are finalized.

We are far from single-sign-on and while working on this project you will have many different accounts.

We use Skype for phone calls.
Use the dedicated Skype account as the official tools to collaborate with the team and to make phone calls.

**Ask our system administrators for all of the followings:**

* A project-related email account on Google - enable 2-step auth.

* Update the email account with the standard signature template from the private wiki for all support related emails.

* System administrators will require a chevah.com account as alerts are delivered through the management server.

* Request for VPN certificates to connect to internal servers/services.

* You will need a GitHub account associated with Chevah org.
  Create a personal GitHub account and ask a team member to add you to the Chevah org.

* Get to know the team by checking the dedicated page in our private wiki.


4. Exploring SFTPPlus for the first time
----------------------------------------

When testing out the software, please take a look at the contents of these folders as it may contain useful files for exploring various features of SFTPPlus.

Test_Data
^^^^^^^^^

In the server repository is a folder called test_data which contains configuration file samples, public/private key samples, various certificates in a number of formats, a test LDAP server to support manual tests ( run as $ ./build* test_data/ldap/server.py), HTTP proxy and simpel HTTP server, and sample execute scripts for post transfer execution.

Users_Files
^^^^^^^^^^^

In the build folder are example folders of a test user which can be used to help test various features of SFTPPlus.

Below is an example of using users_files / the test user to access the HTTPS feature:
>>>>>>> master:docs/office/onboarding.rst

* Get to know the team by checking the dedicated page in our private wiki.
