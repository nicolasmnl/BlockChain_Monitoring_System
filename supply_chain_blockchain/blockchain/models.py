from django.db import models
from hashlib import sha256

# Create your models here.
class Block(models.Model):
    objects = models.Manager()
    index = models.AutoField(primary_key=False)
    previous_hash = models.ForeignKey('self', on_delete=models.RESTRICT)
    current_transactions = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    nonce = models.IntegerField()
    block_content = str(index) + str(previous_hash) + str(timestamp) + str(current_transactions) + str(nonce)
    first_hash = sha256(block_content.encode()).hexdigest()
    hash = models.TextField(sha256(first_hash.encode()).hexdigest(), primary_key=True)


    def __str__(self):
        return str(self.__dict__)
