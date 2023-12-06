=========
Changelog
=========

3.1.0 (2023-12-06)
==================

## What's Changed
* Add GitHub Actions by @crydotsnake in https://github.com/django-cms/djangocms-style/pull/56
* FEATURE: adjust setup metadata by @crydotsnake in https://github.com/django-cms/djangocms-style/pull/58
* FEATURE: add github pr template by @crydotsnake in https://github.com/django-cms/djangocms-style/pull/57
* Removed pinned django-treebeard by @tidenhub in https://github.com/django-cms/djangocms-style/pull/59
* Feat: Django 4.2 support by @mogoh in https://github.com/django-cms/djangocms-style/pull/61
* chore: Improve ruff config by @marksweb in https://github.com/django-cms/djangocms-style/pull/64

## New Contributors
* @crydotsnake made their first contribution in https://github.com/django-cms/djangocms-style/pull/56
* @tidenhub made their first contribution in https://github.com/django-cms/djangocms-style/pull/59
* @mogoh made their first contribution in https://github.com/django-cms/djangocms-style/pull/61
* @marksweb made their first contribution in https://github.com/django-cms/djangocms-style/pull/64

**Full Changelog**: https://github.com/django-cms/djangocms-style/compare/3.0.0...3.1.0

3.0.0 (2020-09-02)
==================

* Added support for Django 3.1
* Dropped support for Python 2.7 and Python 3.4
* Dropped support for Django < 2.2


2.3.0 (2020-01-29)
==================

* Added support for Django 3.0
* Deprecated old ``CMS_STYLE_NAMES`` setting
* Deprecated old ``CMS_STYLE_TAG_TYPES`` setting
* Added further tests to raise coverage
* Fixed smaller issues found during testing


2.2.0 (2019-05-06)
==================

* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Added isort and adapted imports
* Adapted code base to align with other supported addons
* Exclude ``tests`` folder from release build


2.1.0 (2018-11-08)
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
