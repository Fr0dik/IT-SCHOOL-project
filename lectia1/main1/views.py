from django.shortcuts import render, redirect
import requests
import json
import os
from django.contrib import messages
import pandas as pd
from plotly.offline import plot
from plotly.graph_objs import Scatter



def home(request):
    return render(request, 'main1/home.html')


def contacte(request):
    return render(request, 'main1/contacte.html')


def services(request):
    return render(request, 'main1/services.html')


def show_messages(request):
    return render(request, 'main1/includes/show_messages.html')


def currency_data():

    file_path = os.path.join('main1/currencies.json')
    
    with open(file_path, "r") as f:
        currency_data = json.loads(f.read())
    
    return currency_data


def currency(request):
    
    if request.method == "POST":
        value_if = request.POST.get('amount')

        if value_if.isnumeric():
            amount = value_if
        
        elif value_if == None:
            messages.warning(request, 'Please enter value!')
            return redirect('main1/includes/show_messages.html')
        
        else:
            messages.error(request, 'Please enter correct value!')
            return redirect('main1/includes/show_messages.html')

        amount = float(amount)
        currency_from = request.POST.get("currency_from")
        currency_to = request.POST.get("currency_to")
        url = f"https://open.er-api.com/v6/latest/{currency_from}"
        d = requests.get(url).json()
            

        if d["result"] == "success":
            ex_target = d["rates"][currency_to]
            result = ex_target * amount
            result = "{:.2f}".format(result)
            context = {
                        "result":result, 
                        "currency_to":currency_to, 
                        "currency_from":currency_from,
                        "currency_data":currency_data()
                    }
            return render(request, "main1/currency.html", context)

    return render(request, "main1/currency.html", {"currency_data":currency_data()})


def currency_stat(request):

    df = pd.read_csv('main1/euro_dollar.csv')

    plot_div = plot([Scatter(x=df['Year'], y=df['Year Close'],
                        mode='lines', name='Currency USD/EUR',
                        opacity=0.8, marker_color='purple')],
                        output_type='div',
                    )

    return render(request, "main1/currency_stat.html", context={'plot_div': plot_div})




