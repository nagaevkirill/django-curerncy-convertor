from django.shortcuts import render
import requests

# Create your views here.

def exchange(request):
    response = requests.get(url='https://currency-api.free.beeceptor.com/test').json()
    currencies = response.get('rates')
    print(currencies)

    if request.method == 'GET':

        context = {
            'currencies' : currencies
        }

    return render(request=request, template_name='exchange_app/index.html', context=context)