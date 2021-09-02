from django.contrib import admin
from app import models as m
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


admin.site.site_header = "FastShop Admin"
admin.site.site_title = "FastShop Admin Powered By Django"
admin.site.index_title = "FastShop Admin 에서 모델 데이터를 추가, 삭제, 수정, 열람 할 수 있습니다."


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(m.User)
admin.site.register(m.DeliveryAddress)
admin.site.register(m.DeliveryCompany)
admin.site.register(m.Payment)
admin.site.register(m.Category)
admin.site.register(m.Product, ProductAdmin)
admin.site.register(m.ProductOption)
admin.site.register(m.PopUp)
admin.site.register(m.ShoppingCart)
admin.site.register(m.Order)


