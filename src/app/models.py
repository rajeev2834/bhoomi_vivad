# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from phone_field import PhoneField
from django.conf import settings


class Circle(models.Model):
    circle_id = models.CharField(primary_key=True, max_length=3)
    circle_name = models.CharField(max_length=40)
    circle_name_hn = models.CharField(max_length=40)
    last_update = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'circle'
        ordering = ["circle_id"]
    
    def __str__(self):
        return f"{self.circle_name_hn}"


class Panchayat(models.Model):
    panchayat_id = models.CharField(primary_key=True, max_length=3)
    circle = models.ForeignKey(Circle, models.DO_NOTHING, null=True)
    panchayat_name = models.CharField(max_length=40, blank=True, null=True)
    panchayat_name_hn = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'panchayat'
        ordering = ["panchayat_id"]

    def __str__(self):
        return f"{self.panchayat_name_hn}"


class Mauza(models.Model):
    mauza_id = models.AutoField(primary_key=True)
    circle = models.ForeignKey(Circle, models.DO_NOTHING, null = True)
    panchayat = models.ForeignKey('Panchayat', models.DO_NOTHING, blank=True, null=True)
    mauza_name = models.CharField(max_length=40, blank=True, null=True)
    mauza_name_hn = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    thana_no = models.CharField(max_length=4, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'mauza'
        ordering = ["mauza_id"]

    def __str__(self):
        return f"{self.mauza_name_hn}"


class Thana(models.Model):
    thana_id = models.AutoField(primary_key=True)
    circle = models.ForeignKey(Circle, models.DO_NOTHING, null=True)
    thana_name = models.CharField(max_length=40, blank=True, null=True)
    thana_name_hn = models.CharField(max_length=40, blank=True, null=True)
    thana_no = models.CharField(max_length=4, blank=True, null=True)
    last_update = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'thana'
        ordering = ["thana_name_hn"]


class PlotType(models.Model):
    plot_type = models.CharField(max_length=100)

    class Meta:
        db_table= 'plot_type'

    def __str__(self):
        return self.plot_type

class PlotNature(models.Model):
    plot_nature = models.CharField(max_length=50)

    class Meta:
        db_table= 'plot_nature'

    def __str__(self):
        return self.plot_nature


class Vivad(models.Model):
    CASE_STATUS =(
        (0,"Pending"),
        (1,"Closed"),
    )

    vivad_id = models.CharField(primary_key=True, max_length=12)
    circle = models.ForeignKey(Circle, models.DO_NOTHING, blank=True, null=True)
    panchayat = models.ForeignKey(Panchayat, models.DO_NOTHING, blank=True, null=True)
    thana_no = models.CharField(max_length=4, blank=True, null=True)
    khata_no = models.CharField(max_length=10, blank=True, null=True)
    khesra_no = models.CharField(max_length=10, blank=True, null=True)
    rakwa = models.CharField(max_length=5, blank=True, null=True)
    chauhaddi = models.CharField(max_length=100, blank=True, null=True)
    plot_type = models.ForeignKey(PlotType, models.DO_NOTHING, blank=True, null=True)
    plot_nature = models.ForeignKey(PlotNature, models.DO_NOTHING, blank=True, null=True)
    abhidhari_name = models.CharField(max_length=50, blank=True, null=True)
    first_party_name = models.TextField(max_length=50, blank=True)
    first_party_contact = PhoneField(blank=True, help_text='Contact phone number')
    first_party_address = models.TextField(max_length=100, blank=True)
    second_party_name = models.TextField(max_length=50, blank=True)
    second_party_contact = PhoneField(blank=True, help_text='Contact phone number')
    second_party_address = models.TextField(max_length=100, blank=True)
    cause_vivad = models.CharField(max_length=200, blank=True, null=True)
    is_violence = models.BooleanField(max_length=1, default=False, blank=True)
    violence_detail = models.CharField(max_length=200, blank=True, null=True)
    is_fir = models.BooleanField(max_length=1, default=False, blank=True)
    notice_order = models.CharField(max_length=200, blank=True, null=True)
    is_courtpending = models.BooleanField(max_length=1, default=False, blank=True)
    court_status = models.CharField(max_length=200, blank=True, null=True)
    case_status = models.BooleanField(choices=CASE_STATUS, default=0)
    next_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    mauza = models.ForeignKey(Mauza, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'vivad'
        ordering = ["vivad_id"]

    def __str__(self):
        return f"{self.vivad_id}"

class Hearing(models.Model):
    vivad = models.ForeignKey(Vivad, on_delete=models.CASCADE, null=True)
    hearing_date = models.DateTimeField(blank=True)
    remarks = models.TextField(max_length=200, blank=True)

    class Meta:
        db_table = 'hearing'
        ordering = ["vivad", "-hearing_date"]