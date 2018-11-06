# -*- coding: utf-8 -*-
"""
Enables the user to add style plugin that displays a html tag with
the provided settings from the style plugin.
"""
from __future__ import unicode_literals

import re
import warnings

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.datastructures import OrderedSet
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_attributes_field.fields import AttributesField


if hasattr(settings, 'CMS_STYLE_NAMES'):
    CLASS_CHOICES = tuple((setting) for setting in list(settings.CMS_STYLE_NAMES))
    warnings.warn('Please change CMS_STYLE_NAMES to the new DJANGOCMS_STYLE_CHOICES.')
else:
    CLASS_CHOICES = getattr(
        settings,
        'DJANGOCMS_STYLE_CHOICES',
        ['container', 'content', 'teaser'],
    )
    CLASS_CHOICES = tuple((entry, entry) for entry in CLASS_CHOICES)

if hasattr(settings, 'CMS_STYLE_TAG_TYPES'):
    TAG_CHOICES = tuple((setting) for setting in list(settings.CMS_STYLE_TAG_TYPES))
    warnings.warn('Please change CMS_STYLE_TAG_TYPES to the new DJANGOCMS_STYLE_TAGS.')
else:
    TAG_CHOICES = getattr(
        settings,
        'DJANGOCMS_STYLE_TAGS',
        ['div', 'article', 'section', 'header', 'footer', 'aside',
         'h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
    )
    TAG_CHOICES = tuple((entry, entry) for entry in TAG_CHOICES)

CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')
TAG_TYPE_FORMAT = re.compile(r'\w[\w\d]*$')


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_STYLE_TEMPLATES',
        [],
    )
    return choices


@python_2_unicode_compatible
class Style(CMSPlugin):
    """
    Renders a given ``TAG_CHOICES`` element with additional attributes
    """
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the display name in the structure mode.'),
    )
    tag_type = models.CharField(
        verbose_name=_('Tag type'),
        choices=TAG_CHOICES,
        default=TAG_CHOICES[0][0],
        max_length=255,
    )
    class_name = models.CharField(
        verbose_name=_('Class name'),
        choices=CLASS_CHOICES,
        default=CLASS_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    additional_classes = models.CharField(
        verbose_name=_('Additional classes'),
        blank=True,
        max_length=255,
        help_text=_('Additional comma separated list of classes '
                    'to be added to the element e.g. "row, column-12, clearfix".'),
    )
    id_name = models.CharField(
        verbose_name=_('ID name'),
        blank=True,
        max_length=255,
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['class', 'id', 'style'],
    )

    padding_top = models.PositiveSmallIntegerField(
        verbose_name=_('Padding top'),
        blank=True,
        null=True,
    )
    padding_right = models.PositiveSmallIntegerField(
        verbose_name=_('Padding right'),
        blank=True,
        null=True,
    )
    padding_bottom = models.PositiveSmallIntegerField(
        verbose_name=_('Padding bottom'),
        blank=True,
        null=True,
    )
    padding_left = models.PositiveSmallIntegerField(
        verbose_name=_('Padding left'),
        blank=True,
        null=True,
    )

    margin_top = models.PositiveSmallIntegerField(
        verbose_name=_('Margin top'),
        blank=True,
        null=True,
    )
    margin_right = models.PositiveSmallIntegerField(
        verbose_name=_('Margin right'),
        blank=True,
        null=True,
    )
    margin_bottom = models.PositiveSmallIntegerField(
        verbose_name=_('Margin bottom'),
        blank=True,
        null=True,
    )
    margin_left = models.PositiveSmallIntegerField(
        verbose_name=_('Margin left'),
        blank=True,
        null=True,
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label or self.tag_type or str(self.pk)

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display = []
        classes = []

        if self.label:
            display.append(self.label)
        if self.tag_type:
            display.append('<{0}>'.format(self.tag_type))
        if self.class_name:
            classes.append(self.class_name)
        if self.additional_classes:
            classes.extend(item.strip() for item in self.additional_classes.split(',') if item.strip())
        display.append('.{0}'.format('.'.join(classes)))
        if self.id_name:
            display.append('#{0}'.format(self.id_name))
        return ' '.join(display)

    def get_additional_classes(self):
        return ' '.join(item.strip() for item in self.additional_classes.split(',') if item.strip())

    def get_styles(self):
        styles = []
        # padding values
        if self.padding_top:
            styles.append('padding-top: {0:d}px;'.format(self.padding_top))
        if self.padding_right:
            styles.append('padding-right: {0:d}px;'.format(self.padding_right))
        if self.padding_bottom:
            styles.append('padding-bottom: {0:d}px;'.format(self.padding_bottom))
        if self.padding_left:
            styles.append('padding-left: {0:d}px;'.format(self.padding_left))
        # margin values
        if self.margin_top:
            styles.append('margin-top: {0:d}px;'.format(self.margin_top))
        if self.margin_right:
            styles.append('margin-right: {0:d}px;'.format(self.margin_right))
        if self.margin_bottom:
            styles.append('margin-bottom: {0:d}px;'.format(self.margin_bottom))
        if self.margin_left:
            styles.append('margin-left: {0:d}px;'.format(self.margin_left))
        return ' '.join(styles)

    def clean(self):
        # validate for correct class name settings
        if self.additional_classes:
            additional_classes = list(
                html_class.strip() for html_class in self.additional_classes.split(',')
            )
            for class_name in additional_classes:
                class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(class_name):
                    raise ValidationError(
                        _('"{name}" is not a proper CSS class name.').format(name=class_name)
                    )
            self.additional_classes = ', '.join(OrderedSet(additional_classes))
        # validate for correct tag type settings
        if self.tag_type:
            if not TAG_TYPE_FORMAT.match(self.tag_type):
                raise ValidationError(
                    _('"{name}" is not a proper HTML tag.').format(name=self.tag_type)
                )
