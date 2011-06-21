=========================
collective.webrichtlijnen
=========================

Introduction
------------
This theme is aimed at making Plone compliant with the Dutch web guidelines. 

Website of the Dutch web guidelines: http://www.webrichtlijnen.nl/english

A description from the webrichtlijnen.nl website:

::

    Government bodies and companies are facing the challenge of 
    creating websites that are optimally accessible to people as 
    well as browsers and search engines. The Web Guidelines 
    aid in that process.

    There are internationally recognized agreements for creating 
    web sites known as 125 quality requirements standards warrants 
    a significantly better website. The Netherlands government 
    has assembled these international standards in a quality model 
    called the Web Guidelines. This quality model comprises 125 
    quality requirements for the benefit of better websites.


This theme is tested using the Dutch web guidelines quick scan. The quick scan
checks 47 points of 125. There 78 points in the guidelines that need manual
checking. These manual tests involve how the website uses HTML and other relevant
techniques, that the content manager(s) are aware of several guidelines and how
processes supporting the guidelines are defined. In the doc dir an example is
included for all the manual points. The document is named
'niet_toetsbare_webrichtlijnen.odt' and is in Dutch.

If you're from the Dutch central goverment you can login to see the scan results.
Unfortunately local goverments cannot see the complete scan results, they can
use the quick scan.

Installation (short version)
----------------------------

See below for "Full installation notes", notably the part on how to use this
product with a custom theme.

* Add ``collective.webrichtlijnen`` to the list of eggs to install, e.g.::

    [buildout]
    ...
    eggs =
        ...
        Products.PloneTableless
        collective.webrichtlijnen

* Tell the plone.recipe.zope2instance recipe to install a ZCML slug::

    zcml =
        ...
        Products.PloneTableless
        collective.webrichtlijnen

  We consciously do not use z3c.autoinclude here, because we have an
  `overrides.zcml` file here, which might conflict with any overrides you have
  defined in your own theme product, causing the server to not start.

Why aim at these Dutch web guidelines and not the W3C standard?
---------------------------------------------------------------
All websites of the Dutch central goverment need too comply with the Dutch web
guidelines in 2010. (http://www.webrichtlijnen.nl/english/background/). Websites
of the local goverment (ie. municipalities) have the aim to be compliant in 2010. 


Webrichtlijnen compliant HTML/CSS code that is marked as invalid
----------------------------------------------------------------
The following points are marked as invalid by the quick scan. When a manual
check is done these points are invalid.

* Invalid (R-pd.1.1): The use of a width attribute is only allowed with images, the quick scan finds a width attribute. This is not correct no width attribute is used.
* Possible valid (R-pd.8.11): If access keys are used make sure it works on every page on the site and only use numbers. Plone follows this practice and uses a setup that closely matches most international recommendations on access keys.
* Possible valid (R-pd.9.1): The quickscan finds an inline style tag. This is not correct no inline style is used.


Webrichtlijnen non-compliant HTML/CSS code
------------------------------------------
The following points are marked as invalid by the quick scan.

* Invalid (R-pd.2.6): Plone uses CSS3 to create rounded corners. The CSS used fails when using the W3C CSS check. The use of CSS3 is complementary, where this is applied the pages are still visisble with a browser that uses CSS2.1
* Possible invalid (R-pd.3.9): The Plone footer uses a sub element to show the copyright character. The web guidelines advised to avoid using sup (suberscript) and sub (subscript)element where possible.


Plone versions and themes
-------------------------
The webrichtlijnen theme works with Plone 3 and 4. When using the webrichtlijnen
theme the visual appearance of Plone isn't altered. The table below shows which
default Plone theme is used as base and which webrichtlijnen theme version works
with a specific version of Plone/

+---------------+---------------+-----------------+
| Theme version | Plone version | Plone theme     |
+===============+===============+=================+
| 1.0.x         | 3.x           | Plone tableless |
+---------------+---------------+-----------------+
| 1.1.x         | 4.x           | Sunburst theme  |
+---------------+---------------+-----------------+

Sponsor
-------
The development of this theme is funded by http://gemeente.groningen.nl/ - Gemeente
Groningen (municipality of Groningen).
