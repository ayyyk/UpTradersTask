"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path

from showtree.views import showtree

urlpatterns = [
    path('admin/', admin.site.urls),

    path('<path:path>/', showtree, name='menu'),
    path('', showtree, name='showtree2'),


    #this is examples of named_url handling

    path('Бразилия/', showtree, name='bras'),
    path('Китай', showtree, name='kit'),
    path('Россия', showtree, name='rus'),
    path('Япония', showtree, name='yap'),

]
