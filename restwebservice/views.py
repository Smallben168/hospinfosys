#from django.contrib.auth.models import User
#from rest_framework import routers, serializers,  viewsets

import sys
from datetime import datetime

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

import restwebservice.get_extdata
import restwebservice.main_process
import utilitytools.utility_date
from .serializers import *

#Debug 用，標記是否insert into patientStatus :  False
writeFlag = True

#Ben : 此程式段無用
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        print('content=', content, type(content))

        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET','POST'])
def ser_schedule(request):
    #for test
	#return HttpResponse('Django --> getUsers......')
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        obj = JSONParser().parse(request)
        return Response("Please useing GET/POST method !!")
    else:
        return Response("Please useing GET/POST method !!")



@api_view(['GET','POST'])
def getobjectjson(request, objectname):
    """
    get object of json
    """
    if request.method == 'GET':
        stmtWhere = ""
        #---- 取得 param ------
        params = request.GET
        for param in params:
            if stmtWhere == "":
                stmtWhere = " where " + param + '=' + request.GET.get(param)
            else:
                stmtWhere += " and " + param + '=' + request.GET.get(param)
            print(param, stmtWhere)

        #---- 取得 table object -----
        tableObjs = {
		    'chart':   Chart.objects.raw("select * from CHART " + stmtWhere),
		    'schedule' : Schedule.objects.raw("select * from SCHEDULE " + stmtWhere),
		    'area' : Area.objects.raw("select * from AREA " + stmtWhere),
            'registerdevice': RegisterDevice.objects.raw("select * from register_device "  + stmtWhere),
            'deptlocation': DeptLocation.objects.raw("select * from dept_location "  + stmtWhere),
            'beaconinfo': BeaconInfo.objects.raw("select * from beacon_info "  + stmtWhere),
            'reg': Reg.objects.raw("select * from REG "  + stmtWhere),
	    }[objectname]

        serializer = {
            'chart': ChartSerializer(tableObjs, many=True),
            'schedule': ScheduleSerializer(tableObjs, many=True),
            'area': AreaSerializer(tableObjs, many=True, context={'aa': 'aa'}),
            'registerdevice': RegisterDeviceSerializer(tableObjs, many=True),
            'deptlocation': DeptLocationSerializer(tableObjs, many=True),
            'beaconinfo': BeaconInfoSerializer(tableObjs, many=True),
            'reg': RegSerializer(tableObjs, many=True),
        }[objectname]
        #--- for test ----
        #print("type : ", type(serializer.data))
        #print("data : ", serializer.data[0])
        #for d in serializer.data:
        #    d['addfield'] = 'value'
        #-----------------
        return Response(serializer.data)

        #print("serializer.data=", type(serializer.data), serializer.data)
        #return JSONResponse(serializer.data)  #不知有何不同 ?

    return Response("Please useing GET/POST method !!")

#--- del
@api_view(['DELETE'])
def delobject(request, objectname):
    """
    get object of json
    """
    if request.method == 'DELETE':
        stmtWhere = ""
        #---- 取得 param ------
        params = request.GET
        kwargs =  params.dict()
        #kwargs = {'view_date':'1050512', 'chart_no':106733}
        #for param in params:
        #    kwargs[param] = request.GET.get(param)

        #---- 取得 table object -----
        tableObjs = {
            'patient_status': PatientStatus.objects.filter,
            'registerdevice': RegisterDevice.objects.filter,
            'beaconinfo': BeaconInfo.objects.filter,
            'reg': Reg.objects.filter,
	    }[objectname]

        rec = tableObjs(**kwargs)
        num = rec.count()
        if num > 0:
            rec.delete()
            return Response("delete " + objectname + ":" + str(num) + "筆")
        else:
            return Response("not found !!")

        #print("serializer.data=", type(serializer.data), serializer.data)
        #return JSONResponse(serializer.data)  #不知有何不同 ?

    return Response("Please useing DELETE method !!")





@api_view(['GET','POST'])
def p_register_device(request):

    if request.method == 'POST':
        #處理 json 資料
        #print("request.data", request.data)
        #print("request", request)
        #需注意不能設定 header : Content-Type = application/json
        jsonObj = JSONParser().parse(request)

        #print("jsonObj of type :", type(jsonObj)) #list
        #一筆一筆檢查
        for raws in jsonObj:
            print('type(raws)',type(raws))  #dict
            print('id_no1', raws['id_no'])
            #取出 chart 之 chart_no / birth_date
            charts = Chart.objects.all().filter(id_no=raws['id_no'])
            for chart in charts:
                if chart.chart_no > 0:
                    raws['chart_no'] = chart.chart_no
                    raws['birth_date'] = chart.birth_date
                    ptName = chart.pt_name

            print('id_no2', raws['id_no'])
            #日期格式 datetime
            raws['register_datetime'] = datetime.now()   #time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())
            ser = RegisterDeviceSerializer(data=raws)
            print("type(ser)",type(ser))    #restwebservice.serializers.RegisterDeviceSerializer
            if ser.is_valid():
                ser.save()
                #-------------
                rtn = ser.data
                #rtn.update({'pt_name': ptName})
                rtn['pt_name'] = ptName
                #--------------
                return Response(rtn, status=status.HTTP_201_CREATED)
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        params = request.GET
        for param in params:        #目前只實做一個參數
            print("param=", param)
            sqlStr = "select * from register_device where " + param + "=" + request.GET.get(param) + " and EFF_FLAG='Y'"
            print("sqlStr=", sqlStr)
            tableObjs = RegisterDevice.objects.raw(sqlStr)
            serializer = RegisterDeviceSerializer(tableObjs, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("no use" + request.method, status=status.HTTP_400_BAD_REQUEST)

#Ben : 收到Beacon訊號 -> GET
#Ben : 按 [確定] -> POST
@api_view(['GET', 'POST'] )
def p_receiver_beacon(request,param):
    rtnStr = ''
    if request.method == 'GET':
        #---- 取得 param ------
        _uuid = request.GET.get('beacon_uuid')
        _chartno = request.GET.get('chart_no')
        try:
            print('uuid=', _uuid)             #s1: get beacon position
            beaconinfo = BeaconInfo.objects.all().get(uuid=_uuid)
            print('chart_no=', _chartno)            #s2: get chart
            try:
                #chart = Chart.objects.all().get(chart_no=_chartno)
                ptName = restwebservice.get_extdata.get_ptname(_chartno)
                print('beacon=', beaconinfo.location_code )                  #s3: by location_code 預測要做什麼
                _location =beaconinfo.location_code
                #取得今日（民國年）
                _cnow = utilitytools.utility_date.getTodayCDate()
                try:
                    #檢查是否己記錄此位址服務 : YES
                    patientstatus = PatientStatus.objects.get(view_date=_cnow, chart_no=_chartno, location_code=_location)
                    print("have record this ", _cnow, _chartno, _location)

                except PatientStatus.DoesNotExist:
                    #檢查是否己記錄此位址服務 : NO
                    #insert into patientStatus
                    if writeFlag:
                        patientstatus = PatientStatus(view_date = _cnow, chart_no = _chartno, location_code = _location)
                        patientstatus.save()

                    #依 location_code 執行服務
                    fun = {
                        '10':restwebservice.main_process.process_reg,           # 掛號室 / 門口
                        '20':restwebservice.main_process.process_pre_dept,      # 衛教室
                        '31':restwebservice.main_process.process_dept,          # 檢驗科
                    }[beaconinfo.location_code]
                    try:
                        rtnStr = fun(_chartno, _cnow, beaconinfo.location_code, ptName)
                    except:
                        rtnStr = [{"_status":"error", "_status_doc": sys.exc_info()[0]}]
                        print("error : ", sys.exc_info()[0])


            except Chart.DoesNotExist:
                rtnStr = [{"_status":"error", "_status_doc": "未發現病人資料"}]
                return Response(rtnStr, status=status.HTTP_400_BAD_REQUEST)

        except BeaconInfo.DoesNotExist:
            rtnStr = [{"_status":"error", "_status_doc": "未發現Beacon資料"}]
            return Response(rtnStr, status=status.HTTP_400_BAD_REQUEST)

        #s3:記錄至 patient_trace
        patientTrace = PatientTrace(chart_no=_chartno, location_code=_location)
        patientTrace.save()

        #檢查處理 status
        if rtnStr == "":
            return Response(rtnStr, status=status.HTTP_200_OK)
        elif rtnStr[0]['_status'] == 'error':
            return Response(rtnStr, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(rtnStr, status=status.HTTP_200_OK)



    elif request.method == 'POST':
        jsonObj = JSONParser().parse(request)
        #如 _object_name : REG
        #則為預約報到, PATOPD.CHECK_IN_DATETIME = NOW (為國歷日期時間 CYYMMDDhhmm)=hospinfosys.utility_date.getCNow()

        #取得今日（民國年）
        _cnow = utilitytools.utility_date.getTodayCDate()
        for item in jsonObj:
            print('_status_doc :', item['_status_doc'])

            #PRE_DEPT 可能不用(共用 PATIENTSERVICELIST)
            fun = {
                'REG': restwebservice.main_process.update_reg,
                'PRE_DEPT_SCHEDULE': restwebservice.main_process.update_pre_dept,
                'DEPT_SCHEDULE': restwebservice.main_process.update_dept,
            }[item['_status_doc']]

            if item['_status_doc'] == 'REG':
                serviceNo = item['view_no']
            else:
                serviceNo = '0'

            rtnStr = fun(item['view_date'], item['chart_no'], item['duplicate_no'], item['apn'], _cnow, serviceNo, item['location_code'])

        if rtnStr == "":
            return Response(rtnStr, status=status.HTTP_200_OK)
        elif rtnStr[0]['_status'] == 'error':
            return Response(rtnStr, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(rtnStr, status=status.HTTP_201_CREATED)

    else:
        return Response("no use" + request.method, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getDeptList(request, param):
    #get?location_code=20&chart_no=106733
    if request.method == 'GET':
        #---- 取得 param ------
        _locationCode = request.GET.get('location_code')
        _chartno = request.GET.get('chart_no')


        cDate = utilitytools.utility_date.getTodayCDate()
        apn = 1     #表全時段
        locatiodId = restwebservice.get_extdata.getLocationID(_locationCode)

        rtnStr = restwebservice.main_process.getDeptSchedule(_locationCode, _chartno, cDate, apn, locatiodId)
    else:
        rtnStr = [{"_status":"error", "_status_doc" : "未支援此方法" }]

    return Response(rtnStr, status=status.HTTP_200_OK)

class sChart(APIView):
    """
    Table Chart
    """
    def get(self, request, format=None):
        charts =  Chart.objects.all().filter(chart_no__lt=9999)
        serializer = ChartSerializer(charts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChartSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chart =  self.get_object(pk)
        chart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


