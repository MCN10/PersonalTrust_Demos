# Generated by Django 3.2.4 on 2021-06-16 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210616_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiary',
            options={},
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer'),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='id_number',
            field=models.CharField(max_length=20),
        ),
    ]
