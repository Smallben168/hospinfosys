from django.conf.urls import url, patterns

#from django.contrib.auth.models import User
#from rest_framework import routers, serializers,  viewsets

from restwebservice.views import ser_schedule
from restwebservice.views import sChart
from restwebservice.views import getobjectjson
from restwebservice.views import delobject
from restwebservice.views import p_register_device
from restwebservice.views import p_receiver_beacon
from restwebservice.views import getDeptList
from restwebservice.views import getClinicNo
from restwebservice.views import getTodayReg

# Wire up our API using automatic URL routing. -ben
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^ser_schedule/', ser_schedule),
    url(r'^ser_chart/', sChart.as_view()),
    url(r'^get_object/(?P<objectname>\w+)', getobjectjson,name='objectname'),
    url(r'^del_object/(?P<objectname>\w+)', delobject,name='objectname'),
    url(r'^device_register/', p_register_device),
    url(r'^receiver_beacon/(?P<param>\w+)', p_receiver_beacon,name='param'),
    url(r'^getDeptList/(?P<param>\w+)', getDeptList, name='param'),
    url(r'^getClinicNo/(?P<param>\w+)', getClinicNo, name='param'),
    url(r'^getTodayReg/(?P<param>\w+)', getTodayReg, name='param'),
]
