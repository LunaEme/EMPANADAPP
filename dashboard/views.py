from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index login page
def index(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'stock.html')

def sales(request):
    return render(request, 'sales.html')

def reports(request):
    return render(request, 'reports.html')