from django.shortcuts import render

# Create your views here.
def adminpanel(request):
    return render(request, 'adminpanel/adminpanel.html')

def adminpanel_payment(request):
    return render(request, 'adminpanel/payment.html')

def adminpanel_users(request):
    return render(request, 'adminpanel/users.html')

def adminpanel_products(request):
    return render(request, 'adminpanel/products.html')

def adminpanel_delete_sale(request):
    return render(request, 'adminpanel/delete_sale.html')