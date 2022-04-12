from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_added = models.DateTimeField(auto_now_add=True)
    # customer_booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    



