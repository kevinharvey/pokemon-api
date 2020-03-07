from django.contrib import admin

from .models import Pokemon, Attack


class AttackInline(admin.TabularInline):
    model = Attack


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    inlines = (AttackInline,)