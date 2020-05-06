from django.db import models


class Produto(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=100)
    preco = models.DecimalField(verbose_name='Preco',
                                decimal_places=2,
                                max_digits=8)
    estoque = models.IntegerField(verbose_name='Quantidade em estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=100)
    sobrenome = models.CharField(verbose_name='Sobrenome',
                                 max_length=100)
    email = models.EmailField(verbose_name='E-mail',
                              max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
