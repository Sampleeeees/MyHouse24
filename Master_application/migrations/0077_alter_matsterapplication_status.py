# Generated by Django 3.2.15 on 2023-05-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0076_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('Виконано', 'Виконано'), ('Нове', 'Нове'), ('В роботі', 'В роботі')], max_length=50),
        ),
    ]
