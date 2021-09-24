from django.db.models import Prefetch, Avg

from app.models import PopUp, Product, Rating
from django.shortcuts import render

# Create your views here.
from app.utls import now


def product_detail(request, product_id):
    product = (Product.objects.filter(pk=product_id)
               .prefetch_related(
                    Prefetch("productphoto_set"),
                    Prefetch("productoption_set"),
                )
               .first()
               )
    ratings = Rating.objects.filter(product_id=product_id).all()
    return render(request, "product_detail.html", {"product": product, "ratings": ratings})
