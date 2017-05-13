# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_auto_20170513_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='ensemble',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets_ensemble', to='solutions.Ensemble'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='metaensemble',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets_metaensemble', to='solutions.MetaEnsemble'),
        ),
    ]
