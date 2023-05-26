# Generated by Django 3.2.15 on 2023-04-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0015_alter_receipt_status_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[(3000, 'Неоплачена '), (1000, 'Оплачена'), (2000, 'Частково оплачена'), (None, 'Оберіть...')], max_length=50),
        ),
    ]