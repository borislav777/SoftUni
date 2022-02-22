from django.shortcuts import render, redirect

from petstagram_workshop.forms import CreateForm, AddPet, AddPhoto, EditPhoto, DeletePet, EditProfile
from petstagram_workshop.main_app.models import Profile, PetPhoto, Pet
import sys


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = set(PetPhoto.objects.prefetch_related('tagged_pets') \
                     .filter(tagged_pets__user_profile=profile))

    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)


def show_profile(request):
    profile = get_profile()
    pets = set(Pet.objects.filter(user_profile_id=profile))
    pet_photos = set(PetPhoto.objects.filter(tagged_pets__user_profile=profile))
    total_image = len(pet_photos)
    total_likes = sum([x.likes for x in pet_photos])
    context = {
        'profile': profile,
        'pets': pets,
        'total_image': total_image,
        'total_like': total_likes,
    }
    return render(request, 'profile_details.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }

    return render(request, 'photo_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        create_form = CreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    else:
        create_form = CreateForm()

    context = {
        'create_form': create_form,
    }
    return render(request, 'profile_create.html', context)


def add_pet(request):
    if request.method == 'POST':
        add_form = AddPet(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('profile')
    else:
        add_form = AddPet(initial={'user_profile': get_profile()})

    context = {
        'add_form': add_form,
    }
    return render(request, 'pet_create.html', context)


def add_pet_photo(request):
    if request.method == 'POST':
        add_photo = AddPhoto(request.POST, request.FILES)
        if add_photo.is_valid():
            add_photo.save()
            return redirect('dashboard')
    else:
        add_photo = AddPhoto()

    context = {
        'add_photo': add_photo,
    }
    return render(request, 'photo_create.html', context)


def edit_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        edit_photo = EditPhoto(request.POST, instance=photo)
        if edit_photo.is_valid():
            edit_photo.save()
            return redirect('pet photo details', pk)
    else:
        edit_photo = EditPhoto(instance=photo)

    context = {
        'photo': photo,
        'edit_photo': edit_photo,
    }

    return render(request, 'photo_edit.html', context)


def delete_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    photo.delete()
    return redirect('dashboard')


def edit_pet_page(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        edit_pet = AddPet(request.POST, instance=pet)
        if edit_pet.is_valid():
            edit_pet.save()
            return redirect('profile')
    else:
        edit_pet = AddPet(instance=pet)

    context = {
        'pet': pet,
        'edit_pet': edit_pet,
    }
    return render(request, 'pet_edit.html', context)


def delete_pet_page(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':

        pet.delete()
        return redirect('profile')
    else:
        delete_pet = DeletePet(instance=pet)

    context = {
        'delete_pet': delete_pet,
        'pet': pet,
    }

    return render(request, 'pet_delete.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        edit_profile = EditProfile(request.POST, instance=profile)
        if edit_profile.is_valid():
            edit_profile.save()
            return redirect('profile')
    else:
        edit_profile = EditProfile(instance=profile, initial={'gender': 'Do not show'})

    context = {
        'edit_profile': edit_profile,

    }

    return render(request, 'profile_edit.html', context)


def page_not_found(request, exception):
    return render(request, '401_error.html')


def delete_profile_page(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        [p.delete() for p in list(PetPhoto.objects.filter(tagged_pets__user_profile=profile))]
        return redirect('index')

    return render(request, 'profile_delete.html')


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)
