from django.shortcuts import render
from django.http import HttpResponseRedirect
from rainforest.models import Product
# import pdb


def show_all(request):
    products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'show_all.html', context)

def show_product(request, id): 
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'show_product.html', context)
