# Generated by Django 3.2.15 on 2023-05-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statement', '0011_alter_statement_status'),
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
            field=models.CharField(blank=True, choices=[('Прихід', 'Прихід'), ('Розхід', 'Розхід')], max_length=50, null=True),
        ),
    ]