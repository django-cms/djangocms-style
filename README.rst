djangocms-style
===============

A Plugin for django CMS to add CSS classes to other plugins


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-style``.
* If using Django 1.6 and South < 1.0.2 add ``'djangocms_style': 'djangocms_style.south_migrations',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it
  does not exist);
* Add ``'djangocms_style'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_style``.


Usage
-----

You can define styles in your settings.py:

.. code-block:: python

    CMS_STYLE_NAMES = (
        ('info', _("info")),
        ('new', _("new")),
        ('hint', _("hint")),
    )

After that you can place other plugins inside this style plugin.
It will create a div with a class that was prior selected around this plugin.

Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-style/
