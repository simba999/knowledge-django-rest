from __future__ import unicode_literals

from django.db import models
from users.model import Users
from categories.models import Categories
from solution.models import Types
from notebook.models import Notebook
from solutiondetail.models import SolutionDetail
from price.models import Price

# Create your models here.
STATUS_CHOICE = [-1, 0, 1]


class Solution(models.Model):
    """
        Solution model
    """
    category = models.ForeignKey(Categories, default=0)
    type_id = models.ForeignKey(Types, default=0)
    solutiondetail = models.ForeignKey(SolutionDetail, default=0)
    price = models.ForeignKey(Price, default=0)
    workflow_id = models.IntegerField(null=True)
    tags = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    author = models.ForeignKey(Users)
    # status = models.IntegerField(choice=STATUS_CHOICE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# class SolutionLibrary(models.Model):
#   """
#   """
