from django.db import models

# Create your models here.
class Producer(models.Model):
    id_producer = models.AutoField(primary_key=True)
    registro_animal = models.CharField(max_length=5)
    volume = models.FloatField()
    dia_horario = models.DateTimeField()

    tempo_armazenamento = models.FloatField()
    temperatura_armazenamento = models.FloatField()
    ph = models.FloatField()