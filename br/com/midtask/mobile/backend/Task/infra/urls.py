from django.urls import path
from ..interface.views import (
    TaskView,
    TaskListView
)

urlpatterns = [
    path("", TaskView.as_view()),
    path("<uuid:id>", TaskView.as_view()),
    path("list/", TaskListView.as_view())
]
