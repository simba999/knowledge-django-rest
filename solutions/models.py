from __future__ import unicode_literals

from django.db import models
from api.models import User, Category, Type, UserGroup, NotebookType, SolutionType


# Create your models here.
REQUESTED = -1
COMPLETE = 1

SOLUTION_STATUS_CHOICE = (
    (-1, 'requested'),
    (1, 'complete'),
    )

ENSEMBLE_CHOICE = (
    (-1, 'requested'),
    (0, 'complete'),
    (1, 'none')
    )

ENSEMBLE_FOREIGN_TYPE = (
    (0, 'ensemble'),
    (1, 'solution'),
    )

PERFORMANCE_CHOICE = (
    (-1, 'A/B'),
    (0, 'onearmedbandit'),
    (1, 'none')
    )

LIBRARY_CHOICE = (
    (0, 'notebook'),
    (1, 'solution'),
    (2, 'ensemble'),
    (3, 'metaensemble'),
    (4, 'dataset'),
    )

META_ENSEMBLE_CHOICE = (
    (-1, 'requested'),
    (0, 'complete'),
    (1, 'none')
    )


class Solution(models.Model):
    """
        Solution model
    """
    category = models.ForeignKey(Category, default=0)
    user = models.ForeignKey(User, default=0)
    usergroup_ID = models.ForeignKey('UserGroup')
    type = models.ForeignKey(SolutionType, default=0)
    library_id = models.IntegerField()
    solutionparent = models.ForeignKey('Solution', default=0, null=True)
    price = models.ManyToManyField("Price", blank=True)
    workflow_id = models.IntegerField(null=True)
    tags = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    ensemble = models.ForeignKey('Ensemble', null=True)
    metaensemble = models.ForeignKey('MetaEnsemble', null=True)
    dataset = models.ManyToManyField('Dataset', blank=True)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=SOLUTION_STATUS_CHOICE, default=-1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Ensemble(models.Model):
    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    foreign_id = models.IntegerField(null=True, blank=True)
    foreign_type = models.IntegerField(choices=ENSEMBLE_FOREIGN_TYPE, default=0)
    performance = models.ForeignKey('Performance', default=0, null=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ENSEMBLE_CHOICE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Performance(models.Model):
    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    solution = models.ForeignKey('Solution', null=Ture)
    results = models.BinaryField(null=True, blank=True)
    ABTest = models.IntegerField(default=1)
    Date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Notebook(models.Model):
    """
    """
    solution = models.ManyToManyField('Solution', blank=True)
    category = models.ForeignKey(Category, default=0)
    parent = models.ForeignKey('Notebook', null=True)
    type = models.ForeignKey(NotebookType, default=0)
    jupyternotebook_ID = models.IntegerField()
    graphdatabase_ID = models.IntegerField()
    performance = models.ManyToManyField('Performance', blank=True)
    price = models.ManyToManyField('Price', blank=True)
    accessparameters = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    datasource  = models.CharField(max_length=255)
    datafields = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.ManyToManyField(User)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


# class SolutionLibrary(models.Model):
#     user = models.ForeignKey(User)
#     customsolution = models.ForeignKey('CustomSolution')
#     usergroup_ID = models.ForeignKey(User)
#     foreign_id = models.IntegerField()
#     foreign_type = models.IntegerField(choices=LIBRARY_CHOICE, default=0)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)


class MetaEnsemble(models.Model):
    id = models.BigIntegerField(primary_key=True)
    collection_id = models.IntegerField()
    foreign_id = models.IntegerField()
    foreign_type = models.IntegerField(choices=META_ENSEMBLE_CHOICE, default=0)
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=META_ENSEMBLE_CHOICE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class DataSet(models.Model):
    user = models.ForeignKey(User)
    # solution = models.ForeignKey("Solution")
    category = models.ForeignKey(Category)
    # type = models.ForeignKey(Type)
    price = models.ManyToManyField("Price", blank=True)
    accessparameters = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    datafields = models.BinaryField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class DataField(models.Model):
    dataset = models.ForeignKey('DataSet', default=0)
    price = models.ManyToManyField('Price')
    accessparameters = models.CharField(max_length=255, null=True, blank=True, default=None)
    description = models.CharField(max_length=255)
    datatype = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class Price(models.Model):
    user = models.ForeignKey(User)
    # datafield = models.ForeignKey(DataField)
    price = models.FloatField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)





