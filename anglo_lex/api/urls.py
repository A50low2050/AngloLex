from django.urls import path, include
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'dictionary', DictionaryViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('api/v1/account/signup/', SignUpApiView.as_view(), name='api_sign_up')

]
