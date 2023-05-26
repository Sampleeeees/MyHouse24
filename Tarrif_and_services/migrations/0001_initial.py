# Generated by Django 3.2.15 on 2023-03-28 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_measure', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_view', models.BooleanField()),
                ('service', models.CharField(max_length=50)),
                ('measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tarrif_and_services.measure')),
            ],
        ),
        migrations.CreateModel(
            name='Tarrif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tarrif', models.CharField(max_length=250)),
                ('description_tarrif', models.CharField(max_length=300)),
                ('published', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceforTariif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('service', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Tarrif_and_services.service', verbose_name='Послуга')),
                ('tarrif', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Tarrif_and_services.tarrif', verbose_name='Тариф')),
            ],
        ),
    ]
