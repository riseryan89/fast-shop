from app.products.views import product_detail
from django.urls import path

urlpatterns = [
    path("<int:product_id>", product_detail, name="product_detail"),

]
