from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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
            'powers': request.POST.getlist('powers[]')
        }
        return render(request, 'letter.html', context)
    return render(request, 'index.html')