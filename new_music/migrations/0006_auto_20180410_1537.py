# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_music', '0005_auto_20180410_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maingenre',
            old_name='genre',
            new_name='name',
        ),
    ]
