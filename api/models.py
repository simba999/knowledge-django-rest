from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User as AdminMember
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=AdminMember)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         token = Token.objects.create(user=instance)
#         print token.key


class UserGroup(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey('Category', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email, username=username)
        # user.password = make_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user
        return None

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(models.Model):
    user = models.OneToOneField(AdminMember, on_delete=models.CASCADE)
    parent_id = models.IntegerField(default=0)
    group = models.ForeignKey('UserGroup', null=True, blank=True, default=None)
    tags = models.CharField(max_length=255, null=True, blank=True, default=None)
    # username = models.CharField(max_length=255, unique=True)
    # email = models.CharField(max_length=255, unique=True, default=None)
    # password = models.CharField(max_length=255)
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
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    # objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.user.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.user.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# @receiver(post_save, sender=AdminMember)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)

# @receiver(post_save, sender=AdminMember)
# def save_user(sender, instance, **kwargs):
#     instance.user.save()


class Category(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class NotebookType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SolutionType(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

