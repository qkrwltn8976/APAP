# Generated by Django 2.2.2 on 2019-08-09 16:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0017_print_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='color',
            field=models.CharField(blank=True, choices=[('colorful', '컬러'), ('grayish', '흑백')], max_length=10),
        ),
        migrations.AlterField(
            model_name='print',
            name='delivery_price',
            field=models.IntegerField(blank=True, default=2500),
        ),
        migrations.AlterField(
            model_name='print',
            name='direction',
            field=models.CharField(blank=True, choices=[('horizontal', '가로'), ('vertical', '세로')], max_length=10),
        ),
        migrations.AlterField(
            model_name='print',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='print',
            name='gather',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='print',
            name='pages',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='print',
            name='print_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='print',
            name='requests',
            field=models.ManyToManyField(blank=True, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='print',
            name='schedule',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='models.Schedule'),
        ),
        migrations.AlterField(
            model_name='print',
            name='side',
            field=models.CharField(blank=True, choices=[('single', '단면'), ('double', '양면')], max_length=10),
        ),
        migrations.AlterField(
            model_name='print',
            name='uploader',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='print',
            name='valid',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
