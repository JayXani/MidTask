from django.urls import path
from ..interface.views import (
    StatusView,
    StatusListView
)

urlpatterns = [
    path("", StatusView.as_view()),
    path("list/", StatusListView.as_view())
]
