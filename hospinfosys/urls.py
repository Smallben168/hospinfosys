"""hospinfosys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from hismaxdb.views import stmtSelect
from pushnotifications.views import getWeather
from pushnotifications.views import testmsg
from utilitytools.test import testdb
from utilitytools.test import testdb2
from utilitytools.test import ttt
from webroot.views import index
from webroot.createcase import createcase
from webroot.createcase import switchFunction
from webroot.operator_patient import getPatientRecList
from webroot.operator_patient import get_educationInfo
from utilitytools.other_utility import pdf_view

urlpatterns = [
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^ttt/', ttt),
    url(r'^test/', testdb),
    url(r'^test2/', testdb2),
    url(r'^stmt/(?P<objectname>\w+)', stmtSelect, name='objectname'),
    url(r'^rest/', include('restwebservice.urls')),
    url(r'^gcm_test/(?P<chartNo>\w+)', testmsg, name='chartNo'),
    url(r'^weather/', getWeather),
    url(r'^createcase/', createcase),
    url(r'^switchfun/', switchFunction),
    url(r'^procpatient/(?P<action>\w+)', getPatientRecList,name='action'),
    url(r'^geteducation/', get_educationInfo),
    url(r'^pdfviewer/(?P<pdfname>\w+)', pdf_view, name='pdfname'),
]


# Ben Remark
#    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# -->   http://127.0.0.1:8000/api-auth/login/

## 使用 rest 前需先登入 : /rest/login/