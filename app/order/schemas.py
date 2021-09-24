from ninja import Schema
from ninja.orm import create_schema
from pydantic import BaseModel

from app import models as m


DeliveryCompanySchema = create_schema(m.DeliveryCompany)


class OrderBody(BaseModel):
    id: int
    name: str
    price: int
    count: int
    photo: str
