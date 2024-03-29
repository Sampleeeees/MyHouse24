# Generated by Django 3.2.15 on 2023-05-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0067_auto_20230522_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='confirmtext',
        ),
        migrations.AddField(
            model_name='receipt',
            name='confirm_text',
            field=models.CharField(blank=True, choices=[('Не проведена', 'Не проведена'), ('Проведена', 'Проведена')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status_pay',
            field=models.CharField(blank=True, choices=[('Неоплачена', 'Неоплачена '), ('Оплачена', 'Оплачена'), ('Частково оплачена', 'Частково оплачена')], max_length=50),
        ),
    ]
