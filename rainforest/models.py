from django.db import models
# from django import forms
# from django.core.validators import MinValueValidator

from django.core.validators import MinValueValidator
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price_in_cents = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    def __str__(self):
        return f"{self.name} - {self.price_in_cents} in pennies"