# Generated by Django 2.2.2 on 2019-08-05 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_auto_20190805_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='req_print',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='req_print', to='models.Print'),
            preserve_default=False,
        ),
    ]