# Generated by Django 3.2.15 on 2023-05-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0048_auto_20230522_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='residual',
            field=models.CharField(blank=True, choices=[('Є борг', 'Є борг'), ('Немає боргу', 'Немає боргу')], max_length=150, null=True),
        ),
    ]