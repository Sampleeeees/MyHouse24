# Generated by Django 3.2.15 on 2023-05-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0020_alter_personalbook_residual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[('Активний', 'Активний'), ('Неактивний', 'Неактивний')], max_length=50),
        ),
    ]