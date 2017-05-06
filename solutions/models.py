from __future__ import unicode_literals

from django.db import models
from users.models import User, Category, Price, Type, UserGroup


# Create your models here.
class Solution(models.Model):
    """
        Solution model
    """
    REQUESTED = -1
    COMPLETE = 1

    SOLUTION_STATUS_CHOICE = (
        (REQUESTED, 'requested'),
        (COMPLETE, 'complete'),
        )

    category = models.ForeignKey(Category, default=0)
    type_id = models.ForeignKey(Type, default=0)
    solutionparent = models.ForeignKey('Solution', default=0)
    price = models.ManyToManyField(Price, default=0)
    workflow_id = models.IntegerField(null=True)
    tags = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=SOLUTION_STATUS_CHOICE, default=REQUESTED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Ensemble(models.Model):
    ENSEMBLE_CHOICE = (
        (-1, 'requested'),
        (0, 'complete'),
        (1, 'none')
        )

    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    foreign_id = models.IntegerField()
    foreign_type = models.IntegerField()
    performance = models.ForeignKey('Performance')
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ENSEMBLE_CHOICE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Performance(models.Model):
    PERFORMANCE_CHOICE = (
        (-1, 'A/B'),
        (0, 'onearmedbandit'),
        (1, 'none')
        )

    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    solution = models.ForeignKey('Solution')
    # results = 
    ABTest = models.IntegerField(default=1)
    Date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Notebook(models.Model):
    """
    """
    solution = models.ManyToManyField("Solution", default=0)
    category = models.ForeignKey(Category, default=0)
    type_id = models.ForeignKey(Type, default=0)
    jupyternotebook_ID = models.IntegerField()
    graphdatabase_ID = models.IntegerField()
    performance = models.ManyToManyField('Performance', default=0)
    price = models.ManyToManyField(Price, default=0)
    accessparameters = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    datasource  = models.CharField(max_length=255)
    datafields = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.ManyToManyField(User)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class CustomSolution(models.Model):
    """
    """
    user = models.ForeignKey(User)
    ensemble = models.ForeignKey('Ensemble')
    solution = models.ManyToManyField('Solution')
    # metaensemble = models.ForeignKey(MetaEnsemble)
    notebook = models.ForeignKey('Notebook')
    # dataset = models.ForeignKey(Dataset)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SolutionLibrary(models.Model):
    LIBRARY_CHOICE = (
        (0, 'notebook'),
        (1, 'solution'),
        (2, 'ensemble'),
        (3, 'metaensemble'),
        (4, 'dataset'),
        )

    user = models.ForeignKey(User)
    customesolution = models.ForeignKey('CustomSolution')
    foreign_id = models.IntegerField()
    foreign_type = models.IntegerField(choices=LIBRARY_CHOICE, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class MetaEnsembel(models.Model):
    META_ENSEMBLE_CHOICE = (
        (0, 'ensemble'),
        (1, 'solution')
        )

    id = models.BigIntegerField(primary_key=True)
    collection_id = models.IntegerField()
    foreign_id = models.IntegerField()
    foreign_type = models.IntegerField(choices=META_ENSEMBLE_CHOICE, default=0)
    name = models.CharField(max_length=255)
    # status = 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



