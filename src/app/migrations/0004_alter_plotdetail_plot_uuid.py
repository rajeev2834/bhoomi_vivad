# Generated by Django 3.2.4 on 2021-08-18 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_plotdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plotdetail',
            name='plot_uuid',
            field=models.UUIDField(editable=False, unique=True),
        ),
    ]