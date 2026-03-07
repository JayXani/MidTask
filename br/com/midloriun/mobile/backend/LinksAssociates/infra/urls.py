from django.urls import path
from ..interface.views import (LinksView, LinksListView)
urlpatterns = [
    path("", LinksView.as_view()),
    path("<uuid:id>", LinksView.as_view()),
    path("list/", LinksListView.as_view())
]
