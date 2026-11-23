from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=" fecha de creacion ")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Categorias"
    )
    sku = models.CharField(max_length=50, unique=True, verbose_name="Código / SKU")
    name = models.CharField(max_length=200, verbose_name="Nombre del producto")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de venta")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")
    min_stock = models.PositiveIntegerField(default=5, verbose_name="Stock mínimo (Alerta)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta: 
        verbose_name = "Producto"
        verbose_name_plural = "Productos"   
        ordering =['name']

    def __str__(self):
        return f"{self.sku} - {self.name}"

    @property
    def is_low_stock(self):
        """Indica si el producto alcanzo o bajo de su stock minimo"""
        return self.stock <= self.min_stock