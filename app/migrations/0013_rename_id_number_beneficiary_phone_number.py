# Generated by Django 3.2.4 on 2021-06-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_beneficiary_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiary',
            old_name='id_number',
            new_name='phone_number',
        ),
    ]