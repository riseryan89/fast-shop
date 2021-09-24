from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.


class User (AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email_verified = models.BooleanField(default=False)


class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DeliveryAddress(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=20, null=True)


class DeliveryCompany(TimeStampedModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EmailVerification(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=100, null=True)
    item_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product (TimeStampedModel):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    amount = models.IntegerField()
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f"[{self.category.name}] {self.name}"


class Rating (TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"[{self.product.name}] by {self.user} ({self.rating}점)"


class ProductPhoto(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f"[{self.product.name}]"


class ProductOption(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option = models.CharField(max_length=100, null=True)
    amount = models.IntegerField()
    available = models.IntegerField(default=999)


class PopUp(TimeStampedModel):
    photo = models.ImageField(upload_to="pop_up")
    name = models.CharField(max_length=20, null=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    target_url = models.CharField(max_length=2000, null=True)
    ended_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        img = Image.open(self.photo)
        self.width, self.height = img.size
        super().save(*args, **kwargs)  # 실제 save() 를 호출

    def __str__(self):
        return f"{self.name} ({self.width}X{self.height})"


class ShoppingCart(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.JSONField()


class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.JSONField()


class Payment(TimeStampedModel):
    user_id = models.IntegerField()
    payment_id = models.CharField(max_length=100, default="ABCE-WPOW-FMPW-DFJL")
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.CASCADE)
    delivery_invoice = models.CharField(max_length=100, default="OrderNo: 12312")
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order_no = models.CharField(max_length=100, default="OrderNo: 12312")
