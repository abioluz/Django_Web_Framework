from django.contrib import admin

# Register your models here.

from . import models

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin): ...

admin.site.register(models.Category, CategoryAdmin)
# admin.site.register(models.Recipe, CategoryAdmin)