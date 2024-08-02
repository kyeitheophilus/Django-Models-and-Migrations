from django.db import models

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=200)
  price = models.FloatField()
  stock = models.IntegerField()
  image_url =models.ImageField(null=True, blank=True)
  
def __self__(self):
   return self.name