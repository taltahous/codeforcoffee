from django.contrib.auth.models import User
from django.db import models


class Bean(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Roast(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Syrup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Powder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Coffee(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    bean = models.ForeignKey(Bean)
    roast = models.ForeignKey(Roast)
    espresso_shots = models.PositiveIntegerField(default=1)
    water = models.FloatField(default=0)
    steamed_milk = models.BooleanField(default=False)
    foam = models.FloatField(default=False)
    powder = models.ManyToManyField(Powder, blank=True)
    syrup = models.ManyToManyField(Syrup, blank=True)
    extra = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User)
    coffee = models.ForeignKey(Coffee)
    date = models.DateField()

    def __str__(self):
        return str(self.user)
