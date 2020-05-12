"""Core Models"""
import uuid

from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'team/pictures/{filename}'


class Base(models.Model):
    created = models.DateTimeField(verbose_name=_('Data de criacao'),
                                   auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Data de modificacao'),
                                    auto_now=True)
    active = models.BooleanField(verbose_name=_('Ativo?'),
                                 default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', _('Configuracoes')),
        ('lni-stats-up', _('Estatisticas')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Camadas')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )
    service = models.CharField(verbose_name=_('Servico'),
                               max_length=100)
    description = models.TextField(verbose_name=_('Descricao'),
                                   max_length=200)
    icon = models.CharField(verbose_name=_('Ícone'),
                            max_length=12,
                            choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Servico')
        verbose_name_plural = _('Servicos')

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(verbose_name=_('Cargo'),
                                max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.position


class Team(Base):
    name = models.CharField(verbose_name=_('Nome'),
                            max_length=100)
    position = models.ForeignKey('core.Position',
                                 verbose_name=_('Cargo'),
                                 on_delete=models.CASCADE)
    bio = models.TextField(verbose_name=_('Biografia'),
                           max_length=200)
    picture = StdImageField(verbose_name=_('Imagem'),
                            upload_to=get_file_path,
                            variations={
                                'thumb': {
                                    'width': 480,
                                    'height': 480,
                                    'crop': True
                                }
                            })
    facebook = models.CharField(verbose_name='Facebook',
                                max_length=100,
                                default='#')
    twitter = models.CharField(verbose_name='Twitter',
                               max_length=100,
                               default='#')
    instagram = models.CharField(verbose_name='Instagram',
                                 max_length=100,
                                 default='#')

    class Meta:
        verbose_name = _('Colaborador')
        verbose_name_plural = _('Equipes')

    def __str__(self):
        return self.name
