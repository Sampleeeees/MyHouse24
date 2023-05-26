# Generated by Django 3.2.15 on 2023-03-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0006_auto_20230329_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(30, 'Виконано'), (20, 'В роботі'), (10, 'Нове'), (None, '')], max_length=50),
        ),
        migrations.AlterField(
            model_name='matsterapplication',
            name='typeMaster',
            field=models.CharField(blank=True, choices=[(10, 'Сантехник'), (20, 'Електрик'), (None, ''), (30, 'Слюсар')], max_length=50, null=True),
        ),
    ]
