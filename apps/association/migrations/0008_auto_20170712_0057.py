# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0007_association_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='group',
        ),
        migrations.AddField(
            model_name='association',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='association',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]