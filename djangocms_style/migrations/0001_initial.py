# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from djangocms_style.models import CLASS_NAMES, Style

class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, related_name='+', parent_link=True, to='cms.CMSPlugin', primary_key=True)),
                ('class_name', models.CharField(blank=True, max_length=50, choices=CLASS_NAMES, verbose_name='class name', null=True, default=CLASS_NAMES[0][0])),
                ('tag_type', models.CharField(verbose_name='tag Type', default=Style.HTML_TAG_TYPES[0][0], max_length=50, choices=Style.HTML_TAG_TYPES)),
                ('padding_left', models.SmallIntegerField(verbose_name='padding left', blank=True, null=True)),
                ('padding_right', models.SmallIntegerField(verbose_name='padding right', blank=True, null=True)),
                ('padding_top', models.SmallIntegerField(verbose_name='padding top', blank=True, null=True)),
                ('padding_bottom', models.SmallIntegerField(verbose_name='padding bottom', blank=True, null=True)),
                ('margin_left', models.SmallIntegerField(verbose_name='margin left', blank=True, null=True)),
                ('margin_right', models.SmallIntegerField(verbose_name='margin right', blank=True, null=True)),
                ('margin_top', models.SmallIntegerField(verbose_name='margin top', blank=True, null=True)),
                ('margin_bottom', models.SmallIntegerField(verbose_name='margin bottom', blank=True, null=True)),
                ('additional_classes', models.CharField(help_text='Comma separated list of additional classes to apply to tag_type', blank=True, max_length=200, verbose_name='additional clases')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
