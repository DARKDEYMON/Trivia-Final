# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_auto_20141123_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestas',
            name='correcta',
        ),
    ]
