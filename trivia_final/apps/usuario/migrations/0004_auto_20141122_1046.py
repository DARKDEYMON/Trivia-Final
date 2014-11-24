# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_preguntas_respuestas_temas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preguntas',
            options={'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterModelOptions(
            name='respuestas',
            options={'verbose_name': 'Respuestas', 'verbose_name_plural': 'Respuestas'},
        ),
        migrations.AlterModelOptions(
            name='temas',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='rate',
        ),
    ]
