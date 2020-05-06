"""Core Models"""
from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField(verbose_name='Data de criacao',
                                  auto_now_add=True)
    modificado = models.DateTimeField(verbose_name='Data de atualizacao',
                                      auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo?',
                                default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField(verbose_name='Nome',
                            max_length=100)
    preco = models.DecimalField(verbose_name='Preco',
                                max_digits=8,
                                decimal_places=2)
    estoque = models.IntegerField(verbose_name='Estoque')
    imagem = StdImageField(verbose_name='Imagem',
                           upload_to='produtos',
                           variations={'thumb': (124, 124)})
    slug = models.SlugField(verbose_name='Slug',
                            max_length=100,
                            blank=True)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
