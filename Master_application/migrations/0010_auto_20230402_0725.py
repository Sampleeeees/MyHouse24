# Generated by Django 3.2.15 on 2023-04-02 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master_application', '0009_auto_20230402_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matsterapplication',
            name='status',
            field=models.CharField(blank=True, choices=[(10, 'Нове'), (20, 'В роботі'), (None, ''), (30, 'Виконано')], max_length=50),
        ),
        migrations.AlterField(
            model_name='matsterapplication',
            name='typeMaster',
            field=models.CharField(blank=True, choices=[(30, 'Слюсар'), (10, 'Сантехник'), (None, ''), (20, 'Електрик')], max_length=50, null=True),
        ),
    ]