# Generated by Django 3.2.15 on 2023-05-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0021_auto_20230522_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(blank=True, choices=[('Не проведений', 'Не проведений'), ('Проведений', 'Проведений')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='type',
            field=models.CharField(blank=True, choices=[('Прихід', 'Прихід'), ('Розхід', 'Розхід')], max_length=50, null=True),
        ),
    ]
