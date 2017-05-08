from django.contrib import admin
from .models import User, UserGroup, Category, SolutionType, NotebookType
# Register your models here.
admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(Category)
admin.site.register(SolutionType)
admin.site.register(NotebookType)
