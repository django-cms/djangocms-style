from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_style.cms_plugins import StylePlugin

from .fixtures import TestFixture


class StyleTestCase(TestFixture, CMSTestCase):

    def test_style_plugin(self):
        plugin = add_plugin(
            self.placeholder,
            StylePlugin.__name__,
            self.language,
            label="Style plugin",
            additional_classes="btn, btn-default",
        )
        plugin.clean()
        self.assertEqual(plugin.plugin_type, "StylePlugin")

    def test_plugin_structure(self):
        add_plugin(
            self.placeholder,
            StylePlugin.__name__,
            self.language,
            label="Style plugin",
            additional_classes="btn, btn-default",
        )
        self.publish(self.page, self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)

        self.assertContains(
            response,
            """<div class="container btn btn-default"></div>""",
            html=True,
        )

        # now with attributes
        add_plugin(
            self.placeholder,
            StylePlugin.__name__,
            self.language,
            label="Style plugin",
            class_name="container",
            additional_classes="btn btn-default",
            id_name="get-gelp",
            attributes={
                "data-type": "custom",
            },
        )
        self.publish(self.page, self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)

        self.assertContains(
            response,
            """<div id="get-gelp" class="container btn btn-default" data-type="custom"></div>""",
            html=True,
        )
