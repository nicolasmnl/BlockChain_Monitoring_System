from django.db import models
from hashlib import sha256

# Create your models here.
def calculate_hash(content):
    first_hash = sha256(content.encode()).hexdigest()
    second_hash = sha256(first_hash.encode()).hexdigest()
    return second_hash

class Armazenamento(models.Model):
     #Login n precisa adicionar(deve ser preenchido automatico)
    block_index = models.IntegerField(primary_key=False)
    #Login n precisa adicionar(deve ser preenchido automatico)
    #Login n precisa adicionar(deve ser preenchido automatico)
    block_timestamp = models.DateTimeField(auto_now_add=True)
    #Login n precisa adicionar(deve ser preenchido automatico)
    block_nonce = models.IntegerField()

    data = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    volume_tanque_hora_final = models.IntegerField()

    block_transactions = str(data) + str(hora_inicio) + str(hora_fim) + str(volume_tanque_hora_final)

    created_hash = calculate_hash(block_transactions)

    #Hash do bloco é sua chave primária
    block_hash = models.TextField(default=created_hash, primary_key=True)