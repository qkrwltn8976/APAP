# Generated by Django 2.2.2 on 2019-07-28 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20190728_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='user',
        ),
    ]
