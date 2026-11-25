from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User


class PerfilConsumo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_consumo')
    tarifa_kwh_clp = models.FloatField(default=135.0, help_text="Costo por kWh en pesos chilenos")
    presupuesto_mensual_clp = models.FloatField(default=35000.0, help_text="Meta de presupuesto mensual en CLP")

    def __str__(self):
        return f"Perfil de {self.usuario.username} (${self.tarifa_kwh_clp}/kWh)"


class Dispositivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dispositivos')
    nombre = models.CharField(max_length=100)  # Ej: Hervidor, TV Living, Refrigerador
    watts_promedio = models.FloatField()       # Ej: 2000.0, 120.0, 150.0
    encendido = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        estado = "ON" if self.encendido else "OFF"
        return f"{self.nombre} ({self.watts_promedio}W) - [{estado}]"


class LecturaConsumo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lecturas')
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.SET_NULL, null=True, blank=True)
    watts_totales = models.FloatField()
    costo_clp = models.FloatField()
    es_simulado = models.BooleanField(default=True)  # True hoy; False cuando venga del ESP32
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        origen = "SIM" if self.es_simulado else "ESP32"
        return f"[{origen}] {self.watts_totales}W -> ${self.costo_clp:.2f} CLP ({self.fecha_hora:%H:%M:%S})"