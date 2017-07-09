# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_profile_association'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.State'),
        ),
    ]