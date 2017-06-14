# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-13 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170520_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionNavigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solutionnavigations_category', to='api.Category')),
                ('category_child', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solutionnavigations_category_child', to='api.Category')),
                ('library', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Library')),
                ('solition', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solutionnavigations_vertical', to='api.Solution')),
                ('solution_child', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solutionnavigations_solution', to='api.Solution')),
                ('vertical', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='solutionnavigations_vertical', to='api.Vertical')),
            ],
        ),
    ]
