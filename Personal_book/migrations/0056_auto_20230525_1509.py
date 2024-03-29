# Generated by Django 3.2.15 on 2023-05-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0055_auto_20230525_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='residual',
            field=models.CharField(blank=True, choices=[('Є борг', 'Є борг'), ('Немає боргу', 'Немає боргу')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[('Неактивний', 'Неактивний'), ('Активний', 'Активний')], max_length=50),
        ),
    ]
