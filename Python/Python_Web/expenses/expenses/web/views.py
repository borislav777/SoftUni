from django.shortcuts import render, redirect

from expenses.web.forms import CreateProfile, CreateExpense, EditExpense, DeleteExpense, EditProfile, DeleteProfile
from expenses.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    if not profile:
        return redirect('create profile page')

    budget_left = profile.budget - sum(el.price for el in expenses)
    profile.budget = budget_left

    context = {
        'expenses': expenses,
        'profile': profile,
        'budget_left': budget_left,

    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpense(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = CreateExpense()

    context = {
        'form': form,
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpense(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = EditExpense(instance=expense)

    context = {
        'form': form,
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpense(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = DeleteExpense(instance=expense)

    context = {
        'form': form,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    total_items = len(expenses)
    budget_left = profile.budget - sum(el.price for el in expenses)
    context = {
        'profile': profile,
        'total_items': total_items,
        'budget_left': budget_left,

    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = CreateProfile()

    context = {
        'form': form,
        'dont_have_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:

        form = EditProfile(instance=profile)

    context = {
        'form': form,

    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = DeleteProfile(instance=profile)

    context = {
        'form': form,

    }
    return render(request, 'profile-delete.html', context)
