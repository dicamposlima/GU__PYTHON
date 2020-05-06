from django.contrib import admin

from .models import Cliente, Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_editable = ('estoque',)
    list_filter = ('nome',)
    list_display_links = ('nome',)
    ordering = ('nome',)
    popup_response_template = ('nome',)
    search_fields = ('nome',)
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
