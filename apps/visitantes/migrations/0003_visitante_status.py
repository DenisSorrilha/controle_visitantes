# Generated by Django 3.0 on 2021-07-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20210720_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISISTA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
