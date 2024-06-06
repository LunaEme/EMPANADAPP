from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index login page
def index(request):
    return render(request, 'index.html')

# admin panel
def admin_panel(request):
    return render(request, 'admin_panel.html')

def admin_panel_payment(request):
    return render(request, 'admin_panel/payment.html')

def admin_panel_users(request):
    return render(request, 'admin_panel/users.html')

def admin_panel_products(request):
    return render(request, 'admin_panel/products.html')

def admin_panel_delete_sale(request):
    return render(request, 'admin_panel/delete_sale.html')


# stock
def stock(request):
    return render(request, 'stock.html')

def sales(request):
    return render(request, 'sales.html')

def reports(request):
    return render(request, 'reports.html')