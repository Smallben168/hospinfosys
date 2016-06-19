
import hismaxdb.models
from django.db.models import Max

#取得員工/醫師姓名
def getEmployeeName(l_empNo):
    try:
        employee = hismaxdb.models.Employee.objects.get(emp_no=l_empNo)
        rtn = employee.emp_name
    except:
        rtn = l_empNo
    return rtn

#取得目前該科室之服務號
def getCurrentNoByLoc(l_locationCode):
    try:
        patientServiceno = hismaxdb.models.PatientServiceno.objects.get(location_code=l_locationCode)
    except:
        num = 1
    else:
        num = patientServiceno.current_no
    return  num

#依診間號取得位置號
def getLocationCodeByClinic(l_clinic):
    try:
        #print("clinic", l_clinic)
        deptLocation= hismaxdb.models.DeptLocation.objects.get(clinic=l_clinic)
    except deptLocation.DoesNotExist:
        code = '10'
    except:
        code = '10'
    else:
        code = deptLocation.location_code
    return  code

#取得 patientServicelist 中位置/該日期/該時刻 之最大號碼
def getMaxServiceNo(l_location_code, l_view_date, l_apn):
    patientServicelist = hismaxdb.models.PatientServicelist.objects.filter(location_code=l_location_code, view_date=l_view_date, apn=l_apn).aggregate(Max('seq_no'))
    if patientServicelist['seq_no__max'] == None:
        return 1
    else:
        return int(patientServicelist['seq_no__max'])


#取得病人姓名
def get_ptname(l_chartNo):
    try:
        chart = hismaxdb.models.Chart.objects.get(chart_no=l_chartNo)
    except hismaxdb.models.Chart.DoesNotExist:
        return ""
    except:
        return ""
    else:
        return chart.pt_name

#取得病人資料
def getChart(chart_no):
    try:
        chart = hismaxdb.models.Chart.objects.get(chart_no=chart_no)
    except hismaxdb.models.Chart.DoesNotExist:
        return ""
    except:
        return ""
    else:
        return chart

#取得四位數字流水號，依 CODE
def getSeqno(l_code):
    try:
        seqno = hismaxdb.models.Seqno.objects.get(code=l_code)
    except:
        seqno = hismaxdb.models.Seqno(code=l_code, seqno=1)
    else:
        seqno.seqno += 1
    finally:
        seqno.save()

    return l_code + str(seqno.seqno).zfill(4)

#取得位置名稱
def getLocationName(l_locationCode):
    try:
        dept = hismaxdb.models.DeptLocation.objects.get(location_code=l_locationCode)
    except:
        rtnStr = l_locationCode
    else:
        rtnStr = dept.location_name

    return rtnStr

#取得位置物件代號
def getLocationID(l_locationCode):
    id = {
        '10' : 'REG',
        '20' : 'PRE_DEPT_SCHEDULE',
        '31' : 'DEPT_SCHEDULE',
    }[l_locationCode]
    return id

#取得科別代號
def getDivisionName(div_no):
    try:
        div = hismaxdb.models.Division.objects.get(div_no=div_no)
    except:
        rtnStr = div_no
    else:
        rtnStr = div.div_name
    return rtnStr
