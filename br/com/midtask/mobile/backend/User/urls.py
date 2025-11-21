from django.urls import path
from .views import UserViewer

urlpatterns = [
    path('hello/', UserViewer.as_view())
]