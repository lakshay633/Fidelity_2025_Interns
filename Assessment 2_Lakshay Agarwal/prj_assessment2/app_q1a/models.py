from django.db import models

# Create your models here.
class Planet(models.Model):
    pId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    diam=models.IntegerField()
    star=models.CharField(max_length=50)
    rings = models.BooleanField(default=False)