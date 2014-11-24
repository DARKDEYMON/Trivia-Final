# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20141122_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('pregunta', models.ForeignKey(to='usuario.preguntas')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rate',
            },
            bases=(models.Model,),
        ),
    ]
