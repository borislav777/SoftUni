from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram_workshop.accounts.forms import CreateForm, EditProfile
from petstagram_workshop.accounts.models import Profile
from petstagram_workshop.common.viewmixins import RedirectToDashboard
from petstagram_workshop.main_app.models import Pet, PetPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfile

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user_id})


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password_page.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = set(Pet.objects.filter(user_id=self.object.user_id))
        pet_photos = set(PetPhoto.objects.filter(tagged_pets__in=pets))
        total_image = len(pet_photos)
        total_likes = sum([x.likes for x in pet_photos])
        context.update({

            'pets': pets,
            'total_image': total_image,
            'total_like': total_likes,
        })
        return context


class LogoutView(auth_views.LogoutView):

    def get_success_url(self):

        return reverse_lazy('dashboard')
