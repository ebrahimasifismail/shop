from django.shortcuts import render
from textiles.models import Product
from django.views.generic.base import TemplateView
# Create your views here.

# def home(request):
#     return render(request, 'textiles/home.html', {})

class Home(TemplateView):
    template_name = 'textiles/home.html'