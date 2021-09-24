from datetime import datetime

import requests

from app.models import DeliveryCompany
from fast_shop.settings import ST_API


def now():
    return datetime.utcnow()


def save_delivery_company():
    uri = f"https://info.sweettracker.co.kr/api/v1/companylist?t_key={ST_API}"
    res = requests.get(uri)
    header = {"accept":  "application/json;charset=UTF-8"}
    company = res.json().get("Company")
    for c in company:
        DeliveryCompany.objects.create(code=c.get("Code"), name=c.get("Name"))
