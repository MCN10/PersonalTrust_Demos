# Generated by Django 3.2.4 on 2021-06-20 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_task_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
    ]
