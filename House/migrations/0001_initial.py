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
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_home', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='house/image/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='house/image/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='house/image/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='house/image/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='house/image/')),
                ('staff', models.ManyToManyField(blank=True, null=True, related_name='ПрацівникиУБудинку', to='User.User')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_section', models.CharField(max_length=100)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='House.house', verbose_name='Будинок')),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_floor', models.CharField(max_length=100)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='House.house', verbose_name='Будинок')),
            ],
        ),
    ]