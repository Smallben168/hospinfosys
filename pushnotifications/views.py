#測試Client 其 registration_ids':'APA91bEJOQznACdSjOLAE2oGaPiaBAq2GZ59MK6UWaDWZWI8H0SIlw3amuVQpnuRgqoXugtklgbVlDCFNOEBunmUxqv6SLC8VGkgBDZOBO4f80EUc205UpH8Qhyl56snEdJaKN_443Ge'
#Sender ID : 99262725025
#Server API Key : AIzaSyC89W5Scdl3gLGOQ5fAZFluh1qosscJVek 
#Package_Name = tw.com.hismax.test

from django.http import HttpResponse
from hismaxdb.models import RegisterDevice
import time
import json
import requests


def testmsg(request, chartNo):
    event = 'test_event'

    if request.GET != '':
        msg = request.GET.get('message')
    else:
        msg = 'hospinfosys of GCM 訊息測試 from http://163.18.22.69/gcm_test/ !!'
    nowTime = time.strftime('%m/%d %H:%M ',time.localtime())
    notification_params={}
    notification_params['event'] = event
    notification_params['message'] = nowTime + msg

    # Device of Registr Id
    #devRegId=[]
    #devRegId.append('APA91bEJOQznACdSjOLAE2oGaPiaBAq2GZ59MK6UWaDWZWI8H0SIlw3amuVQpnuRgqoXugtklgbVlDCFNOEBunmUxqv6SLC8VGkgBDZOBO4f80EUc205UpH8Qhyl56snEdJaKN_443Ge')
    #devRegId.append('APA91bHgtTnlP9EHOqjs_hKKAUMnLTrE9UFZ91nByt1TXRW4brqrIn__563S5cw6JrOSb8N2x5_t-Yr6PnJCpaagQkEV-qP8LOfqrqH-Bkv1vDAlMcAB50RIowWj2spuykNgGTcMaiBw')
    #--- get from database -- chart_no = 106733
    devRegId = getRegisterDevice(chartNo)
    #-------------------------163.18.22.69

    #json.dumps(notification_params),
    values = {
        'registration_ids':devRegId,
        'data': notification_params,
    }
    #print('data='+json.dumps(notification_params))
    #print("values=", values)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization':'key=AIzaSyC89W5Scdl3gLGOQ5fAZFluh1qosscJVek',
    }

    rtn = requests.post(url='https://android.googleapis.com/gcm/send', data=json.dumps(values), headers=headers)

    if rtn.status_code == 200:
        return HttpResponse("send test message success !! </br> " + rtn.request.body )
    else :
        return HttpResponse("send test message error : code = " + str(rtn.status_code) + " : " + rtn.text)

def sendMsg(request, chart_no, msg_text):
    event = 'send_event'
    #nowTime = time.strftime('%m/%d %H:%M ',time.localtime())
    nowTime = time.strftime('%H:%M',time.localtime())
    notification_params={}
    notification_params['event'] = event
    notification_params['message'] = nowTime + msg_text

    #--- get from database -- chart_no = 106733
    devRegId = getRegisterDevice(chart_no)
    values = {
        'registration_ids':devRegId,
        'data': notification_params,
    }
    headers = {
        'Content-Type' : 'application/json',
        'Authorization':'key=AIzaSyC89W5Scdl3gLGOQ5fAZFluh1qosscJVek',
    }

    rtn = requests.post(url='https://android.googleapis.com/gcm/send', data=json.dumps(values), headers=headers)

    if rtn.status_code == 200:
        return HttpResponse("send test message success !! </br> " + rtn.request.body )
    else :
        return HttpResponse("send test message error : code = " + str(rtn.status_code) + " : " + rtn.text)

def getWeather(request):
    rtn = requests.get(url='http://www.cwb.gov.tw/rss/forecast/36_02.xml')
    return HttpResponse(rtn)

# Ben- 取得 RegisterDevice.registration_id 之 list
def getRegisterDevice(p_chart_no):
    regId = []
    registerDevice = RegisterDevice.objects.all().filter(chart_no=p_chart_no)
    for rows in registerDevice:
        print("Registration_id = " + rows.registration_id)
        regId.append(rows.registration_id)

    return regId
