from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
import os



# Create your views here.
def first_page(request):
    return render(request, 'firstpage.html')

def index(request):
    return render(request, 'index.html')

def letter(request):
    if request.method == 'POST':
        context = {
            'name': request.POST.get('name'),
            'profession': request.POST.get('profession'),
            'cpf': request.POST.get('cpf'),
            'identity_card': request.POST.get('identity_card'),
            'nationality': request.POST.get('nationality'),
            'street': request.POST.get('street'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'zipcode': request.POST.get('zipcode'),
            'country': request.POST.get('country'),
            'email': request.POST.get('email'),
            'maritalstatus': request.POST.get('maritalstatus'),
            'powers': request.POST.getlist('powers[]'),
            'is_pdf': False
        }
        return render(request, 'letter.html', context)
    return render(request, 'index.html')


def download_pdf(request):
    if request.method == 'POST':
        context = {
            'name': request.POST.get('name'),
            'profession': request.POST.get('profession'),
            'cpf': request.POST.get('cpf'),
            'identity_card': request.POST.get('identity_card'),
            'nationality': request.POST.get('nationality'),
            'street': request.POST.get('street'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'zipcode': request.POST.get('zipcode'),
            'country': request.POST.get('country'),
            'email': request.POST.get('email'),
            'maritalstatus': request.POST.get('maritalstatus'),
            'powers': request.POST.getlist('powers[]'),
            'is_pdf': True,
        }

        template = get_template('letter.html')
        html = template.render(context)

        css_path = os.path.join(settings.STATICFILES_DIRS[0], 'pdf.css')

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="letter.pdf"'

        with open(css_path, 'r') as css_file:
            pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback, default_css=css_file.read())

        if pisa_status.err:
            return HttpResponse('We had an error while generating your PDF', status=500)
        
        return response

    return HttpResponse("Invalid request", status=400)

def link_callback(uri, rel):
    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATICFILES_DIRS[0], uri.replace(settings.STATIC_URL, ''))
    else:
        path = finders.find(uri)
        if not path:
            raise Exception(f'Arquivo estático não encontrado: {uri}')
    return path

