# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='Post')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(verbose_name='auto_now_add = True')),
                ('updated_at', models.DateTimeField(verbose_name='auto_now = True')),
                ('reply', models.TextField(blank=True)),
            ],
        ),
    ]
