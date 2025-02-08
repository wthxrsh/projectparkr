from django.db import models

class ParkingSpot(models.Model):
    CITY_CHOICES = [
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Bangalore', 'Bangalore'),
    ]
    
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.city} - {self.price}"

class Booking(models.Model):
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking for {self.parking_spot} for {self.hours} hours"