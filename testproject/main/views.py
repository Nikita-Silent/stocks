from .forms import TaskForm
from django.shortcuts import render, redirect
from .models import Curse, Stocks
from .Parsing import dictionary_curse, dictionary_stock


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def stock(request):
    return render(request, 'main/stock.html', {'title': 'Акции'})


def currency(request):
    return render(request, 'main/currency.html', {'title': 'Валюты'})


def chart(request):
    return render(request, 'main/chart.html', {'title': 'Chart'})


def saving_currency(request):
    return render(request, 'main/saving_currency.html', {'title': 'Saving currency'})


def saving_stocks(request):
    return render(request, 'main/saving_stocks.html', {'title': 'Saving stocks'})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is incorrect!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
