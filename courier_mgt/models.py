from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Bookings(models.Model):
    booking_id = models.IntegerField()
    booking_name = models.CharField(max_length=100)
    booking_email = models.EmailField()
    booking_added = models.DateTimeField(auto_now_add=True)
    # customer_booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.booking_name
    
# Create your models here.
class Consignment(models.Model):
    consignment_id = models.OneToOneField(Bookings, on_delete=models.CASCADE)
    complaint_id = models.IntegerField()
    pick_up = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'ConsignmentID:{self.consignment_id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'Profile: {self.user.username}'

    # def save():
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


