# Generated by Django 3.2.15 on 2023-05-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0026_alter_personalbook_residual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='residual',
            field=models.CharField(blank=True, choices=[('Є борг', 'Є борг'), ('Немає боргу', 'Немає боргу')], max_length=150, null=True),
        ),
    ]
