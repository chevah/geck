Security
########

:menu_order: 009

.. contents::


Overview
========

The following is more of a public-facing overview or a process rather than focusing on the step-by-step portion of security. We also have additional security requirements - sysadmin will utilize more stringent security, travelers will want to utilize more stringent travel security processes, developers will have secure coding practices etc.

The focus is on the human-side of security with some suggestions of tools and tactics.


Onboarding
==========

When onboarding a team member, they will have limited access to Pro:Atria until such a time arrives when further credentials can be provided.

There may instances when certain items are shared to the onboarding member's non-Pro:Atria address or accounts. Once a member is part of the team all use of services / apps related to ProAtria will need to be switched into ProAtria emails.


Work Environment
================

Secure settings all completely depend on the individual OS, hardware, usage etc.

We don't mention details of specific set up in this page but the following are some suggestions:

**Use disk encryption**

For Mac, use File Vault for full disk encryption. For Linux, use LUKS, etc. For Windows, use BitLocker, etc.

**Implement some form of isolation / containerization**

Try to isolate work from personal.  An example is isolating work-only materials within a dedicated encrypted disk image / encrypted file container.

**Use hardware authentication devices for authentication, e.g. the Yubikey or equivalents.** 

Possibly extend this for signing and encrypting/decrypting without exposing the private key, e.g. with the Yubikey Neo / Nano or equivalents.

**Harden web browsers**

Due to web applications being a large attack surface use secure extensions for browsing such as HTTPSEverywhere, ScriptSafe, NoScript, AdBlock.  

**Take stock of accounts that have access to your information and machines.**

For example, are there any accounts that can be deleted or archived?
Does the known_hosts file actually contain known hosts and not suspicious-looking hosts / impersonators?

**Harden SOHO (Small Office, Home Office) networks**

And/or consider connecting via a wired connection instead, or building/securing your own wireless network router.

**Use Github via SSH**

Rather than having to constantly reusing password, use Github via SSH.
Documentation at https://help.github.com/articles/connecting-to-github-with-ssh/


Accounts
========

**Enable multi factor authentication in Gmail.**

Use a hardware key (Yubikey) or mobile, as long as there is 2FA involved

Enforcement: Go to the list of accounts in the organization and see which one has 2FA.  If the account does not have 2FA enabled, contact the account holder.

**Enable multi factor authentication in Github**

Idea: Enable this in Github settings - can use mobile device, hardware key, downloadable codes, etc.

Enforcement: The Google organization owner/admin can see who has MFA.  If MFA is not enabled, contact the account owner to re-enable.

**Enable multi-factor authentication and valid back up** in other services used by SFTPPlus.


Email
=====


Enable S/MIME in Emails
-----------------------

There are free email certificates available.  

A list of S/MIME email certificates that you can use is at http://kb.mozillazine.org/Getting_an_SMIME_certificate

You can use the Comodo email certificate. To obtain a free email certificate from Comodo, go to https://www.instantssl.com/ssl-certificate-products/free-email-certificate.html and sign up to recieve the certificate in your Pro:Atria email. To obtain the Comodo cert in PKCS#12 format, collect the cert in the confirmation email, open Mozilla and go to Advanced > Certificates > View Certificates and backup the cert to obtain the PKCS#12 format.

If you use and recommend another provider please add details in this section.

Once obtained, you can add the digital certificate to your email provider of choice.


I want to use PGP/MIME?
-----------------------

You cannot use both S/MIME and PGP/MIME at the same time.
PGP/MIME really only makes sense in certain situations.  The general use one is S/MIME.


Other email tips
----------------

Add the Pro:Atria Email Signature Template in your emails.

Set your email settings to prevent HTML/images loading and to block remote content.  

Utilize a blacklist of known spam senders.


Use of group emails
-------------------

Do not add team members that are still on trial to the group until such addition is verified by the team lead.

Do not use team group emails for non SFTPPlus purposes like personal and industry newsletters, announcements, and so on.

There may be some cases where we need to use the group email for related services. When using team group emails for SFTPPlus testing or to open SFTPPlus accounts please notify the group email first that the testing / account is legitimate.  That way, when a test is sent to a team account it is not immediately assumed that it is legitimate. 


Phishing and Social Engineering
===============================

If a phishing attack is encountered or you suspect a phishing attack is encountered notify the team.  

Phishing is also utilized as part of active information gathering while enumerating the target and also points to some form of information gathering/enumerating is taking place.

If encountering potential SE (social engineering) attacks notify the team lead.


Passwords
=========

At some point you will need to use services that are reliant on passwords.

If possible, use non-password options.

Use password management tools (ie LastPass, 1Password, etc) and ensure to enable MFA for these tools.

Do not reuse passwords from your personal accounts with SFTPPlus accounts.

Do not send passwords via cleartext or even better - continue to use services that send passwords via cleartext.  

When changing passwords do not use common password mutations like changing a character at the end.

Do not allow opportunities for password profiling, like using company products in your password.


Internet facing information
===========================

Consider what services are facing the Internet.

Consider what information is facing the Internet.

When posting reviews or comments, are there certain details that need to be taken out to sanitize the review or comment?  

Is this public information going to help with someone's enumeration activities? Are there sensitive files, passwords, private key info publicly facing? 


Customers
=========

We work with admins that are already aware of security practices - like not leaving sensitive information in logs.

However we work with a number of customer bases and budgets.


Olark
-----

We use Olark web chat. If talking to a customer verify who they are and their installation.  The other alternative is to move the discussion to email.

Compliance information is found in the User's Guides https://www.sftpplus.com/documentation/sftpplus/latest/guides/index.html


Improving Documentation
-----------------------

If there a customer is having trouble securing their setup and they have read the documentation, ask what they are trying to do.  Then detect what portion of the documentation can be improved and create a ticket for this.

If a customer has gone to support for this issue and it is not an 'edge case' then chances are high that others have had this issue before.


Testing / validating third party apps / software for use
========================================================

There are some instances when we need to set up test accounts - for example to trial a ticketing software, an online web software and so on. When doing a test, try to test using your own individual Pro:Atria email as it helps solve 'noise'.

Take note of what third party services are opened to do testing in the internal wiki.  

If the third party service is no longer being used, or when testing is finished, delete all instances of any irrelevant tests/accounts and unused services.  Then update the wiki with your findings.

If an app is in active use with customers / within the team during the validating period, ensure that whitelisting takes place to help validate/verify that it is an Pro:Atria-used third party product.


Traveling, use of multiple devices etc
=======================================

If you are planning to travel while working, there are additional precautions faced being on the move.  Anything from risk of using hostile networks, to risk of device being stolen/tampered with.  

When in a public space, use a VPN to secure the connection or consider tethering to your phone.

If possible, connect via wired instead of wireless connection.

There is no request, customer or team, so urgent that you need to connect to a potentially hostile public network then and there to do the task.  Mention this and continue to do the task when you are in a better network.

When faced with "I'm overseas and don't have access to..." or similar type of request, ask to use a secondary channel (ie phone call) to continue with the request.  In this case team member contact details must always be kept up to date in the wiki.

Consider using a non-main or travel-only devices while traveling, or live booting via USB.


Readings
========

IT Security and the Normalization of Deviance - Bruce Schneier
https://www.schneier.com/blog/archives/2016/01/it_security_and.html

Kevin Mitnick books on social engineering

What is network enumeration https://en.wikipedia.org/wiki/Network_enumeration

What is social engineering https://en.wikipedia.org/wiki/Social_engineering_(security)

Security focus mailing list http://www.securityfocus.com/archive

