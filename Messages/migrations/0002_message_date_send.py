# Generated by Django 3.2.15 on 2023-04-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_send',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
