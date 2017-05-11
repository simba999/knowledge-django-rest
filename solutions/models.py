from __future__ import unicode_literals

from django.db import models
from api.models import User, Category, UserGroup, NotebookType, SolutionType


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
    user = models.ForeignKey(User, default=0, related_name="user_solution")
    usergroup_ID = models.ForeignKey(UserGroup)
    type = models.ForeignKey(SolutionType, default=0)
    notebook = models.ForeignKey('Notebook', default=0, null=True, blank=True, related_name='solutions_notebook')
    library_id = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('Solution', default=None, null=True, blank=True)
    price = models.ForeignKey("Price", blank=True, null=True, related_name='solutions_price')
    workflow_id = models.IntegerField(null=True)
    tags = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    rating = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    ensemble = models.ForeignKey('Ensemble', null=True, blank=True)
    metaensemble = models.ForeignKey('MetaEnsemble', null=True, blank=True)
    dataset = models.ForeignKey('Dataset', blank=True, null=True, related_name='solutions_dataset')
    author = models.ForeignKey(User, related_name="author_solution")
    status = models.IntegerField(choices=SOLUTION_STATUS_CHOICE, default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_notebooks(self):
        return "\n".join([p.notebook for p in self.notebook.all()])


class Ensemble(models.Model):
    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    parent = models.ForeignKey('Ensemble', null=True, blank=True)
    foreign_id = models.IntegerField(null=True, blank=True)
    foreign_type = models.IntegerField(choices=ENSEMBLE_FOREIGN_TYPE, default=0)
    performance = models.ForeignKey('Performance', default=0, null=True, related_name='ensembles_performance')
    name = models.CharField(max_length=255)
    status = models.IntegerField(choices=ENSEMBLE_CHOICE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Performance(models.Model):
    user = models.ForeignKey(User)
    usergroup = models.ForeignKey(UserGroup)
    solution = models.ForeignKey('Solution', null=True, blank=True)
    notebook = models.ForeignKey('Notebook', null=True, blank=True, related_name='performances_notebook')
    ensemble = models.ForeignKey('Ensemble', null=True, blank=True, related_name='performances_ensemble')
    results = models.BinaryField(null=True, blank=True)
    ABTest = models.IntegerField(default=1)
    PredictionAccuracyScore = models.IntegerField(default=0)
    ChangefromPrevious = models.IntegerField(default=0)
    PredictedImpact = models.IntegerField(default=0)
    RecordsinFile = models.IntegerField(default=0)
    DateRun = models.DateTimeField(null=True, blank=True)
    PerformanceResult = models.ForeignKey('PerformanceResult', null=True, blank=True)   
    Date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Notebook(models.Model):
    """
    """
    solution = models.ForeignKey('Solution', blank=True, null=True, related_name='notebooks_solution')
    category = models.ForeignKey(Category, default=0)
    parent = models.ForeignKey('Notebook', null=True, blank=True, default=None)
    type = models.ForeignKey(NotebookType, default=0, blank=True, null=True)
    jupyternotebook_ID = models.IntegerField(default=0)
    graphdatabase_ID = models.IntegerField(default=0)
    performance = models.ForeignKey('Performance', blank=True, null=True, related_name='notebooks_performance')
    price = models.ForeignKey('Price', blank=True, null=True, related_name='notebooks_price')
    accessparameters = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    datasource  = models.CharField(max_length=255)
    datafields = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.ForeignKey(User, default=None)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


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
    user = models.ForeignKey(User, related_name="user_dataset")
    solution = models.ForeignKey('Solution', null=True, blank=True, related_name='datasets_solution')
    category = models.ForeignKey(Category)
    type = models.IntegerField(default=0)
    price = models.ForeignKey("Price", blank=True, null=True, related_name='datasets_price')
    accessparameters = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    datafields = models.BinaryField()
    author = models.ForeignKey(User, related_name="author_dataset")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class DataField(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name='user_datafields')
    solution = models.ForeignKey('Solution', null=True, blank=True)
    dataset = models.ForeignKey('DataSet', default=0, null=True, blank=True)
    price = models.ForeignKey('Price', blank=True, null=True, related_name='prices_datafield')
    accessparameters = models.CharField(max_length=255, null=True, blank=True, default=None)
    description = models.CharField(max_length=255)
    datatype = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='author_datafield')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class Price(models.Model):
    user = models.ForeignKey(User)
    solution = models.ForeignKey('Solution', null=True, blank=True, related_name='prices_solution')
    notebook = models.ForeignKey('Notebook', null=True, blank=True, related_name='prices_notebook')
    datafield = models.ForeignKey('DataField', null=True, blank=True, related_name='prices_datafield')
    dataset = models.ForeignKey('DataSet', null=True, blank=True, related_name='prices_dataset')
    price = models.FloatField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class PerformanceResult(models.Model):
    logfile = models.CharField(max_length=255, null=True, blank=True)
    outcome = models.CharField(max_length=255, null=True, blank=True)


