# Generated by Django 3.1.5 on 2024-03-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps1', '0003_auto_20240322_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockentry',
            name='itemType',
        ),
        migrations.AddField(
            model_name='stockentry',
            name='item_name',
            field=models.CharField(default='computers', max_length=250),
        ),
    ]
