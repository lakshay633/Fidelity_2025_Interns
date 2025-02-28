from django.db import models
from uuid import uuid4

class Product(models.Model):
    productID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=260)
    image = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "Product"
