from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUp.as_view(), name='sign_up'),

    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    re_path('social-auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('social-auth/', include('social_django.urls', namespace='social-auth')),

    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
