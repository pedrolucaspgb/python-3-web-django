from django.contrib import admin

# Register your models here.
from .models import Course

"""Classe que importa o admin.ModelAdmin para fazer modificações do model do admins. 
o django tem varias opções para fazer essas mudanças
"""
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "start_date",'created_at']# pode ser usado list e tupla
    search_fields = ["name", "slug"]
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Course, CourseAdmin)
