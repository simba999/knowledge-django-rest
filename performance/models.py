from __future__ import unicode_literals

from django.db import models
from users.models import Users, UserGroup
from solution.models import Solution
from notebook.models import Notebook


# Create your models here.
class Performance(models.Model):
    user = models.ForeignKey(Users)
    usergroup = models.ForeignKey(UserGroup)
    solution = models.ForeignKey(Solution)
    notebook = models.ForeignKey(Notebook)
    # results = 
    ABTest = models.IntegerField(default=1)
    Date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)