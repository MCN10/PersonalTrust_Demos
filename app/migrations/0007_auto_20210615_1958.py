# Generated by Django 3.2.4 on 2021-06-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_beneficiary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='id_number',
            field=models.IntegerField(max_length=12),
        ),
    ]
