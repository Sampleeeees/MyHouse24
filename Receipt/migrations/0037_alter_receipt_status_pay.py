# Generated by Django 3.2.15 on 2023-05-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0036_alter_receipt_status_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[(2000, 'Частково оплачена'), (1000, 'Оплачена'), (3000, 'Неоплачена '), (None, 'Оберіть...')], max_length=50),
        ),
    ]
