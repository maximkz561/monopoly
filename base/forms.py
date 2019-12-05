from django import forms

from base.models import CustomUser


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class UserRoom(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('room',)
