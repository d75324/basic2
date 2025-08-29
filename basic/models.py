from django.db import models

# Creación de un modelo de prueba, llamado Product:

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
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

class Registro(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField(verbose_name="Diganos lo que se le cante")
    color = models.CharField(max_length=30, verbose_name="Su color favorito...")
    fruit = models.CharField(max_length=30, verbose_name="Su fruta favorita...")
    #text = models.CharField(max_length=100, verbose_name="De que color es el caballo blanco de San Martín?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
