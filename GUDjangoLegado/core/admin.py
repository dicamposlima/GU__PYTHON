from django.contrib import admin

from core.models import AditivosNutritivos, AditivosNutritivosPicole, Conservantes, ConservantesPicoles, Ingredientes, \
    IngredientesPicole, Lotes, LotesNotaFiscal, NotasFiscais, Picoles, Revendedores, Sabores, TiposEmbalagem, \
    TiposPicole


@admin.register(AditivosNutritivos)
class AditivosNutritivosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'formula_quimica')


@admin.register(AditivosNutritivosPicole)
class AditivosNutritivosPicoleAdmin(admin.ModelAdmin):
    list_display = ('id_aditivo_nutritivo', 'id_picole')


@admin.register(Conservantes)
class ConservantesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(ConservantesPicoles)
class ConservantesPicolesAdmin(admin.ModelAdmin):
    list_display = ('id_conservante', 'id_picole')


@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(IngredientesPicole)
class IngredientesPicoleAdmin(admin.ModelAdmin):
    list_display = ('id_ingrediente', 'id_picole')


@admin.register(Lotes)
class LotesAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_picole', 'quantidade')


@admin.register(LotesNotaFiscal)
class LotesNotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('id_lote', 'id_nota_fiscal')


@admin.register(NotasFiscais)
class NotasFiscaisAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'numero_serie', 'descricao', 'id_revendedor')


@admin.register(Picoles)
class PicolesAdmin(admin.ModelAdmin):
    list_display = ('preco', 'id_sabor', 'id_tipo_embalagem', 'id_tipo_picole')


@admin.register(Revendedores)
class RevendedoresAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'contato')


@admin.register(Sabores)
class SaboresAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(TiposEmbalagem)
class TiposEmbalagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(TiposPicole)
class TiposPicoleAdmin(admin.ModelAdmin):
    list_display = ('nome',)
