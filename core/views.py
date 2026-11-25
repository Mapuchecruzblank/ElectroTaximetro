from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import PerfilConsumo, Dispositivo


def landing(request):
    return render(request, 'landing.html')


def registro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            PerfilConsumo.objects.create(usuario=usuario)
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def dashboard(request):
    perfil, _ = PerfilConsumo.objects.get_or_create(usuario=request.user)
    dispositivos = Dispositivo.objects.filter(usuario=request.user)
    return render(request, 'dashboard.html', {
        'perfil': perfil,
        'dispositivos': dispositivos,
    })