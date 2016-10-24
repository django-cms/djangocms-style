# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def reset_null_values(apps, schema_editor):
    Style = apps.get_model('djangocms_style', 'Style')
    plugins = Style.objects.all()
    plugins.filter(class_name__isnull=True).update(class_name='')


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_style', '0004_use_positive_small_integer_field'),
    ]

    operations = [
        migrations.RunPython(reset_null_values),
    ]
