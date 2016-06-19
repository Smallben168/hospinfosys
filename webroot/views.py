# -*- coding: utf-8 -*-

from django.http import HttpResponse


# Create your views here.
def index(request):
	strhtml = "<div>Apache2 + Django + Mysql : 正常起動......</div> </br><a href='static/readme.html'> 說明 </a>"

	return HttpResponse(strhtml)

