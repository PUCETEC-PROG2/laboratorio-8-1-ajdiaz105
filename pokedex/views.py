from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render,get_object_or_404
from pokedex.forms import PokemonForm,TrainerForm
from .models import Pokemon,Trainer

#importación de autenticacion de usuario
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    ##pokemons = Pokemon.objects.all() ##Select * from pokedex_pokemon
    ##pokemons = Pokemon.objects.order_by('name')##Select * from pokedex_pokemon order by name
    pokemons = Pokemon.objects.order_by('type')
    trainers = Trainer.objects.order_by('level')   
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'trainers': trainers,    
        }
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    ##SELECT * FROM POKEDEX_POKEMON WHERE id=pokemon_id
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon   
        }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer,    
        }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method=='POST':
        form = PokemonForm(request.POST, request.FILES)
        form.save()
        return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'add_pokemon.html',{'form': form})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    
    return render(request, 'add_trainer.html', {'form': form})   

@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk = id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon) 
        
    return render(request, 'add_pokemon.html', {'form': form})  

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk = id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=trainer)
    
    return render(request, 'add_trainer.html', {'form': form})

@login_required
def delete_pokemon(request, id):
     pokemon = get_object_or_404(Pokemon, pk = id)
     pokemon.delete()
     return redirect('pokedex:index')

@login_required
def delete_trainer(required, id):
    trainer = get_object_or_404(Trainer, pk = id)
    trainer.delete()
    return redirect('pokedex:index')


class CustomLoginView(LoginView):
    template_name = "login.html"