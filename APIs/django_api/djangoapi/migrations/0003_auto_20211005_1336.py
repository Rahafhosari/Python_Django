# Generated by Django 3.2.7 on 2021-10-05 10:36

from django.db import migrations, models
import djangoapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=45, validators=[djangoapi.models.validateLength]),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=45, validators=[djangoapi.models.validateLength]),
        ),
    ]