# Generated by Django 3.2.15 on 2023-05-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0035_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('Виконано', 'Виконано'), ('В роботі', 'В роботі'), ('Нове', 'Нове')], max_length=50),
        ),
    ]
