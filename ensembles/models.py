from __future__ import unicode_literals

from django.db import models
from users.models import Users, UserGroup
from performance.models import Performance


# Create your models here.
class Ensembles(models.Model):
    user = models.ForeignKey('Users')
    usergroup = models.ForeignKey('UserGroup')
    # foreign_id = models.ForeignKey()
    foreign_type = models.IntegerField()
    performance = models.ForeignKey('Performance')
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
