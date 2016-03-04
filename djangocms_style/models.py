# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.models import CMSPlugin


CLASS_NAMES = getattr(settings, "CMS_STYLE_NAMES", (
    ('info', _("info")),
    ('new', _("new")),
    ('hint', _("hint"))
))


@python_2_unicode_compatible
class Style(CMSPlugin):
    """
    A CSS Style Plugin
    """

    DIV_TAG = 'div'
    ARTICLE_TAG = 'article'
    SECTION_TAG = 'section'

    HTML_TAG_TYPES = getattr(settings, "CMS_STYLE_TAG_TYPES", (
        (DIV_TAG, _('div')),
        (ARTICLE_TAG, _('article')),
        (SECTION_TAG, _('section')),
    ))

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin, related_name='djangocms_style_style', parent_link=True)

    class_name = models.CharField(
        _("class name"), choices=CLASS_NAMES, default=CLASS_NAMES[0][0],
        max_length=50, blank=True, null=True)

    tag_type = models.CharField(
        verbose_name=_('tag Type'), max_length=50, choices=HTML_TAG_TYPES,
        default=HTML_TAG_TYPES[0][0])

    padding_left = models.SmallIntegerField(
        _("padding left"), blank=True, null=True)
    padding_right = models.SmallIntegerField(
        _("padding right"), blank=True, null=True)
    padding_top = models.SmallIntegerField(
        _("padding top"), blank=True, null=True)
    padding_bottom = models.SmallIntegerField(
        _("padding bottom"), blank=True, null=True)

    margin_left = models.SmallIntegerField(
        _("margin left"), blank=True, null=True)
    margin_right = models.SmallIntegerField(
        _("margin right"), blank=True, null=True)
    margin_top = models.SmallIntegerField(
        _("margin top"), blank=True, null=True)
    margin_bottom = models.SmallIntegerField(
        _("margin bottom"), blank=True, null=True)

    additional_classes = models.CharField(
        verbose_name=_('additional clases'),
        max_length=200,
        blank=True,
        help_text=_('Comma separated list of additional classes to apply to '
                    'tag_type')
    )

    def __str__(self):
        display = self.get_class_name_display() or self.tag_type or u''
        return u"%s" % display

    def inline_style(self):
        style = ""
        if self.padding_left:
            style += "padding-left: %dpx; " % self.padding_left
        if self.padding_right:
            style += "padding-right: %dpx; " % self.padding_right
        if self.padding_bottom:
            style += "padding-bottom: %dpx; " % self.padding_bottom
        if self.padding_top:
            style += "padding-top: %dpx; " % self.padding_top
        if self.margin_left:
            style += "margin-left: %dpx; " % self.margin_left
        if self.margin_right:
            style += "margin-right: %dpx; " % self.margin_right
        if self.margin_top:
            style += "margin-top: %dpx; " % self.margin_top
        if self.margin_bottom:
            style += "margin-bottom: %dpx; " % self.margin_bottom
        return style

    @property
    def get_additional_classes(self):
        if self.additional_classes:
            # Removes any extra spaces
            class_list = self.additional_classes.split(',')
            return ' '.join((html_class.strip() for html_class in class_list))
        return ''
