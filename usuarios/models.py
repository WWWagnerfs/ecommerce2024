from django.db import models


class Pedido(models.Model):
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
