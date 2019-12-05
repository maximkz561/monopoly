from django.contrib.auth.models import User, AbstractUser
from django.db import models

from monopoly import settings


class Money(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.amount

    def circle(self):
        self.amount += 2000000
        self.save()


class Room(models.Model):
    room_id = models.IntegerField()

    def __str__(self):
        return str(self.room_id)


class CustomUser(AbstractUser):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)