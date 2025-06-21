from django.db import models

# Creación de un modelo de prueba, llamado Product:

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        return self.name
