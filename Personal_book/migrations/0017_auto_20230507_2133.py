# Generated by Django 3.2.15 on 2023-05-07 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_book', '0016_auto_20230504_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalbook',
            name='uid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalbook',
            name='status',
            field=models.CharField(blank=True, choices=[(10000, 'Неактивний'), (None, 'Активний')], max_length=50),
        ),
    ]
