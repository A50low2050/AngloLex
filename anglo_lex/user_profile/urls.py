from django.urls import path
from .views import EditProfileUser, logout_user, profile_update


urlpatterns = [
    path('logout_user/', logout_user, name='logout_user'),
    path('edit_profile/<slug:username>', EditProfileUser.as_view(), name='edit_profile'),
    path('profile_update/', profile_update, name='profile_update')
]
