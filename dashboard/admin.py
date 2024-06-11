from django.contrib import admin
from .models import Products, Paymentmethods, Reports, Sales, Salesdetails, Stock, Stockhistory

# Register your models here.
admin.site.register(Products)
admin.site.register(Paymentmethods)
admin.site.register(Reports)
admin.site.register(Sales)
admin.site.register(Salesdetails)
admin.site.register(Stock)
admin.site.register(Stockhistory)
