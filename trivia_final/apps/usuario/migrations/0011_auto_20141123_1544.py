# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_respuestas_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='pregunta',
            field=models.CharField(default=False, max_length=100, unique=True, null=True),
            preserve_default=True,
        ),
    ]
