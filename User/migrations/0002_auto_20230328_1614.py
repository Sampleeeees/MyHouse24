# Generated by Django 3.2.15 on 2023-03-28 16:14

import User.managers
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', User.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
