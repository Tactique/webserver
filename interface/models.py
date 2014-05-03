from django.db import models
from django.contrib.auth.models import User

MAX_CHAR_LENGTH = 128
MAX_JSON_LENGTH = 526

class GameUser(models.Model):
    user = models.OneToOneField(User)
    wins = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)

class LoginData(models.Model):
    userid = models.PositiveIntegerField(default=0)
    # This max_length could be set to the precise length. Or a new field could be made
    token = models.CharField(max_length=MAX_CHAR_LENGTH)

# Create your models here.
class HasSprite(models.Model):
    spriteName = models.CharField(max_length=MAX_CHAR_LENGTH)

    class Meta:
        abstract = True

class Team(models.Model):
    nationType = models.PositiveIntegerField()
    name = models.CharField(max_length=MAX_CHAR_LENGTH)

class Cell(HasSprite):
    cellType = models.PositiveIntegerField()

class WeaponType(models.Model):
    weaponType = models.PositiveIntegerField()
    name = models.CharField(max_length=MAX_CHAR_LENGTH)

class Weapon(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    weaponType = models.ForeignKey('WeaponType')
    power = models.PositiveIntegerField()
    minRange = models.PositiveIntegerField()
    maxRange = models.PositiveIntegerField()

class ArmorType(models.Model):
    armorType = models.PositiveIntegerField()
    name = models.CharField(max_length=MAX_CHAR_LENGTH)

class Armor(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    strength = models.PositiveIntegerField()
    armorType = models.ForeignKey('ArmorType')

class SpeedMap(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    speeds = models.CharField(max_length=MAX_JSON_LENGTH)

class Movement(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    distance = models.PositiveIntegerField(default=1)
    speedMap = models.ForeignKey('SpeedMap')

class Unit(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    health = models.PositiveIntegerField()
    attack_one = models.ForeignKey('Weapon')
    attack_two = models.ForeignKey(
        'Weapon', blank=True, null=True, related_name='attack_two_weapon')
    armor = models.ForeignKey('Armor')
    movement = models.ForeignKey('Movement')

# I'm so lazy...
class World(models.Model):
    lump = models.TextField()

class ResponseTemplate(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    JSON = models.TextField()
