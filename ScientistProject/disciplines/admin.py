from django.contrib import admin

from .models import Disciplines


@admin.register(Disciplines)
class AdminState(admin.ModelAdmin):
    search_fields = ('name',)
