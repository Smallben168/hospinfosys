
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

from restwebservice.main_process import getPatopd
from restwebservice.main_process import getOpdacnt
from restwebservice.main_process import getMedicine
from restwebservice.main_process import getHealthEducation

from utilitytools.utility_date import formatCNow
import restwebservice.get_extdata


def getPatientRecList(request, action):
    params = request.GET
    #urls = "http://127.0.0.1:8000"

    print("action=", action)
    #print("", request.META)
    urls = "http://" + request.META['HTTP_HOST']

    _chart_no = int(params['chart_no'])
    ptName = restwebservice.get_extdata.get_ptname(_chart_no)
    if action == "getlist":
        recs = getPatopd(l_chart_no=_chart_no)

        for rec in recs:
            rec.doctor_name = restwebservice.get_extdata.getEmployeeName(rec.doctor_no)
            rec.div_name = restwebservice.get_extdata.getDivisionName(rec.div_no)
            urls += "/procpatient/getdetail?chart_no=" + str(rec.chart_no) + "&view_date=" + rec.view_date + "&duplicate_no="+ str(rec.duplicate_no)
            rec.link = urls

        return render(request, 'get_record_list.html', {'current_time':format(datetime.now()), 'pt_name': ptName, 'dataObj' : recs,})
    else:
        _view_date = params['view_date']
        _duplicate_no = params['duplicate_no']
        _fmtdate = formatCNow(_view_date)
        recs = getOpdacnt(view_date=_view_date, chart_no=_chart_no, duplicate_no=_duplicate_no)

        for rec in recs:
            medrecs = getMedicine(rec.code)
            rec.formal_name = medrecs.formal_name
            rec.full_name_c = medrecs.full_name_c
            rec.pict = medrecs.image_name
            rec.adaptive = medrecs.adaptive
            rec.usage = medrecs.usage
            rec.side_effect = medrecs.side_effect
            rec.adverse = medrecs.adverse
            rec.note = medrecs.note

        return render(request, 'get_record_detail.html', {'current_time':format(datetime.now()),'pt_name': ptName, 'view_date': _fmtdate, 'dataObj' : recs,})


def get_educationInfo(request):
    pdfpath = "http://" + request.META['HTTP_HOST']+"/static/"
    recs = getHealthEducation()
    for rec in recs:
        urls = "http://drive.google.com/viewerng/viewer?embedded=true&url="+ pdfpath + rec.download_posit
        rec.link = urls
    return render(request, 'get_health_education.html', {'current_time':format(datetime.now()),'dataObj' : recs,})

