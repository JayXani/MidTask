from django.urls import path
from ..interface.views import CheckListView

urlpatterns = [
    path("", CheckListView.as_view())
]
