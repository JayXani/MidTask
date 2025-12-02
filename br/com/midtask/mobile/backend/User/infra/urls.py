from django.urls import path
from ..interface.views import UserViewer

urlpatterns = [
    path('user/', UserViewer.as_view())
]