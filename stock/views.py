from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection

# Create your views here.
@login_required
def stock(request):
    cursor = connection.cursor()
    cursor.execute("SELECT ProductName from Products")
        #cursor.close()
    query = cursor.fetchall()
    return render(request, 'stock.html', {'query': query})