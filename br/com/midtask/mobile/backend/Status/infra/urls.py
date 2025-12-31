from django.urls import path
from ..interface.views import StatusView

urlpatterns = [
    path("", StatusView.as_view())    
]
