# Generated by Django 3.2.15 on 2023-05-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meters_data', '0021_alter_metersdata_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metersdata',
            name='status',
            field=models.CharField(choices=[('Враховано та заплачено', 'Враховано та заплачено'), ('Нульове', 'Нульове'), ('Враховано', 'Враховано'), ('Нове', 'Нове')], max_length=50),
        ),
    ]
