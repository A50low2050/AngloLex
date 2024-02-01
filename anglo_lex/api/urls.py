from django.urls import path, include
from rest_framework import routers
from api.views import (
    DictionaryViewSet,
    SignUpApiView,
    SingInApiView
)


router = routers.DefaultRouter()
router.register(r'dictionary', DictionaryViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/account/signup/', SignUpApiView.as_view(), name='api_sign_up'),
    path('api/v1/account/signin/', SingInApiView.as_view(), name='api_sing_in'),

]
