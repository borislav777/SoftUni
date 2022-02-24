from django.shortcuts import render, redirect

from notes.web.forms import CreateProfile, CreateNote, DeleteNote, DeleteProfile
from notes.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateProfile()
    context = {
        'dont_have_profile': True,
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateNote()
    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateNote(instance=note)
    context = {
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = DeleteNote(instance=note)
    context = {
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = get_profile()
    all_notes = len(Note.objects.all())

    context = {
        'profile': profile,
        'all_notes': all_notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    form = DeleteProfile(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('home page')
