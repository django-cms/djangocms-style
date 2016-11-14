# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0006_removed_null_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='template',
            field=models.CharField(default='default', max_length=255, verbose_name='Template', choices=[('default', 'Default')]),
        ),
    ]
