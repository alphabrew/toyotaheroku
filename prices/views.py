from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import pandas as pd
from django import forms


# Create your views here.
def index(request):
    return render(request, 'base.html')

#def about(request):
    #return render(request, 'about.html')

def get_url(request):
    return render(request, 'get_url.html')

def get_prices(request):
    #input_url='https://parts.sftoyota.com/p/Toyota__Tacoma/TRD-Cat-Back-Exhaust/69527109/PT91089061.html'
    dealers=[
    'cobbcountytoyota',
    'erniepalmertoyota',
    'germaintoyotaofnaples',
    'hamertoyota',
    'heartlandtoyota',
    'hendricktoyotaapex',
    'jimellistoyota',
    'josephtoyota',
    'lagrangetoyota',
    'lewistoyota',
    'maderatoyota',
    'passporttoyota',
    'rogersandrogerstoyota',
    'rohrichtoyota',
    'salinastoyota',
    'sheehytoyotafredericksburg',
    'toyotaofdecatur',
    'toyotaofdeerfieldbeach',
    'toyotaofnorthmiami',
    'villagetoyota']


    gooddealers=[]
    prices=[]
    urls=[]
    input_url=str(request.GET["parturl"])
    url= input_url.split(".")
    base_url=str(url[0])+".{}."+str(url[2]+"."+str(url[3]))
    for dealer in dealers:
        try:
            url=base_url.format(dealer)
            text=requests.get(url).text
            soup= BeautifulSoup(text, 'html5lib')
            #price_list[dealer]=[float(soup.select('.productPriceSpan')[0].text.split()[0][1:]), url]
            prices.append(float(soup.select('.productPriceSpan')[0].text.split()[0][1:]))
            urls.append(url)
            gooddealers.append(dealer)
            #urls.append("<a href="+"\""+url+"\""+">Link</a>")

        except:
            #price_list[dealer]='bad link'
            pass
    df= pd.DataFrame(zip(gooddealers, prices, urls), columns= ['dealer', 'price', 'url']).set_index('dealer')
    df.columns.name = df.index.name
    df.index.name = None
    df.sort_values(['price'], inplace=True)
    df= df.to_html()
    #var1= 10
    #return render(request,'price_list.html', {'var1':var1})
    return render(request,'price_list.html', {'df':df})
