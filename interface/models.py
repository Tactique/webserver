from django.db import models
from django.contrib.auth.models import User

class GameUser(models.Model):
    user = models.OneToOneField(User)
    wins = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)

# Create your models here.
class HasSprite(models.Model):
    spriteName = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Cell(HasSprite):
    cType = models.PositiveIntegerField(default=0)

class Unit(HasSprite):
    distance = models.PositiveIntegerField(default=1)
    movementType = models.CharField(max_length=50)

# I'm so lazy...
class World(models.Model):
    lump = models.TextField()
