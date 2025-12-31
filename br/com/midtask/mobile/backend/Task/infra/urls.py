from django.urls import path
from ..interface.views import TaskView

urlpatterns = [
    path("", TaskView.as_view())
]
