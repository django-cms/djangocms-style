"""
Enables the user to add style plugin that displays a html tag with
the provided settings from the style plugin.
"""
import re

from cms.models import CMSPlugin
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.datastructures import OrderedSet
from django.utils.translation import gettext_lazy as _
from djangocms_attributes_field.fields import AttributesField

CLASS_CHOICES = getattr(
    settings,
    "DJANGOCMS_STYLE_CHOICES",
    ["container", "content", "teaser"],
)
CLASS_CHOICES = tuple((entry, entry) for entry in CLASS_CHOICES)
TAG_CHOICES = getattr(
    settings,
    "DJANGOCMS_STYLE_TAGS",
    ["div", "article", "section", "header", "footer", "aside",
        "h1", "h2", "h3", "h4", "h5", "h6"],
)
TAG_CHOICES = tuple((entry, entry) for entry in TAG_CHOICES)
CLASS_NAME_FORMAT = re.compile(r"^\w[\w_-]*$")
TAG_TYPE_FORMAT = re.compile(r"\w[\w\d]*$")


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ("default", _("Default")),
    ]
    choices += getattr(
        settings,
        "DJANGOCMS_STYLE_TEMPLATES",
        [],
    )
    return choices


class Style(CMSPlugin):
    """
    Renders a given ``TAG_CHOICES`` element with additional attributes
    """
    template = models.CharField(
        verbose_name=_("Template"),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    label = models.CharField(
        verbose_name=_("Label"),
        blank=True,
        max_length=255,
        help_text=_("Overrides the display name in the structure mode."),
    )
    tag_type = models.CharField(
        verbose_name=_("Tag type"),
        choices=TAG_CHOICES,
        default=TAG_CHOICES[0][0],
        max_length=255,
    )
    class_name = models.CharField(
        verbose_name=_("Class name"),
        choices=CLASS_CHOICES,
        default=CLASS_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    additional_classes = models.CharField(
        verbose_name=_("Additional classes"),
        blank=True,
        max_length=255,
        help_text=_('Additional comma separated list of classes '
                    'to be added to the element e.g. "row, column-12, clearfix".'),
    )
    id_name = models.CharField(
        verbose_name=_("ID name"),
        blank=True,
        max_length=255,
    )
    attributes = AttributesField(
        verbose_name=_("Attributes"),
        blank=True,
        excluded_keys=["class", "id", "style"],
    )

    padding_top = models.PositiveSmallIntegerField(
        verbose_name=_("Padding top"),
        blank=True,
        null=True,
    )
    padding_right = models.PositiveSmallIntegerField(
        verbose_name=_("Padding right"),
        blank=True,
        null=True,
    )
    padding_bottom = models.PositiveSmallIntegerField(
        verbose_name=_("Padding bottom"),
        blank=True,
        null=True,
    )
    padding_left = models.PositiveSmallIntegerField(
        verbose_name=_("Padding left"),
        blank=True,
        null=True,
    )

    margin_top = models.PositiveSmallIntegerField(
        verbose_name=_("Margin top"),
        blank=True,
        null=True,
    )
    margin_right = models.PositiveSmallIntegerField(
        verbose_name=_("Margin right"),
        blank=True,
        null=True,
    )
    margin_bottom = models.PositiveSmallIntegerField(
        verbose_name=_("Margin bottom"),
        blank=True,
        null=True,
    )
    margin_left = models.PositiveSmallIntegerField(
        verbose_name=_("Margin left"),
        blank=True,
        null=True,
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name="%(app_label)s_%(class)s",
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label or self.tag_type or str(self.pk)

    def get_short_description(self):
        # display format:
        # Style label <tag> .list.of.classes #id
        display, classes = [], []

        if self.label:
            display.append(self.label)
        if self.tag_type:
            display.append(f"<{self.tag_type}>")
        if self.class_name:
            classes.append(self.class_name)
        if self.additional_classes:
            classes.extend(item.strip() for item in self.additional_classes.split(",") if item.strip())
        if classes:
            display.append(".{}".format(" .".join(classes)))
        if self.id_name:
            display.append(f"#{self.id_name}")
        return " ".join(display)

    def get_additional_classes(self):
        classes = ""
        if self.additional_classes:
            classes = " ".join(item.strip() for item in self.additional_classes.split(",") if item.strip())
        return classes

    def get_styles(self):
        styles = []
        # padding values
        if self.padding_top:
            styles.append(f"padding-top: {self.padding_top:d}px;")
        if self.padding_right:
            styles.append(f"padding-right: {self.padding_right:d}px;")
        if self.padding_bottom:
            styles.append(f"padding-bottom: {self.padding_bottom:d}px;")
        if self.padding_left:
            styles.append(f"padding-left: {self.padding_left:d}px;")
        # margin values
        if self.margin_top:
            styles.append(f"margin-top: {self.margin_top:d}px;")
        if self.margin_right:
            styles.append(f"margin-right: {self.margin_right:d}px;")
        if self.margin_bottom:
            styles.append(f"margin-bottom: {self.margin_bottom:d}px;")
        if self.margin_left:
            styles.append(f"margin-left: {self.margin_left:d}px;")
        return " ".join(styles)

    def clean(self):
        # validate for correct class name settings
        if self.additional_classes:
            additional_classes = [
                html_class.strip() for html_class in self.additional_classes.split(",")
            ]
            for class_name in additional_classes:
                _class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(_class_name):
                    raise ValidationError(
                        _('"{name}" is not a proper CSS class name.').format(name=_class_name)
                    )
            self.additional_classes = ", ".join(OrderedSet(additional_classes))
        # validate for correct tag type settings
        if self.tag_type and not TAG_TYPE_FORMAT.match(self.tag_type):
            raise ValidationError(
                _('"{name}" is not a proper HTML tag.').format(name=self.tag_type)
            )
