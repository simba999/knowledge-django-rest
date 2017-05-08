from django.contrib import admin
from .models import Notebook, Solution, Ensemble, Performance, MetaEnsemble, Price

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Solution)
admin.site.register(Performance)
admin.site.register(Ensemble)
admin.site.register(MetaEnsemble)
admin.site.register(Price)
