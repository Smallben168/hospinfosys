
import datetime

def getNowAPN():
    now = datetime.datetime.now()
    if now.hour <= 12:
        return "1"
    elif now.hour <=18:
        return "2"
    else:
        return "3"

def getTodayCDate(fmt=''):
    now = datetime.datetime.now()
    cyy = now.year - 1911
    cmm = now.month
    cdd = now.day
    return (str(cyy)+fmt+str(cmm).zfill(2)+fmt+str(cdd).zfill(2))

def getCNow(datefmt='', timefmt='', septfmt=''):
    #國曆只傳回至分
    now = datetime.datetime.now()
    cyy = now.year - 1911
    cmm = now.month
    cdd = now.day
    hh = now.hour
    mm = now.minute
    return (str(cyy)+ datefmt + str(cmm).zfill(2) + datefmt +str(cdd).zfill(2) + septfmt + str(hh).zfill(2) + timefmt + str(mm).zfill(2))

def getCNowS(datefmt='', timefmt='', septfmt=''):
    #國曆只傳回至sec
    now = datetime.datetime.now()
    cyy = now.year - 1911
    cmm = now.month
    cdd = now.day
    hh = now.hour
    mm = now.minute
    ss = now.second
    return (str(cyy)+ datefmt + str(cmm).zfill(2) + datefmt +str(cdd).zfill(2) + septfmt + str(hh).zfill(2) + timefmt + str(mm).zfill(2)+ timefmt + str(ss).zfill(2))

def formatCNow(cdate):
    return (cdate[1:3] + "/" + cdate[3:5] + "/" +cdate[5:7])