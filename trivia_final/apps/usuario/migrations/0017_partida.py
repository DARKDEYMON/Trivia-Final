# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0016_preguntas_lista'),
    ]

    operations = [
        migrations.CreateModel(
            name='partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('max_jugadores', models.IntegerField()),
                ('num_preguntas', models.IntegerField()),
                ('tiempo_maximo', models.IntegerField(choices=[(10, 10), (20, 20), (30, 30)])),
                ('acabada', models.BooleanField(default=False)),
                ('temas', models.ManyToManyField(to='usuario.temas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
