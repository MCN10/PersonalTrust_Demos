# Generated by Django 3.2.4 on 2021-06-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
