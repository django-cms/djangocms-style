# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0002_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='style',
            name='id_name',
            field=models.CharField(max_length=255, verbose_name='ID name', blank=True),
        ),
        migrations.AddField(
            model_name='style',
            name='label',
            field=models.CharField(help_text='Overrides the display name in the structure mode.', max_length=255, verbose_name='Label', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='additional_classes',
            field=models.CharField(help_text='Additional comma separated list of classes to be added to the element e.g. "row, column-12, clearfix".', max_length=255, verbose_name='Additional classes', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='class_name',
            field=models.CharField(default='container', choices=[('container', 'container'), ('content', 'content'), ('teaser', 'teaser')], max_length=255, blank=True, verbose_name='Class name'),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_bottom',
            field=models.SmallIntegerField(null=True, verbose_name='Margin bottom', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_left',
            field=models.SmallIntegerField(null=True, verbose_name='Margin left', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_right',
            field=models.SmallIntegerField(null=True, verbose_name='Margin right', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_top',
            field=models.SmallIntegerField(null=True, verbose_name='Margin top', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_bottom',
            field=models.SmallIntegerField(null=True, verbose_name='Padding bottom', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_left',
            field=models.SmallIntegerField(null=True, verbose_name='Padding left', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_right',
            field=models.SmallIntegerField(null=True, verbose_name='Padding right', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_top',
            field=models.SmallIntegerField(null=True, verbose_name='Padding top', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='tag_type',
            field=models.CharField(default='div', max_length=255, verbose_name='Tag type', choices=[('div', 'div'), ('article', 'article'), ('section', 'section'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside'), ('hi', 'hi'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6')]),
        ),
    ]
