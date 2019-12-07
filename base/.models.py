from django.contrib.auth.models import AbstractUser
from django.db import models

from monopoly.settings import AUTH_USER_MODEL


class Money(models.Model):
    amount = models.IntegerField(default=15000000000)

    def __str__(self):
        return self.amount

    def circle(self):
        self.amount += 2000000
        self.save()


class Room(models.Model):
    room_id = models.IntegerField()
    user = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return str(self.room_id)


class CustomUser(AbstractUser):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    money = models.ForeignKey(Money, on_delete=models.CASCADE)