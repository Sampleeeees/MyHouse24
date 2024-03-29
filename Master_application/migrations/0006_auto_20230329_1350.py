# Generated by Django 3.2.15 on 2023-03-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0005_auto_20230329_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(20, 'В роботі'), (None, ''), (10, 'Нове'), (30, 'Виконано')], max_length=50),
        ),
        migrations.AlterField(
            model_name='matsterapplication',
            name='typeMaster',
            field=models.CharField(blank=True, choices=[(20, 'Електрик'), (10, 'Сантехник'), (None, ''), (30, 'Слюсар')], max_length=50, null=True),
        ),
    ]
