import hismaxdb.models
import restwebservice.get_extdata
import restwebservice.serializers
import utilitytools.utility_date
import sys
import utilitytools.msg_utility
from rest_framework.response import Response
from rest_framework import status

#writeFlag = False

#預約掛號查詢(Beacon) -- 不再使用
def process_reg_benbackup(chart_no, cnow, location_code):
    print("process_reg : ", chart_no)

    #檢查預約記錄
    regs = hismaxdb.models.Reg.objects.all().filter(chart_no=chart_no, view_date=cnow)
    print("reg num=", regs.count())
    if regs.count()>0:
        serializer = restwebservice.serializers.RegSerializer(regs, many=True)
        #檢查產檢病人 : X檢查 Mombook
        # PRENATAL_CARE

        for s in serializer.data:
            #---- 加入 doctor_name ----------
            s['doctor_name'] = restwebservice.get_extdata.getEmployeeName(s['doctor_no'])
            #--- 加入 current_no ----
            code = restwebservice.get_extdata.getLocationCodeByClinic(s['clinic'])
            s['current_no'] = restwebservice.get_extdata.getCurrentNoByLoc(code)
            #X-- 檢查是否產檢病人 -- 己在 REG 中新增欄位
            s['location_code'] = location_code
            #for status response
            s['_status'] = "success"
            s['_status_doc'] = "REG"

        return serializer.data
    else:
        return [{"_status" : "error", "_status_doc" : "未發現預約掛號記錄  !!"}]                   #"未發現預約掛號記錄 !!"

#預約掛號查詢(Beacon)
def process_reg(chart_no, cnow, location_code, pt_name):
    print("process_reg : ", chart_no)
    rtnDict = checkRecord(chart_no, cnow, location_code)

    for rec in rtnDict:
        #檢查是否為錯誤訊息
        if '_status' in rec:
            pass
        else:
            #--- 加入診間名稱 ----
            rec['clinic_ps']= restwebservice.get_extdata.gerClinicPs(rec['clinic'])
            #---- 加入 doctor_name ----------
            rec['doctor_name'] = restwebservice.get_extdata.getEmployeeName(rec['doctor_no'])
            rec['pt_name'] = pt_name
            #--- 加入 current_no ----
            code = restwebservice.get_extdata.getLocationCodeByClinic(rec['clinic'])
            #取出目診診間看診號 --- 錯誤
            #rec['current_no'] = restwebservice.get_extdata.getCurrentNoByLoc(code)
            #取出目診診間看診號，Location_code 目前固定為 10
            rec['current_no'] = restwebservice.get_extdata.getCurrentNoByLoc("10",rec['clinic'])
            #X-- 檢查是否產檢病人 -- 己在 REG 中新增欄位
            rec['location_code'] = location_code
            #for status response
            rec['_status'] = "success"
            rec['_status_doc'] = "REG"


    return rtnDict

#預約掛號報到
def update_reg(view_date, chart_no, duplicate_no, apn, cnow, service_no, location_code):
    print("update_reg :", view_date, chart_no, duplicate_no, cnow)
    #1: update patopd.check_in_datetime
    try:
        patopd = hismaxdb.models.Patopd.objects.get(view_date=view_date, chart_no=chart_no, duplicate_no=duplicate_no)
    except hismaxdb.models.Patopd.DoesNotExist:
        rtnStr = [{"_status":"error", "_status_doc" : "找不到門診記錄 !!"}]

    except:
        rtnStr =[{"_status" : "error", "_status_doc":sys.exc_info()[0]}]

    else:
        #Update Patopd
        patopd.check_in_datetime = utilitytools.utility_date.getCNow()
        patopd.save()
        exceptViewTime = patopd.expect_view_time
        viewNo = patopd.view_no
        cardSeq = patopd.card_seq    #41-50 為產檢

        #2: add PatientServicelist
        #--- 取得最大值
        #num = restwebservice.get_extdata.getMaxServiceNo('10', view_date, apn)

        #依看診號 insert into PatientServicelist(未來此 Table 需加記診間，診間需區分看診順序)
        ptName = restwebservice.get_extdata.get_ptname(chart_no)
        patientServicelist = hismaxdb.models.PatientServicelist(location_code=location_code, view_date=view_date, apn=apn, seq_no=service_no, chart_no=chart_no, pt_name=ptName, eff_flag='Y')
        patientServicelist.save()

        rtnStr = [{"_status" : "success", "_status_doc" : "REG", "view_no": viewNo, "except_view_time":exceptViewTime, "card_seq":cardSeq}]
    return rtnStr


def process_dept(chart_no,cnow, location_code, pt_name):
    print("process_dept", chart_no)
    #1. 檢查該患者是否需此服務（check by Requisition)
    rtnDict = checkRecord(chart_no, cnow, location_code)
    if utilitytools.msg_utility.isError(rtnDict) != "":
        #發生 error
        return rtnDict
    else:
        #2. 即將取得之服務號(patient_servicelist- getMaxServiceNo)
        sno = restwebservice.get_extdata.getMaxServiceNo(location_code, cnow, 1)
        #3. 取得目前該 location_code 服務號(patient_serviceno)
        cno = restwebservice.get_extdata.getCurrentNoByLoc(location_code)
        location_name = restwebservice.get_extdata.getLocationName(location_code)

        #fun(item['view_date'], item['chart_no'], item['duplicate_no'], item['apn'], _cnow, serviceNo, item['location_code'])
        for rtn in rtnDict:
            rtn['pt_name'] = pt_name
            rtn['view_date'] = utilitytools.utility_date.getTodayCDate()
            rtn['duplicate_no'] = 0
            rtn['apn'] = 1
            rtn['location_code'] = location_code
            rtn['location_name'] = location_name
            rtn['_status'] = "success"
            rtn['total_num'] = sno          #總人數
            rtn['current_num'] = cno        #目前服務號
            rtn['_status_doc'] = 'DEPT_SCHEDULE'    #科室排班
            #"目前"+location_name+"排隊總人數:"+str(sno)+", 是否報到並加入排隊, 目前己服務至:"+str(cno)
        return rtnDict


def update_dept(view_date, chart_no, duplicate_no, apn, cnow, service_no, location_code):

    #1. 加入排隊
    #    2. 即將取得之服務號(patient_servicelist- getMaxServiceNo)
    sno = restwebservice.get_extdata.getMaxServiceNo(location_code, cnow, 1)+1
    #    3. (insert into PatientServicelist)
    ptName = restwebservice.get_extdata.get_ptname(chart_no)
    patientServicelist = hismaxdb.models.PatientServicelist(location_code=location_code, view_date=view_date, apn=apn, seq_no=sno, chart_no=chart_no, pt_name=ptName, eff_flag='Y')
    patientServicelist.save()

    #2. 取出該順序之前三筆後三筆記錄
    if sno < 3:
        sno_1 = 1
    else:
        sno_1 = sno - 3
    sno_2 = sno + 3

    plist = hismaxdb.models.PatientServicelist.objects.filter(location_code=location_code, view_date=view_date, apn=apn, seq_no__gte=sno_1, seq_no__lte=sno_2)
    serializer = restwebservice.serializers.PatientServicelistSerializer(plist, many=True)
    for s in serializer.data:
        #for status response
        s['_status'] = "success"
        s['_status_doc'] = "DEPT_SCHEDULE"

    rtnStr = serializer.data

    return rtnStr

def process_pre_dept(chart_no, cnow, location_code, pt_name):
    print("process_pre_dept", chart_no)
    #rtn = process_dept(chart_no,cnow, location_code)
    rtnDict = checkRecord(chart_no, cnow, location_code)
    if utilitytools.msg_utility.isError(rtnDict) != "":
        #發生 error
        return rtnDict
    #2. 即將取得之服務號(patient_servicelist- getMaxServiceNo)
    sno = restwebservice.get_extdata.getMaxServiceNo(location_code, cnow, 1)
    #3. 取得目前該 location_code 服務號(patient_serviceno)
    cno = restwebservice.get_extdata.getCurrentNoByLoc(location_code)
    location_name = restwebservice.get_extdata.getLocationName(location_code)

    #fun(item['view_date'], item['chart_no'], item['duplicate_no'], item['apn'], _cnow, serviceNo, item['location_code'])
    rtn = {}
    rtn['view_date'] = cnow
    rtn['chart_no'] = chart_no
    rtn['pt_name'] = pt_name
    rtn['duplicate_no'] = 0
    rtn['apn'] = 1
    rtn['location_code'] = location_code
    rtn['location_name'] = location_name
    rtn['_status'] = "success"
    rtn['total_num'] = sno          #總人數
    rtn['current_num'] = cno        #目前服務號
    rtn['_status_doc'] = 'PRE_DEPT_SCHEDULE'    #衛教室排班
    #"目前"+location_name+"排隊總人數:"+str(sno)+", 是否報到並加入排隊, 目前己服務至:"+str(cno)
    return [rtn]


def update_pre_dept(view_date, chart_no, duplicate_no, apn, cnow, service_no, location_code):

    #1. 加入排隊
    #    2. 即將取得之服務號(patient_servicelist- getMaxServiceNo)
    sno = restwebservice.get_extdata.getMaxServiceNo(location_code, cnow, 1)+1
    #    3. (insert into PatientServicelist)
    ptName = restwebservice.get_extdata.get_ptname(chart_no)
    patientServicelist = hismaxdb.models.PatientServicelist(location_code=location_code, view_date=view_date, apn=apn, seq_no=sno, chart_no=chart_no, pt_name=ptName, eff_flag='Y')
    patientServicelist.save()

    #2. 取出該順序之前三筆後三筆記錄
    if sno < 3:
        sno_1 = 1
    else:
        sno_1 = sno - 3
    sno_2 = sno + 3

    plist = hismaxdb.models.PatientServicelist.objects.filter(location_code=location_code, view_date=view_date, apn=apn, seq_no__gte=sno_1, seq_no__lte=sno_2)
    serializer = restwebservice.serializers.PatientServicelistSerializer(plist, many=True)
    for s in serializer.data:
        #for status response
        s['_status'] = "success"
        s['_status_doc'] = "PRE_DEPT_SCHEDULE"

    rtnStr = serializer.data

    return rtnStr


def getDeptSchedule(_locationCode, _chartno, cDate, apn, locatiodId):
    #取得目前看診號
    cno = restwebservice.get_extdata.getCurrentNoByLoc(_locationCode)
    #需排列
    plist = hismaxdb.models.PatientServicelist.objects.filter(location_code=_locationCode, view_date=cDate, apn=apn, eff_flag='Y')
    serializer = restwebservice.serializers.PatientServicelistSerializer(plist, many=True)
    for item in serializer.data:
        #處理穩私, 標記患者
        item['mark'] = ''
        if item['chart_no'] == int(_chartno):
            item['mark'] = '*'
        if item['seq_no'] == cno:
            item['mark'] = 'C'
        item['_status'] = "success"
        item['_status_doc'] = locatiodId

    return serializer.data

def getCurrentNoByClinicNo(l_location_code, l_clinicNo):
    rtnStr = []
    try:
        patientServiceno = hismaxdb.models.PatientServiceno.objects.get(location_code=l_location_code,clinic_no=l_clinicNo)
    except:
        rtnStr = [{"_status" : "error", "_status_doc" : "沒有此診間號:"+l_clinicNo}]
    else:
        serializer = restwebservice.serializers.PatientServiceNoSerializer(patientServiceno, many=False)
        dat = serializer.data
        #restwebservice.get_extdata.gerClinicPs(l_clinicNo)
        dat['clinic_ps']= restwebservice.get_extdata.gerClinicPs(l_clinicNo)
        rtnStr = dat
    return  rtnStr

def checkRecord(chart_no, cnow, location_code):

    try:
        if location_code == "10":
            recs = hismaxdb.models.Reg.objects.all().filter(chart_no=chart_no, view_date=cnow, duplicate_no=0) #檢查預約記錄
            serializer = restwebservice.serializers.RegSerializer(recs, many=True)
        elif location_code == "20":
            recs = hismaxdb.models.Reg.objects.all().filter(chart_no=chart_no, view_date=cnow, duplicate_no=0, prenatal_care='Y') #檢查預約記錄中產檢欄 'Y'
            serializer = restwebservice.serializers.RegSerializer(recs, many=True)
        elif location_code == "31":
            recs =  hismaxdb.models.Requisition.objects.all().filter(chart_no=chart_no, processed='N', form_no = 'LA')  #Form_No = 'L%'暫時用 'LA' and PROCESSED = 'N'
            serializer = restwebservice.serializers.RequisitionSerializer(recs, many=True)
        elif location_code == "32":
            recs =  hismaxdb.models.Requisition.objects.all().filter(chart_no=chart_no, processed='N', form_no = 'XR')  #Form_No = 'X%'暫時用 'XR' and PROCESSED = 'N'
            serializer = restwebservice.serializers.RequisitionSerializer(recs, many=True)
    except:
        print("error", sys.exc_info())
    if recs:
        rtnStr = serializer.data
    else:
        msg = {
            "10": "未發現預約掛號記錄  !!",
            "20": "未發現產檢記錄  !!",
            "31": "未發現 檢驗申請單 記錄  !!",
            "32": "未發現 X光單申請單 記錄  !!",
        }[location_code]
        rtnStr = [{"_status" : "error", "_status_doc" : msg}]

    return rtnStr

#取得就醫清單
def getPatopd(l_chart_no):
    pat = hismaxdb.models.Patopd.objects.filter(chart_no=l_chart_no).order_by('-view_date')
    return pat

def getOpdacnt(view_date, chart_no, duplicate_no):
    #6:一般口服藥 7:高價口服藥 8:一般外用藥 9:高價外用藥
    opdacnt = hismaxdb.models.Opdacnt.objects.filter(view_date=view_date, chart_no=chart_no, duplicate_no=duplicate_no, acnt_no=6 )
    return opdacnt

def getMedicine(mcode):
    try:
        medicine = hismaxdb.models.Medicine.objects.get(code=mcode)
        #try:
        #    medpict = hismaxdb.models.Medicinephoto.objects.get(code=mcode)
        #except:
        #    medicine.pict = mcode
        #else:
        #    medicine.pict = medpict.photo

    except:
        return ""
    else:
        return medicine


def getHealthEducation():
    recs = hismaxdb.models.HealthEducation.objects.filter(eff_flag='Y')
    return recs