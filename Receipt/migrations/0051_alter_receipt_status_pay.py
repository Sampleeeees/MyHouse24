# Generated by Django 3.2.15 on 2023-05-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0050_auto_20230517_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Частково оплачена', 'Частково оплачена'), ('Оплачена', 'Оплачена'), ('Неоплачена', 'Неоплачена ')], max_length=50),
        ),
    ]
