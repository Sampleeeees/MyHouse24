# Generated by Django 3.2.15 on 2023-05-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0061_auto_20230521_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='confirm',
            field=models.CharField(blank=True, choices=[('Проведена', 'Проведена'), ('Не проведена', 'Не проведена')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Оплачена', 'Оплачена'), ('Неоплачена', 'Неоплачена '), ('Частково оплачена', 'Частково оплачена')], max_length=50),
        ),
    ]