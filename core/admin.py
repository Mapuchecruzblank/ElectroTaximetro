from django.contrib import admin
from .models import PerfilConsumo, Dispositivo, LecturaConsumo

admin.site.register(PerfilConsumo)
admin.site.register(Dispositivo)
admin.site.register(LecturaConsumo)