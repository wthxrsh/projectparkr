from django.db import models
from django.contrib.auth.models import User

class ParkingSpace(models.Model):
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} in {self.city}"

class Booking(models.Model):
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.IntegerField()
    qr_code = models.CharField(max_length=255)  # Placeholder for QR code

    def __str__(self):
        return f"Booking by {self.user.username} for {self.parking_space}"
    
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class ParkingSpace(models.Model):
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this line exists

    def __str__(self):
        return f"{self.location} in {self.city}"
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Booking(models.Model):
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.CharField(max_length=255)  # Assuming this is the filename or identifier for the QR code