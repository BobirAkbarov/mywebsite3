from .models import Article, Category
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404

def makaleler_view(request):
    makale = get_object_or_404(Article, title='bilim va sanat masalasi')

    return HttpResponse('<h1>Hello World</h1>')
