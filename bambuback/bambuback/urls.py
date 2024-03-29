"""
URL configuration for bambuback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')  
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')  ESTA ES LA QUE USAREMOS
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from core import views              ##ESTO ES LO QUE PERMITE CONECTAR LAS PAGINAS A LA APLICACION 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",  views.index, name='home'),
     path("index",  views.index, name='index'),
    path("Galeria", views.galeria, name='galeria'),
    path('mis_reservas',views.mis_reservas, name='mis_reservas'),
    path("servicios", views.servicios, name='servicios'),
]
