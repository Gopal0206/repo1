from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    order_id = models.CharField(max_length=50, unique=True)
    region = models.CharField(max_length=100)
    order_date = models.DateField()

    def __str__(self):
        return self.order_id


class Item(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to="items/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.product
