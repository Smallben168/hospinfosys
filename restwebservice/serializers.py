from rest_framework import serializers

from hismaxdb.models import *


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('form_no', 'form_name', 'note')

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ('chart_no','pt_name', 'id_no', 'birth_date', 'sex')

class AreaSerializer(serializers.ModelSerializer):
    _object_name = serializers.SerializerMethodField('get_ObjectName')
    def get_ObjectName(self,null):
        return "AREA"

    class Meta:
        model = Area
        fields = ('_object_name','area_code','main_name', 'zip_code', 'tel_code')
        #fields = '__all__'
        #使用 '__all__' 來取代 -> fields = ('area_code','main_name', 'zip_code', 'tel_code')
        #使用 exclude = ('old_main_name',) 來排除某一欄

class RegisterDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterDevice
        fields = ('chart_no', 'id_no','birth_date','registration_id','register_datetime','eff_flag')

class DeptLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptLocation
        fields = ('location_code', 'location_type','zone', 'location_name')

class BeaconInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeaconInfo
        fields = ('uuid', 'location_code','major', 'minor','eff_flag')

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg
        fields = ('view_date', 'chart_no', 'duplicate_no','apn','clinic', 'doctor_no', 'view_no','reg_clerk','reg_time','prenatal_care')

class PatientServicelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientServicelist
        fields = ('location_code', 'view_date', 'seq_no', 'chart_no', 'pt_name','eff_flag')

class PatientServiceNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientServiceno
        fields = ('location_code', 'clinic_no', 'current_no')

class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = ('req_no', 'req_datetime', 'inp_opd', 'form_no', 'chart_no', 'serno','order_date', 'processed', 'exam_type')

class PatopdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patopd
        fields = ('view_date', 'chart_no', 'duplicate_no','doctor_no', 'div_no', 'disease_code', 'disease_name')


class OpdacntSerializer(serializers.ModelSerializer):
     class Meta:
        model = Opdacnt
        fields = ('view_date', 'chart_no', 'duplicate_no','rec_count', 'code', 'use', 'qty', 'acnt_no', 'price_type')

#_object_name = serializers.SerializerMethodField('get_ObjectName')
#    def get_ObjectName(self,null):
#        return "REG"
#   fields = ('_object_name',....