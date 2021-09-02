from typing import List

from ninja.router import Router
from django.contrib.auth.decorators import login_required
from time import time

from app.models import DeliveryCompany
from app.order.schemas import DeliveryCompanySchema

order = Router()


@order.get("delivery_company", response={200:List[DeliveryCompanySchema]})
@login_required
def get_delivery_company(request):
    return DeliveryCompany.objects.all()

