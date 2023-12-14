from django.shortcuts import render, HttpResponse



# Create your views here.    ACÀ GENERÈ UNA FUNCIÓN PARA LLAMAR A CADA UNA DE LAS PÁGINAS
## ESE MENÙ GENERADO ARRIBA LO CONCATENO CON EL RESTO DEL CONTENIDO DE LA PÀGINA

def index(request):
    return render(request,"core/index.html")
def galeria(request):
    return render(request,"core/galeria.html")
def mis_reservas(request):
    return render(request,"core/mis_reservas.html")
def servicios(request):
    return render(request,"core/servicios.html")

