# Generated by Django 3.1.2 on 2020-10-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_todo_todo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
