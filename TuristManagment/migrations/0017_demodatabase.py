# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuristManagment', '0016_auto_20171217_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='demodatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col1', models.IntegerField()),
                ('col2', models.CharField(max_length=100)),
            ],
        ),
    ]