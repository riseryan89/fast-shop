from ninja.orm import create_schema
from app import models as m


DeliveryCompanySchema = create_schema(m.DeliveryCompany)
