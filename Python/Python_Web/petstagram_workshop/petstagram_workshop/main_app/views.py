from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect

from petstagram_workshop.common.viewmixins import RedirectToDashboard
from petstagram_workshop.forms import AddPet, AddPhoto, EditPhoto, DeletePet, EditPet
from petstagram_workshop.main_app.models import PetPhoto, Like


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


class PetPhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        context['is_like'] = Like.objects.filter(user=self.request.user)

        return context


class CreatePetPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'main/photo_create.html'
    model = AddPhoto
    form_class = AddPhoto
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    template_name = 'main/photo_edit.html'
    form_class = EditPhoto

    def get_success_url(self):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.id})


def delete_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    photo.delete()
    return redirect('dashboard')


class CreatePetView(views.CreateView):
    template_name = 'main/pet_create.html'
    form_class = AddPet

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    success_url = reverse_lazy('dashboard')


class EditPetView(views.UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = EditPet


class DeletePetView(views.DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePet


def like_pet_photo(request, pk):
    new_like, created = Like.objects.get_or_create(user=request.user, photo_id=pk)
    if created:
        pet_photo = PetPhoto.objects.get(pk=pk)
        pet_photo.likes += 1
        pet_photo.save()

    return redirect('pet photo details', pk)



