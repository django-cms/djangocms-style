# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Style


class StylePlugin(CMSPluginBase):
    model = Style
    name = _('Style')
    render_template = 'djangocms_style/style.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'label',
                ('class_name', 'tag_type'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_classes',
                'id_name',
                'template',
                'attributes',
            ),
        }),
        (_('Inline style settings'), {
            'classes': ('collapse',),
            'fields': (
                ('padding_top', 'padding_right',
                 'padding_bottom', 'padding_left'),
                ('margin_top', 'margin_right',
                 'margin_bottom', 'margin_left'),
            ),
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_style/{}/style.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        context['inline_styles'] = instance.get_styles()
        return super(StylePlugin, self).render(context, instance, placeholder)


plugin_pool.register_plugin(StylePlugin)
