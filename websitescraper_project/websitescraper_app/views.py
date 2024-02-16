from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from websitescraper_app.models import Links


# Create your views here.

def home(request):
    if request.method == "POST":
        link_new = request.POST.get('page', '')
        response = requests.get(link_new)
        beautysoup = BeautifulSoup(response.text, 'html.parser')

        for link in beautysoup.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_address, stringname=li_name)

        return HttpResponseRedirect('/')

    data_values = Links.objects.all()
    return render(request, 'home.html', {'date_values': data_values})