from django.urls import path
from django.views.generic import TemplateView

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
    path('game/<int:room_id>', views.game, name='start_game'),
    path('circle', views.circle, name='circle'),
    path('transfer_money/<int:user_id>', views.transfer_money, name='transfer_money'),
    path('increase_money', views.increase_money, name='increase_money'),
    path('reduce_money', views.reduce_money, name='reduce_money'),
]
