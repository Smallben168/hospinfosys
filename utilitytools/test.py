# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

import hismaxdb.models
from restwebservice.get_extdata import getMaxServiceNo


def ttt(request):
    #l_location_code, l_view_date, l_apn):
	rtnStr = str(getMaxServiceNo('10', '1050514','1'))
	print("回傳值 :", rtnStr)
	return HttpResponse("--> ", rtnStr)


def testdb(request):
	_schedule = hismaxdb.models.Schedule.objects.all()
	return render(request, 'test_result.html', {'current_time':format(datetime.now()), 'scheduletb' : _schedule,})


def testdb2(request):
	_chart = hismaxdb.models.Chart.objects.all().filter(chart_no__lt=9999)
	return render(request, 'test_result2.html', {'current_time':format(datetime.now()), 'charttb' : _chart,})
