from django.shortcuts import render, redirect

from online_library.web.forms import CreateProfile, CreateBook, EditBook, DeleteBook, EditProfile, DeleteProfile
from online_library.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    context = {
        'books': books,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = CreateBook()
    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.all().get(pk=pk)
    if request.method == 'POST':
        form = EditBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = EditBook(instance=book)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.all().get(pk=pk)

    form = DeleteBook(request.POST, instance=book)
    form.save()
    return redirect('home page')


def book_details(request, pk):
    book = Book.objects.all().get(pk=pk)

    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile,

    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = CreateProfile()
    context = {
        'form': form,
        'dont_have_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')

    form = EditProfile(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = DeleteProfile(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
