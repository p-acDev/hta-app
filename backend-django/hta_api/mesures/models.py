from django.db import models

# Create your models here.
class Mesure(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    date_mesure = models.DateTimeField()


