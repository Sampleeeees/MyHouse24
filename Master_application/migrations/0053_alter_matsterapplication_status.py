# Generated by Django 3.2.15 on 2023-05-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0052_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('Нове', 'Нове'), ('Виконано', 'Виконано'), ('В роботі', 'В роботі')], max_length=50),
        ),
    ]
