from django.urls import path

from petstagram_workshop.main_app.views import \
    like_pet_photo, delete_pet_photo, \
    HomeView, DashboardView, CreatePetView, EditPetView, DeletePetView, \
    CreatePetPhotoView, PetPhotoDetailsView,EditPetPhotoView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),



    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like photo'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='add pet photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit pet photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete pet photo'),

    path('pet/add/', CreatePetView.as_view(), name='add pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='pet edit'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='pet delete'),

)
