from django.urls import path
from . import views

urlpatterns = [
     path('adminpanel/',  views.adminpanel, name='adminpanel'),
     path('adminpanel/payment', views.adminpanel_payment, name='adminpanel_payment'),
     path('adminpanel/users', views.adminpanel_users, name='adminpanel_users'),
     path('adminpanel/products', views.adminpanel_products, name='adminpanel_products'),
     path('adminpanel/delete_sale', views.adminpanel_delete_sale, name='adminpanel_delete_sale'),
]
