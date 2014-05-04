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

# I'm so lazy...
class World(models.Model):
    lump = models.TextField()

class ResponseTemplate(models.Model):
    name = models.CharField(max_length=MAX_CHAR_LENGTH)
    JSON = models.TextField()
