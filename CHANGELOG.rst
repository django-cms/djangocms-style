=========
Changelog
=========


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
