# Generated by Django 3.2.15 on 2023-04-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0002_message_date_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_send',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]