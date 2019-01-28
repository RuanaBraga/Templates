from django.db import models

class cadastro(models.Model):
    nome = models.CharField(max_length=100),
    cpf = models.CharField(max_length=14),
    telefone = models.CharField(max_length=15),



