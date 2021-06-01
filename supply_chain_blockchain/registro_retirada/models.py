from django.db import models
from hashlib import sha256

# Create your models here.
def calculate_hash(content):
    first_hash = sha256(content.encode()).hexdigest()
    second_hash = sha256(first_hash.encode()).hexdigest()
    return second_hash

class RegistroRetirada(models.Model):
    #Login n precisa adicionar(deve ser preenchido automatico)
    block_index = models.IntegerField(primary_key=False)
    #Login n precisa adicionar(deve ser preenchido automatico)
    #Login n precisa adicionar(deve ser preenchido automatico)
    block_timestamp = models.DateTimeField(auto_now_add=True)
    #Login n precisa adicionar(deve ser preenchido automatico)
    block_nonce = models.IntegerField()
    
    registro_animal = models.CharField(max_length=5)
    volume = models.FloatField()
    dia_horario = models.DateTimeField()

    block_transactions = str(registro_animal) + str(volume) + str(dia_horario)
    created_hash = calculate_hash(block_transactions)
    
    #Hash do bloco é sua chave primária
    block_hash = models.TextField(default=created_hash, primary_key=True)

    