# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0013_auto_20170716_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association',
            old_name='identifier',
            new_name='user',
        ),
    ]
