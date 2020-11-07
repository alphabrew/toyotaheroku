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
    dealers=['355toyota',
    'adamstoyota',
    'baierltoyota',
    'beavertoyotastaugustine',
    'brewerairporttoyota',
    'cobbcountytoyota',
    'conicellitoyotaofspringfield',
    'dandeerytoyota',
    'darcarstoyota',
    'darcarstoyotaofbaltimore',
    'darcarstoyotaoffrederick',
    'daytonatoyota',
    'delucatoyota',
    'deserttoyota',
    'eastmadisontoyota',
    'elmoretoyota',
    'erniepalmertoyota',
    'foothillstoyota',
    'fredandersontoyota',
    'germaintoyotaofnaples',
    'hamertoyota',
    'heartlandtoyota',
    'hendricktoyotaapex',
    'hendricktoyotaconcord',
    'hickorytoyota',
    'jimellistoyota',
    'josephtoyota',
    'kerrytoyota',
    'koch33toyota',
    'lewistoyota',
    'lhmtoyotalemongrove',
    'lithiatoyotabillings',
    'loyaltytoyotarichmond',
    'maderatoyota',
    'maitatoyota',
    'mariettatoyota',
    'miltonrubentoyota',
    'miracletoyota',
    'myalexandertoyota',
    'passporttoyota',
    'puentehillstoyota',
    'reinhardtmotors',
    'rogersandrogerstoyota',
    'rohrichtoyota',
    'rosevilletoyota',
    'salinastoyota',
    'sftoyota',
    'sheehytoyotafredericksburg',
    'southdadetoyota',
    'sparkstoyota',
    'springhilltoyota',
    'stcloudtoyota',
    'stevenscreektoyota',
    'stevinsontoyotawest',
    'sunrisetoyota',
    'tonydivinotoyota',
    'toyotaofdecatur',
    'toyotaofdeerfieldbeach',
    'toyotaofelcajon',
    'toyotaofgladstone',
    'toyotaofgreenville',
    'toyotaoflakecity',
    'toyotaoflouisville',
    'toyotaofnorthmiami',
    'toyotaofredlands',
    'toyotaofwilmington',
    'tustintoyota',
    'villagetoyota',
    'waldorftoyota',
    'walkertoyota',
    'westcoasttoyotalb',
    'westkendalltoyota',]


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
    #return render(request,'price_list.html', {'price_list':price_list})
    return render(request,'price_list.html', {'df':df})