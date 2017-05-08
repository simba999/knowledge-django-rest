# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-06 18:51
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField()),
                ('tags', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=60)),
                ('remember_token', models.CharField(max_length=100)),
                ('images', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('profile_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('profile_description', models.TextField(blank=True, default=None, null=True)),
                ('api_paypal', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('api_payment', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('commissions', models.DecimalField(decimal_places=8, default=0, max_digits=15)),
                ('commission_rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('commission_total', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=12)),
                ('commission_monthtodata', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=12)),
                ('number_transaction', models.IntegerField(default=0)),
                ('trend', models.IntegerField(choices=[(0, 'not Trend'), (1, 'Trending')], default=0)),
                ('total_earned', models.IntegerField(default=0)),
                ('place', models.IntegerField(default=0)),
                ('potential_place', models.IntegerField(default=0)),
                ('potential_earning', models.IntegerField(default=0)),
                ('total_commission', models.IntegerField(default=0)),
                ('total_purchase', models.DecimalField(decimal_places=8, default=0, max_digits=15)),
                ('proj_earning_to_date', models.IntegerField(default=0)),
                ('proj_earning_overall', models.IntegerField(default=0)),
                ('proj_place_to_date', models.IntegerField(default=0)),
                ('proj_place_overall', models.IntegerField(default=0)),
                ('noteworthy', models.IntegerField(choices=[(0, 'not noteworthy'), (1, 'noteworthy')], default=0)),
                ('redeem_state', models.IntegerField(choices=[(0, 'not redeemed'), (1, 'redeemed')], default=0)),
                ('datascientist_reg', models.IntegerField(choices=[(0, 'buiness user'), (1, 'data scientist'), (2, 'data seller')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('caps', models.TextField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserGroup'),
        ),
    ]