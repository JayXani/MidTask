from django.urls import path
from ..interface.views import (CheckListView, ManyCheckListView)

urlpatterns = [
    path("", CheckListView.as_view()),
    path("<uuid:id>", CheckListView.as_view()),
    path("list/", ManyCheckListView.as_view())
]
