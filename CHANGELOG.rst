=========
Changelog
=========

2.1.0 (unreleased)
==================

* Fixed a validation issue with attributes
* Added support for Django 1.11, 2.0 and 2.1
* Removed support for Django 1.8, 1.9, 1.10
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.5 and 4.0


2.0.2 (2017-03-07)
==================

* Ensure class ordering is maintained #36


2.0.1 (2016-11-22)
==================

* Prevent changes to ``DJANGOCMS_STYLE_XXX`` settings from requiring new
  migrations
* Changed naming of ``Aldryn`` to ``Divio Cloud``
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.4 and dropped 3.2
* Updated translations


2.0.0 (2016-11-15)
==================

* Backwards incompatible changes
    * Moved template from ``templates/cms/plugins/style.html`` to
      ``templates/djangocms_style/default/style.html``
    * Added setting ``DJANGOCMS_STYLE_TEMPLATES``
    * Added setting ``DJANGOCMS_STYLE_CHOICES`` that will replace
      ``CMS_STYLE_NAMES``
    * Added setting ``DJANGOCMS_STYLE_TAGS`` that will replace
      ``CMS_STYLE_TAG_TYPES``
    * Removed Django < 1.8 support
    * Removed ``alt`` attribute and migrated data to Filer
* Added additional fields such as ``label``, ``id_name`` and additional
  ``attributes``
* Updated ``README.txt``
* Updated translations


1.7.0 (2016-03-04)
==================

* Use this version for Django < 1.8 support
