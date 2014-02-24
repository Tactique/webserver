from django.db import models

# Create your models here.
class HasSprite(models.Model):
    spriteName = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Cell(HasSprite):
    cType = models.PositiveIntegerField()

class Unit(HasSprite):
    distance = models.PositiveIntegerField()
    movementType = models.CharField(max_length=50)
