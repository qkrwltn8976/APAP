# Generated by Django 2.2.2 on 2019-08-03 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='print',
            old_name='user',
            new_name='uploader',
        ),
    ]
