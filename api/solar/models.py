from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
# Create your models here.

class Solar(models.Model):
    numero_placas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(180)])
    valor_placa = models.FloatField(validators=[MinValueValidator(1)])
    valor_energia = models.FloatField(validators=[MinValueValidator(1)])
    
    