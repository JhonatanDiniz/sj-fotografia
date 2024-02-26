from django.contrib import admin
from fotografia.models import Corretor

class ListaCorretores(admin.ModelAdmin):
    list_display = ("id", "nome", "agencia", "telefone")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome", "telefone")
    list_filter = ("agencia", )
    list_per_page = 10

admin.site.register(Corretor, ListaCorretores)
