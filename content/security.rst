Security
########

:menu_order: 010

.. contents::


Overview
========

The following is more of a public-facing overview or a process rather than focusing on the step-by-step portion of security. 

The focus is on the human-side of security with some suggestions of tools and tactics.


Onboarding
==========

When onboarding a team member, they will have limited access to Pro:Atria's infrastructure until such a time arrives when further credentials can be provided.

There may instances when certain items are shared to the onboarding member's non-Pro:Atria address or accounts.
Once a member is part of the team all use of services / apps related to Pro:Atria will need to be switched into Pro:Atria emails.
For example, if your personal email was added in the Google Analytics account during onboarding, please ensure that your personal email address is replaced by the new Pro:Atria email address.


Accounts
========

**Enable multi factor authentication in Gmail.**

Use a hardware key (Yubikey) or mobile, as long as there is 2FA (two-factor authentication) involved.

Enforcement: Go to the list of accounts in the organization and see which one has 2FA.  If the account does not have 2FA enabled, contact the account holder.

**Enable multi factor authentication in Github**

Idea: Enable this in Github settings - can use mobile device, hardware key, downloadable codes, etc.

Enforcement: The Google organization owner/administrator can see who has MFA (multi-factor authentication).
If MFA is not enabled, contact the account owner to re-enable.


Testing / validating third party apps / software for use
========================================================

If an app is in active use with customers / within the team during the validating period, ensure that whitelabeling takes place to help validate/verify that it is an Pro:Atria-used third party product.
