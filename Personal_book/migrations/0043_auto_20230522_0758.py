# Generated by Django 3.2.15 on 2023-05-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0042_alter_personalbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='residual',
            field=models.CharField(blank=True, choices=[('Немає боргу', 'Немає боргу'), ('Є борг', 'Є борг')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[('Активний', 'Активний'), ('Неактивний', 'Неактивний')], max_length=50),
        ),
    ]
