# Generated by Django 3.2.4 on 2021-08-19 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210819_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotdetail',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]