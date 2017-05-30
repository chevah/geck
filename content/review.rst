Review
######

:menu_order: 003

This page will discuss the code/changes review process as both the person
who requests a review and a person who checks the review.
The review instructions are platform independent so they apply to tickets,
emails, pull requests, and to all tasks, not only to code reviews.


..  contents::


General
=======

* The goal of a review is to eliminate as many defects as possible,
  regardless of who "caused" the error.
  Branch driver and reviews work together to achieve this goal.

* The review process is a very efficient form of pair-programming.

* Branch driver is the person (or persons) requesting the review and
  responsible for implementing changes during the review.

* The reviewer is the person responsible for checking the code or changes.

* The Review Process is first class citizen of the Quality Assurance process.

* Each defect found during a review is an opportunity to improve the code.
  It is also a defect that a customer
  never sees and another problem that support doesn't have to spend time
  tracking down.

* The branch driver is responsible for getting his/her branch approved.
  In case a branch review is delayed, the branch driver should contact the
  reviewers and urge the review.

* While the main purpose of a review is to assert the quality of the changes,
  the review is at the same time a learning, growing, and communication
  experience.

* Try to observe good things from other team members and feel free to comment
  and let others know about how you think that things can be improved.

* Ideally you will have many small merge requests, because the bigger they
  get, the more costly they are - now and in the future.

* One merge request should do one thing only.

* The target for a small request is no more than 400 touched lines
  (added + removed).

* When you do a refactoring and you need to rename something in many files,
  do it in a dedicated branch which only deals with the renaming.
  This will help a lot with the review.
  Land your changes with the ugly names and then do a follow-up branch for
  the renaming.

* Feel free to submit as many merge requests as you can.
  The size of the merge requests can be an issue, but not their number :).

* Some reasons for keeping the merge requests small:

  * Large changes are much more likely to do many things.
  * It's harder to understand them.
  * It's harder to review them.
  * It's harder to inspect the main branch to find the merge that
    introduced a bug.
  * It's more likely to break the build.
  * It's harder to cherry pick code for backporting / supporting old releases.


For the person requesting a review
==================================

* Once a task/ticket is done, it should be submitted for review.

* **All** changes should be reviewed prior to being merged or released.

* Before requesting a review you should run a full quick test on your local
  computer and on all supported platforms.
  Just run ``paver test_quick`` and ``paver test_review`` and
  Buildbot and GitHub will work together to display the results.
  For documentation changes, run ``paver test_documentation`` for build errors
  and ``paver documentation_standalone`` to see the HTML build for potential
  formatting errors not otherwise caught.

* Before passing the review to others, take another careful look at your work
  and perform a first review yourself.
  Check that all changes are described together with their attached test
  cases.
  It is very important to have a good review request message as it will
  help reviewers understand what you have done.

* Check that all changes are covered by automated tests and if they aren't,
  make sure that the review description contains information regarding why.

* Check the **Reviewer's check list** since those are the things that a
  reviewer will check for sure.

* Before submitting a ticket for review, check that you have documented your
  work accordingly, for example in the affected repository documentation,
  Trac's Wiki, or the Styleguide.


* For Trac: A review request is created by adding the comment and then
  setting the state to 'needs_review'.
  (**don't use keywords**, we are using a strict ticket
  work-flow so use the ticket action form).

* For GitHub: A review request is created using **GitHub Pull requests**.

* When submitting a review for changes not planned in the current milestone,
  update the milestone to the current one.
  Don't leave the old milestone.

* You can start writing your review request as soon as you start coding on a
  branch.
  There is no need to wait for a feature to be fully implemented and
  for tests to pass.
  Writing a review request early, will help you organize and explain
  the work that you plan to do on the branch.

* When the review is ready to be sent to reviewers, leave a comment in the PR
  containing the **needs-review** marker word.
  It will trigger the review request process and the GitHub to Trac
  synchronization.

* GitHub inline comments are great, and you can add them to help with the
  initial review request.
  Just **don't abuse them**!
  Think twice before adding an initial inline comment for the review.
  Ask yourself why that comment is needed and why that line is not
  clear.
  Maybe adding a comment in the code would avoid the
  need for the GitHub inline comment.

* During a review, the reviewer might request changes.
  You can solve the request by either changing the code, or adding a comment
  with the reason why you don't want to change the code.
  After all requests are solved, leave a **new**, separate comment
  containing the keyword **needs-review**.
  This will let reviewers know that you are done and that
  they can check the latest changes.

* Make sure that your review request message is always up to date with the
  latest changes.
  If new changes are made or new test cases are discovered during the review,
  don't forget to update the initial review request message to include a
  summary of these changes.

* The "How to test the changes" section should include **ALL** test cases
  done during the review.
  If a reviewer is following a test case not described in the initial request
  message, it should update the review message with the new test case.


Review request message
----------------------

When submitting a ticket for review, the review request should contain the
following message as described in `pull request template
<https://github.com/chevah/styleguide/blob/master/.github/PULL_REQUEST_TEMPLATE>`_:

* For GitHub review requests, **add the merge commit message as the pull
  request title**.
  The message should include the ticket ID number.
  Example of merge commit message::

      [#1234] What was done in this branch.

* The commit message should be on a single line and preferable under 100
  characters.
  The message should be a clearly articulated phrase, summarizing
  changes done in the branch.
  Further details about the changes can go in the release notes or review
  request body.

* Add the list of persons who should review the branch, using a
  line starting with **reviewers** and followed by GitHub names or each
  reviewer prefixed with **@**.

* If required, using **depends-on** marker, add the list of reviews on which
  this review depends and block the merge of this branch.


Merge your branch
-----------------

After the merge request and review was approved you need to merge your branch
into master.

After your review request was approved, you can send your branch to PQM
for automatic testing and merging.
Use the following command::

    paver pqm GITHUB_PULL_REQUEST_ID

The PQM will check your branch and if it passes all tests, it will be merged
and pushed to master.

If PQM is not enabled for the repo, you will need to do a manual merge.

When doing manual merge using git, use squash merge and don't use the
default commit message.
Here is a sample command for merging branch "1234-what-was-done"::

    git checkout master
    git merge --no-commit --squash 1234-what-was-done
    git commit -a -m "[#1234] What was done in this branch."

It is recommended to define a git alias for `merge --no-commit --squash`.

A merge commit should have a commit message, in the format::

    [#1234] What was done in this branch.


* **#1234** is the ticket number for this branch.
  It is used to get more details about branch work and review.
  It can also be used to associate a commit to a ticket / branch / review /
  task and check the history/story of that commit.


For the person reviewing the changes
====================================

* Aim for a code inspection rate of fewer than 300 – 500 LOC per hour.
  This does not apply to QA team members for which, reviewing changes is the
  main activity.

* Take enough time for a proper, slow review, but not more than 60–90 minutes.
  Take a big break between reviews.

* You should always spend at least five minutes reviewing code, even if it's
  just one line.
  Often, a single line or small changes can have major
  impact throughout the whole system, and it's worth the five minutes to
  think through the possible effects that a change could have.

* The only quality metric of good work / code is **WTF/s**.
  While doing the review you are encouraged to keep track of all your first
  contact / view / read impressions and report them in the review feedback.

* Follow the procedure recommended in the "How to try and test the changes"
  section, record environment and steps and results, and share them through
  a comment.

* In case of errors, leave a comment describing what tests were run, the
  exact steps you took and the actual results.

* If the work is good, you can request the code to be merged by the author
  by setting the state to needs_merge in Trac.

* If the work is good and the GitHub pull request feature was used, submit
  your review as 'Approve'.

* If no merge is required you can close the ticket as solved.

* If minor changes are required, and they are easy to fix, you can try to fix
  them.
  Commit the changes and approve the review at your revision.

* If changes are required, submit the review as 'Request changes' on Github
  and assign the ticket to the person who can make the required changes.

* Don't spend to much time on a review request if it is not clear enough and
  you don't know exactly what to do and how to test.
  This is a problem with the review request and you can 'Request changes'.


Reviewer's check list - Any Role
---------------------------------


* Is there a release notes entry for the changes?

* Are the changes documented?

* Are the new events documented?

* Are the removed events documented?

* Is the documentation updated?

* Does the documentation make sense?


Reviewer's check list - Developer
---------------------------------

* Do the **new** changes comply with latest styleguide?

* Does the code have automated tests for all the new code?

* Does the merge commit message describe what is done by this branch?

* Does the branch name starts with the Trac ticket ID.

* Do **all** tests pass? Does GitHub say that the branch is
  **Good to merge**?

* If there is no ``paver test_review`` for the latest code, you can
  either just reject the review, or trigger a test and wait for results.
  **Never** approve code that is not passing the tests.


Reviewer's check list - QA
--------------------------

* Does the new code perform as expected when running manual tests?

* Do the test scenarios from the review description make sense?
  Can they be executed? Successfully?

* Does the new end-user interaction with the GUI or CLI make sense and is easy to use?

* Are there any corner cases not described in reviews or not covered by
  functional tests?


Reviewer's check list - Support
-------------------------------

* Does the documentation contain old information that needs to be updated?

* Does the documentation makes sense to new and existing users?

* UX: Does the Local Manager make sense along with the text configuration?

* If it's a new feature release, does the information make sense to new
  users?

* Should there be an accompanying Users Guide? FAQ update? API addition?

* Should there be samples, screenshots available?

After a release:

* If a customer-requested feature is added or if a bug fix is made, who
  should be contacted to notify them of the new release?

* Are there further updates for non-Documentation related content, like the
  website or newsletter?


Overview of the GitHub and Trac integration
===========================================

The repository
`github-hooks-server <https://github.com/chevah/github-hooks-server>`_
contains the code responsible for handling GitHub hooks and
applying changes to Trac tickets.

Integration is mainly between GitHub Pull Requests and Trac tickets,
following the workflow described in `review <{filename}/review.rst>`_.

The Pull Request title should start with **[#TRAC_TICKET_ID]** and
each message on this Pull Request triggers a hook looking for special keywords.

When creating the Pull Request the special syntax **reviewers: @user1 @user2**
sets which users should review and approve it.
There is also **depends-on: review1 review2** which blocks this merge until
the reviews it depends on are done.

A comment mentioning **needs-review** issues a review request modifying the
state of the Trac Ticket to `needs_review`.

We have integrated Trac with the new GitHub PR review features.
You can use Github to 'Approve' or 'Request changes' to a PR.

When a reviewer submits a review with 'Approve', it marks the Pull Request as
good to merge.
If all reviewers listed in the Pull Request body comment,
the hook will change the ticket state to `needs-merge`.
