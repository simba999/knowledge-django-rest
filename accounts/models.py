from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User as AdminMember
from rest_framework.authtoken.models import Token 

@receiver(post_save, sender=AdminMember)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)