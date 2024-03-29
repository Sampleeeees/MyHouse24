# Generated by Django 3.2.15 on 2023-03-28 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Appartament', '0001_initial'),
        ('Tarrif_and_services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BooleanField()),
                ('date_created', models.DateField()),
                ('status_pay', models.CharField(blank=True, choices=[(1000, 'Оплачена'), (3000, 'Неоплачена '), (None, 'Оберіть...'), (2000, 'Частково оплачена')], max_length=50)),
                ('appartament', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Appartament.appartament', verbose_name='Квартира')),
                ('tarrif', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Tarrif_and_services.tarrif', verbose_name='Тариф')),
            ],
        ),
    ]
