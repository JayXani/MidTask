from django.urls import path
from ..interface.views import AlertsView

urlpatterns = [
    path("", AlertsView.as_view())
]
