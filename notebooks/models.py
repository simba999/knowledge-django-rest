from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Notebooks(models.Model):
    """
    """
    solution = models.ForeignKey('Solutions', default=0)
    category = models.ForeignKey('Categories', default=0)
    type_id = models.ForeignKey('Types', default=0)
    jupyternotebook_ID = models.IntegerField()
    graphdatabase_ID = models.IntegerField()
    performance = models.ForeignKey('Performance', default=0)
    price = models.ForeignKey('Price', default=0)
    accessparameters = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    datasource  = models.CharField(max_length=255)
    datafields = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    author = models.ForeignKey('Users')
    # status = models.IntegerField()
    created_at = models.DateTiemField(add_auto_now=True)
    updated_at = models.DateTiemField(add_auto_now=True)


