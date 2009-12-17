Introduction
============
This theme is aimed at making Plone complaint with the Dutch web guidelines. 

Website of the Dutch web guidelines: http://www.webrichtlijnen.nl/english

A description from the webrichtlijnen.nl website:

--
Government bodies and companies are facing the challenge of creating websites that are optimally accessible to people as well as browsers and search engines. The Web Guidelines aid in that process.

There are internationally recognized agreements for creating web sites, known as 125 quality requirements standards warrants a significantly better website. The Netherlands government has assembled these international standards in a quality model called the Web Guidelines. This quality model comprises 125 quality requirements for the benefit of better websites.
--

This theme is tested using the Dutch web guidelines quick scan. The quick scan checks 47 point of the 125 total guidelines. There 78 point in the guidelines need manual checking. These manual tests involve how the website uses HTML and other relevant techniques, that the content manager(s) are aware of several guidelines. In the doc dir an example is included for all the manual point. The document is named: niet_toetsbare_webrichtlijnen.odt

If you're from the Dutch central goverment you can login to see the scan results. Unfortunately local goverments cannot see the complete scan results, they can use the quick scan.

Installation
============
See docs/INSTALL.txt, collective.webrichtlijnen depends on Plone.Tableless

Why aim at these Dutch web guidelines and not the W3C standard?
===========================================================

The Dutch web guidelines are following the W3C HTML and WAI standards with added 'guidelines'. These guidelines are aimed at making a website accessible for all people. This means the website must be accessible for all browsers, including the browsers for handicapped people (ie. are deaf or blind).

All websites of the Dutch central goverment need too comply with the Dutch web guidelines in 2010. (http://www.webrichtlijnen.nl/english/background/). Websites of the local goverment (ie. municipalities) have the aim to be complaint in 2010. 


Webrichtlijnen non-complaint HTML code
======================================
There are a few pages in Plone that aren't complaint. The invalid point aren't easy to fix in this package (ie. portlets) or aren't important enough to fix (ie. Plone footer).

- Possible invalid: The Plone footer uses a sub element to show the copyright character. The web guidelines advised to avoid using sup (suberscript) and sub (subscript)element where possible.

- Invalid: The file archetypes has a file icon image that is missing the alt attribute. (http://dev.plone.org/plone/ticket/9948)

- Invalid: Many portlets have a xmlns attribute in in their definition list element. The W3C HTML validator sees this as an error.
 
- Invalid: The login portlet has a form without a fieldset (or similar element). 
no portlets. The W3C HTML validator sees this as an error.
