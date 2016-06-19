# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

#----Ben Momo -----
# python manage.py inspectdb  > models_20160509.py

from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    area_code = models.IntegerField(db_column='AREA_CODE', primary_key=True)  # Field name made lowercase.
    main_name = models.CharField(db_column='MAIN_NAME', max_length=12)  # Field name made lowercase.
    zip_code = models.IntegerField(db_column='ZIP_CODE', blank=True, null=True)  # Field name made lowercase.
    tel_code = models.CharField(db_column='TEL_CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    heaf_code = models.CharField(db_column='HEAF_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    old_main_name = models.CharField(db_column='OLD_MAIN_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREA'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chart(models.Model):
    chart_no = models.IntegerField(db_column='CHART_NO', primary_key=True)  # Field name made lowercase.
    pt_name = models.CharField(db_column='PT_NAME', max_length=20)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_no_ok = models.CharField(db_column='ID_NO_OK', max_length=1)  # Field name made lowercase.
    photocopy = models.CharField(db_column='PHOTOCOPY', max_length=1)  # Field name made lowercase.
    birth_date = models.CharField(db_column='BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    first_view_date = models.CharField(db_column='FIRST_VIEW_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    last_view_date = models.CharField(db_column='LAST_VIEW_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=7)  # Field name made lowercase.
    create_clerk = models.CharField(db_column='CREATE_CLERK', max_length=6)  # Field name made lowercase.
    modify_date = models.CharField(db_column='MODIFY_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1)  # Field name made lowercase.
    pt_type = models.IntegerField(db_column='PT_TYPE')  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=6, blank=True, null=True)  # Field name made lowercase.
    last_xray_date = models.CharField(db_column='LAST_XRAY_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    last_exam_date = models.CharField(db_column='LAST_EXAM_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    med_pack = models.CharField(db_column='MED_PACK', max_length=1)  # Field name made lowercase.
    foreign = models.CharField(db_column='FOREIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    merge_to = models.DecimalField(db_column='MERGE_TO', max_digits=7, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    emp_no = models.CharField(db_column='EMP_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    who_disc = models.CharField(db_column='WHO_DISC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    inp_discount_ptr = models.IntegerField(db_column='INP_DISCOUNT_PTR', blank=True, null=True)  # Field name made lowercase.
    opd_discount_ptr = models.IntegerField(db_column='OPD_DISCOUNT_PTR', blank=True, null=True)  # Field name made lowercase.
    died_trans_clerk = models.CharField(db_column='DIED_TRANS_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    died_trans_date = models.CharField(db_column='DIED_TRANS_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    died_cert_no = models.CharField(db_column='DIED_CERT_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    died_reason = models.CharField(db_column='DIED_REASON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    died_date = models.CharField(db_column='DIED_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vs_when_died = models.CharField(db_column='VS_WHEN_DIED', max_length=6, blank=True, null=True)  # Field name made lowercase.
    comefrom_no = models.CharField(db_column='COMEFROM_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    locking_clerk = models.CharField(db_column='LOCKING_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    locking_datetime = models.CharField(db_column='LOCKING_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    died_time = models.CharField(db_column='DIED_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    blood = models.CharField(db_column='BLOOD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    newborn_id_no = models.CharField(db_column='NEWBORN_ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    newborn_birth_date = models.CharField(db_column='NEWBORN_BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    newborn_note = models.CharField(db_column='NEWBORN_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    first_hr_date = models.CharField(db_column='FIRST_HR_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    grind = models.CharField(db_column='GRIND', max_length=1)  # Field name made lowercase.
    spec_no = models.CharField(db_column='SPEC_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    childbirth_date = models.CharField(db_column='CHILDBIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ic_card_no = models.CharField(db_column='IC_CARD_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g_times = models.IntegerField(db_column='G_TIMES', blank=True, null=True)  # Field name made lowercase.
    p_times = models.IntegerField(db_column='P_TIMES', blank=True, null=True)  # Field name made lowercase.
    sendmsg_all_flag = models.CharField(db_column='SENDMSG_ALL_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_sendmsg_date = models.CharField(db_column='LAST_SENDMSG_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    inj_sendmsg_date = models.CharField(db_column='INJ_SENDMSG_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    breat_sendmsg_date = models.CharField(db_column='BREAT_SENDMSG_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sensitive_label = models.CharField(db_column='SENSITIVE_LABEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lmp_date = models.CharField(db_column='LMP_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    aborigine = models.CharField(db_column='ABORIGINE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    privacy_flag = models.CharField(db_column='PRIVACY_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dnr_flag = models.CharField(db_column='DNR_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dnr_sign = models.CharField(db_column='DNR_SIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    raiseorg_flag = models.CharField(db_column='RAISEORG_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    is_cs_his = models.CharField(db_column='IS_CS_HIS', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHART'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Pttype(models.Model):
    pt_type = models.IntegerField(db_column='PT_TYPE', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME', max_length=10)  # Field name made lowercase.
    price_type = models.IntegerField(db_column='PRICE_TYPE', blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PTTYPE'



class Requisition(models.Model):
    req_no = models.CharField(db_column='REQ_NO', primary_key=True, max_length=13)  # Field name made lowercase.
    req_datetime = models.CharField(db_column='REQ_DATETIME', max_length=13)  # Field name made lowercase.
    print_times = models.IntegerField(db_column='PRINT_TIMES')  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1)  # Field name made lowercase.
    form_no = models.CharField(db_column='FORM_NO', max_length=2)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    serno = models.IntegerField(db_column='SERNO')  # Field name made lowercase.
    order_date = models.CharField(db_column='ORDER_DATE', max_length=7)  # Field name made lowercase.
    processed = models.CharField(db_column='PROCESSED', max_length=1)  # Field name made lowercase.
    seq_no = models.IntegerField(db_column='SEQ_NO', blank=True, null=True)  # Field name made lowercase.
    exam_type = models.CharField(db_column='EXAM_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exam_sample = models.CharField(db_column='EXAM_SAMPLE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    exam_information = models.CharField(db_column='EXAM_INFORMATION', max_length=240, blank=True, null=True)  # Field name made lowercase.
    sch_date = models.CharField(db_column='SCH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sch_time = models.CharField(db_column='SCH_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.TextField(db_column='DIAGNOSIS', blank=True, null=True)  # Field name made lowercase.
    pack_type = models.CharField(db_column='PACK_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirm_datetime = models.CharField(db_column='CONFIRM_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    confirm_clerk = models.CharField(db_column='CONFIRM_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nolend_reason = models.CharField(db_column='NOLEND_REASON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(db_column='STOCK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rel_req_no = models.CharField(db_column='REL_REQ_NO', max_length=13, blank=True, null=True)  # Field name made lowercase.
    scrap_date = models.CharField(db_column='SCRAP_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    exam_anti = models.CharField(db_column='EXAM_ANTI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exam_datetime = models.CharField(db_column='EXAM_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    rel_req_no_o = models.CharField(db_column='REL_REQ_NO_O', max_length=13, blank=True, null=True)  # Field name made lowercase.
    processed_date = models.CharField(db_column='PROCESSED_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    check_in_flag = models.CharField(db_column='CHECK_IN_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    check_in_datetime = models.CharField(db_column='CHECK_IN_DATETIME', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REQUISITION'


class Schedule(models.Model):
    form_no = models.CharField(db_column='FORM_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    form_name = models.CharField(db_column='FORM_NAME', max_length=50)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.
    subtel1 = models.CharField(db_column='SUBTEL1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subtel2 = models.CharField(db_column='SUBTEL2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHEDULE'

# Ben add 2016/05/02
# 存放患者移動設備資訊
class RegisterDevice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    registration_id = models.CharField(db_column='REGISTRATION_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    register_datetime = models.DateTimeField(db_column='REGISTER_DATETIME', blank=True, null=True, auto_now=True)  # Field name made lowercase.
    eff_flag = models.CharField(db_column='EFF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'register_device'


class BeaconInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='MAJOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    minor = models.CharField(db_column='MINOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    eff_flag = models.CharField(db_column='EFF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'beacon_info'

class DeptLocation(models.Model):
    location_code = models.CharField(db_column='LOCATION_CODE', primary_key=True, max_length=5)  # Field name made lowercase.
    location_type = models.CharField(db_column='LOCATION_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='LOCATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept_location'
