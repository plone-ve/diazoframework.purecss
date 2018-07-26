======================
diazoframework.purecss
======================


Introduction
============

``diazoframework.purecss`` package provides the diazo framework implementation of the 
`PureCSS framework`_ using the **theming** and **packaging** features available in the 
`diazoframework.plone`_ core package for create `Diazo`_ theme using `plone.app.theming`_.

They are useful for creating themes based on `PureCSS framework`_. For documentation on the 
framework itself, check the website.

A Diazo framework should provide the framework resources and diazo rules to reuse 
and add to in a Diazo theme.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*You will need enable it via "Add-ons" control 
  panel to use this package*)
- The ``diazoframework.plone`` package (*You will need enable it via "buildout" 
  configuration to use this package*)


Features
========

- Provides the *PureCSS framework* v0.1.0 resources.
- Included Diazo rules for the **head** that contains ``framework-custom``, 
  ``nonresponsive-gridless``, ``nonresponsive``, ``responsive-gridless``, ``responsive`` 
  and ``yui`` CSS styles.
- Included Diazo rules for the **body** that contains ``base``, ``columns``, ``edit``, 
  ``forms``, ``menu``, ``nonresponsive``, ``responsive``, ``search-filter`` and 
  ``tables`` CSS styles.


Installation
============

This add-on can be installed has any other add-ons. It's doesn't have any profile, so 
just add it to your Zope instance, for doing that please the follow steps: 


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``diazoframework.purecss`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        diazoframework.purecss


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'diazoframework.purecss',
    ],


Resources
=========

The resources of this framework can be reached through 
``/++framework++purecss`` and there are placed at 
``diazoframework.purecss/diazoframework/purecss/framework/`` 
directory with following resources files:

::

    _ css
      _ pure-min.css
    _ js
      _ yui-min.js
    _ layout
    _ rules
      _ body
        _ base.xml
        _ columns.xml
        _ edit.xml
        _ forms.xml
        _ menu.xml
        _ nonresponsive.xml
        _ responsive.xml
        _ tables.xml
      _ head
        _ framework-custom.xml
        _ nonresponsive.xml
        _ nonresponsive-gridless.xml
        _ responsive.xml
        _ responsive-gridless.xml
        _ yui.xml
    _ preview.png


Current themes
==============

The `diazoframework.purecss`_ package have the following themes:

`diazotheme.purecss`_.
    which contains themes that can both be used as starters for your own *PureCSS* based theme.


For more frameworks see: the `diazoframework.plone`_ package.


Contribute
==========

- Issue Tracker: https://github.com/TH-code/diazoframework.purecss/issues
- Source Code: https://github.com/TH-code/diazoframework.purecss


License
=======

The project is licensed under the GPLv2.

The *PureCSS framework* is licensed under the BSD license.


Credits
-------

- Thijs Jonkman (t.jonkman at gmail dot com).


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/TH-code/diazoframework.purecss/contributors


.. _`PureCSS framework`: http://purecss.io/
.. _`diazoframework.plone`: https://github.com/collective/diazoframework.plone#current-frameworks
.. _`Diazo`: http://diazo.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`diazoframework.purecss`: https://github.com/TH-code/diazoframework.purecss
.. _`diazotheme.purecss`: https://github.com/TH-code/diazotheme.purecss
