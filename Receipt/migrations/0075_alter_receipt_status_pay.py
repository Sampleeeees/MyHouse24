# Generated by Django 3.2.15 on 2023-05-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0074_alter_receipt_status_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Оплачена', 'Оплачена'), ('Неоплачена', 'Неоплачена'), ('Частково оплачена', 'Частково оплачена')], max_length=50),
        ),
    ]
