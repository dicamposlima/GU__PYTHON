"""Core Models"""
import uuid

from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'team/pictures/{filename}'


class Base(models.Model):
    created = models.DateTimeField(verbose_name='Created Date',
                                   auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modified Date',
                                    auto_now=True)
    active = models.BooleanField(verbose_name='Active?',
                                 default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Cog'),
        ('lni-stats-up', 'Stats'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Layers'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField(verbose_name='Service',
                               max_length=100)
    description = models.TextField(verbose_name='Description',
                                   max_length=200)
    icon = models.CharField(verbose_name='Icon',
                            max_length=12,
                            choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField(verbose_name='Position', max_length=100)

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.position


class Team(Base):
    name = models.CharField(verbose_name='Name',
                            max_length=100)
    position = models.ForeignKey('core.Position',
                                 verbose_name='Position',
                                 on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Bio',
                           max_length=200)
    picture = StdImageField(verbose_name='Image',
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
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name
