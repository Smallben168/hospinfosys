
import sys
import random
import hismaxdb.models
from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
import restwebservice.get_extdata
import utilitytools.utility_date
from django.shortcuts import render
import utilitytools.utility_date
from pushnotifications.views import sendMsg

from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.decorators import authentication_classes

def createcase(request):
    print("ctoday", utilitytools.utility_date.getTodayCDate())
    return render(request, 'CreateCase.html', {'cToday': utilitytools.utility_date.getTodayCDate(),})

@api_view(['POST'])
def switchFunction(request):
    fun1 = request.data.get('button1', '')
    if fun1 != '':
        rtnStr = createOnePatient(request)
    else:
        fun2 = request.data.get('button2', '')
        if fun2 != '':
            rtnStr = creatServerList(request)

        else:
            fun3 = request.data.get('button3', '')
            if fun3 != '':
                rtnStr = createRequisition(request)
            else:
                fun4 = request.data.get('button4', '')
                if fun4 != '':
                    rtnStr = setPatient_serviceno(request)
                else:
                    fun5 = request.data.get('button5', '')
                    if fun5 != '':
                        rtnStr = otherSendMsg(request)
                    else:
                        fun6 = request.data.get('button6', '')
                        if fun6 != '':
                            rtnStr = otherSendMsg(request)
                        else:
                            rtnStr = ''

    return HttpResponse(rtnStr['_status'] + ' : '+ rtnStr['_status_doc'])

#return HttpResponse("PATOPD 建立失敗:" + sys.exc_info()[0])


def createOnePatient(request):

    print("request", request.data)
    _view_date = request.data['view_date']
    _chart_no = request.data['chart_no']
    _view_no = request.data['view_no']
    _dcotorNo = 'D01'
    #0. 每天預設情境是病人只會有一次掛號記錄

    #10. Delete REG(掛號記錄) / PATOPD(門診主檔) / patient_status(病人狀態記錄表)
    regdel = hismaxdb.models.Reg.objects.filter(view_date=_view_date, chart_no=_chart_no)
    regdel.delete()

    opddel =  hismaxdb.models.Patopd.objects.filter(view_date=_view_date, chart_no=_chart_no)
    opddel.delete()

    opdstatus = hismaxdb.models.PatientStatus.objects.filter(view_date=_view_date, chart_no=_chart_no)
    opdstatus.delete()

    #11. create (REG)掛號記錄
    try:
        reg = hismaxdb.models.Reg()
        reg.chart_no = int(_chart_no)
        reg.view_date = _view_date
        reg.apn = 1
        reg.duplicate_no = 0
        reg.clinic = 1
        reg.doctor_no = _dcotorNo
        reg.view_no = _view_no
        reg.reg_clerk = 'test'
        reg.reg_time = datetime.now()
        reg.prenatal_care = 'Y'
        reg.save()
    except:
        return {'_status': 'error', '_status_doc': "REG 建立失敗:" + sys.exc_info()[0]}
        #return HttpResponse("REG 建立失敗:" + sys.exc_info()[0])

    #2. create and Delete 門診主檔 : PATOPD
    try:
        patopd = hismaxdb.models.Patopd()
        patopd.chart_no = int(_chart_no)
        patopd.view_date = _view_date
        patopd.view_no = _view_no
        patopd.duplicate_no = 0
        patopd.apn = 1
        patopd.zone = 'A'
        patopd.clinic = 1
        patopd.doctor_no = _dcotorNo
        patopd.div_no = '05'    #婦產科
        patopd.cash_type = '1'
        patopd.fv_rv = '2'
        patopd.send_chart = 'Y'
        patopd.pt_type = '21'
        patopd.card_seq = '41'
        patopd.visit = 'N'
        patopd.appointment = '2'
        patopd.give_order = '0'
        patopd.supple_flag = 'N'
        patopd.discount_ptr = 0
        patopd.post_attend_fee = 'N'
        patopd.post_reg_flag = 'N'
        patopd.triage = '0'
        patopd.reg_amt = 50
        patopd.disc_reg_amt = 0
        patopd.emg_accrue = 'N'
        patopd.disability_flag = 'N'
        patopd.trans2emr_complete_date = '0'
        patopd.expect_view_time = "1005"

        patopd.save()
    except:
        #return HttpResponse("PATOPD 建立失敗:" + sys.exc_info()[0])
        return {'_status': 'error', '_status_doc': "PATOPD 建立失敗:" + sys.exc_info()[0]}

    #3. Delete 病人狀態記錄表 : patient_status

    #return HttpResponse("建立成功")
    return  {'_status': 'success', '_status_doc': "建立成功 !!"}

def creatServerList(request):
    print("request", request.data)
    _location_code = request.data['location_code']
    _viewdate = request.data['view_date']
    _apn = request.data['apn']
    _recno = int(request.data['rec_no'])
    #1. 刪除排班表
    plst = hismaxdb.models.PatientServicelist.objects.filter(location_code=_location_code, view_date=_viewdate, apn=_apn)
    plst.delete()

    #2. random 產生病歷號
    for seq in range(_recno):
        #random 2 - 163000
        bln = False
        while (not bln):
            cno = random.randrange(100, 160000)
            try:
                chart = hismaxdb.models.Chart.objects.get(chart_no=cno)
            except hismaxdb.models.Chart.DoesNotExist:
                bln = False
            else:
                bln = True
        #3. 重新建立 patient_servicelist
        cr_list = hismaxdb.models.PatientServicelist()
        cr_list.location_code =_location_code
        cr_list.view_date = _viewdate
        cr_list.apn=_apn
        cr_list.seq_no=seq+1
        cr_list.chart_no = chart.chart_no
        cr_list.pt_name = chart.pt_name
        cr_list.eff_flag = 'Y'
        cr_list.save()
    #4. delete patient_serviceno
    serdel = hismaxdb.models.PatientServiceno.objects.filter(location_code=_location_code)
    serdel.delete()
    #4. insert into patient_serviceno
    serno = hismaxdb.models.PatientServiceno(location_code=_location_code, current_no = _recno-2)
    serno.save()


    return  {'_status': 'success', '_status_doc': "排隊清單建立成功 !!"}

def createRequisition(request):
    print("Request", request.data)

    _view_date = request.data['view_date']
    _chart_no = request.data['chart_no']
    _duplicate_no = '0'
    _labFlag = False
    _xRay = False
    _cdate = utilitytools.utility_date.getTodayCDate()

    #delete all Requisition about this patient
    plst = hismaxdb.models.Requisition.objects.filter(chart_no=_chart_no)
    plst.delete()


    try:
        if request.data['check_lab'] == 'lab':
            _labFlag = True
            numL =  restwebservice.get_extdata.getSeqno('LA')
            req = hismaxdb.models.Requisition()
            req.req_no = _cdate + numL
            req.req_datetime = utilitytools.utility_date.getCNowS()
            req.print_times = 0
            req.inp_opd = 'O'
            req.form_no = 'LA'
            req.chart_no = _chart_no
            req.serno = 0
            req.order_date = _view_date         #View_Date
            req.processed = 'N'
            req.save()
    except:
        pass

    try:
        if request.data['check_x'] == 'xray':
            _xRay = True
            numX = restwebservice.get_extdata.getSeqno('XR')
            req = hismaxdb.models.Requisition()
            req.req_no = _cdate + numX
            req.req_datetime = utilitytools.utility_date.getCNow()
            req.print_times = 0
            req.inp_opd = 'O'
            req.form_no = 'XR'
            req.chart_no = _chart_no
            req.serno = 0
            req.order_date = _view_date         #View_Date
            req.processed = 'N'
            req.save()
    except:
        pass

    return  {'_status': 'success', '_status_doc': "申請單建立成功 !!"}

#設定服務號
def setPatient_serviceno(request):
    print("request", request.data)
    _location_code = request.data['location_code']
    _seq_no = request.data['current_no']

    #1: 設定目前服務號, 偷懶未處理診間號
    #2: 目前取號方式，Location_code 如為 10 則固定為診間 1
    #3:
    try :
        serNoRec = hismaxdb.models.PatientServiceno.objects.get(location_code=_location_code)
    except:
        #未有該位置記錄, 新增
        serNoRec = hismaxdb.models.PatientServiceno()
        serNoRec.location_code = _location_code
        if _location_code=='10':
            serNoRec.clinic_no = 1
        else:
            serNoRec.clinic_no = 0
    finally:
        if _location_code=='10':
            serNoRec.clinic_no = 1
        else:
            serNoRec.clinic_no = 0

        serNoRec.current_no = _seq_no
        serNoRec.save()

    #2: Call GCM for Next Patient
    cDate = utilitytools.utility_date.getTodayCDate()
    msgText = "沒有排隊名單, 如為預約掛號請先報到!!"
    pRecs = hismaxdb.models.PatientServicelist.objects.filter(location_code=_location_code, view_date=cDate, apn=1, seq_no__gt=_seq_no)
    for pRec in pRecs:
        ptName = restwebservice.get_extdata.get_ptname(pRec.chart_no)
        msgText = ptName + "您好 !! 目前"
        s1 = {
            "10": "診間看診順序為:" + str(_seq_no) +"您為下一個看診人員，請至診間外部侯診...",
            "20": "衛教室的服務號為:" + str(_seq_no) + "您為下一個服務人員，請至衛教室準備...",
            "31": "檢驗科的服務號為:" + str(_seq_no) + "您為下一個服務人員，請至檢驗科準備...",
            "32": "X光室的服務號為:" + str(_seq_no) + "您為下一個服務人員，請至X光室準備...",
        }[_location_code]
        msgText += s1
        sendMsg(request=request, chart_no=pRec.chart_no, msg_text=msgText)
        break

    return {'_status': 'success', '_status_doc': msgText}


def otherSendMsg(request):
    _chart_no = request.data['chart_no']
    _message = request.data['message']
    sendMsg(request=request, chart_no=_chart_no, msg_text=_message)

    return {'_status':'success', '_status_doc':_message}
