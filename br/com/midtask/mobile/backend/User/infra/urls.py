from django.urls import path
from ..interface.views import UserViewer, Authentication, GoogleAuthenticationView
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('', UserViewer.as_view()),
    path('auth/token', Authentication.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/google/token', GoogleAuthenticationView.as_view())
]