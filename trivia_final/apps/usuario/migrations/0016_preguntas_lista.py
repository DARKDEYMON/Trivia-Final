# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_auto_20141124_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='lista',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
