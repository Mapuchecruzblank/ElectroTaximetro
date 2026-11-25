from django.shortcuts import render, redirect, get_object_or_404
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

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        watts = request.POST.get('watts', '').strip()
        if nombre and watts:
            Dispositivo.objects.create(
                usuario=request.user,
                nombre=nombre,
                watts_promedio=float(watts),
                encendido=True
            )
            return redirect('dashboard')

    dispositivos = Dispositivo.objects.filter(usuario=request.user).order_by('-creado_en')
    watts_activos = sum(d.watts_promedio for d in dispositivos if d.encendido)

    return render(request, 'dashboard.html', {
        'perfil': perfil,
        'dispositivos': dispositivos,
        'watts_activos': watts_activos,
    })


@login_required
def toggle_dispositivo(request, dispositivo_id):
    if request.method == 'POST':
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id, usuario=request.user)
        dispositivo.encendido = not dispositivo.encendido
        dispositivo.save()
    return redirect('dashboard')


@login_required
def eliminar_dispositivo(request, dispositivo_id):
    if request.method == 'POST':
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id, usuario=request.user)
        dispositivo.delete()
    return redirect('dashboard')