from django.contrib import admin

from .models import State
from disciplines.models import Tag


class TagInLine(admin.TabularInline):
    model = Tag
    extra = 0


@admin.register(State)
class AdminState(admin.ModelAdmin):
    inlines = [TagInLine]
    search_fields = ('title',)
