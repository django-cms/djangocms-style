# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0003_adapted_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='margin_bottom',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Margin bottom', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_left',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Margin left', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_right',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Margin right', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='margin_top',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Margin top', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_bottom',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Padding bottom', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_left',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Padding left', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_right',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Padding right', blank=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='padding_top',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Padding top', blank=True),
        ),
    ]
