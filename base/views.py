from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from base.forms import UserForm, RoomForm, MoneyForm
from base.models import CustomUser, Room


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('lobby')
        except ValueError:
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'form': form})


@login_required
def lobby(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        room = form.save(commit=False)
        room.save()
        return HttpResponse('success')
    else:
        form = RoomForm()
        rooms = Room.objects.all()
        user = request.user
        return render(request, 'lobby.html', {'rooms': rooms, 'user': user, 'form': form})


@login_required
def make_room(request):
    form = RoomForm(request.POST)
    room = form.save(commit=False)
    room.owner = request.user
    room.save()
    return redirect('lobby')


@login_required
def join_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        if room.password != request.POST.get('password'):
            raise Exception()
    user = request.user
    user.room = room
    user.save()
    users = CustomUser.objects.filter(room_id=room_id)
    if room.active:
        return redirect(f'../game/{room_id}')
    return redirect(f'../room/{room_id}')


@login_required
def quit(request):
    user = request.user
    if user.room:
        user.room = None
        user.ready = False
        user.money = None
        user.save()
        return redirect('lobby')
    else:
        raise Http404


@login_required
def del_room(request, room_id):
    user = request.user
    room = get_object_or_404(Room, id=room_id)
    if room.owner == user or user.is_superuser:
        room.delete()
        return redirect('lobby')
    else:
        raise Http404


def render_room(request, room_id):
    users = CustomUser.objects.filter(room_id=room_id)
    room = get_object_or_404(Room, id=room_id)
    everybody_is_ready = False
    for user in users:
        if user.ready:
            everybody_is_ready = True
        if not user.ready:
            everybody_is_ready = False
            break
    if everybody_is_ready and room.capacity == len(users):
        return redirect(f'../game/{room_id}')
    else:
        return render(request, 'room.html', {'users': users, 'request_user': request.user})


@login_required()
def ready(request):
    user = request.user
    if user.ready:
        user.ready = False
        user.money = None
    else:
        user.ready = True
        user.money = user.room.start_money
    user.save()
    room = user.room
    users = CustomUser.objects.filter(room_id=room.id, ready=True)
    if len(users) == room.capacity:
        room.active = True
        room.save()
        return redirect(f'game/{room.id}')
    return redirect(f'room/{room.id}')


def game(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    users = CustomUser.objects.filter(room=room).order_by('pk')
    form = MoneyForm()
    return render(request, 'game.html', {'room': room, 'users': users, 'request_user': request.user, 'form': form})


def circle(request):
    user = request.user
    room = user.room
    user.increase(room.circle_money)
    return redirect(f'game/{room.id}')


def transfer_money(request, user_id):
    amount = int(request.POST.get('money'))
    recipient = get_object_or_404(CustomUser, id=user_id)
    user = request.user
    user.transfer(recipient, amount)
    user.save()
    recipient.save()
    room = user.room
    return redirect(f'../game/{room.id}')


def bank(request):
    user = request.user
    button_type = request.POST.get('button_type')
    money = int(request.POST.get('money'))
    if button_type == 'get':
        user.increase(money)
    elif button_type == 'pay':
        user.reduce(money)
    return redirect(f'../game/{user.room.id}')
