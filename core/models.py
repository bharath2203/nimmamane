from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    link = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(blank = True, null = True)
    area = models.CharField(max_length = 100)

class House(models.Model):
    belongs_to = models.ForeignKey(Person, on_delete = models.CASCADE)
    area = models.CharField(max_length = 50)
    dealing_type = models.CharField(
        max_length = 20,
        choices = (
            ('R', 'RENT'),
            ('S', 'SALE'),
            ('L', 'LEASE')
        )    
    )
    is_available = models.BooleanField()


class Lease(models.Model):
    house = models.OneToOneField(
        House,
        on_delete = models.CASCADE,
        primary_key = True     
    )
    price = models.IntegerField()
    period = models.IntegerField()


class Rent(models.Model):
    house = models.OneToOneField(
        House,
        on_delete = models.CASCADE,
        primary_key = True     
    )
    advance = models.IntegerField()
    price = models.IntegerField()


class Sale(models.Model):
    house = models.OneToOneField(
        House,
        on_delete = models.CASCADE,
        primary_key = True     
    )
    price = models.IntegerField()
