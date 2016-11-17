# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from djangocms_style.models import CLASS_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0005_reset_null_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='class_name',
            field=models.CharField(max_length=255, verbose_name='Class name', blank=True, choices=CLASS_CHOICES, default=CLASS_CHOICES[0][0])
        ),
    ]
