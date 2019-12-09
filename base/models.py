from django.contrib.auth.models import AbstractUser
from django.db import models

from monopoly.settings import AUTH_USER_MODEL


# class Money(models.Model):
#     amount = models.IntegerField(default=15000000000)
#
#     def __str__(self):
#         return self.amount
#
#     def circle(self):
#         self.amount += 2000000
#         self.save()


class Room(models.Model):
    # user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    # owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)

    def circle(self):
        self.money += 2000000
        self.save()
