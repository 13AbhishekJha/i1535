# Generated by Django 3.1.7 on 2021-12-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='present',
            field=models.BooleanField(default=True),
        ),
    ]
