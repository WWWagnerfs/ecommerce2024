from django.contrib.auth.models import User
from django.db import models

from catproduto.models import Produto


class Pedido(models.Model):
    cliente = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    # endereco = models.TextField()
    # telefone = models.CharField(max_length=15)
    # cep = models.CharField(max_length=10)
    # cidade = models.CharField(max_length=50)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ('-criado',)

    def __str__(self):
        return f'Pedido do {str(self.id)}'

    def get_total(self):
        return sum(item.get_custo() for item in self.itens_pedido.all())

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedido')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField(default=1)


    class Meta:
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedidos'

    def __str__(self):
        return self.id

    def get_custo(self):
        return self.preco * self.quantidade
