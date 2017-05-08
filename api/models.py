from __future__ import unicode_literals

from django.db import models


class UserGroup(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    parent_id = models.IntegerField(default=0)
    group = models.ForeignKey('UserGroup')
    tags = models.CharField(max_length=255, null=True, blank=True, default=None)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_description = models.CharField(max_length=255, null=True, blank=True, default=None)
    api_paypal = models.CharField(max_length=255, null=True, blank=True, default=0)
    api_payment = models.CharField(max_length=255, null=True, blank=True, default=0)
    commissions = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_rate = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_total = models.DecimalField(max_digits=18, decimal_places=8, default=0)
    commission_monthtodata = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    number_transaction = models.IntegerField(default=0)
    trend = models.IntegerField(default=0)
    potential_place = models.IntegerField(default=0)
    potential_earning = models.IntegerField(default=0)
    total_commission = models.IntegerField(default=0)
    total_purchase = models.FloatField(default=0)
    proj_earning_to_date = models.IntegerField(default=0)
    proj_earning_overall = models.IntegerField(default=0)
    proj_place_to_date = models.IntegerField(default=0)
    proj_place_overall = models.IntegerField(default=0)
    noteworthy = models.IntegerField(default=0)
    redeem_state = models.IntegerField(default=0)
    datascientist_reg = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class NotebookType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SolutionType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

