# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=26, unique=True)),
                ('upper', models.IntegerField()),
                ('lower', models.IntegerField()),
                ('currency', models.CharField(max_length=26, unique=True)),
            ],
        ),
    ]
