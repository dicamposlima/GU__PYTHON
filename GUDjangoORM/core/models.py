from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField(verbose_name='Chassi',
                              max_length=16,
                              help_text='Máximo 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            max_length=50,
                            help_text='Máximo 50 caracteres')

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():
    return Montadora.objects.get_or_create(nome='NI')[0]


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi,
                                  on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora,
                                  on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField(verbose_name='Modelo',
                              max_length=30,
                              help_text='Máximo 30 caracteres')
    preco = models.DecimalField(verbose_name='Preco',
                                max_digits=8,
                                decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.modelo} {self.modelo}'
