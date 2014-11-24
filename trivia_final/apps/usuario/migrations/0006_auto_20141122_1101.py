# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temas',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='temas_p',
            field=models.ManyToManyField(to='usuario.temas'),
            preserve_default=True,
        ),
    ]
