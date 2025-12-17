from django.urls import path
from ..interface.views import UserViewer, Authentication
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('user', UserViewer.as_view()),
    path('user/<uuid:id>', UserViewer.as_view()),
    path('auth/token', Authentication.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view())
]