# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Bilamt(models.Model):
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    bill_no = models.IntegerField(db_column='BILL_NO')  # Field name made lowercase.
    categories = models.CharField(db_column='CATEGORIES', max_length=1)  # Field name made lowercase.
    acnt_no = models.IntegerField(db_column='ACNT_NO')  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    acnt_discount = models.DecimalField(db_column='ACNT_DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    comp_discount = models.DecimalField(db_column='COMP_DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    paid = models.DecimalField(db_column='PAID', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BILAMT'
        unique_together = (('chart_no', 'bill_no', 'categories', 'acnt_no'),)


class Bill(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    bill_no = models.IntegerField(db_column='BILL_NO')  # Field name made lowercase.
    categories = models.CharField(db_column='CATEGORIES', max_length=1)  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1)  # Field name made lowercase.
    bill_date = models.CharField(db_column='BILL_DATE', max_length=7)  # Field name made lowercase.
    serno = models.IntegerField(db_column='SERNO')  # Field name made lowercase.
    pt_type = models.IntegerField(db_column='PT_TYPE')  # Field name made lowercase.
    discount_ptr = models.IntegerField(db_column='DISCOUNT_PTR')  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    acnt_discount = models.DecimalField(db_column='ACNT_DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    comp_discount = models.DecimalField(db_column='COMP_DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    doubt = models.DecimalField(db_column='DOUBT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    overpay = models.DecimalField(db_column='OVERPAY', max_digits=10, decimal_places=0)  # Field name made lowercase.
    paid = models.DecimalField(db_column='PAID', max_digits=10, decimal_places=0)  # Field name made lowercase.
    pay_up_date = models.CharField(db_column='PAY_UP_DATE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    return_date = models.CharField(db_column='RETURN_DATE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    comefrom_no = models.CharField(db_column='COMEFROM_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    part_no = models.CharField(db_column='PART_NO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    part_amt = models.DecimalField(db_column='PART_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    infection_flag = models.CharField(db_column='INFECTION_FLAG', max_length=1)  # Field name made lowercase.
    chronic_flag = models.CharField(db_column='CHRONIC_FLAG', max_length=1)  # Field name made lowercase.
    force_type = models.CharField(db_column='FORCE_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BILL'


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


class Chart1(models.Model):
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    complaint = models.TextField(db_column='COMPLAINT', blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.TextField(db_column='DIAGNOSIS', blank=True, null=True)  # Field name made lowercase.
    temperature = models.IntegerField(db_column='TEMPERATURE', blank=True, null=True)  # Field name made lowercase.
    systolic_pressure = models.IntegerField(db_column='SYSTOLIC_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    diastolic_pressure = models.IntegerField(db_column='DIASTOLIC_PRESSURE', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    pulse = models.IntegerField(db_column='PULSE', blank=True, null=True)  # Field name made lowercase.
    blood_sugar = models.IntegerField(db_column='BLOOD_SUGAR', blank=True, null=True)  # Field name made lowercase.
    print_datetime = models.CharField(db_column='PRINT_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    create_datetime = models.CharField(db_column='CREATE_DATETIME', max_length=11)  # Field name made lowercase.
    create_clerk = models.CharField(db_column='CREATE_CLERK', max_length=6)  # Field name made lowercase.
    modify_datetime = models.CharField(db_column='MODIFY_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    plan = models.TextField(db_column='PLAN', blank=True, null=True)  # Field name made lowercase.
    diagnosis1 = models.TextField(db_column='DIAGNOSIS1', blank=True, null=True)  # Field name made lowercase.
    sona = models.TextField(db_column='SONA', blank=True, null=True)  # Field name made lowercase.
    sona_seq_no = models.IntegerField(db_column='SONA_SEQ_NO', blank=True, null=True)  # Field name made lowercase.
    sona1 = models.TextField(db_column='SONA1', blank=True, null=True)  # Field name made lowercase.
    sona_seq_no1 = models.IntegerField(db_column='SONA_SEQ_NO1', blank=True, null=True)  # Field name made lowercase.
    childbirth_date = models.CharField(db_column='CHILDBIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    p_times = models.IntegerField(db_column='P_TIMES', blank=True, null=True)  # Field name made lowercase.
    ap_childpos = models.CharField(db_column='AP_CHILDPOS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_gs = models.CharField(db_column='AP_GS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_crl = models.CharField(db_column='AP_CRL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_bpd = models.CharField(db_column='AP_BPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ac = models.CharField(db_column='AP_AC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_fl = models.CharField(db_column='AP_FL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ebw = models.CharField(db_column='AP_EBW', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_afi = models.CharField(db_column='AP_AFI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_gs2 = models.CharField(db_column='AP_GS2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_crl2 = models.CharField(db_column='AP_CRL2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_bpd2 = models.CharField(db_column='AP_BPD2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ac2 = models.CharField(db_column='AP_AC2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_fl2 = models.CharField(db_column='AP_FL2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ebw2 = models.CharField(db_column='AP_EBW2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_afi2 = models.CharField(db_column='AP_AFI2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_gs3 = models.CharField(db_column='AP_GS3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_crl3 = models.CharField(db_column='AP_CRL3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_bpd3 = models.CharField(db_column='AP_BPD3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ac3 = models.CharField(db_column='AP_AC3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_fl3 = models.CharField(db_column='AP_FL3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_ebw3 = models.CharField(db_column='AP_EBW3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ap_afi3 = models.CharField(db_column='AP_AFI3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_cs_his = models.CharField(db_column='IS_CS_HIS', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHART1'
        unique_together = (('view_date', 'chart_no', 'duplicate_no'),)


class Clin(models.Model):
    week = models.IntegerField(db_column='WEEK')  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN')  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    eff_date = models.CharField(db_column='EFF_DATE', max_length=7)  # Field name made lowercase.
    eff_time = models.CharField(db_column='EFF_TIME', max_length=6)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=1)  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=6)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    cash_type = models.CharField(db_column='CASH_TYPE', max_length=6)  # Field name made lowercase.
    no_type = models.CharField(db_column='NO_TYPE', max_length=1)  # Field name made lowercase.
    send_chart = models.CharField(db_column='SEND_CHART', max_length=1)  # Field name made lowercase.
    limit = models.IntegerField(db_column='LIMIT')  # Field name made lowercase.
    appoint = models.IntegerField(db_column='APPOINT')  # Field name made lowercase.
    single_view_min = models.IntegerField(db_column='SINGLE_VIEW_MIN')  # Field name made lowercase.
    pause = models.CharField(db_column='PAUSE', max_length=1)  # Field name made lowercase.
    pause_reason = models.CharField(db_column='PAUSE_REASON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    appoint_tel = models.CharField(db_column='APPOINT_TEL', max_length=1)  # Field name made lowercase.
    start_view_time = models.CharField(db_column='START_VIEW_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fv_limit = models.IntegerField(db_column='FV_LIMIT', blank=True, null=True)  # Field name made lowercase.
    rv_limit = models.IntegerField(db_column='RV_LIMIT', blank=True, null=True)  # Field name made lowercase.
    fv_visit = models.IntegerField(db_column='FV_VISIT', blank=True, null=True)  # Field name made lowercase.
    rv_visit = models.IntegerField(db_column='RV_VISIT', blank=True, null=True)  # Field name made lowercase.
    reserve_limit = models.IntegerField(db_column='RESERVE_LIMIT', blank=True, null=True)  # Field name made lowercase.
    stop_flag = models.CharField(db_column='STOP_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIN'
        unique_together = (('week', 'apn', 'zone', 'clinic', 'eff_date', 'eff_time'),)


class Clinic(models.Model):
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN')  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=6)  # Field name made lowercase.
    cash_type = models.CharField(db_column='CASH_TYPE', max_length=6)  # Field name made lowercase.
    send_chart = models.CharField(db_column='SEND_CHART', max_length=1)  # Field name made lowercase.
    limit = models.IntegerField(db_column='LIMIT')  # Field name made lowercase.
    no_type = models.CharField(db_column='NO_TYPE', max_length=1)  # Field name made lowercase.
    pause = models.CharField(db_column='PAUSE', max_length=1)  # Field name made lowercase.
    pause_reason = models.CharField(db_column='PAUSE_REASON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appoint = models.IntegerField(db_column='APPOINT')  # Field name made lowercase.
    single_view_min = models.IntegerField(db_column='SINGLE_VIEW_MIN')  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    appoint_tel = models.CharField(db_column='APPOINT_TEL', max_length=1)  # Field name made lowercase.
    start_view_time = models.CharField(db_column='START_VIEW_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fv_limit = models.IntegerField(db_column='FV_LIMIT', blank=True, null=True)  # Field name made lowercase.
    rv_limit = models.IntegerField(db_column='RV_LIMIT', blank=True, null=True)  # Field name made lowercase.
    fv_visit = models.IntegerField(db_column='FV_VISIT', blank=True, null=True)  # Field name made lowercase.
    rv_visit = models.IntegerField(db_column='RV_VISIT', blank=True, null=True)  # Field name made lowercase.
    reserve_limit = models.IntegerField(db_column='RESERVE_LIMIT', blank=True, null=True)  # Field name made lowercase.
    stop_flag = models.CharField(db_column='STOP_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    end_view_datetime = models.DateTimeField(db_column='END_VIEW_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLINIC'
        unique_together = (('view_date', 'apn', 'doctor_no', 'zone', 'clinic'),)


class Clinno(models.Model):
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN')  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    view_no = models.TextField(db_column='VIEW_NO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLINNO'
        unique_together = (('view_date', 'apn', 'zone', 'clinic'),)


class Clinps(models.Model):
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=14, blank=True, null=True)  # Field name made lowercase.
    floor = models.IntegerField(db_column='FLOOR', blank=True, null=True)  # Field name made lowercase.
    categories = models.CharField(db_column='CATEGORIES', max_length=1)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLINPS'
        unique_together = (('zone', 'clinic'),)


class Disicd(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=8)  # Field name made lowercase.
    title1 = models.CharField(db_column='TITLE1', max_length=210)  # Field name made lowercase.
    title2 = models.CharField(db_column='TITLE2', max_length=210)  # Field name made lowercase.
    sex_type = models.IntegerField(db_column='SEX_TYPE', blank=True, null=True)  # Field name made lowercase.
    he_code = models.CharField(db_column='HE_CODE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    div_kind = models.CharField(db_column='DIV_KIND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    major_care = models.CharField(db_column='MAJOR_CARE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    complaint = models.TextField(db_column='COMPLAINT', blank=True, null=True)  # Field name made lowercase.
    cause = models.TextField(db_column='CAUSE', blank=True, null=True)  # Field name made lowercase.
    advice = models.TextField(db_column='ADVICE', blank=True, null=True)  # Field name made lowercase.
    disease_type = models.CharField(db_column='DISEASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    start_age = models.DecimalField(db_column='START_AGE', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    end_age = models.IntegerField(db_column='END_AGE', blank=True, null=True)  # Field name made lowercase.
    confined_days = models.IntegerField(db_column='CONFINED_DAYS', blank=True, null=True)  # Field name made lowercase.
    importance_flag = models.CharField(db_column='IMPORTANCE_FLAG', max_length=1)  # Field name made lowercase.
    chronic_flag = models.CharField(db_column='CHRONIC_FLAG', max_length=1)  # Field name made lowercase.
    not_main = models.CharField(db_column='NOT_MAIN', max_length=1)  # Field name made lowercase.
    chronic_categories = models.CharField(db_column='CHRONIC_CATEGORIES', max_length=1, blank=True, null=True)  # Field name made lowercase.
    standard_day = models.IntegerField(db_column='STANDARD_DAY', blank=True, null=True)  # Field name made lowercase.
    care_level = models.CharField(db_column='CARE_LEVEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e1_spec_no = models.CharField(db_column='E1_SPEC_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    occupation_flag = models.CharField(db_column='OCCUPATION_FLAG', max_length=1)  # Field name made lowercase.
    clinic_note = models.CharField(db_column='CLINIC_NOTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    congenital = models.CharField(db_column='CONGENITAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ckd_flag = models.CharField(db_column='CKD_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISICD'


class Division(models.Model):
    div_no = models.CharField(db_column='DIV_NO', primary_key=True, max_length=6)  # Field name made lowercase.
    div_name = models.CharField(db_column='DIV_NAME', max_length=30)  # Field name made lowercase.
    opdhe_div = models.CharField(db_column='OPDHE_DIV', max_length=2)  # Field name made lowercase.
    inphe_div = models.CharField(db_column='INPHE_DIV', max_length=2)  # Field name made lowercase.
    precede_div_no = models.CharField(db_column='PRECEDE_DIV_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    emg = models.CharField(db_column='EMG', max_length=1)  # Field name made lowercase.
    tel_div_no = models.CharField(db_column='TEL_DIV_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stop_date = models.CharField(db_column='STOP_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bhp_div = models.CharField(db_column='BHP_DIV', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIVISION'


class Doctordoc(models.Model):
    doctor_no = models.CharField(db_column='DOCTOR_NO', primary_key=True, max_length=12)  # Field name made lowercase.
    context = models.TextField(db_column='CONTEXT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCTORDOC'


class Doctorhe(models.Model):
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    eff_date = models.CharField(db_column='EFF_DATE', max_length=7)  # Field name made lowercase.
    he_doctor_no = models.CharField(db_column='HE_DOCTOR_NO', max_length=6)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    out_date = models.CharField(db_column='OUT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCTORHE'
        unique_together = (('doctor_no', 'eff_date'),)


class Employee(models.Model):
    emp_no = models.CharField(db_column='EMP_NO', primary_key=True, max_length=6)  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=20)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    in_date = models.CharField(db_column='IN_DATE', max_length=7)  # Field name made lowercase.
    out_date = models.CharField(db_column='OUT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    current_stock = models.CharField(db_column='CURRENT_STOCK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    system_no = models.CharField(db_column='SYSTEM_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dept_no = models.CharField(db_column='DEPT_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='PASSWD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    degree = models.CharField(db_column='DEGREE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ordermyself = models.CharField(db_column='ORDERMYSELF', max_length=1)  # Field name made lowercase.
    treat_title = models.CharField(db_column='TREAT_TITLE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    tel_doctor_no = models.CharField(db_column='TEL_DOCTOR_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doctor_phone = models.CharField(db_column='DOCTOR_PHONE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    default_trans_emr_flag = models.CharField(db_column='DEFAULT_TRANS_EMR_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    default_sign_emr_flag = models.CharField(db_column='DEFAULT_SIGN_EMR_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    default_immediate_sign_flag = models.CharField(db_column='DEFAULT_IMMEDIATE_SIGN_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hca_pin = models.CharField(db_column='HCA_PIN', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'


class Feename(models.Model):
    categories = models.CharField(db_column='CATEGORIES', max_length=10)  # Field name made lowercase.
    no = models.IntegerField(db_column='NO')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    bill_categories = models.CharField(db_column='BILL_CATEGORIES', max_length=1)  # Field name made lowercase.
    acnt_flag = models.CharField(db_column='ACNT_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FEENAME'
        unique_together = (('categories', 'no'),)


class Firstview(models.Model):
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN')  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    view_no = models.IntegerField(db_column='VIEW_NO')  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=20)  # Field name made lowercase.
    key = models.CharField(db_column='KEY', max_length=10)  # Field name made lowercase.
    clerk = models.CharField(db_column='CLERK', max_length=6)  # Field name made lowercase.
    reg_time = models.CharField(db_column='REG_TIME', max_length=13)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FIRSTVIEW'
        unique_together = (('view_date', 'zone', 'apn', 'clinic', 'view_no'),)


class Hospital(models.Model):
    hosp_no = models.CharField(db_column='HOSP_NO', primary_key=True, max_length=12)  # Field name made lowercase.
    hosp_name = models.CharField(db_column='HOSP_NAME', max_length=50)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    common = models.CharField(db_column='COMMON', max_length=1)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    hosp_name_f = models.CharField(db_column='HOSP_NAME_F', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=12, blank=True, null=True)  # Field name made lowercase.
    hosp_net = models.CharField(db_column='HOSP_NET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    principal = models.CharField(db_column='PRINCIPAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nhi_hosp_no = models.CharField(db_column='NHI_HOSP_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOSPITAL'


class Hospset(models.Model):
    hosp_no = models.CharField(db_column='HOSP_NO', primary_key=True, max_length=10)  # Field name made lowercase.
    hosp_name = models.CharField(db_column='HOSP_NAME', max_length=50)  # Field name made lowercase.
    hosp_class = models.CharField(db_column='HOSP_CLASS', max_length=1)  # Field name made lowercase.
    hosp_boss = models.CharField(db_column='HOSP_BOSS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hosp_address = models.CharField(db_column='HOSP_ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hosp_tel = models.CharField(db_column='HOSP_TEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hosp_fax = models.CharField(db_column='HOSP_FAX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hosp_licence = models.CharField(db_column='HOSP_LICENCE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hosp_superintendent = models.CharField(db_column='HOSP_SUPERINTENDENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOSPSET'


class Medicine(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=7)  # Field name made lowercase.
    formal_name = models.CharField(db_column='FORMAL_NAME', max_length=100)  # Field name made lowercase.
    full_name_c = models.CharField(db_column='FULL_NAME_C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    med_type = models.CharField(db_column='MED_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    med_type2 = models.CharField(db_column='MED_TYPE2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    med_class = models.CharField(db_column='MED_CLASS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    invkind = models.CharField(db_column='INVKIND', max_length=6, blank=True, null=True)  # Field name made lowercase.
    adaptive = models.TextField(db_column='ADAPTIVE', blank=True, null=True)  # Field name made lowercase.
    usage = models.TextField(db_column='USAGE', blank=True, null=True)  # Field name made lowercase.
    side_effect = models.TextField(db_column='SIDE_EFFECT', blank=True, null=True)  # Field name made lowercase.
    adverse = models.TextField(db_column='ADVERSE', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.
    factor = models.TextField(db_column='FACTOR', blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    full_name_e = models.CharField(db_column='FULL_NAME_E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adaptive_e = models.TextField(db_column='ADAPTIVE_E', blank=True, null=True)  # Field name made lowercase.
    usage_e = models.TextField(db_column='USAGE_E', blank=True, null=True)  # Field name made lowercase.
    side_effect_e = models.TextField(db_column='SIDE_EFFECT_E', blank=True, null=True)  # Field name made lowercase.
    adverse_e = models.TextField(db_column='ADVERSE_E', blank=True, null=True)  # Field name made lowercase.
    note_e = models.TextField(db_column='NOTE_E', blank=True, null=True)  # Field name made lowercase.
    factor_e = models.TextField(db_column='FACTOR_E', blank=True, null=True)  # Field name made lowercase.
    facade = models.TextField(db_column='FACADE', blank=True, null=True)  # Field name made lowercase.
    facade_e = models.TextField(db_column='FACADE_E', blank=True, null=True)  # Field name made lowercase.
    warn_med_note = models.TextField(db_column='WARN_MED_NOTE', blank=True, null=True)  # Field name made lowercase.
    image_name = models.CharField(db_column='IMAGE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDICINE'


class Medicinephoto(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=7)  # Field name made lowercase.
    photo = models.TextField(db_column='PHOTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDICINEPHOTO'


class Medinteract(models.Model):
    med_code = models.CharField(db_column='MED_CODE', max_length=7)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=7)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDINTERACT'
        unique_together = (('med_code', 'code'),)


class Opdacnt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    rec_count = models.IntegerField(db_column='REC_COUNT')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=7)  # Field name made lowercase.
    identify_no = models.IntegerField(db_column='IDENTIFY_NO')  # Field name made lowercase.
    acnt_no = models.IntegerField(db_column='ACNT_NO')  # Field name made lowercase.
    price_type = models.IntegerField(db_column='PRICE_TYPE')  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY')  # Field name made lowercase.
    unuse = models.CharField(db_column='UNUSE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    use = models.CharField(db_column='USE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usetime = models.CharField(db_column='USETIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='DAY')  # Field name made lowercase.
    tqty = models.IntegerField(db_column='TQTY')  # Field name made lowercase.
    self = models.CharField(db_column='SELF', max_length=1)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT')  # Field name made lowercase.
    comp_discount = models.IntegerField(db_column='COMP_DISCOUNT')  # Field name made lowercase.
    amt = models.IntegerField(db_column='AMT')  # Field name made lowercase.
    he_add_fee = models.IntegerField(db_column='HE_ADD_FEE')  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    method1 = models.CharField(db_column='METHOD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    method2 = models.CharField(db_column='METHOD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emg = models.CharField(db_column='EMG', max_length=1)  # Field name made lowercase.
    add_rate = models.IntegerField(db_column='ADD_RATE')  # Field name made lowercase.
    office = models.CharField(db_column='OFFICE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(db_column='STOCK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    order_datetime = models.CharField(db_column='ORDER_DATETIME', max_length=11)  # Field name made lowercase.
    exec_clerk = models.CharField(db_column='EXEC_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    exec_datetime = models.CharField(db_column='EXEC_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    report_clerk = models.CharField(db_column='REPORT_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    report_datetime = models.CharField(db_column='REPORT_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='CASHIER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyin_datetime = models.CharField(db_column='KEYIN_DATETIME', max_length=11)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    modify_datetime = models.CharField(db_column='MODIFY_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    req_no = models.CharField(db_column='REQ_NO', max_length=13, blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='OPERATION', max_length=1, blank=True, null=True)  # Field name made lowercase.
    grind = models.CharField(db_column='GRIND', max_length=1)  # Field name made lowercase.
    cons_no = models.CharField(db_column='CONS_NO', max_length=70, blank=True, null=True)  # Field name made lowercase.
    noexe_reason = models.CharField(db_column='NOEXE_REASON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    office1 = models.CharField(db_column='OFFICE1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    max_price_times = models.IntegerField(db_column='MAX_PRICE_TIMES', blank=True, null=True)  # Field name made lowercase.
    order_pos = models.CharField(db_column='ORDER_POS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    start_time = models.CharField(db_column='START_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dicom_flag = models.CharField(db_column='DICOM_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    project_no = models.CharField(db_column='PROJECT_NO', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPDACNT'


class Patopd(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=6)  # Field name made lowercase.
    cash_type = models.CharField(db_column='CASH_TYPE', max_length=6)  # Field name made lowercase.
    fv_rv = models.CharField(db_column='FV_RV', max_length=1)  # Field name made lowercase.
    send_chart = models.CharField(db_column='SEND_CHART', max_length=1)  # Field name made lowercase.
    pt_type = models.IntegerField(db_column='PT_TYPE')  # Field name made lowercase.
    card_seq = models.CharField(db_column='CARD_SEQ', max_length=4, blank=True, null=True)  # Field name made lowercase.
    part_no = models.CharField(db_column='PART_NO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    expect_view_time = models.CharField(db_column='EXPECT_VIEW_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    comefrom_no = models.CharField(db_column='COMEFROM_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    regkind_no = models.CharField(db_column='REGKIND_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    visit = models.CharField(db_column='VISIT', max_length=1)  # Field name made lowercase.
    sheet_no = models.IntegerField(db_column='SHEET_NO', blank=True, null=True)  # Field name made lowercase.
    appointment = models.CharField(db_column='APPOINTMENT', max_length=1)  # Field name made lowercase.
    check_in_datetime = models.CharField(db_column='CHECK_IN_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    give_order = models.CharField(db_column='GIVE_ORDER', max_length=1)  # Field name made lowercase.
    apn = models.DecimalField(db_column='APN', max_digits=1, decimal_places=0)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    view_no = models.IntegerField(db_column='VIEW_NO')  # Field name made lowercase.
    supple_flag = models.CharField(db_column='SUPPLE_FLAG', max_length=1)  # Field name made lowercase.
    supple_datetime = models.CharField(db_column='SUPPLE_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    supple_clerk = models.CharField(db_column='SUPPLE_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    discount_ptr = models.IntegerField(db_column='DISCOUNT_PTR')  # Field name made lowercase.
    disease_code = models.CharField(db_column='DISEASE_CODE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name = models.CharField(db_column='DISEASE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code1 = models.CharField(db_column='DISEASE_CODE1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name1 = models.CharField(db_column='DISEASE_NAME1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code2 = models.CharField(db_column='DISEASE_CODE2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name2 = models.CharField(db_column='DISEASE_NAME2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code3 = models.CharField(db_column='DISEASE_CODE3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name3 = models.CharField(db_column='DISEASE_NAME3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code4 = models.CharField(db_column='DISEASE_CODE4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name4 = models.CharField(db_column='DISEASE_NAME4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code5 = models.CharField(db_column='DISEASE_CODE5', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name5 = models.CharField(db_column='DISEASE_NAME5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code6 = models.CharField(db_column='DISEASE_CODE6', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name6 = models.CharField(db_column='DISEASE_NAME6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    op_icd9 = models.CharField(db_column='OP_ICD9', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_1 = models.CharField(db_column='OP_ICD9_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_2 = models.CharField(db_column='OP_ICD9_2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_3 = models.CharField(db_column='OP_ICD9_3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_4 = models.CharField(db_column='OP_ICD9_4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    trans_in = models.CharField(db_column='TRANS_IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pricing_clerk = models.CharField(db_column='PRICING_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    drg_code = models.CharField(db_column='DRG_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    post_reg_flag = models.CharField(db_column='POST_REG_FLAG', max_length=1)  # Field name made lowercase.
    post_attend_fee = models.CharField(db_column='POST_ATTEND_FEE', max_length=1)  # Field name made lowercase.
    triage = models.CharField(db_column='TRIAGE', max_length=1)  # Field name made lowercase.
    med_days = models.IntegerField(db_column='MED_DAYS', blank=True, null=True)  # Field name made lowercase.
    med_order = models.IntegerField(db_column='MED_ORDER', blank=True, null=True)  # Field name made lowercase.
    who_disc = models.CharField(db_column='WHO_DISC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hospitalize_clerk = models.CharField(db_column='HOSPITALIZE_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hospitalize_datetime = models.CharField(db_column='HOSPITALIZE_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    serno = models.IntegerField(db_column='SERNO', blank=True, null=True)  # Field name made lowercase.
    blocked_reason = models.CharField(db_column='BLOCKED_REASON', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_clerk = models.CharField(db_column='REG_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    reg_datetime = models.CharField(db_column='REG_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    opd_clerk = models.CharField(db_column='OPD_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    opd_datetime = models.CharField(db_column='OPD_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    treat_clerk = models.CharField(db_column='TREAT_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    treat_datetime = models.CharField(db_column='TREAT_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    reg_amt = models.DecimalField(db_column='REG_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    disc_reg_amt = models.DecimalField(db_column='DISC_REG_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    case_type = models.CharField(db_column='CASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chronic_seq = models.IntegerField(db_column='CHRONIC_SEQ', blank=True, null=True)  # Field name made lowercase.
    he_date = models.CharField(db_column='HE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    begin_duplicate = models.IntegerField(db_column='BEGIN_DUPLICATE', blank=True, null=True)  # Field name made lowercase.
    begin_date = models.CharField(db_column='BEGIN_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_type = models.CharField(db_column='COURSE_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    course_deadline = models.CharField(db_column='COURSE_DEADLINE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_recent_date = models.CharField(db_column='COURSE_RECENT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_total_times = models.IntegerField(db_column='COURSE_TOTAL_TIMES', blank=True, null=True)  # Field name made lowercase.
    course_times = models.IntegerField(db_column='COURSE_TIMES', blank=True, null=True)  # Field name made lowercase.
    discount_relation = models.CharField(db_column='DISCOUNT_RELATION', max_length=6, blank=True, null=True)  # Field name made lowercase.
    reg_status = models.CharField(db_column='REG_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    force_type = models.CharField(db_column='FORCE_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='CARD_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ic_card_no = models.CharField(db_column='IC_CARD_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    child_birth_date = models.CharField(db_column='CHILD_BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    child_born_note = models.CharField(db_column='CHILD_BORN_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_type = models.CharField(db_column='CLINIC_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clinic_new_born_note = models.CharField(db_column='CLINIC_NEW_BORN_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_date_time = models.CharField(db_column='CLINIC_DATE_TIME', max_length=13, blank=True, null=True)  # Field name made lowercase.
    clinic_supple_note = models.CharField(db_column='CLINIC_SUPPLE_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_seq_no = models.CharField(db_column='CLINIC_SEQ_NO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    heal_note = models.CharField(db_column='HEAL_NOTE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    heal_service_item = models.CharField(db_column='HEAL_SERVICE_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pregnant_item = models.CharField(db_column='PREGNANT_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    secure_sign = models.CharField(db_column='SECURE_SIGN', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cardseq_status = models.CharField(db_column='CARDSEQ_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sam_id = models.CharField(db_column='SAM_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    hosp_id = models.CharField(db_column='HOSP_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transed = models.CharField(db_column='TRANSED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    card_error_code = models.DecimalField(db_column='CARD_ERROR_CODE', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(db_column='TRANS_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    trans_kind = models.CharField(db_column='TRANS_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_correct = models.CharField(db_column='DATA_CORRECT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    druggist_no = models.CharField(db_column='DRUGGIST_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    check_druggist_no = models.CharField(db_column='CHECK_DRUGGIST_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stop_recheck_fee = models.CharField(db_column='STOP_RECHECK_FEE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    occup_disease_flag = models.CharField(db_column='OCCUP_DISEASE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    appointment_mode = models.CharField(db_column='APPOINTMENT_MODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    income_clerk = models.CharField(db_column='INCOME_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    income_datetime = models.CharField(db_column='INCOME_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    merge_view_date = models.CharField(db_column='MERGE_VIEW_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    merge_duplicate_no = models.DecimalField(db_column='MERGE_DUPLICATE_NO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    merge_report_class = models.CharField(db_column='MERGE_REPORT_CLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    opdacnt_count = models.IntegerField(db_column='OPDACNT_COUNT', blank=True, null=True)  # Field name made lowercase.
    admittance = models.CharField(db_column='ADMITTANCE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    emg_accrue = models.CharField(db_column='EMG_ACCRUE', max_length=1)  # Field name made lowercase.
    cut_he_date = models.CharField(db_column='CUT_HE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    trans_in_type = models.CharField(db_column='TRANS_IN_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans_out_type = models.CharField(db_column='TRANS_OUT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans_out_hosp = models.CharField(db_column='TRANS_OUT_HOSP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    disability_flag = models.CharField(db_column='DISABILITY_FLAG', max_length=1)  # Field name made lowercase.
    course_merge_status = models.CharField(db_column='COURSE_MERGE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    spec_no = models.CharField(db_column='SPEC_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    need_cut_case = models.CharField(db_column='NEED_CUT_CASE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    undeclared = models.CharField(db_column='UNDECLARED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pt_type_1 = models.DecimalField(db_column='PT_TYPE_1', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    baby_inject = models.CharField(db_column='BABY_INJECT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    check_in_type = models.CharField(db_column='CHECK_IN_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendmsg_flag = models.CharField(db_column='SENDMSG_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reserve_msg_sent = models.CharField(db_column='RESERVE_MSG_SENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    need_trace_flag = models.CharField(db_column='NEED_TRACE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    front_case_type = models.CharField(db_column='FRONT_CASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    he_disease_anys = models.CharField(db_column='HE_DISEASE_ANYS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uc_div = models.CharField(db_column='UC_DIV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ic_limit_date = models.CharField(db_column='IC_LIMIT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    breast_trans_flag = models.CharField(db_column='BREAST_TRANS_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    trans_emr_date = models.DateTimeField(db_column='TRANS_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    sign_emr_date = models.DateTimeField(db_column='SIGN_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    his2emr_complete_date = models.CharField(db_column='HIS2EMR_COMPLETE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    spec_sensitive_label = models.CharField(db_column='SPEC_SENSITIVE_LABEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans2emr_complete_date = models.CharField(db_column='TRANS2EMR_COMPLETE_DATE', max_length=7)  # Field name made lowercase.
    exchange_sign_emr_date = models.DateTimeField(db_column='EXCHANGE_SIGN_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    skin_values = models.CharField(db_column='SKIN_VALUES', max_length=1, blank=True, null=True)  # Field name made lowercase.
    is_occupational = models.CharField(db_column='IS_OCCUPATIONAL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PATOPD'


class Payamt(models.Model):
    pay_no = models.IntegerField(db_column='PAY_NO')  # Field name made lowercase.
    acnt_no = models.IntegerField(db_column='ACNT_NO')  # Field name made lowercase.
    amt = models.IntegerField(db_column='AMT')  # Field name made lowercase.
    comp_discount = models.IntegerField(db_column='COMP_DISCOUNT')  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT')  # Field name made lowercase.
    paid = models.IntegerField(db_column='PAID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAYAMT'
        unique_together = (('pay_no', 'acnt_no'),)


class Payment(models.Model):
    pay_no = models.IntegerField(db_column='PAY_NO', primary_key=True)  # Field name made lowercase.
    pay_date = models.CharField(db_column='PAY_DATE', max_length=7)  # Field name made lowercase.
    pt_type = models.IntegerField(db_column='PT_TYPE', blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='CASHIER', max_length=6)  # Field name made lowercase.
    comefrom_no = models.CharField(db_column='COMEFROM_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1)  # Field name made lowercase.
    opd_date = models.CharField(db_column='OPD_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    serno = models.IntegerField(db_column='SERNO', blank=True, null=True)  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    discount_ptr = models.IntegerField(db_column='DISCOUNT_PTR')  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    ar = models.DecimalField(db_column='AR', max_digits=10, decimal_places=0)  # Field name made lowercase.
    supple_amt = models.DecimalField(db_column='SUPPLE_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    comp_discount = models.DecimalField(db_column='COMP_DISCOUNT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    bill_doubt = models.DecimalField(db_column='BILL_DOUBT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    overpay = models.DecimalField(db_column='OVERPAY', max_digits=10, decimal_places=0)  # Field name made lowercase.
    paid = models.DecimalField(db_column='PAID', max_digits=10, decimal_places=0)  # Field name made lowercase.
    paid_flag = models.CharField(db_column='PAID_FLAG', max_length=1)  # Field name made lowercase.
    paid_type = models.CharField(db_column='PAID_TYPE', max_length=1)  # Field name made lowercase.
    receipt_no = models.DecimalField(db_column='RECEIPT_NO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    scrap_date = models.CharField(db_column='SCRAP_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    scrap_clerk = models.CharField(db_column='SCRAP_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    return_date = models.CharField(db_column='RETURN_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    bill_no = models.DecimalField(db_column='BILL_NO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    billodds_no = models.DecimalField(db_column='BILLODDS_NO', max_digits=9, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    return_clerk = models.CharField(db_column='RETURN_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    discount_relation = models.CharField(db_column='DISCOUNT_RELATION', max_length=6, blank=True, null=True)  # Field name made lowercase.
    deposit_type = models.CharField(db_column='DEPOSIT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    supple_to_deposit = models.CharField(db_column='SUPPLE_TO_DEPOSIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mark_flag = models.CharField(db_column='MARK_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAYMENT'


class Price(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=7)  # Field name made lowercase.
    price_type = models.IntegerField(db_column='PRICE_TYPE')  # Field name made lowercase.
    full_name = models.CharField(db_column='FULL_NAME', max_length=100)  # Field name made lowercase.
    full_name_c = models.CharField(db_column='FULL_NAME_C', max_length=100)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=4)  # Field name made lowercase.
    acnt_no = models.IntegerField(db_column='ACNT_NO')  # Field name made lowercase.
    medicine_code = models.CharField(db_column='MEDICINE_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    op_icd = models.CharField(db_column='OP_ICD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=7)  # Field name made lowercase.
    create_clerk = models.CharField(db_column='CREATE_CLERK', max_length=6)  # Field name made lowercase.
    modify_date = models.CharField(db_column='MODIFY_DATE', max_length=7)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6)  # Field name made lowercase.
    major_care = models.CharField(db_column='MAJOR_CARE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unit_tqty = models.IntegerField(db_column='UNIT_TQTY', blank=True, null=True)  # Field name made lowercase.
    kind_no = models.CharField(db_column='KIND_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    s_unit = models.CharField(db_column='S_UNIT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    req_form = models.CharField(db_column='REQ_FORM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    stop_date = models.CharField(db_column='STOP_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    stop_reason = models.CharField(db_column='STOP_REASON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    replace_code = models.CharField(db_column='REPLACE_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    admit_limit_tqty = models.IntegerField(db_column='ADMIT_LIMIT_TQTY', blank=True, null=True)  # Field name made lowercase.
    limit_tqty = models.IntegerField(db_column='LIMIT_TQTY', blank=True, null=True)  # Field name made lowercase.
    modify_amt = models.CharField(db_column='MODIFY_AMT', max_length=1)  # Field name made lowercase.
    rpt24hours = models.CharField(db_column='RPT24HOURS', max_length=1)  # Field name made lowercase.
    doctor_order = models.CharField(db_column='DOCTOR_ORDER', max_length=1)  # Field name made lowercase.
    project_flag = models.CharField(db_column='PROJECT_FLAG', max_length=1)  # Field name made lowercase.
    licence_flag = models.CharField(db_column='LICENCE_FLAG', max_length=1)  # Field name made lowercase.
    printable = models.CharField(db_column='PRINTABLE', max_length=1)  # Field name made lowercase.
    send_lab = models.CharField(db_column='SEND_LAB', max_length=1)  # Field name made lowercase.
    lab_disc = models.CharField(db_column='LAB_DISC', max_length=1)  # Field name made lowercase.
    need_execute = models.CharField(db_column='NEED_EXECUTE', max_length=1)  # Field name made lowercase.
    need_report = models.CharField(db_column='NEED_REPORT', max_length=1)  # Field name made lowercase.
    default_value = models.CharField(db_column='DEFAULT_VALUE', max_length=1)  # Field name made lowercase.
    dental = models.CharField(db_column='DENTAL', max_length=1)  # Field name made lowercase.
    dental_qty_check = models.CharField(db_column='DENTAL_QTY_CHECK', max_length=1)  # Field name made lowercase.
    med_cons = models.CharField(db_column='MED_CONS', max_length=1)  # Field name made lowercase.
    autocompute = models.CharField(db_column='AUTOCOMPUTE', max_length=1)  # Field name made lowercase.
    anti_tb_med = models.CharField(db_column='ANTI_TB_MED', max_length=1)  # Field name made lowercase.
    op_div_no = models.CharField(db_column='OP_DIV_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sub_div_no = models.CharField(db_column='SUB_DIV_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    defqty = models.DecimalField(db_column='DEFQTY', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    drg_code = models.CharField(db_column='DRG_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    defday = models.IntegerField(db_column='DEFDAY', blank=True, null=True)  # Field name made lowercase.
    defunuse = models.CharField(db_column='DEFUNUSE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    defuse = models.CharField(db_column='DEFUSE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    defusetime = models.CharField(db_column='DEFUSETIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deftqty = models.IntegerField(db_column='DEFTQTY', blank=True, null=True)  # Field name made lowercase.
    defmethod = models.CharField(db_column='DEFMETHOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    defmethod1 = models.CharField(db_column='DEFMETHOD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    defmethod2 = models.CharField(db_column='DEFMETHOD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inp_opd = models.CharField(db_column='INP_OPD', max_length=1)  # Field name made lowercase.
    ctrl_type = models.CharField(db_column='CTRL_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ctrl_class = models.CharField(db_column='CTRL_CLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ctrl_day = models.IntegerField(db_column='CTRL_DAY', blank=True, null=True)  # Field name made lowercase.
    he_note = models.TextField(db_column='HE_NOTE', blank=True, null=True)  # Field name made lowercase.
    ppf_acnt_no = models.IntegerField(db_column='PPF_ACNT_NO', blank=True, null=True)  # Field name made lowercase.
    effect_remark = models.TextField(db_column='EFFECT_REMARK', blank=True, null=True)  # Field name made lowercase.
    opd_drg_code = models.CharField(db_column='OPD_DRG_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    inphe_check_days = models.CharField(db_column='INPHE_CHECK_DAYS', max_length=1)  # Field name made lowercase.
    treat_emg = models.CharField(db_column='TREAT_EMG', max_length=1)  # Field name made lowercase.
    back_flag = models.CharField(db_column='BACK_FLAG', max_length=1)  # Field name made lowercase.
    kind_limit_tqty = models.IntegerField(db_column='KIND_LIMIT_TQTY', blank=True, null=True)  # Field name made lowercase.
    least_tqty = models.IntegerField(db_column='LEAST_TQTY', blank=True, null=True)  # Field name made lowercase.
    grindable = models.CharField(db_column='GRINDABLE', max_length=1)  # Field name made lowercase.
    ppf_flag = models.CharField(db_column='PPF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emg_he_flag = models.CharField(db_column='EMG_HE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    spec_flag = models.CharField(db_column='SPEC_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dq_no = models.CharField(db_column='DQ_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dq_step = models.IntegerField(db_column='DQ_STEP', blank=True, null=True)  # Field name made lowercase.
    eminent_type = models.CharField(db_column='EMINENT_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    start_age = models.IntegerField(db_column='START_AGE', blank=True, null=True)  # Field name made lowercase.
    end_age = models.IntegerField(db_column='END_AGE', blank=True, null=True)  # Field name made lowercase.
    nhi_cons_type = models.CharField(db_column='NHI_CONS_TYPE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nhi_cons_days = models.IntegerField(db_column='NHI_CONS_DAYS', blank=True, null=True)  # Field name made lowercase.
    no_pay_use_med = models.CharField(db_column='NO_PAY_USE_MED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ns_med = models.CharField(db_column='NS_MED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dose = models.CharField(db_column='DOSE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    index_code = models.CharField(db_column='INDEX_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    medtypeb = models.CharField(db_column='MEDTYPEB', max_length=7, blank=True, null=True)  # Field name made lowercase.
    medtyped = models.CharField(db_column='MEDTYPED', max_length=7, blank=True, null=True)  # Field name made lowercase.
    dan_flag = models.CharField(db_column='DAN_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    defcard_seq = models.CharField(db_column='DEFCARD_SEQ', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trans_code = models.CharField(db_column='TRANS_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    medbag_unit_tqty = models.IntegerField(db_column='MEDBAG_UNIT_TQTY', blank=True, null=True)  # Field name made lowercase.
    medbag_unit = models.CharField(db_column='MEDBAG_UNIT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    limit_qty = models.IntegerField(db_column='LIMIT_QTY', blank=True, null=True)  # Field name made lowercase.
    image_flag = models.CharField(db_column='IMAGE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    need_datetime = models.CharField(db_column='NEED_DATETIME', max_length=1)  # Field name made lowercase.
    need_date = models.CharField(db_column='NEED_DATE', max_length=1)  # Field name made lowercase.
    nhi_cons_mm = models.IntegerField(db_column='NHI_CONS_MM', blank=True, null=True)  # Field name made lowercase.
    icd10pcs = models.CharField(db_column='ICD10PCS', max_length=7, blank=True, null=True)  # Field name made lowercase.
    icd10pcs2 = models.CharField(db_column='ICD10PCS2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    icd10pcs3 = models.CharField(db_column='ICD10PCS3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    icd10pcs4 = models.CharField(db_column='ICD10PCS4', max_length=7, blank=True, null=True)  # Field name made lowercase.
    icd10pcs5 = models.CharField(db_column='ICD10PCS5', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRICE'


class Price4(models.Model):
    ptr = models.IntegerField(db_column='PTR')  # Field name made lowercase.
    rec_count = models.IntegerField(db_column='REC_COUNT')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='QTY', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    self_paid_flag = models.CharField(db_column='SELF_PAID_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    he_paid_flag = models.CharField(db_column='HE_PAID_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRICE4'
        unique_together = (('ptr', 'rec_count'),)


class Pricehe(models.Model):
    code = models.CharField(db_column='CODE', max_length=7)  # Field name made lowercase.
    eff_date = models.CharField(db_column='EFF_DATE', max_length=7)  # Field name made lowercase.
    full_name = models.CharField(db_column='FULL_NAME', max_length=100)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=4)  # Field name made lowercase.
    he_code = models.CharField(db_column='HE_CODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    paid_flag = models.CharField(db_column='PAID_FLAG', max_length=1)  # Field name made lowercase.
    add_rate = models.IntegerField(db_column='ADD_RATE')  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE')  # Field name made lowercase.
    auto_flag = models.CharField(db_column='AUTO_FLAG', max_length=1)  # Field name made lowercase.
    ptr = models.IntegerField(db_column='PTR')  # Field name made lowercase.
    inp_ptr = models.IntegerField(db_column='INP_PTR')  # Field name made lowercase.
    he_paid_flag = models.CharField(db_column='HE_PAID_FLAG', max_length=1)  # Field name made lowercase.
    he_add_rate = models.IntegerField(db_column='HE_ADD_RATE')  # Field name made lowercase.
    he_price = models.IntegerField(db_column='HE_PRICE')  # Field name made lowercase.
    he_auto_flag = models.CharField(db_column='HE_AUTO_FLAG', max_length=1)  # Field name made lowercase.
    he_ptr = models.IntegerField(db_column='HE_PTR')  # Field name made lowercase.
    he_inp_ptr = models.IntegerField(db_column='HE_INP_PTR')  # Field name made lowercase.
    he_add_fee = models.IntegerField(db_column='HE_ADD_FEE')  # Field name made lowercase.
    create_clerk = models.CharField(db_column='CREATE_CLERK', max_length=6)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=7)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    modify_date = models.CharField(db_column='MODIFY_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    emg = models.CharField(db_column='EMG', max_length=1)  # Field name made lowercase.
    kid_add = models.CharField(db_column='KID_ADD', max_length=1)  # Field name made lowercase.
    he_emg = models.CharField(db_column='HE_EMG', max_length=1)  # Field name made lowercase.
    he_kid_add = models.CharField(db_column='HE_KID_ADD', max_length=1)  # Field name made lowercase.
    kid_add_60 = models.CharField(db_column='KID_ADD_60', max_length=1)  # Field name made lowercase.
    he_kid_add_60 = models.CharField(db_column='HE_KID_ADD_60', max_length=1)  # Field name made lowercase.
    he_give_type = models.CharField(db_column='HE_GIVE_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    case_type = models.CharField(db_column='CASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    he_cariosity = models.CharField(db_column='HE_CARIOSITY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emg_ptr = models.IntegerField(db_column='EMG_PTR', blank=True, null=True)  # Field name made lowercase.
    he_emg_ptr = models.IntegerField(db_column='HE_EMG_PTR', blank=True, null=True)  # Field name made lowercase.
    case_type_inp = models.CharField(db_column='CASE_TYPE_INP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_clin_bot = models.CharField(db_column='IS_CLIN_BOT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    attend_code = models.CharField(db_column='ATTEND_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    c_app_he_add_rate = models.IntegerField(db_column='C_APP_HE_ADD_RATE', blank=True, null=True)  # Field name made lowercase.
    send_hospid = models.CharField(db_column='SEND_HOSPID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    he_kid_add_ex = models.CharField(db_column='HE_KID_ADD_EX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kid_add_ex = models.CharField(db_column='KID_ADD_EX', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRICEHE'
        unique_together = (('code', 'eff_date'),)


class Pttype(models.Model):
    pt_type = models.IntegerField(db_column='PT_TYPE', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME', max_length=10)  # Field name made lowercase.
    price_type = models.IntegerField(db_column='PRICE_TYPE', blank=True, null=True)  # Field name made lowercase.
    keyin_date = models.CharField(db_column='KEYIN_DATE', max_length=7)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PTTYPE'


class Reg(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN', blank=True, null=True)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC', blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    view_no = models.IntegerField(db_column='VIEW_NO', blank=True, null=True)  # Field name made lowercase.
    reg_clerk = models.CharField(db_column='REG_CLERK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_time = models.DateTimeField(db_column='REG_TIME', blank=True, null=True)  # Field name made lowercase.
    prenatal_care = models.CharField(db_column='PRENATAL_CARE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REG'


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


class Bopdacnt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    rec_count = models.IntegerField(db_column='REC_COUNT')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=7)  # Field name made lowercase.
    identify_no = models.IntegerField(db_column='IDENTIFY_NO')  # Field name made lowercase.
    acnt_no = models.IntegerField(db_column='ACNT_NO')  # Field name made lowercase.
    price_type = models.IntegerField(db_column='PRICE_TYPE')  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY')  # Field name made lowercase.
    unuse = models.CharField(db_column='UNUSE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    use = models.CharField(db_column='USE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usetime = models.CharField(db_column='USETIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='DAY')  # Field name made lowercase.
    tqty = models.IntegerField(db_column='TQTY')  # Field name made lowercase.
    self = models.CharField(db_column='SELF', max_length=1)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT')  # Field name made lowercase.
    comp_discount = models.IntegerField(db_column='COMP_DISCOUNT')  # Field name made lowercase.
    amt = models.IntegerField(db_column='AMT')  # Field name made lowercase.
    he_add_fee = models.IntegerField(db_column='HE_ADD_FEE')  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    method1 = models.CharField(db_column='METHOD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    method2 = models.CharField(db_column='METHOD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emg = models.CharField(db_column='EMG', max_length=1)  # Field name made lowercase.
    add_rate = models.IntegerField(db_column='ADD_RATE')  # Field name made lowercase.
    office = models.CharField(db_column='OFFICE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(db_column='STOCK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    order_datetime = models.CharField(db_column='ORDER_DATETIME', max_length=11)  # Field name made lowercase.
    exec_clerk = models.CharField(db_column='EXEC_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    exec_datetime = models.CharField(db_column='EXEC_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    report_clerk = models.CharField(db_column='REPORT_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    report_datetime = models.CharField(db_column='REPORT_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='CASHIER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyin_datetime = models.CharField(db_column='KEYIN_DATETIME', max_length=11)  # Field name made lowercase.
    keyin_clerk = models.CharField(db_column='KEYIN_CLERK', max_length=6)  # Field name made lowercase.
    modify_datetime = models.CharField(db_column='MODIFY_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    modify_clerk = models.CharField(db_column='MODIFY_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    req_no = models.CharField(db_column='REQ_NO', max_length=13, blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='OPERATION', max_length=1, blank=True, null=True)  # Field name made lowercase.
    grind = models.CharField(db_column='GRIND', max_length=1)  # Field name made lowercase.
    cons_no = models.CharField(db_column='CONS_NO', max_length=70, blank=True, null=True)  # Field name made lowercase.
    noexe_reason = models.CharField(db_column='NOEXE_REASON', max_length=6, blank=True, null=True)  # Field name made lowercase.
    office1 = models.CharField(db_column='OFFICE1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    max_price_times = models.IntegerField(db_column='MAX_PRICE_TIMES', blank=True, null=True)  # Field name made lowercase.
    order_pos = models.CharField(db_column='ORDER_POS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='START_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    start_time = models.CharField(db_column='START_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    end_date = models.CharField(db_column='END_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    end_time = models.CharField(db_column='END_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dicom_flag = models.CharField(db_column='DICOM_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    project_no = models.CharField(db_column='PROJECT_NO', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bOPDACNT'


class Bpatopd(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO')  # Field name made lowercase.
    duplicate_no = models.IntegerField(db_column='DUPLICATE_NO')  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6)  # Field name made lowercase.
    div_no = models.CharField(db_column='DIV_NO', max_length=6)  # Field name made lowercase.
    cash_type = models.CharField(db_column='CASH_TYPE', max_length=6)  # Field name made lowercase.
    fv_rv = models.CharField(db_column='FV_RV', max_length=1)  # Field name made lowercase.
    send_chart = models.CharField(db_column='SEND_CHART', max_length=1)  # Field name made lowercase.
    pt_type = models.IntegerField(db_column='PT_TYPE')  # Field name made lowercase.
    card_seq = models.CharField(db_column='CARD_SEQ', max_length=4, blank=True, null=True)  # Field name made lowercase.
    part_no = models.CharField(db_column='PART_NO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    expect_view_time = models.CharField(db_column='EXPECT_VIEW_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    comefrom_no = models.CharField(db_column='COMEFROM_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    regkind_no = models.CharField(db_column='REGKIND_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    visit = models.CharField(db_column='VISIT', max_length=1)  # Field name made lowercase.
    sheet_no = models.IntegerField(db_column='SHEET_NO', blank=True, null=True)  # Field name made lowercase.
    appointment = models.CharField(db_column='APPOINTMENT', max_length=1)  # Field name made lowercase.
    check_in_datetime = models.CharField(db_column='CHECK_IN_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    give_order = models.CharField(db_column='GIVE_ORDER', max_length=1)  # Field name made lowercase.
    apn = models.DecimalField(db_column='APN', max_digits=1, decimal_places=0)  # Field name made lowercase.
    zone = models.CharField(db_column='ZONE', max_length=1)  # Field name made lowercase.
    clinic = models.IntegerField(db_column='CLINIC')  # Field name made lowercase.
    view_no = models.IntegerField(db_column='VIEW_NO')  # Field name made lowercase.
    supple_flag = models.CharField(db_column='SUPPLE_FLAG', max_length=1)  # Field name made lowercase.
    supple_datetime = models.CharField(db_column='SUPPLE_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    supple_clerk = models.CharField(db_column='SUPPLE_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    discount_ptr = models.IntegerField(db_column='DISCOUNT_PTR')  # Field name made lowercase.
    disease_code = models.CharField(db_column='DISEASE_CODE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name = models.CharField(db_column='DISEASE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code1 = models.CharField(db_column='DISEASE_CODE1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name1 = models.CharField(db_column='DISEASE_NAME1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code2 = models.CharField(db_column='DISEASE_CODE2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name2 = models.CharField(db_column='DISEASE_NAME2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code3 = models.CharField(db_column='DISEASE_CODE3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name3 = models.CharField(db_column='DISEASE_NAME3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code4 = models.CharField(db_column='DISEASE_CODE4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name4 = models.CharField(db_column='DISEASE_NAME4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code5 = models.CharField(db_column='DISEASE_CODE5', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name5 = models.CharField(db_column='DISEASE_NAME5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease_code6 = models.CharField(db_column='DISEASE_CODE6', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disease_name6 = models.CharField(db_column='DISEASE_NAME6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    op_icd9 = models.CharField(db_column='OP_ICD9', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_1 = models.CharField(db_column='OP_ICD9_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_2 = models.CharField(db_column='OP_ICD9_2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_3 = models.CharField(db_column='OP_ICD9_3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    op_icd9_4 = models.CharField(db_column='OP_ICD9_4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    trans_in = models.CharField(db_column='TRANS_IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pricing_clerk = models.CharField(db_column='PRICING_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    drg_code = models.CharField(db_column='DRG_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    post_reg_flag = models.CharField(db_column='POST_REG_FLAG', max_length=1)  # Field name made lowercase.
    post_attend_fee = models.CharField(db_column='POST_ATTEND_FEE', max_length=1)  # Field name made lowercase.
    triage = models.CharField(db_column='TRIAGE', max_length=1)  # Field name made lowercase.
    med_days = models.IntegerField(db_column='MED_DAYS', blank=True, null=True)  # Field name made lowercase.
    med_order = models.IntegerField(db_column='MED_ORDER', blank=True, null=True)  # Field name made lowercase.
    who_disc = models.CharField(db_column='WHO_DISC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hospitalize_clerk = models.CharField(db_column='HOSPITALIZE_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hospitalize_datetime = models.CharField(db_column='HOSPITALIZE_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    serno = models.IntegerField(db_column='SERNO', blank=True, null=True)  # Field name made lowercase.
    blocked_reason = models.CharField(db_column='BLOCKED_REASON', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_clerk = models.CharField(db_column='REG_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    reg_datetime = models.CharField(db_column='REG_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    opd_clerk = models.CharField(db_column='OPD_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    opd_datetime = models.CharField(db_column='OPD_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    treat_clerk = models.CharField(db_column='TREAT_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    treat_datetime = models.CharField(db_column='TREAT_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    reg_amt = models.DecimalField(db_column='REG_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    disc_reg_amt = models.DecimalField(db_column='DISC_REG_AMT', max_digits=10, decimal_places=0)  # Field name made lowercase.
    case_type = models.CharField(db_column='CASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chronic_seq = models.IntegerField(db_column='CHRONIC_SEQ', blank=True, null=True)  # Field name made lowercase.
    he_date = models.CharField(db_column='HE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    begin_duplicate = models.IntegerField(db_column='BEGIN_DUPLICATE', blank=True, null=True)  # Field name made lowercase.
    begin_date = models.CharField(db_column='BEGIN_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_type = models.CharField(db_column='COURSE_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    course_deadline = models.CharField(db_column='COURSE_DEADLINE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_recent_date = models.CharField(db_column='COURSE_RECENT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    course_total_times = models.IntegerField(db_column='COURSE_TOTAL_TIMES', blank=True, null=True)  # Field name made lowercase.
    course_times = models.IntegerField(db_column='COURSE_TIMES', blank=True, null=True)  # Field name made lowercase.
    discount_relation = models.CharField(db_column='DISCOUNT_RELATION', max_length=6, blank=True, null=True)  # Field name made lowercase.
    reg_status = models.CharField(db_column='REG_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    force_type = models.CharField(db_column='FORCE_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='CARD_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ic_card_no = models.CharField(db_column='IC_CARD_NO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    child_birth_date = models.CharField(db_column='CHILD_BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    child_born_note = models.CharField(db_column='CHILD_BORN_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_type = models.CharField(db_column='CLINIC_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clinic_new_born_note = models.CharField(db_column='CLINIC_NEW_BORN_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_date_time = models.CharField(db_column='CLINIC_DATE_TIME', max_length=13, blank=True, null=True)  # Field name made lowercase.
    clinic_supple_note = models.CharField(db_column='CLINIC_SUPPLE_NOTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clinic_seq_no = models.CharField(db_column='CLINIC_SEQ_NO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    heal_note = models.CharField(db_column='HEAL_NOTE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    heal_service_item = models.CharField(db_column='HEAL_SERVICE_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pregnant_item = models.CharField(db_column='PREGNANT_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    secure_sign = models.CharField(db_column='SECURE_SIGN', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cardseq_status = models.CharField(db_column='CARDSEQ_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sam_id = models.CharField(db_column='SAM_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    hosp_id = models.CharField(db_column='HOSP_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transed = models.CharField(db_column='TRANSED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    card_error_code = models.DecimalField(db_column='CARD_ERROR_CODE', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(db_column='TRANS_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    trans_kind = models.CharField(db_column='TRANS_KIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_correct = models.CharField(db_column='DATA_CORRECT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    druggist_no = models.CharField(db_column='DRUGGIST_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    check_druggist_no = models.CharField(db_column='CHECK_DRUGGIST_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    stop_recheck_fee = models.CharField(db_column='STOP_RECHECK_FEE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    occup_disease_flag = models.CharField(db_column='OCCUP_DISEASE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    appointment_mode = models.CharField(db_column='APPOINTMENT_MODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    income_clerk = models.CharField(db_column='INCOME_CLERK', max_length=6, blank=True, null=True)  # Field name made lowercase.
    income_datetime = models.CharField(db_column='INCOME_DATETIME', max_length=11, blank=True, null=True)  # Field name made lowercase.
    merge_view_date = models.CharField(db_column='MERGE_VIEW_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    merge_duplicate_no = models.DecimalField(db_column='MERGE_DUPLICATE_NO', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    merge_report_class = models.CharField(db_column='MERGE_REPORT_CLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    opdacnt_count = models.IntegerField(db_column='OPDACNT_COUNT', blank=True, null=True)  # Field name made lowercase.
    admittance = models.CharField(db_column='ADMITTANCE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    emg_accrue = models.CharField(db_column='EMG_ACCRUE', max_length=1)  # Field name made lowercase.
    cut_he_date = models.CharField(db_column='CUT_HE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    trans_in_type = models.CharField(db_column='TRANS_IN_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans_out_type = models.CharField(db_column='TRANS_OUT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans_out_hosp = models.CharField(db_column='TRANS_OUT_HOSP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    disability_flag = models.CharField(db_column='DISABILITY_FLAG', max_length=1)  # Field name made lowercase.
    course_merge_status = models.CharField(db_column='COURSE_MERGE_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    spec_no = models.CharField(db_column='SPEC_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    need_cut_case = models.CharField(db_column='NEED_CUT_CASE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    undeclared = models.CharField(db_column='UNDECLARED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pt_type_1 = models.DecimalField(db_column='PT_TYPE_1', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    baby_inject = models.CharField(db_column='BABY_INJECT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    check_in_type = models.CharField(db_column='CHECK_IN_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sendmsg_flag = models.CharField(db_column='SENDMSG_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reserve_msg_sent = models.CharField(db_column='RESERVE_MSG_SENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    need_trace_flag = models.CharField(db_column='NEED_TRACE_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    front_case_type = models.CharField(db_column='FRONT_CASE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    he_disease_anys = models.CharField(db_column='HE_DISEASE_ANYS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uc_div = models.CharField(db_column='UC_DIV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ic_limit_date = models.CharField(db_column='IC_LIMIT_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    breast_trans_flag = models.CharField(db_column='BREAST_TRANS_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    trans_emr_date = models.DateTimeField(db_column='TRANS_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    sign_emr_date = models.DateTimeField(db_column='SIGN_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    his2emr_complete_date = models.CharField(db_column='HIS2EMR_COMPLETE_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    spec_sensitive_label = models.CharField(db_column='SPEC_SENSITIVE_LABEL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    trans2emr_complete_date = models.CharField(db_column='TRANS2EMR_COMPLETE_DATE', max_length=7)  # Field name made lowercase.
    exchange_sign_emr_date = models.DateTimeField(db_column='EXCHANGE_SIGN_EMR_DATE', blank=True, null=True)  # Field name made lowercase.
    skin_values = models.CharField(db_column='SKIN_VALUES', max_length=1, blank=True, null=True)  # Field name made lowercase.
    is_occupational = models.CharField(db_column='IS_OCCUPATIONAL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bPATOPD'


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
    clinic = models.IntegerField(db_column='CLINIC', blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='LOCATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept_location'


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


class HealthEducation(models.Model):
    edu_num = models.AutoField(db_column='EDU_NUM', primary_key=True)  # Field name made lowercase.
    div_kind = models.CharField(db_column='DIV_KIND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    edu_name = models.CharField(db_column='EDU_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edu_memo = models.CharField(db_column='EDU_MEMO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    download_posit = models.CharField(db_column='DOWNLOAD_POSIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eff_flag = models.CharField(db_column='EFF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'health_education'


class Mombook(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    doctor_no = models.CharField(db_column='DOCTOR_NO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mombook'


class PatientServicelist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=5)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7)  # Field name made lowercase.
    apn = models.IntegerField(db_column='APN')  # Field name made lowercase.
    seq_no = models.IntegerField(db_column='SEQ_NO', blank=True, null=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    pt_name = models.CharField(db_column='PT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eff_flag = models.CharField(db_column='EFF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_servicelist'


class PatientServiceno(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    clinic_no = models.IntegerField(db_column='CLINIC_NO', blank=True, null=True)  # Field name made lowercase.
    current_no = models.IntegerField(db_column='CURRENT_NO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_serviceno'


class PatientStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    view_date = models.CharField(db_column='VIEW_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_status'


class PatientTrace(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rec_datetime = models.DateTimeField(db_column='REC_DATETIME', blank=True, null=True)  # Field name made lowercase.
    location_code = models.CharField(db_column='LOCATION_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient_trace'


class RegisterDevice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chart_no = models.IntegerField(db_column='CHART_NO', blank=True, null=True)  # Field name made lowercase.
    id_no = models.CharField(db_column='ID_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='BIRTH_DATE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    registration_id = models.CharField(db_column='REGISTRATION_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    register_datetime = models.DateTimeField(db_column='REGISTER_DATETIME', blank=True, null=True)  # Field name made lowercase.
    eff_flag = models.CharField(db_column='EFF_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'register_device'


class Seqno(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SEQNO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seqno'
