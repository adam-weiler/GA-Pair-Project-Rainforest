from django.shortcuts import render
from django.http import HttpResponseRedirect
from rainforest.models import Product
# import pdb


def show_products(request):
    products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'show_products.html', context)