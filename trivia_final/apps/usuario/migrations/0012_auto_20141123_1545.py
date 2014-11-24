# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_auto_20141123_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='pregunta',
            field=models.CharField(max_length=100, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='correcta',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
