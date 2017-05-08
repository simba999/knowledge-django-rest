from django.contrib import admin
from .models import User, UserGroup, Category, Type
# Register your models here.
admin.site.register(User)
admin.site.register(UserGroup)
admin.site.register(Category)
admin.site.register(Type)
