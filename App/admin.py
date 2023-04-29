from django.contrib import admin
from App.models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'species', 'gender','image']
    search_fields = ['name']
    list_per_page = 8


admin.site.register(Character, CharacterAdmin)
