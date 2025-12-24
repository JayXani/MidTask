from django.urls import path
from  ..interface.views import LinksView

urlpatterns = [
    path("", LinksView.as_view()),
    path("<uuid:id>", LinksView.as_view())
]
