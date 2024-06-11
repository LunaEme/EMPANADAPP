from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.db import connection
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout

# Create your views here.

def userlogout(request):
    logout(request)
    return render(request, 'userlogout.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def index(request):
    return render(request, 'index.html')

@login_required
def stock(request):
    cursor = connection.cursor()
    cursor.execute("SELECT ProductName from Products")
        #cursor.close()
    query = cursor.fetchall()
    return render(request, 'stock.html', {'query': query})

@login_required
def sales(request):
    return render(request, 'sales.html')

@login_required
def reports(request):
    return render(request, 'reports.html')


# sql queries

for p in Products.objects.raw("SELECT * from Products"):
    print(p)
    