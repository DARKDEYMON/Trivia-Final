# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0002_auto_20141102_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=100, null=True)),
                ('rate', models.IntegerField(default=0, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='respuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=100)),
                ('pregunta', models.ForeignKey(to='usuario.preguntas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='temas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tema', models.CharField(max_length=100, null=True)),
                ('pregunta', models.ManyToManyField(to='usuario.preguntas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
