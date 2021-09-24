from app.order.views import index
from django.urls import path

urlpatterns = [
    path("", index, name="order_detail"),
]
