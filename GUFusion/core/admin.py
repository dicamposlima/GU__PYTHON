from django.contrib import admin

from .models import Position, Service, Team


@admin.register(Position)
class PositionAdim(admin.ModelAdmin):
    list_display = ('position', 'active', 'modified')


@admin.register(Service)
class ServiceAdim(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified')


@admin.register(Team)
class TeamAdim(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'modified')
