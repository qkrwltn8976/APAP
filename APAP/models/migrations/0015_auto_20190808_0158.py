# Generated by Django 2.2.2 on 2019-08-08 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0014_auto_20190807_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printrequest',
            name='point',
            field=models.IntegerField(blank=True),
        ),
    ]
