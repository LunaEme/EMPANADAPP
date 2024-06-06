from django.urls import path
from . import views

urlpatterns = [
     # index login page
     path('', views.index, name='index'),
     # admin panel
     path('admin_panel/', views.admin_panel, name='admin_panel'),
     path('admin_panel/payment', views.admin_panel_payment, name='admin_panel_payment'),
     path('admin_panel/users', views.admin_panel_users, name='admin_panel_users'),
     path('admin_panel/products', views.admin_panel_products, name='admin_panel_products'),
     path('admin_panel/delete_sale', views.admin_panel_delete_sale, name='admin_panel_delete_sale'),
     # stock
     path('stock/', views.stock, name='stock'),
     path('sales/', views.sales, name='sales'),
     path('reports/', views.reports, name='reports'),
]
