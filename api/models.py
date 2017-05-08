from __future__ import unicode_literals

from django.db import models
from decimal import Decimal


TREND_CHOICE = (
    (0, 'not Trend'),
    (1, 'Trending'),
    )

NOTEWORTHY_CHOICE = (
    (0, "not noteworthy"),
    (1, "noteworthy"),
    )

REDEEMED_CHOICE = (
    (0, "not redeemed"),
    (1, "redeemed"),
    )

BUSINESS_USER = 0
DATA_SCIENTIST = 1
DATA_SELLER = 2

DATASICENTIST_REG_CHOICE = (
    (BUSINESS_USER, 'buiness user'),
    (DATA_SCIENTIST, 'data scientist'),
    (DATA_SELLER, 'data seller'),
    )


# Create your models here.
class UserGroup(models.Model):
    """
    """
    name = models.CharField(max_length=55)
    caps = models.TextField(null=True, blank=True, default=None)
    category = models.ForeignKey('Category', blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode(self):
        return self.name


class User(models.Model):
    """
    """
    parent_id = models.IntegerField()
    group = models.ForeignKey('UserGroup')
    category = models.ForeignKey('Category')
    tags = models.CharField(max_length=255, null=True, blank=True, default=None)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=60)
    remember_token = models.CharField(max_length=100)
    image = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    profile_description = models.TextField(null=True, blank=True, default=None)
    api_paypal = models.CharField(max_length=255, default=0, null=True, blank=True)
    api_payment = models.CharField(max_length=255, default=0, null=True, blank=True)
    commissions = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    commission_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    commission_total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.0'))
    commission_monthtodata = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.0'))
    number_transaction = models.IntegerField(default=0)
    trend = models.IntegerField(choices=TREND_CHOICE, default=0)
    total_earned = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    potential_place = models.IntegerField(default=0)
    potential_earning = models.IntegerField(default=0)
    total_commission = models.IntegerField(default=0)
    total_purchase = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    proj_earning_to_date = models.IntegerField(default=0)
    proj_earning_overall = models.IntegerField(default=0)
    proj_place_to_date = models.IntegerField(default=0)
    proj_place_overall = models.IntegerField(default=0)
    noteworthy = models.IntegerField(choices=NOTEWORTHY_CHOICE, default=0)
    redeem_state = models.IntegerField(choices=REDEEMED_CHOICE, default=0)
    datascientist_reg = models.IntegerField(choices=DATASICENTIST_REG_CHOICE, default=BUSINESS_USER)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SolutionType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class NotebookType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
