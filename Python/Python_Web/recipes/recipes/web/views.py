from django.shortcuts import render, redirect

from recipes.web.forms import CreateRecipe, EditRecipe, DeleteRecipe
from recipes.web.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateRecipe()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = EditRecipe(instance=recipe)

    context = {
        'form': form,

    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = DeleteRecipe(instance=recipe)

    context = {
        'form': form,

    }

    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
