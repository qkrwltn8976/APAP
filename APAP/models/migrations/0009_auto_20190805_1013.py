# Generated by Django 2.2.2 on 2019-08-05 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_auto_20190805_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_lecture', to='models.Lecture'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='lectures',
            field=models.ManyToManyField(related_name='_user_lectures_+', through='models.Schedule', to='models.Lecture'),
        ),
    ]
