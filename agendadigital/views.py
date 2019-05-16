from django.http import HttpResponse
from django.shortcuts import render
#En settings.py se define la ruta de los templates en la linea 57
def homepage(request):
	return render(request, 'index.html')

def documentacion(request):
	return render(request, 'documentacion.html')

def seguimiento(request):
	return render(request, 'seguimiento.html')

def solicitudes(request):
	return render(request, 'solicitudes.html')

def gobiernodigital(request):
	return render(request, 'gobierno-digital.html')

def economiadigital(request):
	return render(request, 'economia-digital.html')

def conectividad(request):
	return render(request, 'conectividad.html')

def fortalecimientoinstitucional(request):
	return render(request, 'fortalecimiento-institucional.html')