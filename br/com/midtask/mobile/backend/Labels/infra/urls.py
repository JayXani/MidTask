from django.urls import path
from ..interfaces.views import LabelView

urlpatterns = [
    path('', LabelView.as_view()),
    path('<uuid:id>', LabelView.as_view())
]