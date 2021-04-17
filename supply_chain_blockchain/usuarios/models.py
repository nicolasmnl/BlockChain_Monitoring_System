from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    telefone = models.IntegerField(max_length=11)


    def __str__(self):
        return "Nome: " + self.name +  "Idade: " + self.age + "Email: " + self.email + "Telefone: " + self.telefone
