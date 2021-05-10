from django.db import models

# Create your models here.
class Industry(models.Model):
    id_industry = models.AutoField(primary_key=True)
    volume_resfriamento = models.FloatField()
    dia_hora_resfriamento = models.DateTimeField()
    temperatura_resfriamento = models.FloatField()
    ph_resfriamento = models.FloatField()

    volume_envase = models.FloatField()
    dia_hora_envase = models.DateTimeField()
    lote = models.CharField(max_length=11)