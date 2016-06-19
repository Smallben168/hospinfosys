
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

#不能用, 路徑有問題 !!
def pdf_view(request, pdfname):
    #http://127.0.0.1:8000/static/health_education/EDU001.pdf
    #pdfname = "static/health_education/EDU001.pdf"
    #pname = "static/health_education/" + pdfname + ".pdf"
    print("static=", static(''))
    pname = static(pdfname)

    #pname = '/static/health_education/EDU001.pdf'
    print ("pname", pname)
    with open(pname, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed