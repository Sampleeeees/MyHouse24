# Generated by Django 3.2.15 on 2023-05-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0022_auto_20230522_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(blank=True, choices=[('Проведений', 'Проведений'), ('Не проведений', 'Не проведений')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='type',
            field=models.CharField(blank=True, choices=[('Розхід', 'Розхід'), ('Прихід', 'Прихід')], max_length=50, null=True),
        ),
    ]