# Generated by Django 3.2.15 on 2023-04-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0013_alter_receipt_status_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[(None, 'Оберіть...'), (2000, 'Частково оплачена'), (3000, 'Неоплачена '), (1000, 'Оплачена')], max_length=50),
        ),
    ]
