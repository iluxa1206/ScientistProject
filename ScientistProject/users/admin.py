from django.contrib import admin
from .models import *


@admin.register(Scientist)
class ScientistAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')

