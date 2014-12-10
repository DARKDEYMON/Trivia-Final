# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0018_auto_20141206_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='jugadores_en_partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('partida', models.ForeignKey(to='usuario.partida')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='partida',
            options={'verbose_name': 'Partida', 'verbose_name_plural': 'Partidas'},
        ),
    ]
