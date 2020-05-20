from django.db import models
from django.urls import reverse
import datetime

class Car(models.Model):
    def get_absoulte_url(self):
        return reverse('cars:detail', kwargs = {'pk:self.pk'})

    def __str__(self):
        return self.Make + '-' + self.Model
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datatime.timedelta(day=1)

    Make = models.CharField('Make', max_length = 100)
    Model = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Year = models.CharField(max_length=100)
    Fuel_Type = models.CharField(max_length = 100)
    VIN_Code = models.CharField(max_length = 100)
    Mileage = models.CharField(max_length = 100)
    car_image = models.CharField(max_length = 100)
class Meta():
    db_tble = 'Car'

