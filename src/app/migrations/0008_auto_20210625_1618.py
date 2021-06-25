# Generated by Django 3.2.4 on 2021-06-25 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210623_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotNature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_nature', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'plot_nature',
            },
        ),
        migrations.CreateModel(
            name='PlotType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'plot_type',
            },
        ),
        migrations.AddField(
            model_name='vivad',
            name='chauhaddi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vivad',
            name='court_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vivad',
            name='is_courtpending',
            field=models.BooleanField(blank=True, default=False, max_length=1),
        ),
        migrations.AddField(
            model_name='vivad',
            name='is_fir',
            field=models.BooleanField(blank=True, default=False, max_length=1),
        ),
        migrations.AddField(
            model_name='vivad',
            name='is_violence',
            field=models.BooleanField(blank=True, default=False, max_length=1),
        ),
        migrations.AddField(
            model_name='vivad',
            name='violence_detail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vivad',
            name='case_status',
            field=models.BooleanField(choices=[('Pending', 0), ('Disposed', 1)], default='Pending'),
        ),
        migrations.AddField(
            model_name='vivad',
            name='plot_nature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.plotnature'),
        ),
        migrations.AlterField(
            model_name='vivad',
            name='plot_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.plottype'),
        ),
    ]