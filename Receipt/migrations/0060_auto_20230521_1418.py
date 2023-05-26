# Generated by Django 3.2.15 on 2023-05-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0059_alter_receipt_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='personal_book',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Оплачена', 'Оплачена'), ('Неоплачена', 'Неоплачена '), ('Частково оплачена', 'Частково оплачена')], max_length=50),
        ),
    ]