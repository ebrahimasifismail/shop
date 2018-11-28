from django.shortcuts import render, get_object_or_404, redirect
from textiles.models import Product, ProductImage
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView, View



# Create your views here.

# def home(request):
#     return render(request, 'textiles/home.html', {})

class Home(TemplateView):
    template_name = 'textiles/home.html'

class IndexList(View):
    template_name = 'textiles/saree.html'
    queryset = Product.objects.filter(product_type="Saree")

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = { 'object_list': self.get_queryset }
        return render(request, self.template_name, context)

class saree_detail(View):
    template_name = 'textiles/saree_detail.html'

    def get_object(self):
        id = self.kwargs.get('pk')
        obj= None
        if id is not None:
            obj = get_object_or_404(Product, id=id)
        return obj
    
    def get(self, request, *args, **kwargs):
        context = { 'saree': self.get_object() }
        return render(request, self.template_name, context)