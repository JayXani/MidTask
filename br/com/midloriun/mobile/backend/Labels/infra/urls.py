from django.urls import path
from ..interfaces.views import LabelView, LabelListView

urlpatterns = [
    path('', LabelView.as_view()),
    path('<uuid:id>', LabelView.as_view()),
    path('list/', LabelListView.as_view())
]