# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('class_name', models.CharField(default=b'info', choices=[(b'info', 'info'), (b'new', 'new'), (b'hint', 'hint')], max_length=50, blank=True, null=True, verbose_name='class name')),
                ('tag_type', models.CharField(default=b'div', max_length=50, verbose_name='tag Type', choices=[(b'div', 'div'), (b'article', 'article'), (b'section', 'section')])),
                ('padding_left', models.SmallIntegerField(null=True, verbose_name='padding left', blank=True)),
                ('padding_right', models.SmallIntegerField(null=True, verbose_name='padding right', blank=True)),
                ('padding_top', models.SmallIntegerField(null=True, verbose_name='padding top', blank=True)),
                ('padding_bottom', models.SmallIntegerField(null=True, verbose_name='padding bottom', blank=True)),
                ('margin_left', models.SmallIntegerField(null=True, verbose_name='margin left', blank=True)),
                ('margin_right', models.SmallIntegerField(null=True, verbose_name='margin right', blank=True)),
                ('margin_top', models.SmallIntegerField(null=True, verbose_name='margin top', blank=True)),
                ('margin_bottom', models.SmallIntegerField(null=True, verbose_name='margin bottom', blank=True)),
                ('additional_classes', models.CharField(help_text='Comma separated list of additional classes to apply to tag_type', max_length=200, verbose_name='additional clases', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
