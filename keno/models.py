from django.db import models
from django.conf import settings

class SorteoKeno(models.Model):
    codigo = models.CharField(max_length=30, unique=True)
    fecha_sorteo = models.DateTimeField(auto_now_add=True)
    numeros_sorteados = models.JSONField(default=list, blank=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Sorteo Keno {self.codigo}"


class BoletoKeno(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="boletos_keno",
    )
    sorteo = models.ForeignKey(
        SorteoKeno,
        on_delete=models.CASCADE,
        related_name="boletos",
        null=True,
        blank=True,
    )
    numeros_elegidos = models.JSONField(default=list)
    apuesta = models.DecimalField(max_digits=8, decimal_places=2)
    aciertos = models.PositiveSmallIntegerField(default=0)
    premio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Boleto #{self.id} - {self.usuario}")
