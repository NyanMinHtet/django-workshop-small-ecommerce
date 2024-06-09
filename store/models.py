from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = [
        ('Phone', 'Phone'),
        ('Food', 'Food'),
        ('Clothes', 'Clothes'),
    ]
    image = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='detail')
    color = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return f"{self.product.name} Details"

class Receipt(models.Model):
    PAYMENT_METHODS = [
        ('Cash on Delivery', 'Cash on Delivery'),
        ('Bank Transfer', 'Bank Transfer'),
    ]

    cus_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    def __str__(self):
        return f"Receipt for {self.cus_name}"