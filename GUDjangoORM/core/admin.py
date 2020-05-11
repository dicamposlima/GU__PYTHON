from django.contrib import admin

from core.models import Chassi, Carro, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')
    list_editable = ('preco',)
    empty_value_display = 'unknown'

    def get_motoristas(self, obj):
        return ', '.join([m.first_name for m in obj.motoristas.all()])
    get_motoristas.short_description = 'Motoristas'
    get_motoristas.empty_value_display = '???'

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
