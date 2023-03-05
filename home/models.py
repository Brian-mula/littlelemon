from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    guest_number=models.IntegerField()
    comment=models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name
    


class Menu(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    description=models.CharField(max_length=2000,null=True)
    image=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name