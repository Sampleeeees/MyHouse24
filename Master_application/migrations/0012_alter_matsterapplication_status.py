# Generated by Django 3.2.15 on 2023-04-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0011_auto_20230402_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(10, 'Нове'), (20, 'В роботі'), (30, 'Виконано'), (None, '')], max_length=50),
        ),
    ]
