"""
URL configuration for empanadapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index import views as dash_views
from django.contrib.auth import views as auth_views
from index import views as index_views
from stock import views as stock_views
from sales import views as sales_views
from reports import views as reports_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.index, name='index'),
    path('stock/', stock_views.stock, name='stock'),
    path('sales/', sales_views.sales, name='sales'),
    path('reports/', reports_views.reports, name='reports'),
    path('login/', auth_views.LoginView.as_view(template_name='userlogin.html'), name='userlogin'),
    path('logout/', dash_views.userlogout, name='userlogout'),
]

