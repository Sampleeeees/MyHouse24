# Generated by Django 3.2.15 on 2023-05-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0053_auto_20230524_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[('Неактивний', 'Неактивний'), ('Активний', 'Активний')], max_length=50),
        ),
    ]
