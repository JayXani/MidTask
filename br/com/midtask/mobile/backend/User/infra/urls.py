from django.urls import path
from .views import UserViewer

urlpatterns = [
    path('user/', UserViewer.as_view())
]