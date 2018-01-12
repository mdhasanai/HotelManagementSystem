# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TuristManagment', '0015_remove_department_deptid'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='deptid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TuristManagment.Department'),
        ),
    ]
