from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('stock/', views.stock, name='stock'),
     path('sales/', views.sales, name='sales'),
     path('reports/', views.reports, name='reports'),
]
