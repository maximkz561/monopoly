from django.contrib.auth.models import AbstractUser
from django.db import models

from monopoly.settings import AUTH_USER_MODEL


class Room(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    active = models.BooleanField(default=False)
    capacity = models.IntegerField(default=4)
    members = models.IntegerField(default=0)
    password = models.CharField(max_length=10, blank=True, null=True, help_text='not necessary')
    start_money = models.IntegerField(default=15000000)
    circle_money = models.IntegerField(default=2000000)

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    ready = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.id

    def circle(self):
        self.money += self.room.circle_money
        self.save()

    def transfer(self, recipient: 'CustomUser', amount: int):
        if self.room == recipient.room and self.money >= amount:
            self.money -= amount
            recipient.money += amount
            self.save()
            recipient.save()
        else:
            raise Exception()

    def increase(self, amount: int):
        self.money += amount
        self.save()

    def reduce(self, amount: int):
        self.money -= amount
        self.save()

    @property
    def friendly_money(self):
        money = self.money
        k = money // 1000 % 1000
        m = money // 1000000
        return f'{m}M {k}K'
