# Generated by Django 3.2.15 on 2023-03-28 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('status_perfom', models.BooleanField()),
                ('comment', models.CharField(max_length=250)),
                ('date_published', models.DateField()),
                ('ownerAppartemnt', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Owner_appartament', to='User.user', verbose_name='ВолодарКвартири')),
                ('user_manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_manager', to='User.user', verbose_name='Менеджер')),
            ],
        ),
    ]
