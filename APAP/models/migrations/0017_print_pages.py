# Generated by Django 2.2.2 on 2019-08-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0016_auto_20190808_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='pages',
            field=models.IntegerField(default=1),
        ),
    ]
