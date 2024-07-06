from django.contrib import admin
from .models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class Pokemonadmin(admin.ModelAdmin):
    pass
