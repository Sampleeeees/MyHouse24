# Generated by Django 3.2.15 on 2023-05-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meters_data', '0045_alter_metersdata_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metersdata',
            name='status',
            field=models.CharField(choices=[('Враховано та заплачено', 'Враховано та заплачено'), ('Нове', 'Нове'), ('Враховано', 'Враховано'), ('Нульове', 'Нульове')], max_length=50),
        ),
    ]