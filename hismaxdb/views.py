from datetime import datetime

from django.shortcuts import render

from .models import *


# Create your views here.

def stmtSelect(request, objectname):
	#request.GET['ptname']
	params = request.GET
	#print ("params =", params)
	#print ("params.items =", params.items)

	#print("a->" + params.__getitem__(''))
	stmtWhere = ''

	for param in params:
		print('參數名稱 : ', param)
		print('參數值 : ', request.GET.get(param))
		if stmtWhere == '':
			stmtWhere = " where " + param + '=' + request.GET.get(param)
		else :
			stmtWhere += ' and ' + param + '=' + request.GET.get(param)

	print('-> ', stmtWhere)

	tableObjs = {
		'chart':   Chart.objects.raw("select * from " + objectname + stmtWhere),
		'schedule' : Schedule.objects.raw("select * from " + objectname  + stmtWhere),
		'area' : Area.objects.raw("select * from " + objectname  + stmtWhere),
	}[objectname]

	#取得此 Table Object 之 欄位 List - 1 (RawQuerySet)
	objectcols = tableObjs.columns
	#取得此 Table Object 之 欄位 List - 2
	#objectcols = tableObjs._meta.get_fields()

	#for tableObj in tableObjs:
    #    tableObjs.columns = dict((field.name, field.value_to_string(object))
    #                                        for field in object._meta.fields)

	print("objectcols type : ", type(objectcols))
	print("tableObjs type", type(tableObjs))
	for rows in tableObjs:
		print(type(rows))
		#not ok : print("rows[1] = ", rows[1])
		for col in rows :
			print(col)

	#if objectname == 'chart':
	#	tableObj =  Chart.objects.raw("select * from " + objectname + " where " + stmtWhere)

	return render(request, 'stmt_select.html', {'current_time':format(datetime.now()), 'stmtObjName': objectname, 'stmtObjWhere': stmtWhere,'stmtObjData':tableObjs, 'objectcols':objectcols,
	})

#not ok
def getPatientDeviceId(p_chart_no):
	_chart = Chart.objects.all().filter(chart_no=p_chart_no)
	return ""

