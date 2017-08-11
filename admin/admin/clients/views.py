from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(request):
	return HttpResponse("Hola desde cliente")

def login(request):
	nombre = 'Ivan'
	edad = 24
	context = {'nombre': nombre, 'edad': edad}
	return render(request, 'login.html', context)