from django.urls import path, include
from . import views as index_views
from stock import views as stock_views
from sales import views as sales_views
from reports import views as reports_views


urlpatterns = [
     path('', index_views.index, name='index'),
     path('stock/', stock_views.stock, name='stock'),
     path('sales/', sales_views.sales, name='sales'),
     path('reports/', reports_views.reports, name='reports'),
]
