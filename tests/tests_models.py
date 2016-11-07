# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_style.models import Style


class StyleTestCase(TestCase):

    def setUp(self):
        Style.objects.create(
            tag_type='div',
        )

    def test_style_instance(self):
        """Style instance has been created"""
        style = Style.objects.get(tag_type='div')
        self.assertEqual(style.tag_type, 'div')
