from __future__ import unicode_literals

from django.db import models
from users.models import Users, UserGroup
from solution.models import Solution
from notebook.models import Notebook
from ensembles.models import Ensemble
from metaensemble.models import MetaEnsemble
from dataset.models import Dataset


# Create your models here.
class CustomSolution(models.Model):
    """
    """
    user = models.ForeignKey(Users)
    solution = models.ForeignKey(Solution)
    ensemble = models.ForeignKey(Ensemble)
    metaensemble = models.ForeignKey(MetaEnsemble)
    notebook = models.ForeignKey(Notebook)
    dataset = models.ForeignKey(Dataset)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

