# Generated by Django 3.1.2 on 2020-11-03 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20201103_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo_user',
        ),
    ]
