# Generated by Django 2.2.2 on 2019-08-03 02:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20190803_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='requests',
            field=models.ManyToManyField(related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]