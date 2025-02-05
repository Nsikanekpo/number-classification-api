from django.urls import path
from .views import NumberClassificationView

urlpatterns = [
    path("classify/", NumberClassificationView.as_view(), name="number-classify"),
]

