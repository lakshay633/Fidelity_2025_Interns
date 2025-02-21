from django.db import models
from uuid import uuid4

class Trip(models.Model):
    tripID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tripDuration = models.IntegerField()
    tripDate = models.DateField()
    boarding = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "trip"

# ✅ UUIDField: Snowflake doesn't handle auto-incrementing primary keys like other DBs. UUIDs are more scalable.
# didn't use bcz update fatt gaya coz url is no more int
# ✅ IntegerField for Duration: Makes querying easier & prevents unnecessary storage overhead.
# ✅ DecimalField for Cost: Supports precise decimal storage, crucial for financial data.
# ✅ CharField for Text: If your boarding and destination are limited in size, CharField with max_length is better than TextField.