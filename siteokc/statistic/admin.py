from django.contrib import admin
from .models import *


# Register your models here.


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'number_of_calls', 'subdivisions', 'add_user')
    list_display_links = ('id', 'date')
    search_fields = ('id', 'date')
    list_filter = ('subdivisions', 'date')


class SubdivisionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Register your models here.


admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Subdivisions, SubdivisionsAdmin)
