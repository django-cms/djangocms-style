# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from djangocms_style.models import get_templates


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0006_removed_null_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='template',
            field=models.CharField(max_length=255, verbose_name='Template', choices=get_templates(), default=get_templates()[0][0])
        ),
    ]
