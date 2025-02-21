from django.db import models

class Price(models.Model):
    itemID = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = "price"