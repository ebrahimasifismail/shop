from django.shortcuts import render
from textiles.models import Product, ProductImage
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView



# Create your views here.

# def home(request):
#     return render(request, 'textiles/home.html', {})

class Home(TemplateView):
    template_name = 'textiles/home.html'

