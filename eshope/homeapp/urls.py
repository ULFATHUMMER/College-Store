"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from homeapp import views
app_name='homeapp'

urlpatterns = [
    path('profile/<int:user>', views.profile,name='profile'),
    path('index', views.index,name='index'),

    #urls for auth
    path('register/', views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #urls for store
    path('products/<int:user>', views.allProdCat, name='allProdCat'),
    #path('<slug:c_slug>/',views.allProdCat,name='Products_of_Category'),
    #path('<slug:c_slug>/<slug:p_slug>', views.proDetails, name='get_product_details'),
    #path('payment/im not here', views.payment, name='payment'),
    path('paymsg', views.paymsg, name='paymsg'),

]
