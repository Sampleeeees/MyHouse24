# Generated by Django 3.2.15 on 2023-05-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0035_auto_20230517_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='residual',
            field=models.CharField(blank=True, choices=[('Немає боргу', 'Немає боргу'), ('Є борг', 'Є борг')], max_length=150, null=True),
        ),
    ]
