"""onlyflans URL Configuration

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
from web.views import index, about, welcome, contact, exito, carousel, recipe, recipe_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('exito/', exito),
    path('accounts/', include('django.contrib.auth.urls')),
    path('carousel/', carousel, name='carousel'),
    path('recipes/', recipe, name='recipe'),
    path('recipe_detail<slug:slug>/', recipe_detail, name='recipe_detail'),
]
