# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP', '0012_auto_20161109_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.CharField(choices=[('File', 'File'), ('Image', 'Image'), ('Text', 'Text')], default='text', max_length=127),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_title',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Instructor', 'Instructor'), ('HR', 'HR'), ('Participant', 'Participant')], default='Participant', max_length=127),
        ),
    ]
