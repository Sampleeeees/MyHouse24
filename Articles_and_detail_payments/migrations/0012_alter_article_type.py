# Generated by Django 3.2.15 on 2023-04-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_and_detail_payments', '0011_alter_article_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(blank=True, choices=[('Розхід', 'Розхід'), ('Прихід', 'Прихід')], max_length=50),
        ),
    ]
