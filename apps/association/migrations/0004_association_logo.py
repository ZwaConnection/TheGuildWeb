# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_association_initials'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='logo',
            field=models.ImageField(blank=True, upload_to='Images/Association/logo'),
        ),
    ]
