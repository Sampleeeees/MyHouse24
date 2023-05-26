# Generated by Django 3.2.15 on 2023-04-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0024_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='matsterapplication',
            name='date_master',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matsterapplication',
            name='time_master',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(20, 'В роботі'), (10, 'Нове'), (30, 'Виконано')], max_length=50),
        ),
    ]
