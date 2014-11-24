# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_temas_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestas',
            name='correcta',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
