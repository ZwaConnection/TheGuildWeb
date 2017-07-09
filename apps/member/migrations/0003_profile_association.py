# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_association_logo'),
        ('member', '0002_auto_20170709_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='association.Association'),
        ),
    ]
