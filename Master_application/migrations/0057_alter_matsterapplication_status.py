# Generated by Django 3.2.15 on 2023-05-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0056_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('В роботі', 'В роботі'), ('Нове', 'Нове'), ('Виконано', 'Виконано')], max_length=50),
        ),
    ]
