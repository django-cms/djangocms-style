# -*- coding: utf-8 -*-
from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_style.models import Style, TAG_CHOICES, CLASS_CHOICES


class StyleTestCase(CMSTestCase):

    def setUp(self):
        self.superuser = self.get_superuser()
        self.home = create_page(
            title="home",
            template="page.html",
            language="en",
        )
        self.home.publish("en")
        self.page = create_page(
            title="help",
            template="page.html",
            language="en",
        )

    def tearDown(self):
        self.page.delete()
        self.home.delete()

    def test_style_instance(self):
        """Style instance has been created"""
        Style.objects.create(
            tag_type='div',
        )
        style = Style.objects.get(tag_type='div')
        self.assertEqual(style.tag_type, 'div')

    def test_style_plugin(self):
        plugin = add_plugin(
            self.page.placeholders.get(slot="content"),
            "StylePlugin",
            "en",
            label="Style plugin",
            additional_classes="btn btn-default",
        )
        self.assertEqual(plugin.additional_classes, "btn btn-default")
        self.assertEqual(plugin.label, "Style plugin")
        self.assertEqual(plugin.tag_type, TAG_CHOICES[0][0])
        self.assertEqual(plugin.class_name, CLASS_CHOICES[0][0])
        self.assertEqual(plugin.id_name, '')

    def test_style_rendering(self):
        add_plugin(
            self.page.placeholders.get(slot="content"),
            "StylePlugin",
            "en",
            label="Style plugin",
            additional_classes="btn btn-default",
        )
        self.page.publish("en")

        with self.login_user_context(self.superuser):
            response = self.client.get(self.page.get_absolute_url('en'))

        self.assertContains(
            response,
            """<div class="container btn btn-default"></div>"""
        )

        # now with attributes
        add_plugin(
            self.page.placeholders.get(slot="content"),
            "StylePlugin",
            "en",
            label="Style plugin",
            class_name=CLASS_CHOICES[0][1],
            additional_classes="btn btn-default",
            id_name="get-gelp",
            attributes={
                "data-type": "custom"
            },
        )
        self.page.publish("en")

        with self.login_user_context(self.superuser):
            response = self.client.get(self.page.get_absolute_url('en'))

        # print(response.content)
        self.assertContains(
            response,
            """<div id="get-gelp" class="container btn btn-default" data-type="custom"></div>"""
        )
