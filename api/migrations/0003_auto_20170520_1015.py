# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-20 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170520_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='Category',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='remember_token',
        ),
    ]