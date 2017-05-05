from __future__ import unicode_literals

from django.db import models

FOREIGN_TYPE = [
    'notebook',
    'solution',
    'ensemble',
    'metaensemble'
]


# Create your models here.
class SolutionLibrary(models.Model):
    user = models.ForeignKey('Users')
    customesolution = models.ForeignKey('CustomSolution')
    foreign_id = models.IntegerField()
    # foreign_type = models.ChoiceField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)