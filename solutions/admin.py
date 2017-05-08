from django.contrib import admin
from .models import Notebook, Solution, SolutionLibrary, Ensemble, Performance, CustomSolution, MetaEnsemble, Price

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Solution)
admin.site.register(SolutionLibrary)
admin.site.register(Performance)
admin.site.register(Ensemble)
admin.site.register(CustomSolution)
admin.site.register(MetaEnsemble)
admin.site.register(Price)
