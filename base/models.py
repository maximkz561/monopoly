from django.contrib.auth.models import AbstractUser
from django.db import models

from monopoly.settings import AUTH_USER_MODEL


class Room(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)

    def circle(self):
        self.money += 2000000
        self.save()

    def transfer(self, recipient: 'CustomUser', amount: int):
        if self.room == recipient.room and self.money >= amount:
            self.money -= amount
            recipient.money += amount
            self.save()
            recipient.save()
        else:
            raise Exception()
