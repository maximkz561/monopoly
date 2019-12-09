from django import forms

from base.models import CustomUser


class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirm_password')
        if password != confirmed_password:
            raise forms.ValidationError("Passwords don't match", code='invalid')

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
