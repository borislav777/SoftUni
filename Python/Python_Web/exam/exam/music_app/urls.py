from django.urls import path

from exam.music_app.views import show_home, add_album, album_details, edit_album, delete_album, profile_details, \
    create_profile, delete_profile

urlpatterns = (
    path('', show_home, name='home page'),
    path('album/add/', add_album, name='add album page'),
    path('album/details/<int:pk>/', album_details, name='album details page'),
    path('album/edit/<int:pk>/', edit_album, name='edit album page'),
    path('album/delete/<int:pk>/', delete_album, name='delete album page'),
    path('profile/details/', profile_details, name='profile details page'),
    path('profile/create/', create_profile, name='create profile page'),
    path('profile/delete/', delete_profile, name='delete profile page'),
)
