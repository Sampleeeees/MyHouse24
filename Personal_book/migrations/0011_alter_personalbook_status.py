# Generated by Django 3.2.15 on 2023-04-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0010_alter_personalbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[(None, 'Активний'), (10000, 'Неактивний')], max_length=50),
        ),
    ]
