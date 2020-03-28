from django.db import models

# Create your models here.
class Compra(models.Model):
	proveedor = models.CharField(max_length=255)
	fecha = models.DateField(auto_now_add=True)

class DetalleCompra(models.Model):
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	producto = models.CharField(max_length=255)
	cantidad = models.DecimalField(max_digits=5, decimal_places=2)
	precio_compra = models.DecimalField(max_digits=5,decimal_places=2)

