from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField(default=1)
    BookingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.Title