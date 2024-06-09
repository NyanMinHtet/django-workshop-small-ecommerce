from django.db import models

# Create your models here.


class Product(models.Model):

    PRODUCT_CATEGORY = [
        ('Phone', 'Phone'),
        ('Food', 'Food'),
        ('Clothes', 'Clothes'),
    ]
    image = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=PRODUCT_CATEGORY)
    can_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    
    CHOICE_COLOR = (
        (RED,"red"),
        (GREEN,"green"),
        (YELLOW,"yellow")
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='detail')
    color = models.CharField(max_length=50, choices=CHOICE_COLOR)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
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
    productdetail = models.OneToOneField(ProductDetail,on_delete=models.PROTECT, related_name="product_detail",null=True,blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    def __str__(self):
        return f"Receipt for {self.cus_name}"
