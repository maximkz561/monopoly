from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from base import views

urlpatterns = [
    path('registration', views.register, name='registration'),
    path('lobby', views.lobby, name='lobby'),
    path('', TemplateView.as_view(template_name='base.html')),
    path('make_room', views.make_room, name='make_room'),
    path('join_room/<int:room_id>', views.join_room, name='join_room'),
    path('del_room/<int:room_id>', views.del_room, name='del_room'),
    path('quit', views.quit, name='quit'),
    path('room/<int:room_id>', views.render_room, name='room'),
    path('ready', views.ready, name='ready'),
    path('game/<int:room_id>', views.start_game, name='start_game')
]
