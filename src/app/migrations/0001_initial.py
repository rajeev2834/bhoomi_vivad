# Generated by Django 3.2.4 on 2021-08-08 17:35

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('circle_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('circle_name', models.CharField(max_length=40)),
                ('circle_name_hn', models.CharField(max_length=40)),
                ('last_update', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'circle',
                'ordering': ['circle_id'],
            },
        ),
        migrations.CreateModel(
            name='Hearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hearing_date', models.DateTimeField(blank=True)),
                ('is_first_present', models.BooleanField(blank=True, default=False, max_length=1)),
                ('is_second_present', models.BooleanField(blank=True, default=False, max_length=1)),
                ('remarks', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'hearing',
                'ordering': ['-hearing_date'],
            },
        ),
        migrations.CreateModel(
            name='Mauza',
            fields=[
                ('mauza_id', models.AutoField(primary_key=True, serialize=False)),
                ('mauza_name', models.CharField(blank=True, max_length=40, null=True)),
                ('mauza_name_hn', models.CharField(blank=True, max_length=40, null=True)),
                ('last_update', models.DateTimeField()),
                ('thana_no', models.CharField(blank=True, max_length=4, null=True)),
                ('circle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.circle')),
            ],
            options={
                'db_table': 'mauza',
                'ordering': ['mauza_id'],
            },
        ),
        migrations.CreateModel(
            name='Panchayat',
            fields=[
                ('panchayat_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('panchayat_name', models.CharField(blank=True, max_length=40, null=True)),
                ('panchayat_name_hn', models.CharField(blank=True, max_length=40, null=True)),
                ('last_update', models.DateTimeField()),
                ('circle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.circle')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'panchayat',
                'ordering': ['panchayat_id'],
            },
        ),
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
        migrations.CreateModel(
            name='Vivad',
            fields=[
                ('vivad_id', models.AutoField(primary_key=True, serialize=False)),
                ('thana_no', models.CharField(blank=True, max_length=4, null=True)),
                ('abhidhari_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_party_name', models.TextField(blank=True, max_length=50)),
                ('first_party_contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('first_party_address', models.TextField(blank=True, max_length=100)),
                ('second_party_name', models.TextField(blank=True, max_length=50)),
                ('second_party_contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('second_party_address', models.TextField(blank=True, max_length=100)),
                ('cause_vivad', models.CharField(blank=True, max_length=200, null=True)),
                ('is_violence', models.BooleanField(blank=True, default=False, max_length=1)),
                ('violence_detail', models.CharField(blank=True, max_length=200, null=True)),
                ('is_fir', models.BooleanField(blank=True, default=False, max_length=1)),
                ('notice_order', models.CharField(blank=True, max_length=200, null=True)),
                ('is_courtpending', models.BooleanField(blank=True, default=False, max_length=1)),
                ('court_status', models.CharField(blank=True, max_length=200, null=True)),
                ('case_status', models.BooleanField(choices=[(0, 'Pending'), (1, 'Closed')], default=0)),
                ('next_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('circle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.circle')),
                ('mauza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.mauza')),
                ('panchayat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.panchayat')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vivad',
                'ordering': ['vivad_id'],
            },
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('thana_id', models.AutoField(primary_key=True, serialize=False)),
                ('thana_name', models.CharField(blank=True, max_length=40, null=True)),
                ('thana_name_hn', models.CharField(blank=True, max_length=40, null=True)),
                ('thana_no', models.CharField(blank=True, max_length=4, null=True)),
                ('last_update', models.DateTimeField()),
                ('circle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.circle')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'thana',
                'ordering': ['thana_name_hn'],
            },
        ),
        migrations.CreateModel(
            name='PlotDetail',
            fields=[
                ('plot_id', models.AutoField(primary_key=True, serialize=False)),
                ('thana_no', models.CharField(blank=True, max_length=4, null=True)),
                ('khata_no', models.CharField(blank=True, max_length=10, null=True)),
                ('khesra_no', models.CharField(blank=True, max_length=10, null=True)),
                ('rakwa', models.CharField(blank=True, max_length=5, null=True)),
                ('chauhaddi', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.models.plot_image_file_path)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('circle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.circle')),
                ('mauza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.mauza')),
                ('panchayat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.panchayat')),
                ('plot_nature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.plotnature')),
                ('plot_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.plottype')),
            ],
            options={
                'db_table': 'plot_detail',
                'ordering': ['plot_id'],
            },
        ),
        migrations.AddField(
            model_name='mauza',
            name='panchayat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.panchayat'),
        ),
        migrations.AddField(
            model_name='mauza',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
