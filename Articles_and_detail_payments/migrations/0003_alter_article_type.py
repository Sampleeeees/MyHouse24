# Generated by Django 3.2.15 on 2023-03-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_and_detail_payments', '0002_alter_article_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(blank=True, choices=[('Прихід', 'Прихід'), ('Розхід', 'Розхід')], max_length=50),
        ),
    ]
