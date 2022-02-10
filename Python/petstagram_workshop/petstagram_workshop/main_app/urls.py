from django.urls import path

from petstagram_workshop.main_app.views import show_home, show_dashboard, show_profile, show_pet_photo_details, \
    like_pet_photo, create_profile, add_pet, add_pet_photo, edit_pet_photo, delete_pet_photo, edit_pet_page, \
    delete_pet_page, edit_profile_page, delete_profile_page

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like photo'),
    path('profile/create/', create_profile, name='create profile'),
    path('pet/add/', add_pet, name='add pet'),
    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete pet photo'),
    path('pet/edit/<int:pk>/', edit_pet_page, name='pet edit'),
    path('pet/delete/<int:pk>/', delete_pet_page, name='pet delete'),
    path('profile/edit/', edit_profile_page, name='edit profile'),
    path('profile/delete/', delete_profile_page, name='delete profile'),
)
