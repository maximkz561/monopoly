from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from base.forms import UserForm
from base.models import CustomUser, Room


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            user = form.save(commit=False)
            # password = user.cleaned_data.get('password')
            user.set_password(user.password)
            user.save()
            return HttpResponse('success')
        except ValueError:
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'form': form})


@login_required
def lobby(request):
    rooms = Room.objects.all()
    user = request.user
    return render(request, 'lobby.html', {'rooms': rooms, 'user': user})


@login_required
def make_room(request):
    Room.objects.create(owner=request.user)
    return redirect('lobby')


@login_required
def join_room(request, room_id):
    user = request.user
    user.room = get_object_or_404(Room, id=room_id)
    user.save()
    users = CustomUser.objects.filter(room_id=room_id)
    return render(request, 'room.html', {'users': users})


@login_required
def quit(request):
    user = request.user
    if user.room:
        user.room = None
        user.save()
        return redirect('lobby')
    else:
        raise Http404


@login_required
def del_room(request, room_id):
    user = request.user
    room = get_object_or_404(Room, id=room_id)
    if room.owner == user:
        room.delete()
        return redirect('lobby')
    else:
        raise Http404
