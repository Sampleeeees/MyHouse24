# Generated by Django 3.2.15 on 2023-05-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0072_auto_20230523_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Частково оплачена', 'Частково оплачена'), ('Неоплачена', 'Неоплачена'), ('Оплачена', 'Оплачена')], max_length=50),
        ),
    ]
