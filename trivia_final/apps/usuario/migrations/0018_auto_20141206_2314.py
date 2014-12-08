# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0017_partida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partida',
            old_name='nombre',
            new_name='nombre_de_partida',
        ),
    ]
