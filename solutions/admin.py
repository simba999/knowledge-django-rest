from django.contrib import admin
from .models import Notebook, Solution, Ensemble, Performance, Category
from .models import MetaEnsemble, Price, DataSet, DataField, Library, Vertical

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Performance)
admin.site.register(Ensemble)
admin.site.register(MetaEnsemble)
admin.site.register(Price)
admin.site.register(DataSet)
admin.site.register(DataField)
admin.site.register(Solution)
admin.site.register(Library)
admin.site.register(Vertical)
admin.site.register(Category)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('Tags')
