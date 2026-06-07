from django.db import models

CHOICES_DIMENCIONES = ( 
    ("CH", "CHICO"),
    ("M", "MEDIANO"),
    ("G", "GRANDE")
)

CHOICES_COLORES = (
    ("AZ", "AZUL"),
    ("RO", "ROJO"),
    ("VE", "VERDE"),
    ("AM", "AMARILLO"),
    ("NE", "NEGRO"),
    ("BL", "BLANCO"),
    ("GR", "GRIS"),
    ("NA", "NARANJA"),
    ("ROSA", "ROSA"),
    ("MO", "MORADO"),
)

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    descripcion = models.TextField(blank=True, null=True)
    vendedor = models.CharField(max_length=100,blank=True, null=True)
    color = models.CharField(max_length=4, choices=CHOICES_COLORES, default="NA")
    dimenciones = models.CharField(max_length=2, choices=CHOICES_DIMENCIONES, default= "CH")