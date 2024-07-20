from django.contrib import admin
from .models import Pokemon,Trainer

# Register your models here.
@admin.register(Pokemon)
class Pokemonadmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class Traineradmin(admin.ModelAdmin):
    pass

