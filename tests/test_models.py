from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase

from djangocms_style.models import (
    CLASS_CHOICES, TAG_CHOICES, Style, get_templates,
)


class StyleModelTestCase(TestCase):

    def test_settings(self):
        self.assertEqual(get_templates(), [('default', 'Default')])
        settings.DJANGOCMS_STYLE_TEMPLATES = [('feature', 'Feature')]
        self.assertEqual(get_templates(), [('default', 'Default'), ('feature', 'Feature')])
        # class choices
        self.assertEqual(CLASS_CHOICES, (
            ('container', 'container'),
            ('content', 'content'),
            ('teaser', 'teaser'),
        ))
        self.assertEqual(TAG_CHOICES, (
            ('div', 'div'), ('article', 'article'),
            ('section', 'section'), ('header', 'header'),
            ('footer', 'footer'), ('aside', 'aside'),
            ('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3'),
            ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6'),
        ))

    def test_style_instance(self):
        Style.objects.create(
            template=get_templates()[0][0],
            label="some label",
            tag_type=TAG_CHOICES[1][0],
            class_name=CLASS_CHOICES[1][0],
            additional_classes="xs, large, blue",
            id_name="top",
            attributes="{'type': 'style'}",
            padding_top=10,
            padding_right=20,
            padding_bottom=30,
            padding_left=40,
        )
        instance = Style.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = Style.objects.first()
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.label, "some label")
        self.assertEqual(instance.tag_type, "article")
        self.assertEqual(instance.class_name, "content")
        self.assertEqual(instance.additional_classes, "xs, large, blue")
        self.assertEqual(instance.id_name, "top")
        self.assertEqual(instance.attributes, "{'type': 'style'}")
        self.assertEqual(instance.padding_top, 10)
        instance.clean()
        # test classes
        self.assertEqual(instance.get_additional_classes(), "xs large blue")
        self.assertEqual(
            instance.get_styles(),
            "padding-top: 10px; padding-right: 20px; padding-bottom: 30px; padding-left: 40px;",
        )
        instance.padding_top, instance.padding_right = None, None
        instance.padding_bottom, instance.padding_left = None, None
        self.assertEqual(instance.get_styles(), "")
        instance.clean()
        instance.margin_top = 11
        instance.margin_right = 21
        instance.margin_bottom = 31
        instance.margin_left = 41
        self.assertEqual(
            instance.get_styles(),
            "margin-top: 11px; margin-right: 21px; margin-bottom: 31px; margin-left: 41px;",
        )
        # test strings
        self.assertEqual(str(instance), "some label")
        self.assertEqual(
            instance.get_short_description(),
            "some label <article> .content .xs .large .blue #top",
        )
        instance.label = None
        self.assertEqual(str(instance), "article")
        self.assertEqual(
            instance.get_short_description(),
            "<article> .content .xs .large .blue #top",
        )
        instance.tag_type = None
        self.assertEqual(str(instance), "1")
        self.assertEqual(
            instance.get_short_description(),
            ".content .xs .large .blue #top",
        )
        instance.class_name = None
        instance.additional_classes = None
        instance.id_name = None
        self.assertEqual(instance.get_short_description(), "",)
        self.assertEqual(instance.get_additional_classes(), "")
        # test clean errors
        instance.clean()
        instance.additional_classes = "%1up"
        instance.tag_type = "%1up"
        with self.assertRaises(ValidationError):
            # is not a proper CSS class name
            instance.clean()
        instance.additional_classes = ""
        with self.assertRaises(ValidationError):
            # is not a proper HTML tag
            instance.clean()
