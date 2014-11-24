# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trivia_final.apps.usuario.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datos_adicionales_usuario',
            options={'verbose_name': 'Datos Adicionales de usuario', 'verbose_name_plural': 'Datos Adicionales de usuarios'},
        ),
        migrations.RenameField(
            model_name='datos_adicionales_usuario',
            old_name='usernamem',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='datos_adicionales_usuario',
            name='avatar',
            field=trivia_final.apps.usuario.thumbs.ImageWithThumbsField(null=True, upload_to=b'avatares/'),
        ),
    ]
