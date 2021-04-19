from django.db import models
from hashlib import sha256

# Create your models here.
class Block(models.Model):
    objects = models.Manager()
    #Login n precisa adicionar(deve ser preenchido automatico)
    index = models.IntegerField(primary_key=False)
    #Login n precisa adicionar(deve ser preenchido automatico)
    previous_hash = models.ForeignKey('self',blank=True ,null=True,on_delete=models.RESTRICT)
    current_transactions = models.TextField()
    #Login n precisa adicionar(deve ser preenchido automatico)
    timestamp = models.DateTimeField(auto_now_add=True)
    #Login n precisa adicionar(deve ser preenchido automatico)
    nonce = models.IntegerField()

    block_content = str(index) + str(previous_hash) + str(timestamp) + str(current_transactions) + str(nonce)
    first_hash = sha256(block_content.encode()).hexdigest()
    second_hash = sha256(first_hash.encode()).hexdigest()
    hash = models.TextField(default=second_hash,primary_key=True)

    def __str__(self):
        return str(self.hash)


    def calculate_hash(self, block_content):
        first_hash = sha256(block_content.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash


#sha256(first_hash.encode()).hexdigest()