from django.urls import path
from ..interface.views import (
    TaskView,
    TaskListView,
    TaskExpiredView
)

urlpatterns = [
    path("", TaskView.as_view()),
    path("<uuid:id>", TaskView.as_view()),
    path("list/", TaskListView.as_view()),
    path("list/expired/", TaskExpiredView.as_view())
]
