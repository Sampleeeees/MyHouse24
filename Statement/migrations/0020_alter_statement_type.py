# Generated by Django 3.2.15 on 2023-05-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0019_auto_20230522_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='type',
            field=models.CharField(blank=True, choices=[('Прихід', 'Прихід'), ('Розхід', 'Розхід')], max_length=50, null=True),
        ),
    ]
