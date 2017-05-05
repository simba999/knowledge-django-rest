from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserGroup(models.Model):
    """
    """
    name = models.CharField(max_length=55)
    caps = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Users(models.Model):
    """
    """
    parent_id = models.IntegerField()
    group = models.ForeignKey('UserGroup')
    tags = models.CharField(max_length=255, null=True, blank=True, default=None)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # password = models.CharField(max_length=60)
    remember_token = models.CharField(max_length=100)
    images = models.CharField(max_length=255, null=True)
    profile_name = models.CharField(max_length=255, null=True)
    profile_description = models.TextField(null=True)
    api_paypal = models.CharField(null=True, default=0)
    api_payment = models.CharField(null=True, default=0)
    # commissions = models.DoubleField(default=0)
    commission_rate = models.DoubleField(default=0)
    commission_total = models.DoubleField(default=0)
    commission_monthtodata = models.DoubleField(default=0)
    number_transaction = models.IntegerField(default=0)
    # trend = 
    total_earned = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    potential_place = models.IntegerField(default=0)
    potential_earning = models.IntegerField(default=0)
    total_commission = models.IntegerField(default=0)
    total_purchase = models.DoubleField(default=0)
    proj_earning_to_date = models.IntegerField(default=0)
    proj_earning_overall = models.IntegerField(default=0)
    proj_place_to_date = models.IntegerField(default=0)
    proj_place_overall = models.IntegerField(default=0)
    # noteworthy = model.IntegerField(default=0)
    # redeem_state = models.IntegerField()
    datascientist_reg = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# class Price(models.Model):
#     user = 
