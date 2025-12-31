from django.urls import path
from ..interface.views import (
    AlertsView,
    AlertsListView
)

urlpatterns = [
    path("", AlertsView.as_view()),
    path("<uuid:id>", AlertsView.as_view()),
    path("list/", AlertsListView.as_view())
]
