"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from order.views import create_order, create_model_order, index
from pizzas.views import pizza_detail_view
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('<slug:slug>', pizza_detail_view, name="pizza_detail"),
    path('create_order/', create_order, name="createorder"),
    path('createmodelorder/', create_model_order, name="createmodelorder"),
    path('__debug__/', include(debug_toolbar.urls)),
]
