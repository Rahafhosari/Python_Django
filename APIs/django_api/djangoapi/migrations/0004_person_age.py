# Generated by Django 3.2.7 on 2021-10-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0003_auto_20211005_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
