from django.contrib import admin
from .models import *


# Register your models here.


class JournalAdmin(admin.ModelAdmin):

    list_display = ('id', 'quantity_departure', 'region', 'city', 'town', 'date_of_receipt_message', 'information',
                    'subdivisions', 'quantity_peoples', 'quantity_technics', 'departure_date',
                    'time_of_arrival_to_the_place', 'barrel_feed_time', 'area', 'localization_time', 'area2',
                    'liquidation', 'liquidation_time', 'time_return_to_location', 'type_of_fire', 'quantity_rescued',
                    'quantity_victims', 'quantity_dead', 'quantity_rescued_kids', 'quantity_victims_kids',
                    'quantity_dead_kids', 'quantity_ammunition', 'violated_conditions', 'quantity_objects')
    search_fields = ('information',)
    list_filter = ('date_of_receipt_message', )
    ordering = ('-date_of_receipt_message',)


class FireTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class SubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TownAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class NoFireAdmin(admin.ModelAdmin):

    list_display = ('id',  'date_of_receipt_message', 'information', 'departure_date',
                    'time_of_arrival_to_the_place', 'time_return_to_location')
    search_fields = ('information',)
    list_filter = ('date_of_receipt_message', )


# Register your models here.

admin.site.register(Journal, JournalAdmin)
admin.site.register(FireType, FireTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NoFire, NoFireAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Subtype, SubtypeAdmin)
