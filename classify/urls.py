from django.urls import path
from .views import NumberClassificationView

urlpatterns = [
    path("classify/<int:number/>", NumberClassificationView.as_view(), name="number-classify"),
]

