from django.contrib import admin

from .models import Circle, Panchayat, Mauza, Thana, Vivad, Hearing, PlotNature, PlotType

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):

    list_display = ("circle_name_hn",)

@admin.register(Panchayat)
class PanchayatAdmin(admin.ModelAdmin):

    list_display = ("circle", "panchayat_name_hn")

@admin.register(Mauza)
class MauzaAdmin(admin.ModelAdmin):

    list_display = ("circle", "panchayat", "mauza_name_hn")


@admin.register(Thana)
class ThanaAdmin(admin.ModelAdmin):

    list_display = ("circle","thana_name_hn")

@admin.register(Vivad)
class VivadAdmin(admin.ModelAdmin):

    list_display = ("vivad_id", "circle","panchayat", "mauza")

@admin.register(Hearing)
class HearingAdmin(admin.ModelAdmin):

    list_display = ("vivad", "hearing_date", "remarks" )

@admin.register(PlotType)
class PlotTypeAdmin(admin.ModelAdmin):

    list_display = ("id","plot_type")

@admin.register(PlotNature)
class PlotNatureAdmin(admin.ModelAdmin):

    list_display = ("id", "plot_nature")
    

