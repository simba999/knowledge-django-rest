# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessparameters', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('datatype', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_datafield', to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0)),
                ('accessparameters', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('datafields', models.BinaryField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_dataset', to='api.User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ensemble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_id', models.IntegerField(blank=True, null=True)),
                ('foreign_type', models.IntegerField(choices=[(0, 'ensemble'), (1, 'solution')], default=0)),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(-1, 'requested'), (0, 'complete'), (1, 'none')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Ensemble')),
            ],
        ),
        migrations.CreateModel(
            name='MetaEnsemble',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_id', models.IntegerField()),
                ('foreign_id', models.IntegerField()),
                ('foreign_type', models.IntegerField(choices=[(0, 'ensemble'), (1, 'solution')], default=0)),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(-1, 'requested'), (0, 'complete'), (1, 'none')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jupyternotebook_ID', models.IntegerField(default=0)),
                ('graphdatabase_ID', models.IntegerField(default=0)),
                ('accessparameters', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('datasource', models.CharField(max_length=255)),
                ('datafields', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.User')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('ensemble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notebooks_ensemble', to='solutions.Ensemble')),
                ('metaensemble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notebooks_metaensemble', to='solutions.MetaEnsemble')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Notebook')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.BinaryField(blank=True, null=True)),
                ('ABTest', models.IntegerField(default=1)),
                ('PredictionAccuracyScore', models.IntegerField(default=0)),
                ('ChangefromPrevious', models.IntegerField(default=0)),
                ('PredictedImpact', models.IntegerField(default=0)),
                ('RecordsinFile', models.IntegerField(default=0)),
                ('DateRun', models.DateTimeField(blank=True, null=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logfile', models.CharField(blank=True, max_length=255, null=True)),
                ('outcome', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('datafield', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices_datafield', to='solutions.DataField')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices_dataset', to='solutions.DataSet')),
                ('notebook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices_notebook', to='solutions.Notebook')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_id', models.IntegerField(blank=True, null=True)),
                ('workflow_id', models.IntegerField(null=True)),
                ('tags', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('rating', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(-1, 'requested'), (1, 'complete')], default=-1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_solution', to='api.User')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions_dataset', to='solutions.DataSet')),
                ('ensemble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Ensemble')),
                ('metaensemble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.MetaEnsemble')),
                ('notebook', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions_notebook', to='solutions.Notebook')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Solution')),
                ('price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions_price', to='solutions.Price')),
                ('type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.SolutionType')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_solution', to='api.User')),
                ('usergroup_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserGroup')),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices_solution', to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='price',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='performance',
            name='PerformanceResult',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.PerformanceResult'),
        ),
        migrations.AddField(
            model_name='performance',
            name='ensemble',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performances_ensemble', to='solutions.Ensemble'),
        ),
        migrations.AddField(
            model_name='performance',
            name='notebook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performances_notebook', to='solutions.Notebook'),
        ),
        migrations.AddField(
            model_name='performance',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='performance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='performance',
            name='usergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserGroup'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='performance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notebooks_performance', to='solutions.Performance'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notebooks_price', to='solutions.Price'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notebooks_solution', to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='type',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.NotebookType'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='performance',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ensembles_performance', to='solutions.Performance'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='usergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserGroup'),
        ),
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
        migrations.AddField(
            model_name='dataset',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets_price', to='solutions.Price'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasets_solution', to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dataset', to='api.User'),
        ),
        migrations.AddField(
            model_name='datafield',
            name='dataset',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.DataSet'),
        ),
        migrations.AddField(
            model_name='datafield',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices_datafield', to='solutions.Price'),
        ),
        migrations.AddField(
            model_name='datafield',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='datafield',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_datafields', to='api.User'),
        ),
    ]
