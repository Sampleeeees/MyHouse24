# Generated by Django 3.2.15 on 2023-05-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0004_statement_sattus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='sattus',
        ),
        migrations.AddField(
            model_name='statement',
            name='status',
            field=models.CharField(choices=[('Проведений', 'Проведений'), ('Не проведений', 'Не проведений')], max_length=50, null=True),
        ),
    ]
