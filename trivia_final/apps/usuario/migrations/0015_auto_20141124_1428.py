# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_remove_respuestas_correcta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='preguntas',
            field=models.OneToOneField(to='usuario.preguntas'),
            preserve_default=True,
        ),
    ]
