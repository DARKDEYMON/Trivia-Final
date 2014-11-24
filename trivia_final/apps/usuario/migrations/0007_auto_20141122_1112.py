# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_auto_20141122_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntas',
            old_name='temas_p',
            new_name='temas',
        ),
        migrations.RenameField(
            model_name='preguntas',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='pregunta',
            new_name='preguntas',
        ),
        migrations.RenameField(
            model_name='respuestas',
            old_name='pregunta',
            new_name='preguntas',
        ),
    ]
