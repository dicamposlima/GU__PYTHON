# Generated by Django 3.0.6 on 2020-05-11 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200510_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(on_delete=models.SET('IN'), to='core.Montadora'),
        ),
    ]
