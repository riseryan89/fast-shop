import json
from typing import List

import requests
import yagmail
from ninja.router import Router
from django.contrib.auth.decorators import login_required
from time import time

from app.models import DeliveryCompany
from app.order.schemas import DeliveryCompanySchema, OrderBody
from fast_shop.settings import ST_API, EMAIL_ID, EMAIL_PW

order = Router()


@order.get("delivery_company", response={200:List[DeliveryCompanySchema]})
@login_required
def get_delivery_company(request):
    return DeliveryCompany.objects.all()


@order.get("delivery")
@login_required
def get_delivery_invoice(request, t_code, t_invoice):
    url = f"https://info.sweettracker.co.kr/api/v1/trackingInfo?t_key={ST_API}&t_code={t_code}&t_invoice={t_invoice}"
    header = {"accept": "application/json;charset=UTF-8"}
    # header = {"accept": "application/xml;charset=UTF-8"}
    res = requests.get(url, headers=header)
    return res.json()


@order.post("done", response={200: None})
@login_required
def done_order(request, body: List[OrderBody]):
    yag = yagmail.SMTP({EMAIL_ID: "주문알림"}, EMAIL_PW)
    # https://myaccount.google.com/u/1/lesssecureapps
    content = ""
    for b in body:
        content += f"{str(json.dumps(b.dict(), indent=2, ensure_ascii=False))}\n"
    contents = [content]
    yag.send(EMAIL_ID, f"주문내역 {request.user}", contents)
    return 200, None
