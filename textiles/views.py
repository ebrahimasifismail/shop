from django.shortcuts import render, get_object_or_404, redirect
from textiles.models import Product, ProductImage, Order
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView, View
from paytm import Checksum


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
        # ordered_by = request.user
        # order_id = paytm.Checksum.__id_generator__()
        # product = self.get_object()
        # Order.objects.create(ordered_by=ordered_by, order_id=order_id, product=product)
        return render(request, self.template_name, context)

    
def buy_view(request, pk, **kwargs):
    context = {}
    # id = request.kwargs.get('pk')
    obj= None
    if id is not None:
        obj = get_object_or_404(Product, id=pk)
    ordered_by = request.user
    order_id = Checksum.__id_generator__()
    product = obj
    Order.objects.create(ordered_by=ordered_by, order_id=order_id, product=product)
    return redirect('textiles:cart')
        
        
def cart_view(request, *args, **kwargs):
    user = request.user 
    checkout_price=0
    incart = Order.objects.filter(ordered_by=user, is_active=True)
    
    for order in incart:    
        checkout_price += order.product.price
    
    total = checkout_price

    return render(request, 'textiles/cart.html', {'cart': incart, 'total': total})


class OrderDelete(View):
    template_name = 'textiles/order_confirm_delete.html'

    def get_object(self):
        id = self.kwargs.get('pk')
        obj= None
        if id is not None:
            obj = get_object_or_404(Order, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('textiles:cart')
        return render(request, self.template_name, context) 

