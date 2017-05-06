# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-06 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ensemble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_id', models.IntegerField()),
                ('foreign_type', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(-1, 'requested'), (0, 'complete'), (1, 'none')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaEnsembel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('collection_id', models.IntegerField()),
                ('foreign_id', models.IntegerField()),
                ('foreign_type', models.IntegerField(choices=[(0, 'ensemble'), (1, 'solution')], default=0)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jupyternotebook_ID', models.IntegerField()),
                ('graphdatabase_ID', models.IntegerField()),
                ('accessparameters', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('datasource', models.CharField(max_length=255)),
                ('datafields', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='users.User')),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ABTest', models.IntegerField(default=1)),
                ('Date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_id', models.IntegerField()),
                ('foreign_type', models.IntegerField(choices=[(0, 'notebook'), (1, 'solution'), (2, 'ensemble'), (3, 'metaensemble'), (4, 'dataset')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('customesolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.CustomSolution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='solution',
            name='price',
        ),
        migrations.AddField(
            model_name='solution',
            name='price',
            field=models.ManyToManyField(default=0, to='users.Price'),
        ),
        migrations.AddField(
            model_name='performance',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='performance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AddField(
            model_name='performance',
            name='usergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserGroup'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='performance',
            field=models.ManyToManyField(default=0, to='solutions.Performance'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='price',
            field=models.ManyToManyField(default=0, to='users.Price'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='solution',
            field=models.ManyToManyField(default=0, to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='type_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Type'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.Performance'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='usergroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserGroup'),
        ),
        migrations.AddField(
            model_name='customsolution',
            name='ensemble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.Ensemble'),
        ),
        migrations.AddField(
            model_name='customsolution',
            name='notebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solutions.Notebook'),
        ),
        migrations.AddField(
            model_name='customsolution',
            name='solution',
            field=models.ManyToManyField(to='solutions.Solution'),
        ),
        migrations.AddField(
            model_name='customsolution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
