# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_music', '0015_auto_20180411_0922'),
    ]

    operations = [
        migrations.RenameField('SubGenre', 'name', 'subname'),
    ]