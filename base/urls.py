from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from base import views

urlpatterns = [
    path('registration', views.register, name='registration'),
    path('lobby', views.lobby, name='lobby'),
    path('', TemplateView.as_view(template_name='base.html')),
]