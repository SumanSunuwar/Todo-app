# Generated by Django 3.1.2 on 2020-10-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201023_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
