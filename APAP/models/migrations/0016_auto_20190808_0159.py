# Generated by Django 2.2.2 on 2019-08-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_auto_20190808_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printrequest',
            name='point',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
