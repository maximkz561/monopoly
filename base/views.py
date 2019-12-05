from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from base.forms import UserForm, UserRoom
from base.models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            user = form.save(commit=False)
            user.save()
            return HttpResponse('success')
        except ValueError:
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'form': form})


@login_required
def lobby(request):
    if request.method == 'POST':
        form = UserRoom(request.POST)
        try:
            room = form.save(commit=False)
            user = get_object_or_404(CustomUser, id=request.user.id)
            user.room = room
            user.save()
        except ValueError:
            return redirect('lobby')
    else:
        form = UserRoom()
        return render(request, 'lobby.html', {'form': form})
