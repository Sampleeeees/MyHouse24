# Generated by Django 3.2.15 on 2023-05-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0030_alter_receipt_status_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[(2000, 'Частково оплачена'), (None, 'Оберіть...'), (1000, 'Оплачена'), (3000, 'Неоплачена ')], max_length=50),
        ),
    ]
