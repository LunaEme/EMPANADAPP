from django.urls import path, include
from . import views

urlpatterns = [
     # index login page
     path('', views.index, name='index'),
     # admin panel
     #path('adminpanel/', views.adminpanel, name='adminpanel'),
     #path('adminpanel/', include('adminpanel.urls')),
     # stock
     path('stock/', views.stock, name='stock'),
     path('sales/', views.sales, name='sales'),
     path('reports/', views.reports, name='reports'),
]
