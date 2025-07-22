from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


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
            'is_pdf': True
        }

        template = get_template('letter.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="letter.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('We had an error while generating your PDF', status=500)
        
        return response

    return HttpResponse("Invalid request", status=400)