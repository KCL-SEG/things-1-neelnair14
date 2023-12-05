from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Thing(models.Model):
    name = models.CharField(unique=True, blank=False,max_length=30)
    description = models.CharField(unique = False, blank = True, max_length = 120)
    quantity = models.IntegerField(unique = False, blank = True, validators=[
            MinValueValidator(0, message="Quantity must be at least 0."),
            MaxValueValidator(100, message="Quantity must be at most 100."),
        ])
