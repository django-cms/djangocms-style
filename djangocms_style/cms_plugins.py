from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import Style


class StylePlugin(CMSPluginBase):
    model = Style
    name = _("Style")
    render_template = "djangocms_style/style.html"
    allow_children = True

    fieldsets = (
        (None, {
            "fields": (
                "label",
                ("class_name", "tag_type"),
            )
        }),
        (_("Advanced settings"), {
            "classes": ("collapse",),
            "fields": (
                "additional_classes",
                "id_name",
                "template",
                "attributes",
            ),
        }),
        (_("Inline style settings"), {
            "classes": ("collapse",),
            "fields": (
                ("padding_top", "padding_right",
                 "padding_bottom", "padding_left"),
                ("margin_top", "margin_right",
                 "margin_bottom", "margin_left"),
            ),
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        return f"djangocms_style/{instance.template}/style.html"

    def render(self, context, instance, placeholder):
        context["inline_styles"] = instance.get_styles()
        return super().render(context, instance, placeholder)


plugin_pool.register_plugin(StylePlugin)
