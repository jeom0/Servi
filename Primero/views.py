from urllib.request import Request
from django.shortcuts import render

def inicio(request):

    return render(request, "index.html")

def detalles(request):
    
    return render(request, "article-details.html")

def terminos(request):
    
    return render(request, "privacy-policy.html")

def politica(request):
    
    return render(request, "terms-conditions.html")