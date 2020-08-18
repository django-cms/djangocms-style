from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_style.cms_plugins import StylePlugin


class StyleTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title="help",
            template="page.html",
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()

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
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        add_plugin(
            self.placeholder,
            StylePlugin.__name__,
            self.language,
            label="Style plugin",
            additional_classes="btn, btn-default",
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

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
                "data-type": "custom"
            },
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        # print(response.content)
        self.assertContains(
            response,
            """<div id="get-gelp" class="container btn btn-default" data-type="custom"></div>""",
            html=True,
        )
