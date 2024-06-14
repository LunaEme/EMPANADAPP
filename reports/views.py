from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection

# Create your views here.

@login_required
def reports(request):
    return render(request, 'reports.html')