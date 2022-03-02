from django.shortcuts import render, redirect

from exam.music_app.forms import CreateProfile, AddAlbum, EditAlbum, DeleteAlbum, DeleteProfile
from exam.music_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return redirect('create profile page')

    context = {
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AddAlbum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = AddAlbum()

    context = {
        'form': form,

    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditAlbum(instance=album)

    context = {
        'form': form,
        'album': album,

    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = DeleteAlbum(instance=album)

    context = {
        'form': form,
        'album': album,

    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    total_albums = len(albums)

    context = {
        'profile': profile,
        'total_albums': total_albums,
    }

    return render(request, 'profile-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST)
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
