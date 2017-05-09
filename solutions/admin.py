from django.contrib import admin
from .models import Notebook, Solution, Ensemble, Performance, MetaEnsemble, Price, DataSet, DataField

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Performance)
admin.site.register(Ensemble)
admin.site.register(MetaEnsemble)
admin.site.register(Price)
admin.site.register(DataSet)
admin.site.register(DataField)
admin.site.register(Solution)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('Tags')
