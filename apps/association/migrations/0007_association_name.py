# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0006_auto_20170712_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
