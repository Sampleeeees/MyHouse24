# Generated by Django 3.2.15 on 2023-05-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0072_alter_matsterapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('Нове', 'Нове'), ('В роботі', 'В роботі'), ('Виконано', 'Виконано')], max_length=50),
        ),
    ]