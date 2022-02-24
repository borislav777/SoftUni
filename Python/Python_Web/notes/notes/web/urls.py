from django.urls import path

from notes.web.views import home_page, add_note, edit_note, delete_note, note_details, profile_page, create_profile, \
    delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', note_details, name='note details'),
    path('profile/', profile_page, name='profile page'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/delete', delete_profile, name='delete profile')

)
