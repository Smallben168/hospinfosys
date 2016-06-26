from django.contrib import admin

# from  ---- import
import hismaxdb.models

class PatientStatusAdmin(admin.ModelAdmin):
    list_display = ('view_date', 'chart_no', 'location_code')

class ChartAdmin(admin.ModelAdmin):
    list_display = ('chart_no', 'pt_name', 'id_no', 'birth_date', 'sex')

# Register your models here.
admin.site.register(hismaxdb.models.Chart, ChartAdmin)
admin.site.register(hismaxdb.models.BeaconInfo)
admin.site.register(hismaxdb.models.PatientStatus, PatientStatusAdmin)
admin.site.register(hismaxdb.models.PatientServiceno)
admin.site.register(hismaxdb.models.PatientTrace)
