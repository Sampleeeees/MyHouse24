# Generated by Django 3.2.15 on 2023-04-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0008_auto_20230402_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(20, 'В роботі'), (10, 'Нове'), (None, ''), (30, 'Виконано')], max_length=50),
        ),
        migrations.AlterField(
            model_name='matsterapplication',
            name='typeMaster',
            field=models.CharField(blank=True, choices=[(30, 'Слюсар'), (20, 'Електрик'), (10, 'Сантехник'), (None, '')], max_length=50, null=True),
        ),
    ]
