# Generated by Django 3.2.5 on 2021-08-02 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210802_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='url',
        ),
    ]
