from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram_workshop.accounts.views import UserLoginView, ProfileDetailsView, \
    UserRegisterView, ChangeUserPasswordView, EditProfileView, LogoutView

urlpatterns = (

    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('<int:pk>', ProfileDetailsView.as_view(), name='profile'),
    path('create/', UserRegisterView.as_view(), name='register'),
    path('edit-profile/<int:pk>', EditProfileView.as_view(), name='edit profile'),

    # path('profile/delete/', delete_profile_page, name='delete profile'),

)
