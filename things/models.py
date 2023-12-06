from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(validators=[MaxLengthValidator(limit_value=120)], blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name