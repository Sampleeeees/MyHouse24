# Generated by Django 3.2.15 on 2023-05-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0031_alter_statement_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='status',
            field=models.CharField(blank=True, choices=[('Не проведений', 'Не проведений'), ('Проведений', 'Проведений')], max_length=50, null=True),
        ),
    ]
