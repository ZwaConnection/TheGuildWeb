# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20170731_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
