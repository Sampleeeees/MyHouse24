# Generated by Django 3.2.15 on 2023-04-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_alter_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='about_user'),
        ),
    ]
