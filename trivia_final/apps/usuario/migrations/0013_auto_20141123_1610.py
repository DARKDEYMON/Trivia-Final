# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_auto_20141123_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuestas',
            old_name='respuesta',
            new_name='respuesta_correcta',
        ),
        migrations.AddField(
            model_name='respuestas',
            name='respuesta_opcional_1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestas',
            name='respuesta_opcional_2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestas',
            name='respuesta_opcional_3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuestas',
            name='respuesta_opcional_4',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
