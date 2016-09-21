# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0005_reset_null_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='class_name',
            field=models.CharField(default='container', max_length=255, verbose_name='Class name', blank=True, choices=[('container', 'container'), ('content', 'content'), ('teaser', 'teaser')]),
        ),
    ]
