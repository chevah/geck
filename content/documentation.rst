Documentation
#############

:menu_order: 101

.. contents::


General
=======

General introduction about why we want documentation, how the documentation
is presented

talk aboud different documentation formats and different audiance


Marketing / Promotional Materials
=================================

Targeted to all users.

Presented on our website and promotions/marketing materials

Should be as generic and non-technical as possible


Narrative documentation
=======================

Split each idea in its own paragraph.

Describe the 2 styles of narrative documentation which we use

Technical Documentation
-----------------------

targeted to technical users, but should also be accesible to less techinical
users, once they have followed a user guide

used to describe each configuration option and its 
used for example to describe in details our REST API
comments in sample files


User Guides / Knowledge Base
----------------------------

targeted to less technical users

used to describe how task X can be performed by applying varoius configuration
options

used to contain answers to common/frequent questions so that the support
team can direct users to a doc page


Release Notes
=============

move info from /release-process.html#release-notes


talk about how release notes should be written.
that they should only talk about public things API / interaction

that for bugfixes they should describe what was wrong and how it was fixed.

that they should sort the notes into sections:

* new features
* bugfixes
* removals/deprecation

that security related issues should be highligted or taged for easy filtering
that bugfixes should have an internal bug id


Known Issues
============

Similar to release notes, why we need them and what is the style in which
they should be written

they should have reference to internal issues

maybe info about workarround

maybe info about when a fix is expected


Docstrings
==========

targeted to developers and dev team members

Talks about the general style for the docstring

Both production and test code docstring. Talk about the purpose of each string.
