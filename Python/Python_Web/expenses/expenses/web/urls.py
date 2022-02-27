from django.urls import path

from expenses.web.views import home_page, create_expense, edit_expense, delete_expense, show_profile, edit_profile, \
    delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', create_expense, name='create expense page'),
    path('edit/<int:pk>/', edit_expense, name='edit expense page'),
    path('delete/<int:pk>/', delete_expense, name='delete expense page'),
    path('profile/', show_profile, name='profile page'),
    path('profile/create/', create_profile, name='create profile page'),
    path('profile/edit/', edit_profile, name='edit profile page'),
    path('profile/delete/', delete_profile, name='delete profile page'),
)
