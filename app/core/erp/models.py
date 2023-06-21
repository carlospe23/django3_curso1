from django.db import models
from datetime import datetime

from core.erp.choices import gender_choices

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Nombre",
        unique=True
    )


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Nombre",
        unique=True
    )
    category_id = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='product/%Y/%m/%d',
        null=True,
        blank=True
    )
    pvp = models.DecimalField(
        default=0.00,
        max_digits=9,
        decimal_places=2
    )


    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Products'
        ordering = ['id']



class Client(models.Model):
    names = models.CharField(
        max_length=150, 
        verbose_name='Nombres',
    )
    surnames = models.CharField(
        max_length=150,
        verbose_name="Apellidos"
    )
    dni = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name='DNI'
    )
    birthday = models.DateField(
        default=datetime.now,
        verbose_name="Fecha de nacimiento"
    )
    address = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Direccion"
    )
    sexo = models.CharField(
        max_length=10,
        choices=gender_choices,
        default="Male",
        verbose_name="Sexo"
    )


    def __str__(self) -> str:
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

        
class Sale(models.Model):

    cli = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    date_joined = models.DateField(
        default=datetime.now
    )
    subtotal = models.DecimalField(
        default=0.0,
        max_digits=9,
        decimal_places=2
    )
    iva = models.DecimalField(
        default=0.0,
        max_digits=9,
        decimal_places=2
    )
    total = models.DecimalField(
        default=0.0,
        max_digits=9,
        decimal_places=2
    )


    def __str__(self) -> str:
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(
        Sale, 
        on_delete=models.CASCADE
    )
    prod = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        default=0.0,
        max_digits=9,
        decimal_places=2
    )
    cant = models.IntegerField(
        default=0
    )
    subtotal = models.DecimalField(
        default=0.00,
        max_digits=9,
        decimal_places=2
    )


    def __str__(self) -> str:
        return self.prod.names

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']