# Generated by Django 3.2.15 on 2023-04-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0007_alter_personalbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[(10000, 'Неактивний'), (None, 'Активний')], max_length=50),
        ),
    ]
