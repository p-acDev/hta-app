from django.db import models

# Create your models here.
class Mesure(models.Model):
    systole = models.IntegerField()
    diastole = models.IntegerField()
    date_mesure = models.DateTimeField()