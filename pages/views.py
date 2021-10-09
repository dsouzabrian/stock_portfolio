from django.shortcuts import render
import requests
import json
import urllib3 
URL = "http://test.papka.nl:12349/restdemo"
    
# Create your views here.
def index(request):
    r = requests.get(url = URL)
    data = r.json()
    values = data.values()
    values_in_list = list(values)
    return render(request,'pages/index.html',{"data":values_in_list[0]})

def portfolio(request):
    if request.method == 'POST':
        form = request.POST.get('account')
        if(form=="Kindly Select"):
            return index()
        else:
            get_account_number = int(form)
            
            newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

            encoded_body = json.dumps({
                'account':get_account_number
            })
            response = requests.post(URL,
                                    encoded_body,
                                    headers=newHeaders)

            print("Status code: ", response.status_code)

            portfolio = response.json()
            
            get_free_cash = portfolio.get('freecash')
            getvalue = {
                "freecash" : get_free_cash,
                "amt" : "20000"
            }
            get_portfolio = portfolio.get('portfolio')
            print(get_portfolio)
            
            portfolio["free"] = get_free_cash
             
            
            return render(request,'pages/index.html',portfolio)

def charts(request):
    return render(request,'pages/home.html')