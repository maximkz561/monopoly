from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
    return render(request, 'lobby.html', {'rooms': rooms})


@login_required
def make_room(request):
    Room.objects.create(owner=request.user)
    return redirect('lobby')


def join_room(request, room_id):
    user = request.user
    user.room = get_object_or_404(Room, id=room_id)
    user.save()
    return HttpResponse('success')
