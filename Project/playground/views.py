from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return render(request, 'playground/hello.html', {'name': 'Farhan', 'day': '100'})

# Create your views here.
