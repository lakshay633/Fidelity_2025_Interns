from django.db import models

class Loc(models.Model):
    pincode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    class Meta:
        db_table = "locations"